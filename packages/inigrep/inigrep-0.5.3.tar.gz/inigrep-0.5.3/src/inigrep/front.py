#!/usr/bin/python3

from __future__ import annotations
from typing import Callable, Iterable
import functools
import os

from .core import (
    FileReader,
    _r_clone,
    _r_list_keys,
    _r_list_paths,
    _r_list_sections,
    _r_raw_values,
    _r_values,
    SingleFileReader,
    KeypathT,
    SectionT,
)

__doc__ = """
inigrep
=======

grep for (some) INIs

inigrep is designed to read a particular simplistic dialect of
INI configuration files. In a sense, it can be considered as
a "grep for INIs", in that rather than parsing the file into
a typed memory structure for later access, it passes file each
time a query is done, and spits out relevant parts; treating
everything as text. Hence, it's not intended as replacement
for a full-blown configuration system but rather a quick & dirty
"swiss axe" for quick & dirty scripts.

That's not to say that you cannot do things nicely; but don't
count on speed -- well since you're using bash you obviously
don't -- and compliance -- simple things are simple, but there
are a bit unusual pitfalls.


The format by examples
----------------------

The most basic example understood by inigrep is identical
to most INI formats:

    # Let's call this simple.ini

    [foo]
        bar = baz
        qux = quux

    [corge]
        grault = graply

Structure here is obvious: two sections named `foo` and `corge`,
the first one has two key/value pairs and the other has one pair.

Getting values from this file is trivial:

    inigrep foo.bar simple.ini
    inigrep foo.qux simple.ini
    inigrep corge.grault simple.ini

would list `baz`, `quux` and `graply`.

This is where 80% of use cases are covered.


Multi-line
----------

Multi-line values are rather unusual but very simple:

    [lipsum]

        latin = Lorem ipsum dolor sit amet, consectetur adipiscing
        latin = elit, sed do eiusmod tempor incididunt ut labore et
        latin = dolore magna aliqua. Ut enim ad minim veniam, quis
        latin = ...

        english = [32] But I must explain to you how all this mistaken
        english = idea of denouncing of a pleasure and praising pain
        english = was born and I will give you a complete account of
        english = ...

This file can be read as:

    inigrep lipsum.latin lipsum.ini
    inigrep lipsum.english lipsum.ini


Exploration
-----------

Other than basic value retrieval, inigrep allows you to look around
first. For example, to list all keypaths available in a file:

    inigrep -P simple.ini

In case of simple.ini, this would print:

    foo.bar
    foo.qux
    corge.grault

Similarly:

    inigrep -S simple.ini

would list just the section names:

    foo
    corge

and

    inigrep -K foo simple.ini

would list all keys from section 'foo'

    bar
    qux
"""


def clone(files: list[str], kpath: str = '.') -> Iterable[str]:
    """
    Return replica of INI file that is concatenation of *files*.
    """
    for value in _r_clone(reader=FileReader(files), kpath=kpath):
        yield str(value)


def values(files: list[str], kpath: str) -> Iterable[str]:
    """
    Return list of values from files *files* at key path *kpath*.

    *kpath* must be key path, i.e. string containing section and
    key names delimited by period.

    *files* must list of file paths.
    """
    for value in _r_values(reader=FileReader(files), kpath=kpath):
        yield str(value)


def raw_values(files: list[str], kpath: str) -> Iterable[str]:
    """
    Return list of raw values found in *files* at key path *kpath*.

    Same as values(), but uses raw inigrep engine, which keeps in-line
    comments and value leading/trailing whitespace.
    """
    for value in _r_raw_values(reader=FileReader(files), kpath=kpath):
        yield str(value)


def list_sections(files: list[str]) -> Iterable[str]:
    """
    Return list of sections found in *files*.
    """
    for value in _r_list_sections(reader=FileReader(files)):
        yield str(value)


def list_keys(files: list[str], section: str) -> Iterable[str]:
    """
    Return list of keys found in *files* under *section*.
    """
    return _r_list_keys(reader=FileReader(files), section=section)


def list_paths(files: list[str], keypath: str = '.') -> Iterable[str]:
    """
    Return list of all key paths found by *in files*.
    """
    return _r_list_paths(reader=FileReader(files), keypath=keypath)


