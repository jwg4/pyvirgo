from virgo import parse


def test_parse_simple_edge():
    s = "a -> b"
    result = parse(s)
    assert result is not None
    assert "a" in result.nodes
    assert result.direct_successors_of("a") == ["b"]
    assert result.successors_of("a") == ["b"]
    assert result.direct_successors_of("b") == []
    assert result.successors_of("b") == []


def test_parse_simple_edge_with_newline():
    s = "a -> b\n"
    result = parse(s)
    assert result is not None
