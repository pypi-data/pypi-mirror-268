# `relationalai.std.graphs.EdgeInstance.to`

Returns a `Producer` object that produces the target node(s) of the [`EdgeInstance`](./README.md).

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with a `Person` type.
model = rai.Model("socialNetwork3")
Person = model.Type("Person")

# Add some people to the model and connect them with a 'follows' property.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    alice.set(follows=bob)

# Create a graph and add edges to it.
graph = Graph(model)
graph.Edge.extend(Person.follows)

# Display the source nodes of the edges.
with model.query() as select:
    edge = graph.Edge()
    target_node = edge.to
    response = select(target_node.name)

print(response.results)
# Output:
#   name
# 0  Bob
```

## See Also

- [`EdgeInstance.from_`](./from_.md)
