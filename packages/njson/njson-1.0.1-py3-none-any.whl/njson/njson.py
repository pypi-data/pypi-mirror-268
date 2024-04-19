from typing import Iterable, Union, Hashable, Any, Type
from types import GeneratorType
from itertools import zip_longest, dropwhile
from collections import deque, abc
from pathlib import Path
import json, io

# -----------------------------------------------------------------------------
# Unitily functions to parse data before creating NestedJson class object

def read_json(path):
    """Return NestedJson, loaded from file-like object containing
    a JSON document."""
    p = Path(path)
    if p.exists() and not p.is_dir():
        with io.open(p, 'r') as f:
            data = json.load(f)
        return NestedJson(data)
    else:
        raise FileNotFoundError(f'File {p} was not found or is a directory.')

def read_json_str(data: str):
    """Return NestedJson, loaded from json string."""
    return NestedJson(json.loads(data))

def from_flat_dict(data):
    """Return NestedJson with data parsed as flat-dict.
    Flat-dict data is dictionary with tuple keys, such as
    `{('a', 'b'): 1, ('c',): 2}`.
    """
    return NestedJson(NestedJson._nest_flat_dict(data))

def from_nested_flat_dict(data):
    """Return NestedJson with data parsed as nested flat-dict.
    Nested flat-dict data is dictionary with nested flat-dict data.
    Flat-dict data is dictionary with tuple keys.
    """
    return NestedJson(NestedJson._nested_nest_flat_dict(data))

def from_series(data):
    """Return NestedJson with data parsed as data-series.
    Data-series data is dictionary with uniform length tuple keys,
    such as `{('a', 'b'): 1, ('c', ''): 2}`.
    """
    return NestedJson(NestedJson._nest_series(data))

def from_nested_series(data):
    """Return NestedJson with data parsed as nested data-series."""
    return NestedJson(NestedJson._nested_nest_series(data))

# -----------------------------------------------------------------------------
# ParsedNestedJson class
class _ParsedNestedJson:
    """Provide grouped attributes for NestedJson with lazy parsing of data.

    Attributes:
        fd (NestedJson): NestedJson with data parsed as flat-dict.
        ds (NestedJson): NestedJson with data parsed as data-series.
        nfd (NestedJson): NestedJson with data parsed as nested flat-dict.
        nds (NestedJson): NestedJson with data parsed as nested data-series.
    """
    def __init__(self, parent):
        self.parent = parent

    @property
    def fd(self):
        return self.parent._as_parsed_flat_dict

    @property
    def ds(self):
        return self.parent._as_parsed_data_series

    @property
    def nfd(self):
        return self.parent._as_parsed_nested_flat_dict

    @property
    def nds(self):
        return self.parent._as_parsed_nested_data_series

# -----------------------------------------------------------------------------
# NestedJson class

