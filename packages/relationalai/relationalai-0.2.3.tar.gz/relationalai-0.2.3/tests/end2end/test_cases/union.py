import relationalai as rai

model = rai.Model(name=globals().get("name", "test_union"), config=globals().get("config"))
Person = model.Type("Person")
Adult = model.Type("Adult")

LegalEntity = model.Type("LegalEntity")
Control = model.Type("Control")
TotalOwnership = model.Type("TotalOwnership")

with model.rule():
    Person.add(name="Joe", age=84)
    Person.add(name="Bob", age=40)
    Person.add(name="Jane", age=10)

with model.query() as select:
    p = Person()
    with model.union() as cool:
        with p.age > 80:
            cool.add("amazing", rating=1000)
        with p.age > 60:
            cool.add("rad", rating=100)
        with p.age > 18:
            cool.add("awesome", rating=10)
    z = select(p.name, cool, cool.rating)

print(z.results)