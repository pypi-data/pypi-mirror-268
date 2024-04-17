from __future__ import annotations
import sys
from typing import Iterable
from dataclasses import dataclass, field

from ._meta import VERSION
from .core import (
    ClonedLineT,
    LineT,
    ValueT,
    RawValueT,
    KeyT,
    SectionT,
    KeypathT,
    _r_values,
    _r_raw_values,
    _r_clone,
    _r_list_keys,
    _r_list_sections,
    _r_list_paths,
    KeypathError,
)
import inigrep
import inigrep.front


_USAGE: str = """
usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -c|--clone [file]...
    inigrep [-1] -e|--basic section.key [file]...
    inigrep [-1] -r|--raw section.key [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help
    inigrep --version
"""

__doc__ = """
Query INI file(s) for data

Usage:
    inigrep [-1] [section].[key] [file]...
    inigrep [-1] -c|--clone [file]...
    inigrep [-1] -e|--basic section.key [file]...
    inigrep [-1] -r|--raw section.key [file]...
    inigrep [-1] -K|--lskey section [file]...
    inigrep [-1] -S|--lssct [file]...
    inigrep [-1] -P|--lspth [file]...
    inigrep --help
    inigrep --version

First form implies the basic engine.

Option *-r* switches to raw mode, in which comments,
empty lines and whitespace are all preserved in applicable
contexts.

Key *keypath* consists of section name and key name delimited
by dot. Note that keypath may contain dots but key may not.

If *file* is not given or is a single dash, standard input
is read. Note that standard input is not duplicated in case
of multiple dashes.

If suitable key is found at multiple lines, all values
are printed, which allows for creating multi-line values.
Providing *-1* argument, however, always prints only one
line.

Options -K, -S and -P can be used for inspecting file structure;
-K needs an argument of section name and will list all keys from
that section. -S will list all sections and -P will list all
existing keypaths.


#### Examples ####

Having INI file such as

    [foo]
    bar=baz
    quux=qux
    quux=qux2
    quux=qux3

* `inigrep foo.bar ./file.ini` gives "bar".
* `inigrep foo.quux ./file.ini` gives three lines "qux", "qux2"
    and "qux3".
* `inigrep -P ./file.ini` gives two lines "foo.bar" and "foo.quux".
* `inigrep -K foo ./file.ini` gives two lines "bar" and "quux".
* `inigrep -S ./file.ini` gives "foo".
"""


class UsageError(RuntimeError):
    pass


class HelpNeeded(RuntimeError):
    pass


class VersionNeeded(RuntimeError):
    pass


@dataclass
class Args:
    args: list[str]

    def take1(self) -> str:
        if not self.args:
            raise UsageError('missing argument')
        return self.args.pop(0)

    def take2(self) -> tuple[str, str]:
        if len(self.args) < 2:
            raise UsageError('missing arguments')
        return self.args.pop(0), self.args.pop(0)

    def next(self) -> str:
        return self.args[0]

    def next_is(self, *cases) -> bool:
        return self.args[0] in cases

    def rest(self) -> list[str]:
        return self.args[:]


class Engine:

    def __init__(self, **fnargs):
        self.fnargs = fnargs

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[str]:
        raise NotImplementedError

    def run(self, files: list[str]) -> Iterable[str]:
        raise NotImplementedError


class NoEngine(Engine):

    pass


class BasicEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[ValueT]:
        return _r_values(reader=reader, **self.fnargs)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.values(files=files, **self.fnargs)


class RawEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[RawValueT]:
        return _r_raw_values(reader=reader, **self.fnargs)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.raw_values(files=files, **self.fnargs)


class ListKeysEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[KeyT]:
        return _r_list_keys(reader=reader, **self.fnargs)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.list_keys(files=files, **self.fnargs)


class ListSectionsEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[SectionT]:
        return _r_list_sections(reader=reader)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.list_sections(files=files)


class ListPathsEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[KeypathT]:
        return _r_list_paths(reader=reader, **self.fnargs)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.list_paths(files=files, **self.fnargs)


class CloneEngine(Engine):

    def _r_run(self, reader: Iterable[LineT]
               ) -> Iterable[ClonedLineT]:
        return _r_clone(reader=reader, **self.fnargs)

    def run(self, files: list[str]) -> Iterable[str]:
        return inigrep.front.clone(files=files, **self.fnargs)


@dataclass
class Options:
    engine: Engine = NoEngine()
    oneline: bool = False
    files: list[str] = field(default_factory=list)

    @classmethod
    def from_args(cls, args: list[str]) -> Options:
        o = cls()
        a = Args(args)
        while a.rest():
            if a.next_is('--help'):
                raise HelpNeeded()
            if a.next_is('--version'):
                raise VersionNeeded()
            elif a.next_is('-1'):
                o.oneline = True
                a.take1()
            elif a.next_is('-c', '--clone'):
                o.engine = CloneEngine()
                a.take1()
            elif a.next_is('-s', '--clsct'):
                o.engine = CloneEngine(kpath=a.take2()[1] + '.')
            elif a.next_is('-e', '--basic'):
                o.engine = BasicEngine(kpath=a.take2()[1])
            elif a.next_is('-r', '--raw'):
                o.engine = RawEngine(kpath=a.take2()[1])
            elif a.next_is('-K', '--lskey'):
                o.engine = ListKeysEngine(section=a.take2()[1])
            elif a.next_is('-S', '--lssct'):
                o.engine = ListSectionsEngine()
                a.take1()
            elif a.next_is('-P', '--lspth'):
                o.engine = ListPathsEngine()
                a.take1()
            elif a.next().startswith('-'):
                raise UsageError('unknown engine: %s' % a.next())
            else:
                break
        if isinstance(o.engine, NoEngine):
            o.engine = BasicEngine(kpath=a.take1())
        files = a.rest()
        if not files:
            files = ['-']
        elif files == ['']:
            # FIXME: this is strange but turns out saturnin relies on it
            files = ['-']
        o.files = files
        return o


def main() -> None:

    try:
        options = Options.from_args(sys.argv[1:])
    except UsageError as e:
        sys.stderr.write('%s\n' % _USAGE[1:])
        sys.stderr.write('error: %s\n' % e)
        sys.exit(2)
    except HelpNeeded as e:
        sys.stderr.write('%s\n' % __doc__)
        sys.stderr.write('%s\n' % e)
        sys.exit(0)
    except VersionNeeded:
        sys.stderr.write('%s\n' % VERSION)
        sys.exit(0)

    gen = options.engine.run(files=options.files)

    try:
        for line in gen:
            print(line)
            if options.oneline:
                break
    except KeypathError as e:
        sys.stderr.write('%s\n' % e)
        sys.exit(2)