class NestedJson(abc.Mapping):
    """Provide fast JSON-like data transformation to and from nested
    parent-child and flat label-value data items, such as Pandas `Series` with
    MultiIndex index.

    Args:
        data (list,dict): json-like nested data

    Attributes:
        data (dict,list): Return data.
        str (str): Return data as json str.
        flat_dict (dict): Return a flat dict where keys are tuples with parent
            keys from the nested json-like data.
        data_series (dict): Return a flat dict. If the iterables are of 
            uneven length, missing values are filled-in with '' at the start of
            key tuples.
        data_series_bfill (dict): Return a flat dict. If the iterables are of 
            uneven length, missing values are filled-in with '' at the end of
            key tuples.
        values (list): Return values of the nested json-like data.
        keys (list): Return keys of the nested json-like data.
        keys_fillna_end (list): Return keys of the nested json-like data. If the
            iterables are of uneven length, missing values are filled-in with ''
            at the end of key tuples.
        keys_fillna_start (list): Return keys of the nested json-like data. If
            the iterables are of uneven length, missing values are filled-in
            with '' at the start of key tuples.
        parsed.nfd (NestedJson): NestedJson with data parsed as nested flat-dict.
            Provides convenient access above listed NestedJson attributes after
            parsing source data. For example, `.parsed.nfd.data` will return 
            flat-dict source data transformed to nested json-like data.
        parsed.nds (NestedJson): NestedJson with data parsed as nested data-series.
        parsed.fd (NestedJson): NestedJson with data parsed as flat-dict.
        parsed.ds (NestedJson): NestedJson with data parsed as data-series.

    Example usage:
        ## Flatten and unflatten nested json-like or flat-dict-like data.
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

        ## Transforming Pandas `Series`, `DataFrame` to and from JSON-like data
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

    """

    _FILLVALUE = ''

    def __init__(
        self,
        data: Union[dict, list] = None,
    ) -> None:
        self.__data = data
        if type(self.__data) is GeneratorType:
            self.data = dict(self.__data)
        else:
            self.data = self.__data

    def __getitem__(self, key) -> dict:
        """Implement evaluation of self[key]."""
        return self.get(key)

    def __len__(self) -> int:
        """Return the number of items in NestedJson."""
        return len(self.keys)

    def __str__(self) -> str:
        """Return the string value of the instance."""
        return str(self.flat_dict)

    def __repr__(self) -> str:
        """Return the string representation of the instance."""
        return '<{} {}>"'.format(
            self.__class__.__name__,
            str(self)
        )

    def __reduce__(self) -> Union[list, set, tuple, dict]:
        """Return state information for pickling."""
        return type(self), (self.data)

    def __iter__(self) -> iter:
        """Iterate over dictionary key tuples."""
        return iter(self.flat_dict)

    @staticmethod
    def _not_fillvalue(d):
        """Check if an object is data_series fillvalue."""
        return d is not NestedJson._FILLVALUE

    @staticmethod
    def _is_fillvalue(d):
        """Check if an object is data_series fillvalue."""
        return d is NestedJson._FILLVALUE

    @staticmethod
    def _drop_fillvalue(data):
        orig_type = type(data)
        return orig_type(filter(NestedJson._not_fillvalue, data))

    @staticmethod
    def _drop_fillvalue_start(data):
        orig_type = type(data)
        return orig_type(dropwhile(NestedJson._is_fillvalue,iter(data)))

    @staticmethod
    def _drop_fillvalue_end(data):
        orig_type = type(data)
        return orig_type(dropwhile(NestedJson._is_fillvalue,reversed(data)))[::-1]

    @staticmethod
    def _has_listlike_keys(data: dict) -> bool:
        """Check if a dict is list-like."""
        if data is dict():
            return False
        for i,k in enumerate(data.keys()):
            if i != k:
                return False
        return True

    @staticmethod
    def _has_nested_list_dict(data: dict) -> bool:
        """Check if dict has list or dict values."""
        for k,v in data.items():
            if type(v) is list or type(v) is dict:
                return True
        return False

    @staticmethod
    def _listlikedict_to_list(data: dict) -> Union[list,dict]:
        if type(data) is dict and NestedJson._has_listlike_keys(data):
            return list(data.values())
        else:
            return data

    @staticmethod
    def _nested_listlikedict_to_list(data: Union[list,dict,Any]) -> Union[list,dict,Any]:
        if data in [{}, []]:
            return data
        elif type(data) is dict:
            if NestedJson._has_listlike_keys(data):
                return [NestedJson._nested_listlikedict_to_list(val) for val in data.values()]
            else:
                if NestedJson._has_nested_list_dict(data):
                    return {key: NestedJson._nested_listlikedict_to_list(val) for key,val in data.items()}
                else:
                    return NestedJson._listlikedict_to_list(data)
        elif type(data) is list:
            return [NestedJson._nested_listlikedict_to_list(val) for val in data]
        else:
            return data

    @staticmethod
    def _align_start(keys: tuple) -> tuple:
        """Return keys with key items aligned at the start and fill values moved to end."""
        if keys[0] is NestedJson._FILLVALUE:
            d = deque(keys)
            while d[0] is NestedJson._FILLVALUE:
                d.rotate(-1)
            return tuple(d)
        else:
            return keys

    @staticmethod
    def _align_end(keys: tuple) -> tuple:
        """Return keys with key items aligned at the end and fill values moved to start."""
        if keys[-1] is NestedJson._FILLVALUE:
            d = deque(keys)
            while d[-1] is NestedJson._FILLVALUE:
                d.rotate(1)
            return tuple(d)
        else:
            return keys

    @staticmethod
    def _nested_get_values(data) -> list:
        if not (
            type(data) is dict or
            type(data) is list or
            type(data) is tuple or
            type(data) is set
        ):
            return data
        elif len(data) == 0:
            return data
        else:
            result = []
            for value in (data.values() if type(data) is dict else data):
                if (
                    type(value) is dict or
                    type(value) is list or
                    type(value) is tuple or
                    type(value) is set
                ):
                    if len(value) == 0:
                        result.append(value)
                    else:
                        result += NestedJson._nested_get_values(value)
                else:
                    result.append(value)
            return result

    @staticmethod
    def _to_dictlike_mapping(data):
        if (
            type(data) is list or
            type(data) is tuple or
            type(data) is set
        ):
            return zip(range(len(data)), data)
        elif type(data) is dict:
            return data.items()

    @staticmethod
    def _nested_get_keys_lists(data) -> list:
        if not (
            type(data) is dict or
            type(data) is list or
            type(data) is tuple or
            type(data) is set
        ):
            return []
        else:
            result = []
            for key, value in list(NestedJson._to_dictlike_mapping(data)):
                if isinstance(key, tuple):
                    key = list(key)
                else:
                    key = [key]
                if (
                    type(value) is dict or
                    type(value) is list or
                    type(value) is tuple or
                    type(value) is set
                ):
                    if len(value) == 0:
                        result.append(key)
                    else:
                        for subkey in NestedJson._nested_get_keys_lists(value):
                            result.append(
                                key + subkey
                            )
                else:
                    result.append(key)
            return result

    @staticmethod
    def _nested_get_keys(data):
        return list(map(tuple, NestedJson._nested_get_keys_lists(data)))

    @staticmethod
    def _nest_flat_dict(data: dict) -> Union[dict,list]:
        result = dict()
        for key, value in data.items():
            if isinstance(key, tuple):
                d = result
                for part in key[:-1]:
                    if part not in d:
                        d[part] = dict()
                    d = d[part]
                d[key[-1]] = value
            else:
                d = result
                d[key] = value
        return NestedJson._nested_listlikedict_to_list(result)

    @staticmethod
    def _nested_nest_flat_dict(data: Union[list,dict,Any]) -> Union[list,dict,Any]:
        if data in [{}, []]:
            return data
        elif type(data) is dict:
            if NestedJson._has_nested_list_dict(data):
                return NestedJson._listlikedict_to_list(
                    NestedJson._nest_flat_dict(
                        {key: NestedJson._nested_nest_flat_dict(val) for key,val in data.items()}
                    )
                )
            else:
                return NestedJson._nest_flat_dict(data)
        elif type(data) is list:
            return [NestedJson._nested_nest_flat_dict(val) for val in data]
        else:
            return data

    @staticmethod
    def _nest_data_series(data: dict) -> Union[dict,list]:
        result = dict()
        for key, value in data.items():
            if isinstance(key, tuple):
                key = tuple(filter(NestedJson._not_fillvalue, key))
                d = result
                for part in key[:-1]:
                    if part not in d:
                        d[part] = dict()
                    d = d[part]
                d[key[-1]] = value
            else:
                d = result
                d[key] = value
        return NestedJson._nested_listlikedict_to_list(result)

    @staticmethod
    def _nested_nest_data_series(data: Union[list,dict,Any]) -> Union[list,dict,Any]:
        if data in [{}, []]:
            return data
        elif type(data) is dict:
            if NestedJson._has_nested_list_dict(data):
                return NestedJson._listlikedict_to_list(
                    NestedJson._nest_data_series(
                        {key: NestedJson._nested_nest_data_series(val) for key,val in data.items()}
                    )
                )
            else:
                return NestedJson._nest_data_series(data)
        elif type(data) is list:
            return [NestedJson._nested_nest_data_series(val) for val in data]
        else:
            return data

    @property
    def keys(self):
        return NestedJson._nested_get_keys(self.data)

    @property
    def keys_fillna_end(self):
        return list(map(
            tuple,
            zip(*zip_longest(*self.keys, fillvalue = self._FILLVALUE))
        ))

    @property
    def keys_fillna_start(self):
        return list(map(
            tuple,
            map(reversed,zip(*zip_longest(*map(reversed, self.keys), fillvalue = self._FILLVALUE)))
        ))

    @property
    def values(self):
        return NestedJson._nested_get_values(self.data)

    @property
    def flat_dict(self):
        return dict(zip(self.keys, self.values))

    @property
    def data_series(self) -> dict:
        return dict(zip(self.keys_fillna_end, self.values))

    @property
    def data_series_bfill(self) -> dict:
        return dict(zip(self.keys_fillna_start, self.values))

    @property
    def _as_parsed_flat_dict(self):
        return self.__class__(self._nest_flat_dict(self.data))

    @property
    def _as_parsed_nested_flat_dict(self):
        return self.__class__(self._nested_nest_flat_dict(self.data))

    @property
    def _as_parsed_data_series(self):
        return self.__class__(self._nest_data_series(self.data))

    @property
    def _as_parsed_nested_data_series(self):
        return self.__class__(self._nested_nest_data_series(self.data))

    @property
    def str(self):
        return json.dumps(self.data)

    @property
    def parsed(self):
        return _ParsedNestedJson(self)

    def get(self, *keys: Hashable) -> Any:
        '''Get sub-element value.'''
        data = self.data
        for k in keys: data = data[k]
        return data

    def to_data_series(self, into: Type[Iterable] = dict, bfill = False) -> Iterable:
        """
        Return an iterable object (default dictionary) of nested json-like data 
        with padded label key tuples.

        into (Type[Iterable]): default dict
            Iterable type to convert to the returned iterable object, such as,
            list, tuple, pandas `Series`.
        bfill (bool): default False
            Fill nested key tuples backward (default) or forward.

        Returns
        -------
        Data converted into specified Iterable Type object.
        """
        print(str(into))
        data_series = self.data_series_bfill if bfill else self.data_series
        if into in [dict]:
            return data_series
        elif into in [set()] or (
            isinstance(into, Type) and
            str(into) == "<class 'pandas.core.series.Series'>"
        ):
            return into(data_series)
        elif into in [set()] or (
            isinstance(into, Type) and
            str(into) == "<class 'pandas.core.frame.DataFrame'>"
        ):
            return into.from_dict({0: data_series})
        else:
            return into(data_series.items())

    def pipe_data(self, fn: Type) -> Any:
        '''Apply function to data.'''
        return fn(self.data)