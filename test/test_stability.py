import virgo
from virgo.error import VirgoException

from hypothesis import given
from hypothesis.strategies import text


ALPHABET = "abcedfghijklmnopqrstuvwxyz0123456789-<>,\n"


#@given(s=text())
@given(s=text(alphabet=ALPHABET))
def test_gets_parsed_or_throws_good_error(s):
    try:
        g = virgo.loads(s)
        assert g is not None
    except VirgoException:
        pass
