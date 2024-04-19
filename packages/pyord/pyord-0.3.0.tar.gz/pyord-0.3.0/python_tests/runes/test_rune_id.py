import pytest
from pyord import RuneId


def test_repr():
    rune_id = RuneId(
        block=1,
        tx=2,
    )
    assert repr(rune_id) == "RuneId(block=1, tx=2)"


def test_from_str():
    assert RuneId.from_str("1234:56") == RuneId(
        block=1234,
        tx=56,
    )
    with pytest.raises(ValueError):
        RuneId.from_str('123')
    with pytest.raises(ValueError):
        RuneId.from_str('456')
    with pytest.raises(ValueError):
        RuneId.from_str('123:456:')
    with pytest.raises(ValueError):
        RuneId.from_str('foo:bar')
