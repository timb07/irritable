#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `irritable` package."""

import pytest


from irritable import irrit, StopIrritation


def test_irrit():
    i = irrit(range(2))
    assert next(i) == 0
    assert next(i) == 1
    with pytest.raises(StopIteration):
        next(i)
    with pytest.raises(StopIrritation):
        next(i)


def test_irrit_repeat():
    i = irrit(range(2), repeat=True)
    assert next(i) == 0
    assert next(i) == 1
    with pytest.raises(StopIteration):
        next(i)
    assert next(i) == 0
    assert next(i) == 1
    with pytest.raises(StopIteration):
        next(i)
    assert next(i) == 0
    assert next(i) == 1
    with pytest.raises(StopIteration):
        next(i)


def test_irrit_resume():
    """Probabilistic test: may fail very occasionally"""
    count_empty = 0
    l = list(range(10))
    for _ in range(100):
        i = irrit(range(10), resume=True)
        l1 = [n for n in i]
        if len(l1) == 0:
            count_empty += 1
        elif len(l1) < 10:
            l2 = [n for n in i]
            assert l1 + l2 == l
        else:
            assert l1 == l
    assert 0 < count_empty < 100
