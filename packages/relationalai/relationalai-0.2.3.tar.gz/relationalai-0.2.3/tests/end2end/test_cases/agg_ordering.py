import relationalai as rai
from relationalai.std import rel, aggregates
model = rai.Model(name=globals().get("name", ""), config=globals().get("config"))

v = 2
Foo = model.Type("Foo")

with model.rule():
    Foo.add(name="A")
    Foo.add(name="B")
    Foo.add(name="C")

with model.query() as select:
    f = Foo()
    z = select(rel.minimum(v, aggregates.count(f)))

print(z.results)