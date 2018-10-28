# Copyright (c) 2016-2018 Renata Hodovan, Akos Kiss.
#
# Licensed under the BSD 3-Clause License
# <LICENSE.rst or https://opensource.org/licenses/BSD-3-Clause>.
# This file may not be copied, modified, or distributed except
# according to those terms.

import pytest

from os.path import join

import fuzzinator

from common_fuzzer import resources_dir

mock_tests = join(resources_dir, 'mock_tests')


@pytest.mark.parametrize('pattern, contents, exp', [
    (join(mock_tests, '*'), True, {b'foo\n', b'bar\n', b'baz\n'}),
    (join(mock_tests, '**', '*'), True, {b'foo\n', b'bar\n', b'baz\n', b'qux\n'}),
    (join(mock_tests, '*'), False, {join(mock_tests, 'baz.txt'), join(mock_tests, 'bar.txt'), join(mock_tests, 'foo.txt')}),
    (join(mock_tests, '**', '*'), False, {join(mock_tests, 'baz.txt'), join(mock_tests, 'bar.txt'), join(mock_tests, 'foo.txt'), join(mock_tests, 'subdir', 'qux.txt')}),
])
def test_list_directory(pattern, contents, exp):
    fuzzer = fuzzinator.fuzzer.ListDirectory(pattern=pattern, contents=contents)
    with fuzzer:
        tests = set()
        index = 0
        while True:
            test = fuzzer(index=index)
            if test is None:
                break

            tests.add(test)
            index += 1

    assert tests == exp
