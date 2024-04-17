#!/usr/bin/env python3

# SPDX-License-Identifier: GPL-3.0
# Copyright (C) 2024 Michał Góral.

import typing
from typing import (
    TypeVar,
    Generic,
    Optional,
    Dict,
    List,
    Tuple,
    Union,
    Any,
    TextIO,
    Type,
    ClassVar,
    overload,
)

from collections.abc import Callable, Iterable

import os
import sys
import argparse
import csv
import re
import dataclasses
import datetime
import types
from datetime import datetime as dt
from zoneinfo import ZoneInfo
from pathlib import Path
from dataclasses import dataclass, field
from decimal import Decimal
from functools import partial
from operator import attrgetter
from fnmatch import fnmatch, fnmatchcase
from enum import Enum


T = TypeVar("T")
ConditionT = Optional[Callable[["Transaction"], bool]]
Rule = Callable[["Transaction"], None]
RuleList = List[Tuple[Rule, ConditionT]]
Converter = Callable[[Any], T]
Factory = Callable[[], T]


def eprint(*a, **kw):
    kw["file"] = sys.stderr
    print(*a, **kw)


class InputError(Exception):
    pass


# A sentinel which forces creating a new instance of default_factory
class _CreateDefaultFactory:
    pass


_CREATE_DEFAULT_FACTORY = _CreateDefaultFactory()


# A sentinel which indicates not existing default/default_factory for a member
class _MissingArgument:
    pass


_MISSING = _MissingArgument()


@dataclass
class uopen:
    _default: ClassVar[Path | None] = None
    _suppress_files: ClassVar[bool] = False

    _file: TextIO | None = None
    _path: Path = Path()

    @classmethod
    def configure(
        cls, default_path: Path | None = None, suppress_files: bool = False
    ) -> None:
        cls._default = default_path
        cls._suppress_files = suppress_files

    def __init__(self, path: str | Path | None = None, *open_a, **open_kw):
        if path is None:
            assert self._default is not None, "path and default cannot be both unset"
            path = Path(self._default)

        self._path = Path(path)

        if path is None or path == Path("-"):
            self._file = sys.stdout
        elif not self._suppress_files:
            self._file = open(path, *open_a, **open_kw)

    def __enter__(self):
        return self

    def __exit__(self, exctype, excval, tb):
        self.close()

    def close(self):
        if self._file and self._file != sys.stdout:
            self._file.close()

    def write(self, *a, **kw):
        if self._file:
            self._file.write(*a, **kw)

    def writeln(self, ln: str = ""):
        if self._file:
            self._file.write(ln + "\n")

    def writelines(self, lines: Iterable[str]):
        if self._file:
            for ln in lines:
                self._file.write(ln + "\n")

    @property
    def path(self):
        return self._path

    @property
    def size(self):
        try:
            return os.stat(self._file.fileno()).st_size  # type: ignore[union-attr]
        except (AttributeError, OSError):
            return 0


class Conversion(Generic[T]):
    @overload
    def __init__(self, conv: Converter) -> None:
        ...

    @overload
    def __init__(self, conv: Converter, *, default: T, always: bool = False) -> None:
        ...

    @overload
    def __init__(
        self, conv: Converter, *, default_factory: Factory, always: bool = False
    ) -> None:
        ...

    def __init__(
        self, conv, *, default=_MISSING, default_factory=_MISSING, always=False
    ):
        if default is not _MISSING and default_factory is not _MISSING:
            raise ValueError("cannot specify both default and default_factory")

        self._conv = conv
        self._default = default
        self._default_factory = default_factory
        self._always = always
        self._name: str = ""
        self._pubname: str = ""
        self._tp = None

    def __set_name__(self, cls, name: str):
        self._pubname = name
        self._name = "_" + name

    def __get__(self, obj, cls=None):
        # dataclasses determines default value by calling
        # descriptor.__get__(obj=None, tp=cls)
        if obj is None:
            if self._default is not _MISSING:
                return self._default
            if self._default_factory is not _MISSING:
                return _CREATE_DEFAULT_FACTORY
            raise AttributeError("no default")

        return getattr(obj, self._name)

    def __set__(self, obj, value):
        if value is _CREATE_DEFAULT_FACTORY and self._default_factory:
            value = self._default_factory()

        # Don't convert values which already match desired type
        if self._always or not isinstance(value, self._target_type(obj)):
            try:
                value = self._conv(value)
            except Exception:
                raise ValueError(f"conversion error for '{self._pubname}': {value}")

        if not isinstance(value, self._target_type(obj)):
            raise TypeError(
                f"unexpected type after conversion for '{self._pubname}': {type(value)}"
            )

        setattr(obj, self._name, value)

    def _target_type(self, obj) -> Type:
        if not self._tp:
            hints = typing.get_type_hints(obj)
            cls = type(obj).__name__
            assert (
                self._pubname in hints
            ), f"missing mandatory type annotation for {cls}.{self._pubname}"

            # automatically extract a tuple
            myhint = hints[self._pubname]
            (tp,) = typing.get_args(myhint)

            # duck-typing validate that annotated type is suitable for
            # isinstance (only types, tuples of types and Unions are)
            try:
                isinstance(None, tp)
            except TypeError as e:
                raise TypeError(
                    f"invalid type annotation for {cls}.{self._pubname}: {myhint}"
                ) from e

            self._tp = tp

        assert self._tp is not None
        return self._tp


