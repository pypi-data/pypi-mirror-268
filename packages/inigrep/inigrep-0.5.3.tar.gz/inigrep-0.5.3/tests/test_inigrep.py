import itertools

import hoover

import tests.fw

import inigrep.front


def gamehint(raw=False):
    """
    Create oracle hint for games_with_spaces.ini
    """
    ns = [0, 1, 2, 3, 4]
    chars = ['', ' ', '	', ' 	', '	 ']
    for nvec in itertools.product(ns, ns, ns, ns, ns):
        char1, char2, char3, char4, char5 = [chars[n] for n in nvec]
        parts = ['value', char4] + [str(n) for n in nvec]
        if raw:
            parts = [char3] + parts + [char5]
        yield ''.join(parts)


class ValuesDriver(tests.fw.InigrepDriver):

    def fetch(self, files, kpath):
        return list(inigrep.front.values(files, kpath))


class IniValuesDriver(tests.fw.InigrepDriver):

    def fetch(self, files, kpath):
        return list(inigrep.front.load(files).values(kpath))


class ValuesTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        ValuesDriver,
        IniValuesDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            kpath='',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '' is missing period",
            }
        )

        yield self.mkcase(
            kpath='.bar',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '.bar' is missing section",
            }
        )

        yield self.mkcase(
            kpath='foo.',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: 'foo.' is missing key",
            }
        )

        yield self.mkcase(
            kpath='.',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '.' is missing section and key",
            },
        )

        yield self.mkcase(
            kpath='.',
            files=['tests/data/foo.ini'],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '.' is missing section and key",
            },
        )

        yield self.mkcase(
            kpath='foo.bar',
            files=['tests/data/foo.ini'],
            hint=[
                'baz1',
                'baz2',
                'baz3',
            ],
        )

        yield self.mkcase(
            kpath='bar.qux',
            files=['tests/data/foo.ini'],
            hint=[
                'quux',
            ],
        )

        yield self.mkcase(
            kpath='foo.quux',
            files=['tests/data/foo.ini'],
            hint=[],
        )

        yield self.mkcase(
            kpath='with.comments.value',
            files=['tests/data/foo.ini'],
            hint=[
                '0',
            ],
        )

        yield self.mkcase(
            kpath='0.1',
            files=['tests/data/foo.ini'],
            hint=['2'],
        )

        yield self.mkcase(
            kpath='maybe spaced.spaced key',
            files=['tests/data/games_with_spaces.ini'],
            hint=list(gamehint()),
        )


class RawValuesDriver(tests.fw.InigrepDriver):

    def fetch(self, files, kpath):
        return list(inigrep.front.raw_values(files, kpath))


class IniRawValuesDriver(tests.fw.InigrepDriver):

    def fetch(self, files, kpath):
        return list(inigrep.front.load(files).raw_values(kpath))


class RawValuesTest(ValuesTest):

    driver_classes = [
        hoover.HintingDriver,
        RawValuesDriver,
        IniRawValuesDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            kpath='',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '' is missing period",
            },
        )

        yield self.mkcase(
            kpath='.',
            files=[],
            hint_ex={
                'cls': "KeypathError",
                's': "invalid keypath: '.' is missing section and key",
            },
        )

        yield self.mkcase(
            kpath='foo.bar',
            files=['tests/data/foo.ini'],
            hint=[
                ' baz1',
                ' baz2',
                ' baz3',
            ],
        )

        yield self.mkcase(
            kpath='bar.qux',
            files=['tests/data/foo.ini'],
            hint=[
                ' quux',
            ],
        )

        yield self.mkcase(
            kpath='foo.quux',
            files=['tests/data/foo.ini'],
            hint=[],
        )

        yield self.mkcase(
            kpath='with.comments.value',
            files=['tests/data/foo.ini'],
            hint=[
                ' 0   # roughly',
            ],
        )

        yield self.mkcase(
            kpath='0.1',
            files=['tests/data/Foo.ini'],
            hint=[' 2'],
        )

        yield self.mkcase(
            kpath='maybe spaced.spaced key',
            files=['tests/data/games_with_spaces.ini'],
            hint=list(gamehint(raw=True)),
        )


class ListSectionsDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, files):
        return list(inigrep.front.list_sections(files))


class IniListSectionsDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, files):
        return list(inigrep.load(files).list_sections())


class ListSectionsTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        ListSectionsDriver,
        IniListSectionsDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            files=[],
            hint=[],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini'],
            hint=[
                'foo',
                'bar',
                '0',
                'emp',
                'with.dots',
                'with.comments',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/foo.ini'],
            hint=[
                'foo',
                'bar',
                '0',
                'emp',
                'with.dots',
                'with.comments',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'Foo',
                'Bar',
                '0',
                'Emp',
                'With.Dots',
                'With.Comments',
                'foo',
                'bar',
                'emp',
                'with.dots',
                'with.comments',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
                'foo',
                'bar',
                '0',
                'emp',
                'with.dots',
                'with.comments',
                'Foo',
                'Bar',
                'Emp',
                'With.Dots',
                'With.Comments',
            ],
        )


class ListKeypathsDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, **args):
        return list(inigrep.front.list_paths(**args))


class IniListKeypathsDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, files):
        return list(inigrep.load(files).list_paths())


class ListKeypathsTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        ListKeypathsDriver,
        IniListKeypathsDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            files=[],
            hint=[],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini'],
            hint=[
                'foo.bar',
                'foo.baz',
                'bar.qux',
                '0.1',
                'with.dots.dotty',
                'with.comments.value',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini'],
            hint=[
                'Foo.Bar',
                'Foo.Baz',
                'Bar.Qux',
                '0.1',
                'With.Dots.Dotty',
                'With.Comments.Value',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/foo.ini'],
            hint=[
                'foo.bar',
                'foo.baz',
                'bar.qux',
                '0.1',
                'with.dots.dotty',
                'with.comments.value',
                'foo.renegade',   # TODO: not sure we want this, really
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'Foo.Bar',
                'Foo.Baz',
                'Bar.Qux',
                '0.1',
                'With.Dots.Dotty',
                'With.Comments.Value',
                'Foo.renegade',   # TODO: not sure we want this, really
                'foo.bar',
                'foo.baz',
                'bar.qux',
                'with.dots.dotty',
                'with.comments.value',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
                'foo.bar',
                'foo.baz',
                'bar.qux',
                '0.1',
                'with.dots.dotty',
                'with.comments.value',
                'foo.Renegade',   # TODO: not sure we want this, really
                'Foo.Bar',
                'Foo.Baz',
                'Bar.Qux',
                'With.Dots.Dotty',
                'With.Comments.Value',
            ],
        )


class ListKeysDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files', 'section']

    def fetch(self, files, section):
        return list(inigrep.front.list_keys(files, section))


class IniListKeysDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files', 'section']

    def fetch(self, files, section):
        return list(inigrep.load(files).list_keys(section))


class ListKeysTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        ListKeysDriver,
        IniListKeysDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            section=[''],
            files=[],
            hint_ex=self.mkhint_ex(
                "invalid type: section must be str, got list"
            ),
        )

        yield self.mkcase(
            section='',
            files=[],
            hint_ex=self.mkhint_ex(
                "section must not be empty: ''",
            ),
        )

        yield self.mkcase(
            section='nonexistent',
            files=['tests/data/foo.ini'],
            hint=[
            ],
        )

        yield self.mkcase(
            section='emp',
            files=['tests/data/foo.ini'],
            hint=[
            ],
        )

        yield self.mkcase(
            section='nonexistent',
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
            ],
        )

        yield self.mkcase(
            section='non.existent',
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
            ],
        )

        yield self.mkcase(
            section='foo',
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
                'bar',
                'baz',
                'Renegade',       # TODO: not sure we want this, really
            ],
        )

        yield self.mkcase(
            section='foo',
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'bar',
                'baz',
            ],
        )

        yield self.mkcase(
            section='Foo',
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'Bar',
                'Baz',
                'renegade',
            ],
        )

        yield self.mkcase(
            section='bar',
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'qux',
            ],
        )

        yield self.mkcase(
            section='Bar',
            files=['tests/data/Foo.ini'],
            hint=[
                'Qux',
            ],
        )

        yield self.mkcase(
            section='With.Dots',
            files=['tests/data/foo.ini', 'tests/data/foo.ini'],
            hint=[
            ],
        )

        yield self.mkcase(
            section='With.Dots',
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
                'Dotty',
            ],
        )

        yield self.mkcase(
            section='With.Dots',
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                'Dotty',
            ],
        )

        yield self.mkcase(
            section='With.Dots',
            files=['tests/data/Foo.ini', 'tests/data/Foo.ini'],
            hint=[
                'Dotty',
            ],
        )


class CloneDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, **args):
        return list(inigrep.front.clone(**args))


class IniCloneDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, files, **args):
        return list(inigrep.load(files).clone(**args))


class CloneTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        CloneDriver,
        IniCloneDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            files=[],
            hint=[],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini'],
            hint=[
                '',
                '[foo]',
                '    bar = baz1',
                '    baz = heya',
                '    bar = baz2',
                '',
                '[bar]',
                '    qux = quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[emp]',
                '',
                '[with.dots]',
                '    dotty = polka',
                '',
                '[with.comments]',
                '    value = 0   # roughly',
                '',
                '[foo]',
                '    bar = baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini'],
            hint=[
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Bar]',
                '    Qux = Quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[Emp]',
                '',
                '[With.Dots]',
                '    Dotty = Polka',
                '',
                '[With.Comments]',
                '    Value = 0   ; Precisely',
                '',
                '[Foo]',
                '    Bar = Baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/foo.ini'],
            hint=[
                '',
                '[foo]',
                '    bar = baz1',
                '    baz = heya',
                '    bar = baz2',
                '',
                '[bar]',
                '    qux = quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[emp]',
                '',
                '[with.dots]',
                '    dotty = polka',
                '',
                '[with.comments]',
                '    value = 0   # roughly',
                '',
                '[foo]',
                '    bar = baz3',
                '    renegade = sectionless key',   # TODO: don't want this
                '',
                '[foo]',
                '    bar = baz1',
                '    baz = heya',
                '    bar = baz2',
                '',
                '[bar]',
                '    qux = quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[emp]',
                '',
                '[with.dots]',
                '    dotty = polka',
                '',
                '[with.comments]',
                '    value = 0   # roughly',
                '',
                '[foo]',
                '    bar = baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint=[
                '',
                '[foo]',
                '    bar = baz1',
                '    baz = heya',
                '    bar = baz2',
                '',
                '[bar]',
                '    qux = quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[emp]',
                '',
                '[with.dots]',
                '    dotty = polka',
                '',
                '[with.comments]',
                '    value = 0   # roughly',
                '',
                '[foo]',
                '    bar = baz3',
                '    Renegade = Sectionless Key',   # TODO: don't want this
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Bar]',
                '    Qux = Quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[Emp]',
                '',
                '[With.Dots]',
                '    Dotty = Polka',
                '',
                '[With.Comments]',
                '    Value = 0   ; Precisely',
                '',
                '[Foo]',
                '    Bar = Baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint=[
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Bar]',
                '    Qux = Quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[Emp]',
                '',
                '[With.Dots]',
                '    Dotty = Polka',
                '',
                '[With.Comments]',
                '    Value = 0   ; Precisely',
                '',
                '[Foo]',
                '    Bar = Baz3',
                '    renegade = sectionless key',   # TODO: don't want this
                '',
                '[foo]',
                '    bar = baz1',
                '    baz = heya',
                '    bar = baz2',
                '',
                '[bar]',
                '    qux = quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[emp]',
                '',
                '[with.dots]',
                '    dotty = polka',
                '',
                '[with.comments]',
                '    value = 0   # roughly',
                '',
                '[foo]',
                '    bar = baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/Foo.ini'],
            hint=[
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Bar]',
                '    Qux = Quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[Emp]',
                '',
                '[With.Dots]',
                '    Dotty = Polka',
                '',
                '[With.Comments]',
                '    Value = 0   ; Precisely',
                '',
                '[Foo]',
                '    Bar = Baz3',
                '    Renegade = Sectionless Key',   # TODO: don't want this
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Bar]',
                '    Qux = Quux',
                '',
                '[0]',
                '    1 = 2',
                '',
                '[Emp]',
                '',
                '[With.Dots]',
                '    Dotty = Polka',
                '',
                '[With.Comments]',
                '    Value = 0   ; Precisely',
                '',
                '[Foo]',
                '    Bar = Baz3',
            ],
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/Foo.ini'],
            kpath='Foo.',
            hint=[
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Foo]',
                '    Bar = Baz3',
                '    Renegade = Sectionless Key',   # TODO: don't want this
                '',
                '[Foo]',
                '    Bar = Baz1',
                '    Baz = Heya',
                '    Bar = Baz2',
                '',
                '[Foo]',
                '    Bar = Baz3',
            ],
        )


