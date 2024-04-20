<!-- markdownlint-disable MD024 -->

# `relationalai.std.graphs.EdgeInstance`

`EdgeInstance` objects produce edges in graphs.
They behave similarly to [`Instance`](../Instance/README.md) objects,
but rather than representing a single object in a model,
they represent a pair of objects in an edge relationship in a graph.
As a result, you can't add `EdgeInstance` objects to `Type` objects.

You create `EdgeInstance` objects by calling a graph's [`Edge`](../Graph/Edge.md) object.

```python
class relationalai.std.graphs.EdgeInstance(edge: Edge, from_: Producer, to: Producer, **kwargs)
```

## Parameters

| Name | Type | Description |
| :--- | :--- | :------ |
| `edge` | [`Edge`](../Graph/Edge.md) | The `Edge` object from which the `EdgeInstance` is created. |
| `from_` | [`Producer`](../Producer/README.md) | The source node(s) of the edge(s). |
| `to` | [`Producer`](../Producer/README.md) | The `target node(s) or the edge(s). |
| `**kwargs` | `Dict[str, Any]` | The properties of the edge(s). |

## Attributes

- [`EdgeInstance.from_`](./from_.md)
- [`EdgeInstance.to`](./to.md)

## Methods

- [`EdgeInstance.set()`](./set.md)

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with `Person` and `Transaction` types.
model = rai.Model("socialNetwork")
Person = model.Type("Person")

# Add some people and transactions to the model.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    alice.set(follows=bob)

# Create a graph and add edges to it.
graph = Graph(model)
graph.Edge.extend(Person.follows)

# Display the edges of the graph.
with model.query() as select:
    edge = graph.Edge()  # `edge` is an EdgeInstance object
    response = select(edge.from_.name, edge.to.name)

print(response.results)
# Output:
#   name  name2
# 0  Bob  Alice
```