def load(files: list[str]) -> Ini:
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_files().
    """
    return Ini.from_files(files)


def load_existent(files: list[str]) -> Ini:
    """
    Create Ini file from concatenated files at paths *files*.

    Same as Ini.from_existent_files().
    """
    return Ini.from_existent_files(files)


class Ini:
    """
    Set of cached INI files
    """

    @classmethod
    def from_files(cls, files: list[str]) -> Ini:
        """
        Initialize Ini object containing lines of all *files*.
        """
        cache = []
        for path in files:
            for line in SingleFileReader(path):
                cache.append(line)
        return cls(cache)

    @classmethod
    def from_existent_files(cls, files: list[str]) -> Ini:
        """
        Initialize Ini object containing lines of all existent *files*.

        Similar to Ini.from_files(), but non-existent files are silently
        ignored.
        """
        cache = []
        for path in files:
            if not os.path.exists(path):
                continue
            for line in SingleFileReader(path):
                cache.append(line)
        return cls(cache)

    def __init__(self, cache):
        self._cache = cache

    def branch(self, prefix: str) -> Ini:
        """
        Create new Ini object containing only sections that
        start with *prefix*.
        """
        want_scts: list[str] = []
        lines = []
        for sct in self.list_sections():
            if sct.startswith(prefix + '.'):
                want_scts.append(sct.replace(prefix + '.', '', 1))
        for sct in want_scts:
            lines.append('[%s]' % sct)
            for key in self.list_keys('%s.%s' % (prefix, sct)):
                branch_keypath = '%s.%s.%s' % (prefix, sct, key)
                for value in self.raw_values(branch_keypath):
                    lines.append('    %s =%s' % (key, value))
        return self.__class__(lines)

    def mkreader1(self, *kpath: str) -> Callable[[], str | None]:
        """
        Create function to read single-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either single-line string corresponding to value
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _read1(*kpath):
            out = list(self.values('.'.join(kpath)))
            if out:
                return out[0]
            return None
        return functools.partial(_read1, *kpath)

    def mkreaderN(self, *kpath: str) -> Callable[[], list[str]]:
        """
        Create function to read multi-line value at *kpath*.

        *kpath* must be list of the path elements.

        Return function which can be called without parameters and
        will return either list of strings corresponding to values
        at the key path *kpath*, or None, if there's no such value
        in the whole Ini object.
        """
        def _readN(*kpath):
            return list(self.values('.'.join(kpath)))
        return functools.partial(_readN, *kpath)

    def _cache_reader(self):
        for line in self._cache:
            yield line

    def data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all INI data

        Uses basic inigrep engine.

        A flat dictionary is returned, mapping all valid
        keypaths to lists of lines.
        """
        data: dict[str, list[str]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.values(kpath))
        return data

    def clone(self, kpath: str = '.') -> Iterable[str]:
        """
        Return lines of INI file with the same data as in this object
        """
        vg = _r_clone(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def raw_data(self) -> dict[str, list[str]]:
        """
        Return dictionary containing all raw INI data

        Same as Ini.data(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        data: dict[str, list[str]] = {}
        for kpath in self.list_paths():
            data[kpath] = list(self.raw_values(kpath))
        return data

    def values(self, kpath: str) -> Iterable[str]:
        """
        Return list of values at key path *kpath*.

        Uses basic inigrep engine.
        """
        vg = _r_values(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def raw_values(self, kpath: str) -> Iterable[str]:
        """
        Return list of values at key path *kpath*.

        Same as Ini.values(), but uses raw inigrep engine (keeps
        comments and value leading/trailing whitespace).
        """
        vg = _r_raw_values(
            reader=self._cache_reader(),
            kpath=KeypathT(kpath),
        )
        return (str(v) for v in vg)

    def list_sections(self) -> Iterable[str]:
        """
        Return list of sections.

        Similar to Ini.values(), but uses section listing engine.
        """
        vg = _r_list_sections(
            reader=self._cache_reader(),
        )
        return (str(v) for v in vg)

    def list_keys(self, section: str) -> Iterable[str]:
        """
        Return list of keys under *section*.

        Similar to Ini.values(), but uses key listing engine.
        """
        vg = _r_list_keys(
            reader=self._cache_reader(),
            section=SectionT(section),
        )
        return (str(v) for v in vg)

    def list_paths(self, keypath: str = '.') -> Iterable[str]:
        """
        Return list of all defined key paths.

        Similar to Ini.values(), but uses key path listing engine.
        """
        vg = _r_list_paths(
            reader=self._cache_reader(),
            keypath=KeypathT(keypath),
        )
        return (str(v) for v in vg)
