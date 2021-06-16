# FAQ

## How can I see the code generated by pyserde?

pyserde provides `inspect` submodule that works as commandline:
```
python -m serde.inspect <PATH_TO_FILE> <CLASS>
```

e.g. in pyserde project

```
cd pyserde
poetry shell
python -m serde.inspect examples/simple.py Foo
```

Output
```python
Loading simple.Foo from examples.

==================================================
                       Foo
==================================================

--------------------------------------------------
          Functions generated by pyserde
--------------------------------------------------
def to_iter(obj, reuse_instances=True, convert_sets=False):
    if reuse_instances is Ellipsis:
        reuse_instances = True
    if convert_sets is Ellipsis:
        convert_sets = False
    if not is_dataclass(obj):
        return copy.deepcopy(obj)

    Foo = serde_scope.types["Foo"]
    res = []
    res.append(obj.i)
    res.append(obj.s)
    res.append(obj.f)
    res.append(obj.b)
    return tuple(res)
...
```