class GapList(Generic[T]):
    def __init__(self):
        self._data: Dict[int, T] = {}

    def getfirst(self, default=None):
        try:
            key = min(self._data.keys())
            return self._data[key]
        except ValueError:
            return default

    def getlast(self, default=None):
        try:
            key = max(self._data.keys())
            return self._data[key]
        except ValueError:
            return default

    def append(self, value: Any):
        key = max(self.keys(), default=0) + 1
        self[key] = value
        return key, self[key]

    def clear(self):
        self._data.clear()

    def keys(self):
        return self._data.keys()

    def items(self):
        return self._data.items()

    def copy(self):
        def _copy(v):
            try:
                return v.copy()
            except AttributeError:
                return v

        ret: GapList[Posting] = GapList()
        ret._data = {i: _copy(v) for i, v in self.items()}  # lint: off
        return ret

    def __getitem__(self, key: int):
        if not isinstance(key, int):
            raise TypeError("list indices must be integers")
        if key <= 0:
            raise KeyError("field number must be higher than 0")
        return self._data[int(key)]

    def __setitem__(self, key: Union[int, str], value: Any):
        if not isinstance(key, int):
            raise TypeError("list indices must be integers")
        if key <= 0:
            raise KeyError("field number must be higher than 0")
        self._data[key] = value

    def get(self, key: int, default=None):
        try:
            return self._data[key]
        except KeyError:
            return default

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        for key in sorted(self.keys()):
            yield self[key]

    def __eq__(self, other):
        if isinstance(other, GapList):
            return self._data == other._data
        if isinstance(other, dict):
            return self._data == other
        if isinstance(other, (list, tuple)):
            if len(other) != len(self):
                return False
            return all(
                (i + 1 in self._data and self._data[i + 1] == val)
                for i, val in enumerate(other)
            )

        # support e.g. transaction.commodity == "USD" when there's only 1
        # commodity set
        return len(self) == 1 and self.getfirst() == other

    def __repr__(self):
        return repr(self._data)


def empty_str_to_none(v: Optional[str]) -> Optional[str]:
    if v:
        return v
    return None


def strip_empty_str_to_none(v: Optional[str]) -> Optional[str]:
    if v:
        v = v.strip()
    return v if v else None


@dataclass
class Latest:
    date: Conversion[datetime.date] = Conversion(datetime.date.fromisoformat)
    description: Conversion[Optional[str]] = Conversion(
        strip_empty_str_to_none, default=None, always=True
    )
    amount: Conversion[Optional[Decimal]] = Conversion(Decimal, default=None)
    commodity: Conversion[Optional[str]] = Conversion(
        strip_empty_str_to_none, default=None, always=True
    )

    @classmethod
    def from_transaction(cls, tr: "Transaction") -> "Latest":
        posting = tr.postings.getfirst(Posting())
        return Latest(tr.date, tr.description, posting.amount, posting.commodity)

    @classmethod
    def from_latest_csv(cls, row: List[str]) -> "Latest":
        if not row or not row[0]:
            raise InputError(f".latest: empty row")

        date = row[0].strip()
        description = row[1] if len(row) > 1 and row[1] else None
        amount = row[2].strip() if len(row) > 2 and row[2] else None
        commodity = row[3].strip() if len(row) > 3 and row[3] else None

        try:
            return Latest(
                date=date, description=description, amount=amount, commodity=commodity
            )
        except AttributeError as e:
            raise InputError(".latest: date not set") from e
        except ValueError as e:
            raise InputError(f".latest: {str(e)}") from e

    def __eq__(self, other):
        if not isinstance(other, Latest):
            return NotImplemented

        ret = self.date == other.date
        if self.description:
            ret &= bool(other.description) and self.description == other.description
        if self.amount:
            ret &= bool(other.amount) and self.amount == other.amount
        if self.commodity:
            ret &= bool(other.commodity) and self.commodity == other.commodity
        return ret


