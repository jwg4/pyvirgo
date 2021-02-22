import virgo


def test_parse_basic_example():
    with open("test/files/config.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 


def test_parse_harder_example():
    with open("test/files/make.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 


def test_parse_edge_statement():
    with open("test/files/edges.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 


def test_parse_node_statement():
    with open("test/files/nodes.vgo") as f:
        data = f.read()
    g = virgo.parse(data)
    assert g is not None 
