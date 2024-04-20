# `relationalai.std.graphs.Edge.__call__()`

```python
relationalai.std.graphs.Edge.__call__(self, from_: Producer = None, to: Prodcuer = None, **kwargs) -> EdgeInstance
```

Returns an [`EdgeInstance`](../EdgeInstance/README.md) object that produces
edges matching that optional `from_` and `to` arguments with properties set to the provided keyword arguments.
You must call an `Edge` instance from within a [rule](../Model/rule.md) or [query](../Model/query.md) context.

## Parameters

| Name | Type | Description |
| :--- | :--- | :------ |
| `from_` | [`Producer`](../../../Producer/README.md) | The node(s) that matched edges must have in the `from_` position. |
| `to` | [`Producer`](../../../Producer/README.md) | The node(s) that matched edges must have in the `to` position. |
| `*kwargs` | `Any` | Properties that matched edges must have set. |

## Returns

An [`EdgeInstance`](../EdgeInstance/README.md) object.

## Example

When you call an `Edge` object without any arguments it returns an [`EdgeInstance`](../Instance/README.md)
that produces every edge in a graph:

```python
import relationalai as rai
from relationalai.std.graphs import Graph

# Create a model with `Person` and `Transaction` types.
model = rai.Model("transactions2")
Person = model.Type("Person")
Transaction = model.Type("Transaction")

# Add some people and transactions to the model.
with model.rule():
    alice = Person.add(name="Alice")
    bob = Person.add(name="Bob")
    Transaction.add(sender=bob, receiver=alice, amount=100.0)

# Create a graph.
graph = Graph(model)
graph.Node.extend(Person)

# Add transactions to the graph as edges.
with model.rule():
    transaction = Transaction()
    graph.Edge.add(
        from_=transaction.sender,
        to=transaction.receiver,
        weight=transaction.amount
    )

# Display all edges in the graph.
with model.query() as select:
    edge = graph.Edge()
    response = select(edge.from_.name, edge.to.name, edge.weight)

print(response.results)
# Output:
#   name  name2      v
# 0  Bob  Alice  100.0
```

Pass property values as keyword arguments when you call a type to
get an `EdgeInstance` that produces objects with those properties:

```python
with model.query() as select:
    edge = graph.Edge(weight=100.0)

print(response.results)
# Output:
#   name  name2      v
# 0  Bob  Alice  100.0
```

## See Also

[`EdgeInstance`](../EdgeInstance/README.md)