class SymbolSide(Enum):
    left = "left"
    right = "right"
    leftjoin = "leftjoin"
    rightjoin = "rightjoin"


@dataclass
class Posting:
    account: Conversion[str] = Conversion[str](str, default="unknown")
    amount: Conversion[Optional[Decimal]] = Conversion(Decimal, default=None)
    commodity: Conversion[Optional[str]] = Conversion(
        empty_str_to_none, default=None, always=True
    )
    # default is right, but this is set to None to allow seamless work of
    # setting c.default.symbolside, which deduces whether setting is set by
    # user by comparing it against None
    symbolside: Conversion[Optional[SymbolSide]] = Conversion(SymbolSide, default=None)

    def copy(self):
        return dataclasses.replace(self)

    def is_balanced_virtual(self) -> bool:
        return self._wrapped_by(self.account, "[", "]")

    def is_unbalanced_virtual(self) -> bool:
        return self._wrapped_by(self.account, "(", ")")

    def _wrapped_by(self, val: Optional[str], left: str, right: str) -> bool:
        if not val:
            return False
        v = val.strip()
        return v.startswith(left) and v.endswith(right)


class PostingPartProxy:
    def __init__(self, fieldname: str, postings: GapList[Posting], default: Posting):
        self._fieldname = fieldname
        self._postings = postings
        self._default = default

    def __getitem__(self, key):
        p = self._postings[key]
        return getattr(p, self._fieldname, None)

    def __setitem__(self, key, value):
        try:
            p = self._postings[key]
            setattr(p, self._fieldname, value)
        except KeyError:
            pkw = self._default.copy()
            setattr(pkw, self._fieldname, value)
            self._postings[key] = pkw

    def __repr__(self) -> str:
        lst = ", ".join(
            f"[{k}]:{getattr(v, self._fieldname)}" for k, v in self._postings.items()
        )
        return f"{{{lst}}}"


class balance_commodities:
    def __init__(self, postings: GapList[Posting]):
        self.real: dict[str, Decimal] = {}
        self.virtual: dict[str, Decimal] = {}
        self.balance_postings_real: dict[str, Posting] = {}
        self.balance_postings_virtual: dict[str, Posting] = {}

        for posting in postings:
            if posting.is_unbalanced_virtual():
                continue

            self._add_posting(posting)

        self._balance("real")
        self._balance("virtual")

    def _choose_dicts(self, acctype: str):
        assert acctype in ("real", "virtual")
        if acctype == "real":
            return self.real, self.balance_postings_real
        return self.virtual, self.balance_postings_virtual

    def _add_posting(self, posting: Posting):
        acctype = "virtual" if posting.is_balanced_virtual() else "real"
        balances, balance_postings = self._choose_dicts(acctype)

        commodity = posting.commodity
        if posting.amount is None:
            if commodity in balance_postings:
                raise ValueError(
                    f"there can't be more than one {acctype} posting with no amount"
                )

            balance_postings[commodity] = posting
            return

        curr = balances.get(commodity, Decimal(0))
        balances[commodity] = curr + posting.amount

    def _balance(self, acctype: str):
        balances, balance_postings = self._choose_dicts(acctype)
        unbalanced = []

        for commodity, balance in list(balances.items()):
            if balance == 0:
                continue

            c_balance_posting = balance_postings.get(commodity)
            if c_balance_posting:
                c_balance_posting.amount = -balance
                continue

            super_balance_posting = balance_postings.get(None)
            if super_balance_posting:
                continue

            commodity_name = commodity if commodity else "<missing commodity>"
            unbalanced.append((commodity_name, balance))

        if unbalanced:
            unbalanced_str = ", ".join(f"{cname}: {bal}" for cname, bal in unbalanced)
            raise ValueError(
                f"the transaction has unbalanced {acctype} postings: {unbalanced_str}"
            )


