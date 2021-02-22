import pytest

import virgo


def test_parse_make_example():
    with open("test/files/make.vgo") as f:
        data = f.read()
    g = virgo.loads(data)
    assert g is not None 
    assert "src files" in g.nodes
    assert g.nodes["src files"] == "go build ./..."
    assert set(g.direct_successors_of("src files")) == {"test"}
    assert set(g.successors_of("src files")) == {"test"}
    assert set(g.direct_predecessors_of("src files")) == {"parser", "lexer"}
    assert set(g.predecessors_of("src files")) == {"clean", "parser", "lexer"}


def test_parse_edge_statement_successors():
    with open("test/files/edges.vgo") as f:
        data = f.read()
    g = virgo.loads(data)
    assert g is not None 
    assert set(g.direct_successors_of("b")) == {"d", "e", "h", "i"}
    assert set(g.successors_of("b")) == {"d", "e", "h", "i"}
    assert set(g.successors_of("a")) == {"b", "c", "d", "e", "h", "i"}


def test_topological_sorting():
    filename = "test/files/sorting.vgo"
    g = virgo.load(filename)
    l = list(g.topological_sort())
    assert l.index("x7") < l.index("x11")


def test_topological_sorting_of_single_cycle():
    filename = "test/files/cycle.vgo"
    g = virgo.load(filename)
    with pytest.raises(Exception):
        list(g.topological_sort())


def test_topological_sorting_of_cycles():
    filename = "test/files/grid.vgo"
    g = virgo.load(filename)
    with pytest.raises(Exception):
        list(g.topological_sort())
