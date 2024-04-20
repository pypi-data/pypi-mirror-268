# `relationalai.std.graphs.EdgeInstance.from_`

Returns a `Producer` object that produces the source node(s) of the [`EdgeInstance`](./README.md).

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

# Display the source nodes of the edges.
with model.query() as select:
    edge = graph.Edge()
    source_node = edge.from_
    response = select(source_node.name)

print(response.results)
# Output:
#     name
# 0  Alice
```

## See Also

- [`EdgeInstance.to`](./to.md)