def zero_empty_amounts(postings: GapList[Posting]):
    for posting in postings:
        if posting.amount is None and posting.commodity:
            posting.amount = 0


class Transaction:
    def pget(self, fieldname):
        return PostingPartProxy(fieldname, self._postings, self._default)

    account = property(partial(pget, fieldname="account"), doc="Get account")
    amount = property(partial(pget, fieldname="amount"), doc="Get amount")
    commodity = property(partial(pget, fieldname="commodity"), doc="Get commodity")

    del pget

    date: Conversion[datetime.date] = Conversion(datetime.date.fromisoformat)

    def __init__(
        self,
        description: str = "",
        date: datetime.date = datetime.date.today(),
        postings: Optional[List[Posting]] = None,
    ):
        self.description: str = description
        self.date: datetime.date = date
        self._postings: GapList[Posting] = GapList()
        self._default: Posting = Posting()
        self._skip = False
        self._done = False
        self._end = False

        if postings:
            for i, p in enumerate(postings, 1):
                self._postings[i] = p

    def __repr__(self):
        return (
            f"Transaction(description={self.description}, date={self.date}, "
            f"postings={self._postings})"
        )

    @property
    def postings(self):
        return self._postings

    def normalize(self):
        if len(self.postings) == 0:
            return

        if (
            len(self.postings) == 1
            and (oldpost := self.postings.getfirst())
            and not oldpost.is_unbalanced_virtual()
        ):
            if oldpost.amount is None:
                oldpost.amount = 0

            acc = self._default.account
            if oldpost.is_balanced_virtual():
                acc = f"[{acc}]"

            newpost = Posting(
                account=acc,
                amount=-oldpost.amount,
                commodity=oldpost.commodity,
            )
            self.postings.append(newpost)

        if (
            self._default.amount
            and len(self.postings) > 1
            and all(p.amount is None for p in self.postings)
        ):
            self.postings.getfirst().amount = self._default.amount

        if (
            self._default.commodity is not None
            and len(self.postings) > 0
            and all(p.commodity is None for p in self.postings)
        ):
            for p in self.postings:
                p.commodity = self._default.commodity

        balance_commodities(self.postings)
        zero_empty_amounts(self.postings)

    def copy(self) -> "Transaction":
        # we could deepcopy the whole Transaction class, but it made the whole script
        # 2x slower...
        ret = Transaction(self.description, self.date)
        ret._postings = self._postings.copy()
        ret._default = self._default.copy()
        ret._skip = self._skip
        ret._done = self._done
        ret._end = self._end
        return ret

    def skip(self):
        """Don't output this transaction"""
        self._skip = True

    def done(self):
        """Stop processing any further rules for this transaction"""
        self._done = True

    def end(self):
        """End processing any rules or transactions immediately"""
        self._done = True
        self._end = True

    @property
    def skipped(self):
        return self._skip

    @property
    def rules_done(self):
        return self._done

    @property
    def ended(self):
        return self._end


# TODO: test
class DefaultTransaction(Transaction):
    def __init__(self, *a, default: Optional[Posting] = None, **kw):
        super().__init__(*a, **kw)

        if default:
            self._default = default

    def pget(self, fieldname):
        return PostingPartProxy(fieldname, self._postings, self._default)

    def pset(self, value, fieldname):
        setattr(self._default, fieldname, value)
        for p in self.postings:
            try:
                if getattr(p, fieldname) is None:
                    setattr(p, fieldname, value)
            except AttributeError:
                pass

    account = property(
        partial(pget, fieldname="account"),
        partial(pset, fieldname="account"),
        doc="Get account",
    )
    amount = property(
        partial(pget, fieldname="amount"),
        partial(pset, fieldname="amount"),
        doc="Get amount",
    )
    commodity = property(
        partial(pget, fieldname="commodity"),
        partial(pset, fieldname="commodity"),
        doc="Get commodity",
    )
    symbolside = property(
        partial(pget, fieldname="symbolside"),
        partial(pset, fieldname="symbolside"),
        doc="Get side on which commodity symbol is placed",
    )

    del pget
    del pset

    normalize = None  # type: ignore
    copy = None  # type: ignore

    def into_transaction(self) -> Transaction:
        return super().copy()


