# easy_init
Python decorator for automatically assigning arguments to class variables.

It will only assign positional arguments and named arguments, including default values.
```*args``` and ```**kwargs``` will be ignored.

# installation
  TODO

# usage
Import the module and decorate your classes constructor functions.
The following example makes easy_init take care of the class variable assignment.

```python
from easy_init import easy_init

class DummyClass(object):
    @easy_init
    def __init__(self, one, two, three=False, *args, **kwargs):
        pass
```
