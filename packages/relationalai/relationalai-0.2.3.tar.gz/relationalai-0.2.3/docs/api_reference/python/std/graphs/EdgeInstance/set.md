# `relationalai.std.graphs.EdgeInstance.set()`

```python
EdgeInstance.set(**kwargs) -> EdgeInstance
```

Sets properties on an [`EdgeInstance`](./README.md) object and returns the `EdgeInstance`.

## Parameters

| Name | Type | Description |
| :--- | :--- | :------ |
| `*kwargs` | `Any` | Properties and values to set on the `EdgeInstance`. |

## Returns

An [`EdgeInstance`](./README.md) object.

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with a `Person` type.
model = rai.Model("socialNetwork")
Person = model.Type("Person")

# Add some people to the model and connect them with a 'follows' property.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    alice.set(follows=bob)

# Create a graph and add edges to it.
graph = Graph(model)
graph.Edge.extend(Person.follows)

# Add a color property to the edge and set it to "red".
with model.rule():
    edge = graph.Edge(from_=Person(name="Alice"), to=Person(name="Bob"))
    edge.set(color="red")
```

## See Also

[`Edge.add()`](../Edge/add.md)