@dataclass(order=True)
class Field:
    _base: str
    _id: Optional[int] = None

    @classmethod
    def fromstr(cls, s: str) -> "Field":
        s = s.strip()
        pat = re.compile(r"^([0-9a-zA-Z_]+)(?:\[(\d+)\])?$")
        m = pat.match(s)
        if m is None:
            return Field(s)
        else:
            base = m.group(1)
            id = int(m.group(2)) if m.group(2) else None
            return Field(base, id)

    @property
    def base(self) -> str:
        return self._base

    @property
    def id(self) -> Optional[int]:
        return self._id

    def __hash__(self):
        return hash((self.base, self.id))


@dataclass
class CSV:
    fields: list = field(default_factory=list)
    skip: Conversion[int] = Conversion(int, default=0)
    separator: str = ","


# @condition decorator which allows composition of  complex conditions by
# overloading `&` and `|` operators.
class Condition:
    def __init__(self, fn):
        self.fn = fn
        if self.fn.__doc__:
            self.__doc__ = fn.__doc__
        self.__name__ = fn.__name__

    def __call__(self, *a, **kw) -> bool:
        return self.fn(*a, **kw)

    def __and__(self, other) -> "_And":
        return _And(self, other)

    def __rand__(self, other) -> "_And":
        return _And(other, self)

    def __or__(self, other) -> "_Or":
        return _Or(self, other)

    def __ror__(self, other) -> "_Or":
        return _Or(other, self)

    def __invert__(self) -> "Condition":
        return _Not(self)

    def __repr__(self):
        if self.__doc__:
            return self.__doc__
        return self.__name__

    @classmethod
    def _get_repr(cls, fn):
        if isinstance(fn, Condition):
            return repr(fn)
        if fn.__doc__:
            return fn.__doc__
        return fn.__name__


class _Not(Condition):
    def __init__(self, c: Condition) -> None:
        self._c = c

    def __call__(self, *a, **kw) -> bool:
        return not self._c(*a, **kw)

    def __repr__(self):
        return f"~{repr(self._c)}"

    def __invert__(self) -> Condition:
        return self._c


class _And(Condition):
    def __init__(self, *fns):
        self.fns = fns

    def __call__(self, *a, **kw) -> bool:
        return all(fn(*a, **kw) for fn in self.fns)

    def __and__(self, other) -> "_And":
        if isinstance(other, _And):
            return _And(*self.fns, *other.fns)  # associativity
        return _And(*self.fns, other)

    def __rand__(self, other) -> "_And":
        if isinstance(other, _And):
            return _And(*other.fns, *self.fns)  # associativity
        return _And(other, *self.fns)

    def __repr__(self):
        return "(" + " & ".join(self._get_repr(fn) for fn in self.fns) + ")"


class _Or(Condition):
    def __init__(self, *fns):
        self.fns = fns

    def __call__(self, *a, **kw) -> bool:
        return any(fn(*a, **kw) for fn in self.fns)

    def __or__(self, other: Condition) -> "_Or":
        if isinstance(other, _Or):
            return _Or(*self.fns, *other.fns)  # associativity
        return _Or(*self.fns, other)

    def __ror__(self, other: Condition) -> "_Or":
        if isinstance(other, _Or):
            return _Or(*other.fns, *self.fns)  # associativity
        return _Or(other, *self.fns)

    def __repr__(self):
        return "(" + " | ".join(self._get_repr(fn) for fn in self.fns) + ")"


def match_factory(pattern: str, field="description", i=False):
    """Condition which matches field of transaction (description by default)
    against a pattern. Matching is case-sensitive, unless "i" is set to True."""

    @Condition
    def _match(tr):
        # eval to easily allow e.g. e.account[1]
        try:
            fval = eval(f"str(tr.{field})", dict(tr=tr))
        except (AttributeError, KeyError):
            return False
        except SyntaxError:
            eprint(f"invalid field for match(): '{field}'")
            return False
        pat = pattern

        if i:
            return fnmatch(fval.lower(), pat.lower())
        return fnmatchcase(fval, pat)

    _match.__doc__ = f"{'i' if i else ''}match({pattern})"
    return _match


