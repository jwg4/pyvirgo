from virgo import parse


def test_parse_simple_edge():
    s = "a -> b"
    result = parse(s)
    assert result is not None


def test_parse_simple_edge_with_newline():
    s = "a -> b\n"
    result = parse(s)
    assert result is not None
