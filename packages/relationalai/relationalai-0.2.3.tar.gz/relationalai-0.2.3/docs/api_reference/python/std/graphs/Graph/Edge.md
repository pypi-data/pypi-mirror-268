# `relationalai.std.graphs.Graph.Edge`

Returns an [`Edge`](../Edge/README.md) object that can be used to add and query edges in a graph.

## Returns

A [`Edge`](../Edge/README.md) object.

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with a `Person` type.
model = rai.Model("socialNetwork")
Person = model.Type("Person")

# Add some people to the model and connect them with a `follows` property.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    alice.set(follows=bob)

# Create a graph from the model add edges from the `Person.follows` property.
# The nodes from each edge are automatically added to the graph.
graph = Graph(model)
graph.Edge.extend(Person.follows)
```

## See Also

[`Edge`](../Edge/README.md)
