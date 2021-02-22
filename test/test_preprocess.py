from virgo.parse import preprocess


def test_simple_line():
    s = "a -> b"
    result = preprocess(s)
    assert result == s + "\n"
