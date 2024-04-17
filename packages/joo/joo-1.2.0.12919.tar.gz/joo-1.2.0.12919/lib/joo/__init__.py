"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import time

class ManagedObject:
    """Base class of the managed object types.

    Managed object could be:
    - The object acquires some resource during its lifecycle.  The resource
    must be released when object is deleted.
    - The object is controlled by a state machine.  The state must be back
    to original state when object is deleted.

    Typical managed object classes include paired methods as:
    - open()/close()
    - create()/delete()

    Derived classes could use the _state to maintain the state of the object.
    And it must have the logic to make sure the _state back to None before
    it's deleted, otherwise, exception will be raised.

    NOTICE: Make sure __init__() and __del__() in base class will be called
    in derived classes when they are overrided.

    class DerivedClass(ManagedObject):
        def __init__(self):
            ManagedObject.__init__(self)
            ...

        def __del__(self):
            ...
            ManagedObject.__del__(self)
    """
    def __init__(self):
        self._state = None

    def __del__(self):
        if self._state != None:
            raise Exception("Object must be released explicitly.", self)
        
    @property
    def state(self): return self._state

class ManagedObjects(list):
    """List of objects to be managed.

    NOTICE: This class is independent to ManagedObject although their names
    are similar!!!

    This class is used to maintain a list of objects.
    
    And it also provides a simple GC (garbage collection) mechanism so that
    the objects in the list could be deleted gracefully.  GC is optional
    when using the ManagedObjcts class, but when GC is needed, make sure
    the objects added into the list is with gc() where the cleanup could be
    well handled.

    One of the use cases of ManagedObjects is to have a keeper of all
    objects created with the type in a subsystem, so that the GC could
    be controlled globally.  It could be defined as:

    class ObjectClass:
        _objects = ManagedObjects()

        @classmethod
        def GC(cls): cls._objects.gc()

        def __init__(self):
            self._objects.register_object(self)
            ...
        
        def __del__(self):
            ...
            self._objects.unregister_object(self)
        
        def gc(self):
            self.close()
            self._objects.unregister_object(self)
            del self

        def open(self):
            ...
        
        def close(self):
            ...
    """
    def register_object(self, obj, obj_type=None):
        if obj is None: return
        if obj_type:
            if not isinstance(obj, obj_type): raise Exception()
        if obj not in self: self.append(obj)

    def unregister_object(self, obj):
        while obj in self: self.remove(obj)
    
    def gc(self):
        for obj in self: obj.gc()
        self.clear()

class DebugTimer:
    def __init__(self):
        self._checkpoints = []
        self.reset()

    def reset(self):
        self._checkpoints.clear()
        self.record()

    def record(self, finished_step_label=""):
        self._checkpoints.append((time.perf_counter(), finished_step_label))

    def __enter__(self):
        self.reset()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.record()
        
    def get_results(self):
        if len(self._checkpoints) <= 1: return None
        results = []
        base_ts = 0.0
        last_ts = None
        for (ts, label) in self._checkpoints:
            if last_ts is None:
                base_ts = ts
            else:
                results.append((label, ts - last_ts, ts - base_ts))
            last_ts = ts
        return results
    
    def get_step_duration(self, step_label=None):
        results = self.get_results()
        if results is None: return None
        if step_label is None:
            return results[-1][2]  # total duration
        else:
            for (label, step_duration, process_duration) in results:
                if label == step_label: return step_duration
        return None
    
    def format_results(self, show_step_percentage=False, show_total_duration=False):
        results = self.get_results()
        if results is None: return ""
        
        # steps
        t = ""
        total_duration = results[-1][2]
        index = 1
        for (label, step_duration, process_duration) in results:
            step_label = label if label != "" else "(#{})".format(index)
            if t != "": t += "\r\n"
            t += "{}: {:.4f} seconds".format(step_label, step_duration)
            if show_step_percentage and total_duration > 0.0:
                t += " ({:.2f}%)".format(step_duration / total_duration * 100.0)
            index += 1
        
        # total
        if show_total_duration:
            t += "\r\nTotal: {:.4f} seconds".format(total_duration)
        #
        return t
    
class DebugBlock:
    def __init__(self, name, logger=None, mode="b/e"):
        self.name = name
        self.logger = logger
        if mode in ["b/e", "begin/end"]: self.verbs = ("Begin", "End")
        elif mode in ["s/e", "start/end"]: self.verbs = ("Start", "End")
        elif mode in ["o/c", "open/close"]: self.verbs = ("Open", "Close")
        elif mode in ["e/l", "enter/leave"]: self.verbs = ("Enter", "Leave")
        else: self.verbs = ("", "")

    def __enter__(self):
        text = ">>>>>>>> " + (self.verbs[0] + " " + self.name).strip() + " >>>>>>>>"
        if self.logger:
            self.logger.debug(text)
        else:
            print(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        text = "<<<<<<<< " + (self.verbs[1] + " " + self.name).strip() + " <<<<<<<<"
        if self.logger:
            self.logger.debug(text)
        else:
            print(text)