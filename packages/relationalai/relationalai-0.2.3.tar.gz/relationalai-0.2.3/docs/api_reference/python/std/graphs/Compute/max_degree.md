# `relationalai.std.graphs.Compute.max_degree()`

```python
relationalai.std.graphs.Compute.max_degree() -> Expression
```

An [Expression](docs/api_reference/python/Expression.md) object that produces the maximum degree of the graph.
For directed graphs, the degree of a node is the sum of the [indegree](./indegree.md) and [outdegree](./outdegree.md) of the node.

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
    max_degree = graph.compute.max_degree()
    response = select(max_degree)
    
print(response.results)
# Output:
#    v
# 0  1
```
