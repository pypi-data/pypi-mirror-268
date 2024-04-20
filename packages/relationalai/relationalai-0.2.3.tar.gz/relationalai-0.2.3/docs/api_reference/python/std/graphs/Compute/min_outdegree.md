# `relationalai.std.graphs.Compute.min_outdegree()`

```python
relationalai.std.graphs.Compute.min_outdegree() -> Expression
```

An [Expression](docs/api_reference/python/Expression.md) object that produces
the minimum [outdegree](./outdegree.md) of the graph.

## Supported Graph Types

| Graph Type | Supported | Notes |
| :--- | :--- | :------ |
| Directed | Yes |   |
| Undirected | Yes |   |
| Weighted | Yes | Weights are ignored. |

## Parameters

No parameters are needed.

## Returns

An [Expression](docs/api_reference/python/Expression.md) object.

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
    alice.set(follows=bob)
    
# Create an undirected graph and add all Person objects to the set of nodes
graph = Graph(model, undirected=True)
graph.Node.extend(Person, label=Person.name)
graph.Edge.extend(Person.follows)

# Compute the minimum degree of the graph
with model.query() as select:
    min_outdegree = graph.compute.min_outdegree()
    response = select(min_outdegree)
    
print(response.results)
# Output:
#    v
# 0  0
```