@dataclass
class Config:
    source: Conversion[Optional[Path]] = Conversion(Path, default=None)
    filetype: Optional[str] = None  # helper to manually specify a filetype of source
    decimalmark: str = "."
    dateformat: Optional[str] = None
    timezone: Optional[str] = None
    default: DefaultTransaction = field(default_factory=DefaultTransaction)
    csv: CSV = field(default_factory=CSV)

    # TODO: annotate as RuleList, but it includes a type forward reference
    # ("Transaction"), which isn't defined yet and Conversion's get_type_hints
    # complains.
    _rules: List = field(default_factory=list, init=False, repr=False)
    _load_stack: List[Path] = field(default_factory=list, init=False, repr=False)

    @property
    def rules(self) -> RuleList:
        return self._rules

    # rule decorator which accepts optional condition parameter can be used as
    # @rule, @rule() or @rule(condition=func);
    #
    # name is aliased from 'add_rule' to 'rule' in globals passed to the
    # executed source file
    def add_rule(self, fn=None, *, condition=None) -> Callable[..., None]:
        def deco(fn):
            self._rules.append((fn, condition))
            return fn

        if fn is None:  # @rule(), @rule(condition=func)
            return deco

        return deco(fn)  # @rule

    def load(self, path: str | Path) -> None:
        if not isinstance(path, Path):
            path = Path(path)

        if not path.is_absolute():
            if self._load_stack:
                path = self._load_stack[-1].parent / path
            else:
                path = path.absolute()

        if path in self._load_stack:
            eprint(f"Stopped recursive load of rules: {path}")
            return

        try:
            self._load_stack.append(path)
            self._load(path)
        finally:
            self._load_stack.pop()

    def _load(self, path: Path) -> None:
        module = types.ModuleType("rules")
        module.rule = self.add_rule  # type: ignore
        module.condition = Condition  # type: ignore
        module.match = match_factory  # type: ignore
        module.config = self  # type: ignore
        module.c = self  # type: ignore  # shorthand
        module.__file__ = str(path)

        with path.open("rb") as f:
            source = f.read()

        code = compile(source, path, "exec")
        exec(code, module.__dict__)


def convert_arg_options(s: str) -> Tuple[str, str]:
    key, _, val = s.partition("=")
    key, val = key.strip(), val.strip()
    if not key or not val:
        raise argparse.ArgumentError(None, "expected option=newval for option override")
    return key, val


def prepare_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a list of transactions to a Ledger format"
    )

    parser.add_argument(
        "rules", help="rules file for input format description", type=Path
    )

    parser.add_argument(
        "-o", "--output", type=Path, default=Path("-"), help="write output to the file"
    )

    parser.add_argument(
        "-c",
        "--config-option",
        dest="options",
        action="append",
        type=convert_arg_options,
        default=[],
        help="set or override options set in the rules file (format: -c cfg=value)",
    )

    parser.add_argument(
        "-l",
        "--latest",
        help="destination for a cache of latest processed dates",
        type=Path,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="don't make any permanent changes; ledgerify will still print results to the standard output, if selected",
    )

    parser.add_argument(
        "--debug", action="store_true", help="print debugging informations"
    )

    return parser.parse_args(argv)


def preprocess_date(field: Field, data: Dict[Field, Any], cfg: Config):
    rawdate = data[field]
    processed = (
        dt.strptime(rawdate, cfg.dateformat)
        if cfg.dateformat
        else dt.fromisoformat(rawdate)
    )

    if not processed.tzinfo and cfg.timezone:
        tz = ZoneInfo(cfg.timezone)
        processed = processed.replace(tzinfo=tz)

    # Localize date to the system timezone. Works for both naive and non-naive
    # datetimes
    data[field] = processed.astimezone().date()


def preprocess_amount(field: Field, data: Dict[Field, Any], cfg: Config):
    dm = cfg.decimalmark
    amount_re = re.compile(rf"^([^\d\-{dm}]*)([ \d\-{dm}]+)([^\d\-{dm}]*)$")

    m = amount_re.match(str(data[field]))
    if not m:
        raise ValueError(f"Unsupported amount format: {data[field]}")

    amount = m[2].strip().replace(dm, ".").replace(" ", "")
    commodity = (m[3] if m[3] else m[1]).strip()

    data[field] = amount

    if commodity:
        data.setdefault(Field("commodity", field.id), commodity)


