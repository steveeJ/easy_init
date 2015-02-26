def easy_init(init):
    """
    This decorator is meant to be used on the __init__ function of classes.
    It that makes object initialization easy, by assigning every positional
    and known keyword argument to self.
    """
    import inspect
    import functools

    @functools.wraps(init)
    def new_init(o, *varargs, **varkw):
        callargs = inspect.getcallargs(init, o, *varargs, **varkw)
        print(callargs)
        del callargs['self']
        for k, v in callargs.items():
            if v is dict:
                for k2, v2 in varkw.items():
                    setattr(o, k2, v2)
            elif v is tuple:
                setattr(o, v[0], v[1])
            else:
                setattr(o, k, v)
        return init(o, *varargs, **varkw)
    return new_init
