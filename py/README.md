## Contents
* Python Features
  * [Sequence Types](#sequence-types)
  * [Lists](#lists)
  * [List Comprehensions](#list-comprehensions)
  * [Generator Expressions](#generator-expressions)
  * [Iterator / Tuple Unpacking](#iterator--tuple-unpacking)
  * [Slicing](#slicing)
  * [Mapping](#mapping)
  * [Strings](#strings)
  * [Function Decorators / Closures](#function-decorators--closures)
  * [Object orientation](#object-orientation)
  * [Iterators / Generators](#iterators--generators)
  * [Context Managers](#context-managers)
  * [Coroutines](#coroutines)
  * [Concurrency / Parallelism](#concurrency--parallelism)
* [References](#references)

## Python Features

* List comprehensions (build a new list)
* Generator expressions (build anything)
* Tuple unpacking / Iterator unpacking

### Sequences
**Classification**
* Container vs. Flat
  * **Container:** elements can be of different types. E.g,. `list`, `tuple`, `dequeue`
  * **Flat:** elements must be of the same type. E.g., `str`, `bytes`, `bytearray`, `array`, `memoryview`
* Mutable vs. Immutable
  * **Mutable:** Elements in sequence can be modified. E.g., `list`, `bytearray`, `array`, `dequeue`, `memoryview`
  * **Immutable:** Elements in sequence cannot be modified after creation. E.g., `tuple`, `str`, `bytes`

### Immutability
* => objects cannot be changed after creation
* strs, tuples are immutable
* Advantages:
  * Hashability (cannot hash mutable objects)
  * Performance optimization due not having to copy strs/tuples

### Lists
Alternatives to `list`

**Arrays**
* Use when all items are of the same data type (i.e., all numbers)
* More efficient than lists; as efficient as C arrays (w.r.t time & space)
* Mutable (has `.pop`, `.insert`, `.extend` operations)
* Must specify typecode (i.e., data type) of elements during creation (e.g., `array('b')`)
* Provides `tofile` and `fromfile` functions to save/append to/from files. Alternatively, use `pickle`
* For numeric arrays representing binary data, use `bytes` & `bytearray` types

```python
from array import array
array('d', <iterable>) # create array of double-precision floats
array('d')
```

**Memory views**
* Shared-memory sequence type where slices do not require copying bytes; very useful for large data sets
* Inspired by `NumPy`; a memoryview is a generalized NumPy array structure in Python

**Queues**
* `list` can be used as stack & queue
* for stack (LIFO), use `.append` & `.pop(0)` on list
* Changes at left end (0-index end) are expensive since entire list needs to be shifted
* `dequeue`: thread-safe, bounded, double-ended queue for fast insertion/removal at either end, but not the middle. Bounded => it can discard items from the other end when limit is reached & new items are appended
 * Queues are also available via:
  * `queue` - thread-safe classes for Queue, LifoQueue, PriorityQueue. All are bounded and block insertion when max limit is reached
  * `multiprocessing` - has a bounded queue for IPC & JoinableQueue for task management
  * `asyncio` - provides Queue, LifoQueue, PriorityQueue for managing async tasks
  * `heapq` - no queue, but can use heappush & heappop to a mutable sequence as heap queue or priority queue

**References**
* Chap 2, `Fluent Python`


### List comprehensions
* ?

### Generator expressions
* ?

### Iterator / Tuple Unpacking
* ?

### Slicing
* ?

### Mapping

**Hashable**

An object is *hashable* if:
1. It has a `hash()` function via the `__hash__` method that always returns the same value during the lifetime of the object
2. It has an `__eq__` method to determine equality to other objects
3. `a == b` == `True` => `hash(a) == hash(b)`


* `frozenset` is always hashable since its elements must be hashable
* `tuple` is hashable only if all its items are hashable
* User-defined types are hashable because their hash value is their `id` (integer that is unique & constant for the lifetime of the object) & they are all not equal.
* Classes with custom `__eq__` types require custom `__hash__` method because `a == b` must => `hash(a) == hash(b)`.
* If the custom `__eq__` method depends on mutable state, then `__hash__` must return `unhashable type`

**Dictionaries**
* Widely used in programs & as part of Python implementation (module namespaces, class/instance attributes, function keyword arguments)
* Based on `hash tables`
* `{}` represents an empty dict (not an empty set)
* dict comp creates a dictionary by generating key:value pairs from any iterable
* Variations of dict include:
  * `collections.defaultdict` - assigns default value to missing key & returns this value
  * `collections.OrderedDict` - maintains keys in insertion order
  * `collections.ChainMap` - hold a list of mappings & looks for input key in all of them 
  * `collections.Counter` - mapping that holds an integer count for each key. Used to count instances of hashable objects
  * `collections.UserDict` - Works like a standard dict; designed to be sub-classed instead of `dict` since `dict` has various shortcuts that force methods to be overridden in sub-classes. This is not needed when sub-classing from `UserDict`.
* `setdefault` is useful while inserting new keys or updating values of existing keys
* To handle missing keys, use `defaultdict` to return a default value or sub-class `dict` and add a `__missing__` method
* In `defaultdict`, when `__get_item__` is called, callable defined in `default_factory` is invoked to provide the default value. This does not happen when `get` is called (None is returned if key is missing).
* In `dict`, `__missing__` method is not defined but if a sub-class defines it, then `__get_item__` will call it if key is missing instead of raising `KeyError`. `__missing__` calls `default_factory` with no arguments if it is not `None` or raises a `KeyError` if `default_factory` is `None`. Only `__get_item__` calls `__missing__`. Other methods like `get` & `contains` don't call `__missing__`
* `MappingProxyType` returns a dynamic read-only view of the underlying mapping. Changes to the underlying mapping are available in the view immediately but no changes can be made from the view.

```python
from types import MappingProxyType
d = {'a': 1, 'b': 2}
dp = MappingProxyType(d)
assert d['a'] == dp['a']
```

Implementation requirements/characteristics:
1. dicts are based on hash tables (sparse arrays). Each bucket in the hash table contains a ref to the key & a ref to the item => all buckets have the same size => access individual bucket by offset
1. `hash()` works directly for built-in types and calls `__hash__` for user-defined types. `a == b` => `hash(a) == hash(b)`
1. Hash functions should spread values as much as possible.
1. `dict[key]` calls `hash(key)` & uses least significant bits of hash value to calculate offset of bucket in hash table. If bucket is empty, then raise `KeyError`. If bucket is not empty but keys don't match, then hash collision occurred, so calculate offset using different bits in hash value and go to that bucket. If bucket not empty & keys match, return value in bucket. During insertion, new value overwrites previous value in bucket, if any.
1. If hash table is getting too full, Python copies contents to a new, larger hash table. Avg # collisions per search is 1 - 2.
1. Keys must be hashable
1. Require significant memory overhead (since hash table must be sparse & Python tries to keep at least 1/3rd of the buckets empty). For large number of records, use list of tuples instead of dicts
1. Key search is very fast as long as dict fits in memory (space is traded for time)
1. Key order depends on insertion order. Hash collisions can assign keys to different buckets depending on the order in which the key was inserted
1. Adding items to dict can change the order of existing keys (hash table might get too full resulting in copy of items to a new, larger hash table resulting in hash collisions and new ordering of keys). Don't update keys while iterating over them.


* Python3: `.keys()`, `.items()`, `.values()` return dictionary views (no copy of dict contents)
* Python2: the methods return lists

* Dict comprehensions

**Sets**

* A set is a collection of unique objects; mainly used to remove duplicates
* Set elements must be hashable (i.e., cannot contain mutable types like `list`). Also cannot contain `set` since it is not hashable. But can contain `frozenset`.
* Create empty set as `set()`; `{}` refers to an empty dict; create non-empty set as `{a, b, c}`
* Set comprehensions:
  * e.g., `{x**2 for x in range(10)}`
* Set operations are `intersection`, `union`, `relative difference`, `symmetric difference`,
* Comparison operations are `in`, `<=`, `<` (improper / proper subset of), `>`, `>=` (improper / proper superset of)
* Other operations include `copy`, `__iter__`, `len` for `set` & `frozenset` & `add/clear/discard/pop/remove` for `set` only

Implementation:

* `set` & `frozenset` are based on hash tables with each bucket holding only a ref to the set element (i.e., key only, no value)
* Same requirements/characteristics of dicts apply to sets

**References**
* Chap 3, `Fluent Python`

### Strings
* ?

### Function decorators / closures
* ?

### Object orientation
* ?

### Iterators / Generators
* ?

### Context managers
* ?

### Coroutines
* ?

### Concurrency / Parallelism

* GIL prevents true parallelism in CPython since only once thread can run at a time
* Alternative: write performance-critical code as C extension module since C runs much faster than Python. C extension module can also release the GIL and run multiple threads/processes in parallel. But code is more difficult to understand
* 


#### Subprocesses
* Use `subprocess` module to start a new process from Python to run an external program
* Use `run` function from Python 3.5+. Waits for cmd to complete & returns a `CompletedProcess` object with details of cmd execution
```python
import subprocess
subprocess.run(["ls", "-l"])
subprocess.run(["ls", "-l"], stdout=subprocess.PIPE)
subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
```

* Use `call` function for Python 3.5-
```python
import subprocess
subprocess.call(["ls", "-l"])
```

* Can pipe data into child process & get output from child process
* Can create a chain of parallel processes by sending output of one process into input of another process
* Use `timeout` param to kill processes if they take too long to complete or if they hang

#### Threads
* Use for IO-bound operations, not for CPU-bound operations (use processes instead)
* Use `queue` to coordinate between threads
* Use locking to prevent race conditions between threads

#### concurrent.futures / multiprocessing
* Same interface for both threads & processes
* Utilize multiple cores by running multiple Python interpreters in parallel, each in a separate child process and with its own GIL

#### asyncio
* ?

## References
* `Fluent Python`, Luciano Ramalho, O'Reilly, 2015
* `Effective Python`, Brett Slatkin, Addison Wesley, 2015
* `Python Cookbook`, David Beazley, Brian Jones, 3rd Ed, O'Reilly, 2013

