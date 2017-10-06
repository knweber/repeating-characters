import pytest

def test_repeats():
    assert repeats('the dog said bananas') == 'bananas'

def test_repeats_tie():
    assert repeats('the Apple said apple!') == 'Apple'

def test_repeats_multiples():
    assert repeats('Romeo Romeo wherefore Romeo') == 'wherefore'
