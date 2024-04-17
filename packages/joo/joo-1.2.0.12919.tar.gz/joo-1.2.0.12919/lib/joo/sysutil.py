"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import os
import re
import sys
import json
import uuid
import time
import shutil
import base64
import getopt
import hashlib
import datetime
import tempfile
from abc import ABC, abstractmethod
from joo import ManagedObject, ManagedObjects
if os.name == "posix":
    import fcntl

def create_folder(folderpath):
    try:
        if not os.path.exists(folderpath): os.makedirs(folderpath)
    except:
        pass
    return os.path.isdir(folderpath)

def create_parent_folder(fpath):
    parent_folderpath = os.path.split(fpath)[0]
    return create_folder(parent_folderpath)

def alter_fname(ref_filepath, fname):
    return os.path.join(os.path.dirname(os.path.abspath(ref_filepath)), fname)

def alter_ext(ref_filepath, ext):
    return os.path.splitext(os.path.abspath(ref_filepath))[0] + ext

def normalize_fname(fname):
    fname = fname.strip()
    c_list = ['\\', '/', ':', '*', '?', '<', '>', '|', '"', '\t', '\b', '\n', '\r']
    for c in c_list: fname = fname.replace(c, "")
    return fname

def file_exists(filepath):
    return os.path.isfile(filepath)

def folder_exists(folderpath):
    return os.path.isdir(folderpath)

def delete_file(filepath):
    try:
        os.remove(filepath)
    except:
        pass
    return not file_exists(filepath)

def delete_folder(folderpath):
    try:
        shutil.rmtree(folderpath)
    except:
        pass
    return not folder_exists(folderpath)

def copy_file(source_filepath, dest_filepath):
    try:
        shutil.copy(source_filepath, dest_filepath)
        return True
    except:
        return False

def move_file(source_filepath, dest_filepath):
    try:
        shutil.move(source_filepath, dest_filepath)
        return True
    except:
        return False

def copy_folder(source_folderpath, dest_folderpath):
    try:
        shutil.copytree(source_folderpath, dest_folderpath)
        return True
    except:
        return False

def list_all(folderpath, recursive=False):
    def __walk(folderpath, l, recursive):
        fnames = os.listdir(folderpath)
        for fname in fnames:
            fpath = os.path.join(folderpath, fname)
            if os.path.isfile(fpath):
                l.append((fpath, False))
            else:
                l.append((fpath, True))
                if recursive:
                    if not __walk(fpath, l, recursive): return False
        return True

    l = []
    if not __walk(os.path.abspath(folderpath), l, recursive): return None
    return l

def list(folderpath, pattern=".*", recursive=False,
         match_fullpath=False,
         include_files=True, include_folders=True):
    l = []
    items = list_all(folderpath, recursive)
    if items is None: return None
    for fpath, is_folder in items:
        #file/folder filter
        if is_folder:
            if not include_folders: continue
        else:
            if not include_files: continue

        #pattern filter
        if match_fullpath:
            text = fpath.lower()
        else:
            text = os.path.basename(fpath).lower()
        if re.fullmatch(pattern, text): l.append((fpath, is_folder))
    return l

def list_files(folderpath, pattern=".*", recursive=False,
               match_fullpath=False):
    l = []
    items = list(folderpath, pattern, recursive, match_fullpath, True, False)
    if items is None: return None
    for item in items: l.append(item[0])
    return l

def list_folders(folderpath, pattern=".*", recursive=False,
                 match_fullpath=False):
    l = []
    items = list(folderpath, pattern, recursive, match_fullpath, False, True)
    if items is None: return None
    for item in items: l.append(item[0])
    return l

def load_file_contents(filepath, encoding="utf-8"):
    try:
        with open(filepath, "r", encoding=encoding) as f: contents = f.read()
        return contents
    except:
        return None

