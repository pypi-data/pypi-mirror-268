import re

# import unidecode


def slugify(text):
    # text = unidecode.unidecode(text)
    return re.sub(r"[\W_]+", "_", text.lower())


def extract_uniques(elements, comp=lambda left, right: left == right):
    keep = []
    for e in elements:
        if not any(comp(e, k) for k in keep):
            keep.append(e)
    return keep


def groupby(iterable, key):
    mapping = {}
    for el in iterable:
        k = key(el)
        siblings = mapping.setdefault(k, [])
        siblings.append(el)
    return mapping


# class OverFlowQueue:
#     def __init__(self, size):
#         if size < 1:
#             raise Exception("Size of OverFlowQueue must greater or equal to 1")
#         self._size = size
#         self._elements = []
#         self._mutex = Lock()
#     def append(self, element, default=None):
#         with self._mutex:
#             self._elements.append(element)
#             if len(self._elements) > self._size:
#                 return self._elements.pop(0)
#             return default


# def ratelimited(count, duration, extra=1):
#     """
#         Limit execution of the function to a maximum of `count` execution per slice of `duration` time.
#         An extra wait can be added
#     """
#     def decorator(func):
#         timestamps_queue = OverFlowQueue(count)
#         @wraps(func)
#         def wrapper(*args,**kargs):
#             now = time.perf_counter()
#             first = timestamps_queue.append(now)
#             if first is not None:
#                 to_wait = math.ceil(duration - (now - first))
#                 if to_wait > 0:
#                     to_wait += extra
#                     logging.debug(f"Waiting {to_wait} because of rate limit ({count} calls every {duration} seconds)")
#                     time.sleep(to_wait)
#             return func(*args,**kargs)
#         return wrapper
#     return decorator
