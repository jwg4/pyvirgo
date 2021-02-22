from virgo import parse


def test_parse_simple_edge():
    s = "a -> b"
    result = parse(s)
    assert result is not None
    assert "a" in result.nodes
    assert list(result.direct_successors_of("a")) == ["b"]
    assert list(result.direct_successors_of("b")) == []


def test_parse_simple_edge_with_newline():
    s = "a -> b\n"
    result = parse(s)
    assert result is not None


def test_parse_simple_node_description():
    s = "parser = `goyacc parser.y`"
    result = parse(s)
    assert result is not None
    assert "parser" in result.nodes
    assert result.nodes["parser"] == "goyacc parser.y"


def test_parse_simple_node_description_with_blank_line():
    s = "\nparser = `goyacc parser.y`"
    result = parse(s)
    assert result is not None
    assert "parser" in result.nodes
    assert result.nodes["parser"] == "goyacc parser.y"


def test_parse_simple_node_description_with_blank_lines():
    s = "\n\nparser = `goyacc parser.y`"
    result = parse(s)
    assert result is not None
    assert "parser" in result.nodes
    assert result.nodes["parser"] == "goyacc parser.y"