def save_file_contents(filepath, contents, encoding="utf-8", create_parent=True):
    try:
        if create_parent: create_parent_folder(filepath)
        with open(filepath, "w", encoding=encoding) as f: f.write(contents)
        return True
    except:
        return False

def load_file_bytes(filepath):
    try:
        with open(filepath, "rb") as f: contents = f.read()
        return contents
    except:
        return None

def save_file_bytes(filepath, contents, create_parent=True):
    try:
        if create_parent: create_parent_folder(filepath)
        with open(filepath, "wb") as f: f.write(contents)
        return True
    except:
        return False

def load_file_json(filepath, encoding="utf-8"):
    try:
        with open(filepath, "r", encoding=encoding) as f: data = json.load(f)
        return data
    except:
        return None

def save_file_json(filepath, data, encoding="utf-8", create_parent=True):
    try:
        if create_parent: create_parent_folder(filepath)
        with open(filepath, "w", encoding=encoding) as f:
            json.dump(data, f, indent="\t")
        return True
    except:
        return False

def load_file_base64(filepath, encoding="utf-8"):
    try:
        with open(filepath, "rb") as f:
            if encoding is None:
                contents = base64.b64encode(f.read())
            else:
                contents = base64.b64encode(f.read()).decode(encoding)
        return contents
    except:
        return None

class TempFileSystemObject(ManagedObject):
    _objects = ManagedObjects()

    @classmethod
    def GC(cls): cls._objects.gc()

    def __init__(self):
        self._objects.register_object(self)
        ManagedObject.__init__(self)

        # control
        self._is_folder = False
        self._fpath = None

    def __del__(self):
        ManagedObject.__del__(self)
        self._objects.unregister_object(self)

    def gc(self):
        self.delete()
        self._objects.unregister_object(self)
        del self

    @property
    def path(self): return self._fpath

    def create(self, temp_folderpath=None):
        # create
        if temp_folderpath is None: temp_folderpath = tempfile.gettempdir()
        while True:
            fpath = os.path.join(temp_folderpath, str(uuid.uuid4()))
            if not os.path.exists(fpath): break
        if self._is_folder:
            if not create_folder(fpath): return None
        else:
            save_file_contents(fpath, "")
            if not file_exists(fpath): return None
        
        # attach
        return self.attach(fpath)

    def attach(self, fpath):
        # delete
        self.delete()

        # attach
        self._state = "created"
        self._fpath = fpath

    def detach(self):
        # detach
        fpath = self._fpath
        self._fpath = None
        self._state = None
        return fpath

    def delete(self):
        # delete
        if self._fpath:
            if self._is_folder:
                delete_folder(self._fpath)
            else:
                delete_file(self._fpath)
        self._fpath = None
        self._state = None

class TempFile(TempFileSystemObject):
    def __init__(self, temp_folderpath=None):
        TempFileSystemObject.__init__(self)
        self._is_folder = False
        self.create(temp_folderpath)

class TempFolder(TempFileSystemObject):
    def __init__(self, temp_folderpath=None):
        TempFileSystemObject.__init__(self)
        self._is_folder = True
        self.create(temp_folderpath)

def create_temp_file(temp_folderpath=None):
    obj = TempFile(temp_folderpath)
    if obj.path is None: return None
    return obj

def create_temp_folder(temp_folderpath=None):
    obj = TempFolder(temp_folderpath)
    if obj.path is None: return None
    return obj

def create_temp_f(is_folder=False, temp_folderpath=None):
    return create_temp_folder(temp_folderpath) if is_folder else create_temp_file(temp_folderpath)

