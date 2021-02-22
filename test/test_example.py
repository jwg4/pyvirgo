import virgo


def test_parse_basic_example_from_file():
    g = virgo.load("test/files/config.vgo")
    assert g is not None 


def test_parse_basic_example():
    with open("test/files/config.vgo") as f:
        data = f.read()
    g = virgo.loads(data)
    assert g is not None 


def test_parse_harder_example():
    g = virgo.load("test/files/make.vgo")
    assert g is not None 
    assert "src files" in g.nodes
    assert g.nodes["src files"] == "go build ./..."
    assert set(g.direct_successors_of("src files")) == {"test"}


def test_parse_example_with_multiline_comments():
    g = virgo.load("test/files/comments.vgo")
    assert g is not None 
    assert "src files" in g.nodes
    assert g.nodes["src files"] == "go build ./..."
    assert set(g.direct_successors_of("src files")) == {"test"}


def test_parse_edge_statement():
    g = virgo.load("test/files/edges.vgo")
    assert g is not None 
    assert set(g.direct_successors_of("b")) == {"d", "e", "h", "i"}


def test_parse_node_statement():
    g = virgo.load("test/files/nodes.vgo")
    assert g is not None 
    assert "vertex_definition_1" in g.nodes
    assert g.nodes["vertex_definition_1"] == """
    anything
    can
    go
    ${here}
"""
