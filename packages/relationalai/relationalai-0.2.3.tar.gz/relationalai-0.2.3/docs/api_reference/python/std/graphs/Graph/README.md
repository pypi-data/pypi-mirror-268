# `relationalai.std.graphs.Graph`

The `Graph` class is used to create graphs representing relationships between objects in a model.
You can use `Graph` objects to perform graph analytics on data in your model.

```python
class relationalai.std.graphs.Graph(model: Model, undirected: bool = False, weighted: bool = False, default_weight: float = 1.0)
```

## Parameters

| Name | Type | Description |
| :--- | :--- | :------ |
| `model` | [`Model`](../../../Model/README.md) | The model on which the `Graph` is instantiated. |
| `undirected` | `bool` | Whether the graph is undirected. Default is `False`. |
| `weighted` | `bool` | Whether the graph is weighted. Default is `False`. |

## Attributes

- [`Graph.compute`](./compute.md)
- [`Graph.Edge`](./Edge.md)
- [`Graph.id`](./id.md)
- [`Graph.model`](./model.md)
- [`Graph.Node`](./Node.md)
- [`Graph.undirected`](./undirected.md)

## Methods

- [`Graph.fetch()`](./fetch.md)
- [`Graph.visualize()`](./visualize.md)

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

# Create a graph from the model and visualize it.
graph = Graph(model)
graph.Node.extend(Person, label=Person.name)
graph.Edge.extend(Person.follows)
graph.visualize().display()  # In Jupyter notebooks, only .visualize() is needed.
```

![A graph with two nodes labeled Alice and Bob and an edge pointing from Alice to Bob.](./img/simple-social-network.png)

By default, the `Graph` class creates directed graphs.
You can create undirected graphs by setting the `undirected` parameter to `True`.

Weighted graphs are supported by setting the `weighted` parameter to `True`:

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with `Person` and `Transaction` types.
model = rai.Model("transactions")
Person = model.Type("Person")
Transaction = model.Type("Transaction")

# Add some people and a transaction to the model.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    transaction = Transaction.add(sender=alice, recipient=bob, amount=100.0)

# Create a weighted graph from the model.
graph = Graph(model, weighted=True)
graph.Node.extend(Person, label=Person.name)

with model.rule():
    t = Transaction()
    graph.Edge.add(t.sender, t.recipient, weight=t.amount)
```

In a weighted graph, edges have a `weight` attribute that can be used in graph algorithms.
The `default_weight` parameter, which defaults to 1.0,
sets the default weight for edges in the graph in which a `weight` property is not set.
