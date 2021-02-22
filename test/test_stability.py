import virgo
from virgo.error import VirgoException

from hypothesis import given
from hypothesis.strategies import text


@given(s=text())
def test_gets_parsed_or_throws_good_error(s):
    try:
        g = virgo.loads(s)
        assert g is not None
    except VirgoException:
        pass