class IniDataDriver(tests.fw.InigrepDriver):

    mandatory_args = ['files']

    def fetch(self, files, **args):
        return inigrep.load(files).data()


class IniDataTest(tests.fw.InigrepTestCase):

    driver_classes = [
        hoover.HintingDriver,
        IniDataDriver,
    ]

    @property
    def cases(self):

        yield self.mkcase(
            files=[],
            hint={},
        )

        yield self.mkcase(
            files=['tests/data/foo.ini'],
            hint={
                '0.1': [
                    '2',
                ],
                'bar.qux': [
                    'quux',
                ],
                'foo.bar': [
                    'baz1',
                    'baz2',
                    'baz3',
                ],
                'foo.baz': [
                    'heya',
                ],
                'with.comments.value': [
                    '0',
                ],
                'with.dots.dotty': [
                    'polka',
                ],
            },
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini'],
            hint={
                '0.1': [
                    '2',
                ],
                'Bar.Qux': [
                    'Quux',
                ],
                'Foo.Bar': [
                    'Baz1',
                    'Baz2',
                    'Baz3',
                ],
                'Foo.Baz': [
                    'Heya',
                ],
                'With.Comments.Value': [
                    '0',
                ],
                'With.Dots.Dotty': [
                    'Polka',
                ],
            },
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/foo.ini'],
            hint={
                '0.1': [
                    '2',
                    '2',
                ],
                'bar.qux': [
                    'quux',
                    'quux',
                ],
                'foo.bar': [
                    'baz1',
                    'baz2',
                    'baz3',
                    'baz1',
                    'baz2',
                    'baz3',
                ],
                'foo.baz': [
                    'heya',
                    'heya',
                ],
                'foo.renegade': [
                    'sectionless key'
                ],
                'with.comments.value': [
                    '0',
                    '0',
                ],
                'with.dots.dotty': [
                    'polka',
                    'polka',
                ],
            },
        )

        yield self.mkcase(
            files=['tests/data/foo.ini', 'tests/data/Foo.ini'],
            hint={
                '0.1': [
                    '2',
                    '2',
                ],
                'bar.qux': [
                    'quux',
                ],
                'foo.bar': [
                    'baz1',
                    'baz2',
                    'baz3',
                ],
                'foo.baz': [
                    'heya',
                ],
                'foo.Renegade': [
                    'Sectionless Key'
                ],
                'with.comments.value': [
                    '0',
                ],
                'with.dots.dotty': [
                    'polka',
                ],
                'Bar.Qux': [
                    'Quux',
                ],
                'Foo.Bar': [
                    'Baz1',
                    'Baz2',
                    'Baz3',
                ],
                'Foo.Baz': [
                    'Heya',
                ],
                'With.Comments.Value': [
                    '0',
                ],
                'With.Dots.Dotty': [
                    'Polka',
                ],
            },
        )

        yield self.mkcase(
            files=['tests/data/Foo.ini', 'tests/data/foo.ini'],
            hint={
                '0.1': [
                    '2',
                    '2',
                ],
                'bar.qux': [
                    'quux',
                ],
                'foo.bar': [
                    'baz1',
                    'baz2',
                    'baz3',
                ],
                'foo.baz': [
                    'heya',
                ],
                'with.comments.value': [
                    '0',
                ],
                'with.dots.dotty': [
                    'polka',
                ],
                'Bar.Qux': [
                    'Quux',
                ],
                'Foo.Bar': [
                    'Baz1',
                    'Baz2',
                    'Baz3',
                ],
                'Foo.Baz': [
                    'Heya',
                ],
                'Foo.renegade': [
                    'sectionless key'
                ],
                'With.Comments.Value': [
                    '0',
                ],
                'With.Dots.Dotty': [
                    'Polka',
                ],
            },
        )
