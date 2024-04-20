# `relationalai.std.graphs.Graph.Node`

A [`Type`](../../../Type/README.md) object representing the set of nodes in a graph.

## Returns

A [`Type`](../../../Type/README.md) object.

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

# Create a graph.
graph = Graph(model)

# Add all of the people in the model to the graph's nodes using `Node.extend()`.
graph.Node.extend(Person, label=Person.name)

# Alternatively, you can add specific nodes in a rule using `Node.add()`.
with model.rule():
    p = Person(name="Alice")
    graph.Node.add(p, label=p.name)

# You can query the nodes the same way you query any other `Type` object.
with model.query() as select:
    node = graph.Node()
    response = select(node.label)

print(response.results)
# Output:
#    label
# 0  Alice
# 1    Bob
```

## See Also

[`Type`](../../../Type/README.md)