def preprocess_input(raw_data: Dict[str, str], cfg: Config) -> Dict[Field, Any]:
    preprocessors = [("date", preprocess_date), ("amount", preprocess_amount)]
    data = {Field.fromstr(key): value for key, value in raw_data.items()}

    for fieldbase, pp in preprocessors:
        matchfields = [field_ for field_ in data if field_.base == fieldbase]
        for field_ in matchfields:
            pp(field_, data, cfg)

    return data


def get_csv(fileobj: TextIO, cfg: CSV) -> Iterable[Dict[str, str]]:
    # csv module doesn't omit empty lines the way we'd like. For example,
    # it parses a line filled with spaces
    def file_iter(file):
        for line in file:
            line = line.strip()
            if line:
                yield line

    reader = csv.DictReader(
        file_iter(fileobj), cfg.fields, delimiter=cfg.separator, skipinitialspace=True
    )

    to_skip = cfg.skip
    for row in reader:
        if to_skip > 0:
            to_skip -= 1
            continue

        row.pop(None, None)
        yield row


def is_stdin(path: Optional[Path]) -> bool:
    return path in (None, Path("-"))


def find_source(path: Path, rules: Path) -> Path:
    try:
        path = path.expanduser()
    except RuntimeError:
        pass

    if path.is_absolute():
        return path

    try_paths = [
        Path(os.getenv("XDG_DOWNLOAD_DIR", Path.home() / "Downloads")) / path,
        rules.absolute().parent / path,
    ]

    for possibility in try_paths:
        if possibility.exists():
            return possibility

    return path.absolute()


def assign_input_to_transaction(transaction: Transaction, input_data: Dict[Field, Any]):
    for field_, val in input_data.items():
        if field_.id:
            try:
                dest_field = getattr(transaction, field_.base)
                dest_field[field_.id] = val
            except (AttributeError, KeyError) as e:
                raise InputError(f"cannot assign multi-field '{field_}'") from e
        else:
            setattr(transaction, field_.base, val)


def get_transactions(cfg: Config) -> Iterable[Transaction]:
    getters = {"csv": partial(get_csv, cfg=cfg.csv)}

    filetype = (
        cfg.filetype
        if cfg.filetype
        else (cfg.source.suffix.lstrip(".") if cfg.source else "")
    )
    getter = getters.get(filetype)
    if not getter:
        raise InputError(f"unsupported filetype for source '{cfg.source}': {filetype}")

    fileobj = sys.stdin if is_stdin(cfg.source) else cfg.source.open()  # type: ignore[union-attr]
    with fileobj:
        for posting_input in getter(fileobj):
            preprocessed_input = preprocess_input(posting_input, cfg)

            transaction = cfg.default.into_transaction()
            assign_input_to_transaction(transaction, preprocessed_input)

            yield transaction


def ordered_transactions(it: Iterable[Transaction]) -> list[Transaction]:
    transactions = list(it)

    if len(transactions) < 2:
        return []

    # when first transaction is later than the last one, we assume that global order
    # of transactions is e[-1], e[-2], ... e[0] (earliest transaction is the
    # last one on the list). We can't simply sort this in reversed order,
    # because Python sort is stable and it'd reverse the order of transactions
    # on the same day.
    if transactions[0].date > transactions[-1].date:
        transactions.reverse()

    # In case transactions arent' already sorted in the input...
    transactions.sort(key=attrgetter("date"))
    return transactions


def override_config(config: Config, override: list[tuple[str, str]]):
    for key, val in override:
        setattr(config, key, val)


def read_latest(latest_path: Path) -> List[Latest]:
    try:
        lines = latest_path.read_text("utf-8").splitlines()
    except OSError:
        lines = []

    latestreader = csv.reader(lines)
    latest = [Latest.from_latest_csv(row) for row in latestreader]
    latest.sort(key=attrgetter("date"))
    return latest


def get_latest(transactions: List[Transaction]) -> List[Latest]:
    if not transactions:
        return []

    maxdate = max(transactions, key=attrgetter("date")).date
    return [Latest.from_transaction(tr) for tr in transactions if tr.date == maxdate]


def write_latest(latest: List[Latest], latest_path: Path):
    if not latest:
        return

    with uopen(latest_path, mode="w", encoding="utf-8") as f:
        latestwriter = csv.writer(f)
        for lt in latest:
            latestwriter.writerow([lt.date, lt.description, lt.amount, lt.commodity])


