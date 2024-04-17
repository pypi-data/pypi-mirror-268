"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import threading
from abc import ABC, abstractmethod
from joo import ManagedObject
from joo.logging import LoggerHelper

class Connection(ABC, ManagedObject, LoggerHelper):
    def __init__(self, **kwargs):
        ManagedObject.__init__(self)
        LoggerHelper.__init__(self)

        # control
        self._owner = None  # (connection owner object, connection pool object)
        self._handle = None  # connection handle owned by self

    def __del__(self):
        self.gc()
        ManagedObject.__del__(self)

    @property
    def handle(self):
        if self._owner:
            return self._owner[0].handle
        else:
            return self.open()

    @abstractmethod
    def _open(self, **kwargs): return None

    def open(self, **kwargs):
        if self._state:
            return (self._handle if self._state == "opened" else None)

        # open connection owned by self
        self._owner = None
        try:
            self._handle = self._open(**kwargs)
            if self._handle is None: return None
            self._state = "opened"
            return self._handle
        except Exception as ex:
            self.exception(ex)
            self._handle = None
            self._state = None
            return None
        
    @abstractmethod
    def _close(self, handle): pass

    def close(self):
        if self._state != "opened": return

        # close connection owned by self
        self._close(self._handle)
        self._handle = None
        self._state = None

    def link(self, connection_pool, connection_obj):
        if self._state is not None: return None
        if connection_pool is None: return None
        if connection_obj is None: return None
        if connection_obj._handle is None: return None

        # commence lease of connection from pool
        self._handle = None
        self._owner = (connection_obj, connection_pool)
        connection_pool.commence_lease(self, connection_obj)
        self._state = "linked"
    
    def unlink(self):
        if self._state != "linked": return

        # terminate lease of connection from pool
        connection_pool = self._owner[1]
        connection_obj = self._owner[0]
        connection_pool.terminate_lease(self, connection_obj)
        self._owner = None
        self._state = None

    def gc(self):
        if self._state == "opened": self.close()
        elif self._state == "linked": self.unlink()

class ConnectionPool(ManagedObject, LoggerHelper):
    def __init__(self, connection_class, min_size=0, max_size=0, init=True, **kwargs):
        ManagedObject.__init__(self)
        LoggerHelper.__init__(self)

        # settings
        self._connection_class = connection_class
        self._connection_params = kwargs
        self._pool_min_size = min_size
        self._pool_max_size = max_size

        # initialize
        self._pool = None  # (connection owner object, connection lessee object)
        self._pool_lock = threading.Lock()
        if init: self._initialize()  # NOTE: Logger is not binded yet! 

    def __del__(self):
        self._cleanup()
        ManagedObject.__del__(self)

    def __add_connection(self):
        try:
            connection_obj = self._connection_class(**self._connection_params)
            connection_obj.bind_logger(self.logger)
            if connection_obj.open(**self._connection_params) is None: return None
            self._pool.append([connection_obj, None])
            return connection_obj
        except Exception as ex:
            self.exception(ex)
            return None
        
    def __lease_connection(self, connection_obj):
        try:
            lessee_obj = self._connection_class(**self._connection_params)
            lessee_obj.bind_logger(self.logger)
            lessee_obj.link(self, connection_obj)
            return lessee_obj
        except Exception as ex:
            self.exception(ex)
            return None
        
    def _initialize(self):
        if self._state: return

        # initialize the pool with minimum connections 
        self._pool = []
        with self._pool_lock:
            try:
                while len(self._pool) < self._pool_min_size:
                    if self.__add_connection() is None: return
            except Exception as ex:
                self.exception(ex)
        self._state = "inited"
    
    def initialize(self): self._initialize()

    def _cleanup(self):
        if self._state is None: return

        # clean up the pool by closing all connections
        with self._pool_lock:
            try:
                item = self._pool.pop()
                while len(self._pool) > 0:
                    item = self._pool.pop()
                    item[0].close()
            except Exception as ex:
                self.exception(ex)
        self._pool = None
        self._state = None
    
    def cleanup(self): self.cleanup()

    def commence_lease(self, lessee_obj, owner_obj):
        for item in self._pool:
            if item[0] != owner_obj: continue
            if item[1]: raise Exception()  # invalid call beyond framework
            item[1] = lessee_obj
            break

    def terminate_lease(self, lessee_obj, owner_obj):
        for item in self._pool:
            if item[0] != owner_obj: continue
            if item[1] != lessee_obj: raise Exception()  # invalid call beyond framework
            item[1] = None
            break

    def get_connection(self):
        if self._state is None: return

        # lease connection
        with self._pool_lock:
            # lease existing connection
            for item in self._pool:
                if item[1]: continue
                return self.__lease_connection(item[0])
            
            # lease new connection
            if self._pool_max_size > 0:
                if len(self._pool) >= self._pool_max_size: return None
            connection_obj = self.__add_connection()
            if connection_obj is None: return None
            return self.__lease_connection(connection_obj)
