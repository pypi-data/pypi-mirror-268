import relationalai as rai
from relationalai import std

# Query snapshots are output in same order as this list.
ALGOS = [
    "jaccard_similarity",
    "cosine_similarity",
]

model = rai.Model(name=globals().get("name", ""), config=globals().get("config"))
Object = model.Type("Object")
Relationship = model.Type("Relationship")

with model.rule():
    obj1 = Object.add(id=1)
    obj2 = Object.add(id=2)
    Relationship.add(from_=obj1, to=obj2)

# cosine_similarity only supports undirected graphs.
graph = std.graphs.Graph(model, undirected=True)

with model.rule():
    r = Relationship()
    graph.Edge.add(r.from_, r.to)

for algo_name in ALGOS:
    with model.query() as select:
        o1 = Object()
        o2 = Object()
        algo = getattr(graph.compute, algo_name)(o1, o2)
        select(o1, o2, algo)