def validate_config(cfg: Config, args: argparse.Namespace):
    if is_stdin(cfg.source) and not cfg.filetype:
        raise ValueError(
            "filetype must be set when reading a source from standard input"
        )

    if not is_stdin(cfg.source):
        cfg.source = find_source(cfg.source, args.rules)  # type: ignore[arg-type]

    if not args.latest:
        parentdir = cfg.source.parent if cfg.source else Path()
        source_name = cfg.source.name if cfg.source else "-"
        args.latest = parentdir / f".latest.{source_name}"


def filter_latest(
    transactions: List[Transaction], latest: List[Latest]
) -> List[Transaction]:
    latest_copy = latest[:]

    def rule(transaction: Transaction):
        if latest_copy and transaction.date < latest_copy[0].date:
            return False
        elif latest_copy and transaction.date == latest_copy[0].date:
            cmp = Latest.from_transaction(transaction)
            try:
                i = latest_copy.index(cmp)
                del latest_copy[i]
            except ValueError:
                return True
            else:
                return False
        return True

    return list(filter(rule, transactions))


def apply_rules(
    transactions: List[Transaction], rules: List[Tuple[Rule, ConditionT]]
) -> List[Transaction]:
    transformed = []
    for transaction in transactions:
        for rule, cond in rules:
            if not cond or cond(transaction):
                rule(transaction)

            if transaction.skipped or transaction.rules_done or transaction.ended:
                break

        if not transaction.skipped:
            transaction.normalize()
            transformed.append(transaction)

        if transaction.ended:
            break

    return transformed


def amount2str(posting: Posting):
    amount = f"{posting.amount:.2f}" if posting.amount is not None else ""
    commodity = posting.commodity if posting.commodity is not None else ""

    # default symbol side is right
    symbolside = posting.symbolside if posting.symbolside else SymbolSide.right

    space = " " if symbolside in (SymbolSide.left, SymbolSide.right) else ""
    if symbolside in (SymbolSide.left, SymbolSide.leftjoin):
        return commodity + space + amount
    return amount + space + commodity


def print_transaction(transaction: Transaction, file_: uopen) -> None:
    maxacc = max(len(p.account) for p in transaction.postings)

    file_.writeln(f"{transaction.date} {transaction.description}")
    for posting in transaction.postings:
        negative = -1 if posting.amount and posting.amount < 0 else 0
        padding = 5 + maxacc + negative
        file_.writeln(f"    {posting.account:<{padding}}{amount2str(posting)}".rstrip())


def print_transactions(transactions: List[Transaction]):
    if not transactions:
        return

    with uopen(mode="a+", encoding="utf-8") as f:
        if f.size > 0:
            f.writeln()

        first = True
        for transaction in transactions:
            if not first:
                f.writeln()
            print_transaction(transaction, f)
            first = False


def _real_main(args: argparse.Namespace):
    uopen.configure(args.output, args.dry_run)

    cfg = Config()
    cfg.load(args.rules)
    override_config(cfg, args.options)
    validate_config(cfg, args)

    all_transactions = ordered_transactions(get_transactions(cfg))

    current_latest = read_latest(args.latest)
    latest_transactions = filter_latest(all_transactions, current_latest)
    new_latest = get_latest(latest_transactions)

    to_print = apply_rules(latest_transactions, cfg.rules)

    write_latest(new_latest, args.latest)
    # Print transactions ONLY when we're sure that ALL data is valid
    print_transactions(to_print)

    if not to_print:
        eprint("No transactions")
    else:
        eprint(f"Processed {len(to_print)} new transaction(s)")


def main(argv: Optional[List[str]] = None):
    sys.dont_write_bytecode = True  # to not clutter directories with rules.py

    args = prepare_args(argv)

    try:
        _real_main(args)
    except Exception as e:
        import traceback

        eprint(f"error: {str(e)}")

        if args.debug:
            traceback.print_tb(e.__traceback__)
            return 1

        if isinstance(e, InputError):
            return 1

        for f in traceback.extract_tb(e.__traceback__):
            if f.filename != __file__:
                eprint(f"  in: {f.filename}:{f.lineno}:  {f.line}")

        return 1


if __name__ == "__main__":
    sys.exit(main())
