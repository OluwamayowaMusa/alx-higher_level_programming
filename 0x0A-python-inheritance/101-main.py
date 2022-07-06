#!/usr/bin/python3
add_attribute = __import__("101-add_attribute").add_attribute


class MyClass():
    pass


class LockedClass:
    __slots__ = ["first_name"]


mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    a = LockedClass()
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
