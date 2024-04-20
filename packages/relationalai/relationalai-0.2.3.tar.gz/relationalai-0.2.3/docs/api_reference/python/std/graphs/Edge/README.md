# `relationalai.std.graphs.Edge`

The `Edge` class is used to represent the edge set of a graph.
You do not need to create an `Edge` instance directly.
Each `Graph` object has an `Edge` instance that you can access via [`Graph.Edge`](../Graph/Edge.md),
which returns an instance of the `Edge` class.

`Edge` objects behave similarly to [`Type`](../../../Type/README.md) objects,
except that instead of returning [`Instance`](../../../Instance/README.md) objects,
they return [`EdgeInstance`](../EdgeInstance/README.md) objects.

```python
class relationalai.std.graphs.Edge(graph: Graph)
```

## Parameters

| Name | Type | Description |
| :--- | :--- | :------ |
| `graph` | [`Graph`](../Graph/README.md) | The graph on which the `Edges` object is instantiated. |

## Methods

- [`Edge.__call__()`](./call__.md)
- [`Edge.add()`](./add.md)
- [`Edge.extend()`](./extend.md)

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model named `socialNetwork` with a `Person` type.
model = rai.Model("socialNetwork")
Person = model.Type("Person")

# Add some people to the model and connect them with a `follows` property.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    alice.set(follows=bob)

# Create a directed graph.
graph = Graph(model)

# Add edges to the graph based on the `follows` property.
# Note that nodes are automatically added to the graph when edges are added.
graph.Edges.extend(Person.follows)

# You may add specific edges to a graph using the `Edge.add()` method inside of a rule.
with model.rule():
    p = Person(name="Alice")
    graph.Edge.add(from_=p, to=p.follows)

# To query edges, call the `Edge` object and select the desired properties.
with model.query() as select:
    edge = graph.Edge()
    response = select(edge.from_.name, edge.to.name)

print(response.results)
# Output:
#   name  name2
# 0  Bob  Alice
```

## See Also

[`Graph.Edge`](../Graph/Edge.md) and [`Graph.Node`](../Graph/Node.md).
