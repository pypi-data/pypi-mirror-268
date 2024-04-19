# njson: efficient JSON-like data transformation tool

## What is it?
Provide fast JSON-like data transformation to and from nested
parent-child and flat label-value data items, such as Pandas `Series` with
MultiIndex index.

## Features

* Transformation are optimized for speed, to allow parsing deeply nested json-like data with millions of data points in seconds.
* Transformation are lazily computed properties only calculated when accessed for the first time. Initializing NestedJson object does not require parsing the source data.
* NestedJson is Pure-Python package that runs on JupyterLite, Pyodide, PyScript, Cloudflare Workers in Python, etc.
* Itegrates with pandas for quick data transformation to and from pandas `Series` and `DataFrame`.
* Provides easy access to nested data at any level using parent keys.

## Example usage
### Flatten and unflatten nested json-like or flat-dict-like data.
```python
>>> import njson as nj
>>> d = {'a': 1, 'b': [{}}, {'d': 2}]}
>>> njd = nj.NestedJson(d)
>>> print(njd.data) # source data
>>> print(njd.flat_dict) # data as flat-dict with parent key tuples
>>> print(njd.data_series) # data as flat-dict with parent key tuples
>>> print(njd.data_series_bfill) # ... even length key tuples aligned "rigth"
>>> print(njd.get('b')) # get data
>>> print(njd.get('b', 0)) # get nested data
>>> print(njd.get('b', 1)) # get data at any nesting level
>>> njd.parsed.nfd.str # json str of origianl data parsed as nested flat-dict
{'a': 1, 'b': [{}, {'d': 2}]}
{('a',): 1, ('b', 0): {}, ('b', 1, 'd'): 2}
{('a', '', ''): 1, ('b', 0, ''): {}, ('b', 1, 'd'): 2}
{('', '', 'a'): 1, ('', 'b', 0): {}, ('b', 1, 'd'): 2}
[{}, {'d': 2}]
{}
{'d': 2}
'{"a": 1, "b": [{}, {"d": 2}]}'
```

**Note**
* All flat-dict keys are tuples representing parent keys of json-like data.
* The flat-dict labels keys for nested lists are integer values.
* Empty dict,  list, tuple, set values are not flattened, as they have no values
  or parent keys.
* The `.data_series` flat-dict with even length key tuples has similar data
  structure to pandas `MultiIndex` `Series`. Key tuple length normalization 
  prepares data for efficient creation of Pandas `Series` objects from deeply
  nested JSON object data.

### Transforming Pandas `Series`, `DataFrame` to and from JSON-like data
```python
>>> import pandas as pd
>>> import njson as nj
>>> d = {'a': 1, 'b': [{}, {'d': 2}]}
>>> njd = nj.NestedJson(d)
>>> ds = njd.to_data_series(pd.Series)
>>> print(ds)
>>> print(ds.unstack(level = [0]))
>>> print(ds.to_dict(into = NestedJson).parsed.nds.data)
<class 'pandas.core.series.Series'>
a           1
b  0       {}
   1  d     2
dtype: object
            d
a      1  NaN
b 0   {}  NaN
  1  NaN    2
a           1
b  0       {}
   1  d     2
dtype: object
{'a': 1, 'b': [{}, {'d': 2}]}
```

**Note**
* Pass pandas Series `pd.Series` to NestedJson 
  `NestedJson.to_data_series(into = NestedJson)` to directly 
  derive Pandas `Series` data. Then access `.parsed.nds.data`
  attribute to return nested JSON-like data.
* Pass `NestedJson` to pandas `Series.to_dict(into = NestedJson)` to directly 
  derive `NestedJson` from Pandas `Series` data.
* Stacking and unstacking Pandas `Series` with `.unstack()` and `.stack()`
  allows to tranform the nested JSON-like data to and from convenient 
  tabular-like Pandas `DataFrame` data structure. Note that (un)stacking
  by default sorts the level(s) in the resulting index/columns and therefore can
  alter the order of elements.

### Read JSON files

```python
>>> import njson as nj
>>> njd_from_file = nj.read_json('path-to.json')
>>> njd_from_str = nj.read_json_str('{"a": 1, "b": [{}, {"d": 2}]}')
>>> njd_from_str.flat_dict
{('a',): 1, ('b', 0): {}, ('b', 1, 'd'): 2}
```