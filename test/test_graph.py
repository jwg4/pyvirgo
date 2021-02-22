import virgo


def test_parse_harder_example():
    with open("test/files/make.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 
    assert "src files" in g.nodes
    assert g.nodes["src files"] == "go build ./..."
    assert set(g.direct_successors_of("src files")) == {"test"}


def test_parse_edge_statement_successors():
    with open("test/files/edges.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 
    assert set(g.direct_successors_of("b")) == {"d", "e", "h", "i"}
    assert set(g.successors_of("b")) == {"d", "e", "h", "i"}
    assert set(g.successors_of("a")) == {"b", "c", "d", "e", "h", "i"}
    
