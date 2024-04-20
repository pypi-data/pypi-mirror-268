# `relationalai.std.graphs.Compute.num_edges()`

```python
relationalai.std.graphs.Compute.num_edges() -> Expression
```

An [Expression](docs/api_reference/python/Expression.md) object that produces the number of edges in the graph.

## Supported Graph Types

| Graph Type | Supported | Notes |
| :--- | :--- | :------ |
| Directed | Yes |   |
| Undirected | Yes |   |
| Weighted | Yes | Weights are ignored. |


## Parameters

No parameters are needed.

## Returns

Returns an [Expression](docs/api_reference/python/Expression.md) that produces the number of edges in the graph.

## Example

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model named "socialNetwork" with a Person type
model = rai.Model("socialNetwork")
Person = model.Type("Person")

# Add some people to the graph and connect them with a `follows` property
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    charlie = Person.add(name="Charlie")
    alice.set(follows=bob)
    bob.set(follows=charlie)
    charlie.set(follows=alice).set(follows=bob)
    
# Create an undirected graph and add all Person objects to the set of nodes
graph = Graph(model, undirected=True)
graph.Node.extend(Person, label=Person.name)
graph.Edge.extend(Person.follows)

# Compute the number of edges in the graph
with model.query() as select:
    num_edges = graph.compute.num_edges()
    response = select(num_edges)
    
print(response.results)
# Output:
#    v
# 0  3
```