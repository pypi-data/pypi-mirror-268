import asyncio
import inspect
from functools import wraps

# These are attempts to make a decorator/metaclass so that we automatically
# provide the same functionality as async code
# https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-5.html#executors-and-multithreading

# def get_method_class(func):
#     qualname = func.__qualname__
#     parts = qualname.split(".")
#     print(parts)
#     if len(parts) < 2:
#         return None
#     classname = parts[-2]
#     print(classname)
#     print(func.__globals__.keys())
#     return func.__globals__.get(classname)

# def make_async_test(name=None, prefix="async_"):
#     def decorator(f):
#         funcname = f.__name__
#         new_name = name if name else f"{prefix}{funcname}"
#         cls = get_method_class(f) # inspect._findclass(f)
#         if cls is None:
#             raise Exception(f"Function {f} is not part of a class")
#         @wraps(f)
#         async def wrapper(self, *args, **kwargs):
#             def executor():
#                 method = getattr(self, funcname)
#                 return method(*args, **kwargs)
#             return asyncio.get_event_loop().run_in_executor(executor)
#         setattr(cls, new_name, wrapper)
#         return f
#     return decorator


# def make_async_test(name=None, prefix="async_"):
#     def decorator(f):
#         funcname = f.__name__
#         new_name = name if name else f"{prefix}{funcname}"
#         @wraps(f)
#         async def wrapper(self, *args, **kwargs):
#             def executor():
#                 method = getattr(self, funcname)
#                 return method(*args, **kwargs)
#             return asyncio.get_event_loop().run_in_executor(executor)
#         return f, wrapper
#     return decorator


def make_async(f, name=None, prefix="async_"):
    funcname = f.__name__

    @wraps(f)
    async def wrapper(*args, **kwargs):
        def executor():
            return f(*args, **kwargs)

        # return asyncio.get_event_loop().to_thread(executor)
        # None => default executor
        return await asyncio.get_event_loop().run_in_executor(None, executor)

    new_name = name if name else f"{prefix}{funcname}"
    wrapper.__qualname__ = wrapper.__qualname__.removesuffix(funcname) + new_name
    wrapper.__name__ = new_name
    return wrapper


def make_methods_async(cls):
    methods = inspect.getmembers(cls, predicate=inspect.isfunction)
    public_methods = [m for m in methods if not m[0].startswith("_")]
    for funcname, func in public_methods:
        new_name = f"async_{funcname}"
        setattr(cls, new_name, make_async(func, new_name))
    return cls