class FileSystemDataStore:
    def __init__(self, root_folderpath=None):
        self.root_folderpath = root_folderpath if root_folderpath else os.getcwd()

    def get_path(self, fname, create_parent=False):
        fpath = os.path.join(self.root_folderpath, fname)
        if create_parent: create_parent_folder(fpath)
        return fpath

    def get_parent_path(self, fname):
        return os.path.split(self.get_path(fname))[0]

    def get_dated_path(self, fname, date=None, create_parent=False):
        date_part = None
        if date:
            if type(date) == str:
                date_part = date
            elif type(date) == datetime.datetime:
                date_part = date.strftime("%Y-%m-%d")
        if date_part is None:
            date_part = datetime.datetime.today().strftime("%Y-%m-%d")
        fpath = os.path.join(self.root_folderpath, date_part, fname)
        if create_parent: create_parent_folder(fpath)
        return fpath

    def get_dated_parent_path(self, fname, date=None):
        return os.path.split(self.get_dated_path(fname, date))[0]

    def get_temp_folderpath(self):
        return self.get_path(".temp")
    
    def create_temp_file(self): return create_temp_file(self.get_temp_folderpath())

    def create_temp_folder(self): return create_temp_folder(self.get_temp_folderpath())

FSDS = FileSystemDataStore
Workspace = FileSystemDataStore

