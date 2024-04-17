# flatjsondict: efficient JSON-like data transformation tool

## What is it?
**flatjsondict** is nested JSON-like object transformation tool that provides 
`FlatJson` object for flat Pandas `Series` index-like label and filesystem 
path-like label access and manipulation for nested JSON-like data. Primarily 
used to efficently transform Pandas `Series` with MultiIndex index to nested 
JSON-like (dict, list) object and nested JSON-like data to flat Pandas 
`Series` with MultiIndex index.

Labels need to be tuples or path-like strings. The default separator for 
path-like text labels is ``/``, but can be configured by constructor or 
updated by calling :meth:`FlatJson.set_keypath_separator`.

Note that `FlatJson` provides :meth:`FlatJson.to_series()` to prepare 
JSON-like data for efficiently creating Pandas `Series` object with data 
MultiIndex index allowing to efficiently transform nested JSON-like object 
to Pandas `Series`.

Note that `FlatJson` provides :meth:`FlatJson.to_json()` to efficiently 
create nested JSON-like object from flat tuple-like label dictionary. 
Alternatively, `FlatJson` can be used as the target dictionary-like class when 
calling `Series.to_dict(FlatJson)`, then `FlatJson.to_json()` can be called 
to return nested json-like data for use with JSON:API applications.

## Examples
Constructing `FlatJson` from a nested dictionary.
```python
>>> import flatjsondict as fj
>>> d = {'a': 1, 'b': {'c': 3}}
>>> d_fj = fj.FlatJson(data=d)
>>> d_fj.to_dict()
{('a',): 1, ('b', 'c'): 3}
```

Note that the nested objects are dictionaries hence all label keys are 
string values.

```python
>>> d = {'a': 1, 'b': ['c', 3]}
>>> d_fj = fj.FlatJson(data=d)
>>> d_fj.to_dict()
{('a',): 1, ('b', 0): 'c', ('b', 1): 3}
```

Note that the labels keys for nested lists are integer values.

```python
>>> d = {'a': 1, 'b': ['c', 3]}
>>> d_fj = fj.FlatJson(data=d)
>>> d_fj.to_series()
{('a', ''): 1, ('b', 0): 'c', ('b', 1): 3}
```

Note that for nested object with varying nesting depth the label tuple 
length is normalized (padded) when calling :meth:`FlatJson.to_series()`. 
Such label length normalization prepares `FlatJson` data for efficient 
creation of Pandas `Series` objects with MultiIndex index allowing to 
transform deeply nested JSON object data to Pandas `Series`.

Transforming Pandas `Series` and `DataFrame` to and from nested JSON-like data.
```python
>>> import pandas as pd
>>> import flatjsondict as fj
>>> d = {'a': 1, 'b': ['c', 3]}
>>> ds = FlatJson(d).to_series(into = pd.Series)
>>> ds
a       1
b  0    c
    1    3

>>> ds.to_dict(into = fj.FlatJson)
{('a',): 1, ('b', 0): 'c', ('b', 1): 3}

>>> ds.to_dict(into = fj.FlatJson).to_json()
{'a': 1, 'b': ['c', 3]}
```

Note that you can pass `FlatJson` to Pandas `Series.to_dict(into = FlatJson)` 
to directly derive `FlatJson` from Pandas `Series` data. Then use
`FlatJson.to_json()` to return nested JSON-like data.

```python
>>> ds.unstack()
    0    1     
a  NaN  NaN    1
b    c    3  NaN

>>> ds.unstack().stack()
a       1
b  0    c
    1    3
```

Note that (un)stacking Pandas `Series` with `.unstack()` and `.stack()`
allows to tranform the nested JSON-like data to and from convenient 
tabular-like Pandas `DataFrame` data structure. Note that (un)stacking
by default sorts the level(s) in the resulting Pandas `DataFrame`
`MultiIndex` columns and therefore can alter the order or elements.

Constructing nested json-like data from `FlatJson`-like dictioaries.
```python
>>> import flatjsondict as fj
>>> d = {('a', ''): 1, ('b', 0): 'c', ('b', 1): 3}
>>> d_fj = fj.FlatJson(data=d)
>>> d_fj.to_dict()
{('a',): 1, ('b', 0): 'c', ('b', 1): 3}
>>> d_fj.to_json()
{'a': 1, 'b': ['c', 3]}

>>> d_fj.paths()
['a', 'b/0', 'b/1']
>>> d_fj.to_dict(join_key_tuples = True)
{'a': 1, 'b/0': 'c', 'b/1': 3}
```

Note that you can pass `FlatJson` to Pandas `Series.to_dict(FlatJson)` 
to directly derive `FlatJson` from Pandas `Series` data. Then use
`FlatJson.to_json()` to return nested JSON-like data.

Slicing `FlatJson` using multiple keys.
```python
>>> import flatjsondict as fj
>>> d = {'a': 1, 'b': ['c', 3]}
>>> d_fj = fj.FlatJson(data=d)
>>> d_fj.to_dict()
{('a',): 1, ('b', 0): 'c', ('b', 1): 3}
>>> d_fj.slice(('a',), ('b', 1)).to_json()
{'a': 1, 'b': [3]}
```