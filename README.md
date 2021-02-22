# PyVirgo

This is a Python implementation of Virgo, the graph declarative language.

You can find details of Virgo with the Go implementation at https://github.com/r2d4/virgo

Virgo is designed so that we can express graphs in a config file. These could be dependency graphs, for example of a build process, or any other graph structure.

To invoke PyVirgo:
```
>>> import virgo
>>> g = virgo.loads("a -> b, c <- d")
>>> g       # doctest: +ELLIPSIS
<virgo.graph.Graph object at ...>
>>> sorted(list(g.direct_successors_of("a")))
['b', 'c']

```

It's more likely that we will want to load a graph from a file:
```
>>> g2 = virgo.load("test/files/make.vgo")
>>> g2      # doctest: +ELLIPSIS
<virgo.graph.Graph object at ...>
>>> g2.direct_successors_of("src files")
{'test'}

```

We can access the 'node data' for each node, by identifier.
```
>>> g2.nodes["src files"]
'go build ./...'

```
