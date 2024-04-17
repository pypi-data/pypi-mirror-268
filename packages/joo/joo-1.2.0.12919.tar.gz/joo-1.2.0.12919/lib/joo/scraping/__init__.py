"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import time
import json
import chardet
import hashlib
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup, Tag
from joo import ManagedObject
from joo.logging import LoggerHelper

class Session(ABC, ManagedObject, LoggerHelper):
    def __init__(self):
        ManagedObject.__init__(self)
        LoggerHelper.__init__(self)

        # control
        self._handle = None

    def __del__(self):
        self.close()
        ManagedObject.__del__(self)

    @abstractmethod
    def open(self, **kwargs): return None

    @abstractmethod
    def close(self): pass

    @abstractmethod
    def _get_page(self, url, cache, format, **kwargs): return None

    def get_page(self, url, cache=None, format="soup", **kwargs):
        if format == "html":
            return self._get_page(url, cache, "html", **kwargs)
        elif format == "soup":
            try:
                html = self.get_page(url, cache, "html", **kwargs)
                if html is None: return None
                return BeautifulSoup(html, "html.parser")
            except Exception as ex:
                self.exception(ex)
                return None
        else:
            return self._get_page(url, cache, format, **kwargs)

    @property
    def handle(self):
        return self.open()

    @classmethod
    def wait(cls, secs=1.0):
        time.sleep(secs)

    def bytes_str(self, content_bytes, encoding=None):
        try:
            if content_bytes is None: return ""
            if encoding:
                if encoding == "ISO-8859-1": encoding = None
            if encoding is None: encoding = chardet.detect(content_bytes)["encoding"]
            if encoding == "GB2312": encoding = "GBK"
            content_str = str(content_bytes, encoding, errors='replace')
        except:
            content_str = str(content_bytes, errors='replace')
        return content_str
    
    @classmethod
    def json_loads(cls, text):
        try:
            return json.loads(text)
        except:
            return None
        
    @classmethod
    def hash(cls, content):
        return hashlib.md5(content.encode(encoding="utf-8")).hexdigest()

    @classmethod
    def soup_walk(cls, base_node, recursive, cb_proc, cb_data):
        def __walk(base_node, recursive, cb_proc, cb_data, include_base_node):
            if base_node is None: return True  # keep walking
            if include_base_node:
                if not cb_proc(base_node, cb_data): return False  # stop walking
            if hasattr(base_node, "children"):
                for child_node in base_node.children:
                    if child_node is None: continue
                    if not cb_proc(child_node, cb_data): return False  # stop walking
                    if recursive:
                        if not __walk(child_node, recursive,
                                      cb_proc, cb_data,
                                      False): return False  # stop walking
            return True  # keep walking
        
        try:
            __walk(base_node, recursive, cb_proc, cb_data, True)
            return True  # successful
        except:
            return False  # failed

    @classmethod
    def soup_find_all(cls, node, name=None, attrs={}, limit=None):
        def __match_proc(node, data):
            if not isinstance(node, Tag): return True  # keep walking

            # check name
            name = data["name"]
            if name:
                if node.name != name: return True  # keep walking
            
            # check attrs
            matched = False
            attrs = data["attrs"]
            if attrs is None: attrs = {}
            if len(attrs) == 0:
                matched = True
            else:
                for (key, value) in attrs.items():
                    # expected value(s)
                    # key: value
                    # key: [value1, value2, ...]
                    expected_values = value if isinstance(value, list) else [value]

                    # node value(s)
                    t = node.attrs.get(key)
                    if t is None: continue  # doesn't have the attribute
                    if isinstance(t, list):
                        node_values = t  # key: [value1, value2, ...]
                    else:
                        # NOTICE: There should be some bug in BeautifulSoup that
                        # sometime the values are not automatically splitted,
                        # and that resulted in element could not be found via
                        # find_xxx() calls. 
                        node_values = t.split(" ")  # key: "value1 value2 ..."
                    for node_value in node_values:
                        if node_value in expected_values:
                            matched = True
                            break
                    if matched: break
            if not matched: return True  # keep walking

            # add to results
            results = data["results"]
            results.append(node)

            # check limit
            limit = data["limit"]
            return (True if limit is None else (len(results) < limit))

        results = []
        if not cls.soup_walk(node, True,
                             __match_proc, {
                                 "name": name,
                                 "attrs": attrs,
                                 "limit": limit,
                                 "results": results
                             }): return None
        return results

    @classmethod
    def soup_find(cls, node, name=None, attrs={}):
        results = cls.soup_find_all(node, name, attrs, 1)
        if results is None: return None
        return None if len(results) < 1 else results[0]