class FileSystemLock(ManagedObject, FileSystemDataStore):
    def __init__(self, id, temp_folderpath=None):
        ManagedObject.__init__(self)
        FileSystemDataStore.__init__(self, None)

        # control
        self.id = id
        if temp_folderpath is None: temp_folderpath = tempfile.gettempdir()
        self.root_folderpath = os.path.join(temp_folderpath, id)
        self.lockfile = None

    def __del__(self):
        self.unlock()
        ManagedObject.__del__(self)

    def gc(self):
        self.unlock()

    def lockfile_filepath(self):
        return self.get_path("lock.ctl", True)
    
    def is_locked(self):
        filepath = self.lockfile_filepath()
        if not file_exists(filepath): return False
        if os.name == "nt":
            try:
                os.remove(filepath)
                return False
            except:
                return True
        elif os.name == "posix":
            f = None
            try:
                f = open(filepath, "w")
                fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                f.close()
                return False
            except:
                if f: f.close()
                return True
        else: raise Exception()

    def lock(self):
        if self._state: return self._state
       
        if self.is_locked():
            self._state = "visitor"
        else:
            try:
                # lock
                self.lockfile = open(self.lockfile_filepath(), "w")
                if os.name == "nt":
                    pass
                elif os.name == "posix":
                    fcntl.flock(self.lockfile.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                else: raise Exception()

                # update state
                self._state = "owner"

                # initialize workspace
                self.initialize_workspace()
            except:
                if self.lockfile:
                    self.lockfile.close()
                    self.lockfile = None
                self._state = None
        return self._state
    
    def unlock(self):
        if self._state == "owner":
            # clean up workspace
            self.cleanup_workspace()

            # unlock
            if os.name == "nt":
                pass
            elif os.name == "posix":
                fcntl.flock(self.lockfile.fileno(), fcntl.LOCK_UN)
            else: raise Exception()
            self.lockfile.close()
            self.lockfile = None
            delete_file(self.lockfile_filepath())

            # delete parent folder
            delete_folder(self.root_folderpath)
        self._state = None

    def initialize_workspace(self):
        self.cleanup_workspace()

    def cleanup_workspace(self):
        fpath_lockfile = os.path.realpath(self.lockfile_filepath())
        items = list_all(self.root_folderpath)
        for fpath, is_folder in items:
            if is_folder:
                delete_folder(fpath)
            else:
                if os.path.realpath(fpath) == fpath_lockfile: continue
                delete_file(fpath)

FSL = FileSystemLock
FSLock = FileSystemLock

class Cache(ABC):
    @abstractmethod
    def set(self, key, value, text_format=False): pass

    @abstractmethod
    def remove(self, key): pass

    @abstractmethod
    def get(self, key, valid_period=0, text_format=False): pass

    @abstractmethod
    def clear(self, valid_period=0): pass

    @classmethod
    def make_key(cls, resource_id):
        return hashlib.md5(resource_id.encode(encoding="utf-8")).hexdigest()
    
class FileSystemCache(Cache, FileSystemDataStore):
    def __init__(self, root_folderpath=None):
        FileSystemDataStore.__init__(self, root_folderpath)

    def _get_filepath(self, key):
        return self.get_path(key, True)

    def set(self, key, value, text_format=False):
        fpath = self._get_filepath(key)
        if value is None:
            delete_file(fpath)
        else:
            if text_format:
                save_file_contents(fpath, value)
            else:
                save_file_bytes(fpath, value)

    def remove(self, key):
        fpath = self._get_filepath(key)
        delete_file(fpath)

    def get(self, key, valid_period=0, text_format=False):
        fpath = self._get_filepath(key)
        if not file_exists(fpath): return None
        if valid_period > 0:
            # NOTE: getctime() is with issue on some systems.
            # For example, on Windows with some file system (aka. drives), when a file
            # is deleted and recreated, the ctime could be as the file before it's deleted.
            if (time.time() - os.path.getmtime(fpath)) > valid_period: return None
        if text_format:
            return load_file_contents(fpath)
        else:
            return load_file_bytes(fpath)

    def clear(self, valid_period=0):
        fpaths = list_files(self.root_folderpath)
        t_now = time.time()
        if fpaths is None: return
        if valid_period > 0:
            for fpath in fpaths:
                if (t_now - os.path.getmtime(fpath)) > valid_period:
                    delete_file(fpath)
        else:
            for fpath in fpaths:
                delete_file(fpath)

def parse_command_line(parts):
    """Parse command line.

    Syntax of command list is as:
    program <command 1> <command 2> ... [option 1] [option 2] ...

    Commands are required and options are optional, and commands are always
    before options.
    
    "parts" is specifying the definition of all arguments.  It's a list
    of tuples of (key, short, long) to define a command or an option.
    "key" is the name or argument.  "__" prefixed name are reserved.
    "short" is the short format of an option.  eg. "-t:" expects an option
    givenas "-t <value>", "-t" expects an option without value.  Short must
    be one character.
    "long" is the long format of an option.  eg. "time=" expects an option
    give as "--time=<value>", "time" expects an option given as "--time".
    When "short" and "long" are both empty(""), it specifies a command.

    Example:
    
    test.py calculate -b -i 123 --p1=456 --p2

    "parts" = [
        ("verb", "", ""),
        ("b", "-b", ""),
        ("i", "-i:", ""),
        ("p1", "", "p1="),
        ("p2", "", "p2")
    ]

    result = {
        '__cmd__': 'test.py calculate -b -i 123 --p1=456 --p2',
        '__argn__': 7,
        '__argv0__': 'test.py',
        'verb': 'calculate',
        'b': '',
        'i': '123',
        'p1': '456',
        'p2': '',
        '__args__': []
    }
    """
    try:
        #process parts
        parts_commands = []
        parts_options = []
        shortopts = ""
        longopts = []
        for name, short, long in parts:
            if short == "" and long == "":
                parts_commands.append(name)
            else:
                shortopts += short
                longopts.append(long)
                formats = []
                if short != "": formats.append(short.replace(":", ""))
                if long != "": formats.append("--" + long.replace("=", ""))
                parts_options.append((name, formats))

        #get basic information
        r = {}
        r["__cmd__"] = " ".join(sys.argv)
        r["__argn__"] = len(sys.argv)
        r["__argv0__"] = sys.argv[0]
        if len(sys.argv) <= 1: return r

        #get commands
        command_count = len(parts_commands)
        if len(sys.argv) < 1 + command_count: return None
        for i in range(0, command_count):
            r[parts_commands[i]] = sys.argv[1 + i]

        #get options
        opts, args = getopt.getopt(sys.argv[1 + command_count:], shortopts, longopts)
        for opt_name, opt_value in opts:
            for name, formats in parts_options:
                if opt_name in formats:
                    r[name] = opt_value

        #get args
        r["__args__"] = args

        #
        return r
    except:
        return None