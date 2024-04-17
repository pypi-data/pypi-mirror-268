"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import os
import time
import threading
import traceback
from abc import ABC, abstractmethod
from joo import ManagedObject, ManagedObjects

class MessageLevel:
    GENERAL = 5
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
    SEPARATOR = 100

class Logger(ABC, ManagedObject):
    def __init__(self):
        ManagedObject.__init__(self)

        # settings
        self.enabled_level = 0  # log messages at any level (level >= 0)
        self.use_log_lock = False  # use thread lock when logging message

    def __del__(self):
        # NOTE: Not calling close() here to make sure the object will be
        # closed explicitly to make sure it's closed gracefully before
        # garbage collection process.
        ManagedObject.__del__(self)

    def open(self):
        if self._state is not None: return True
        self._log_lock = threading.Lock() if self.use_log_lock else None
        self._state = "opened"
        return True

    def close(self):
        if self._state is None: return
        self._log_lock = None
        self._state = None

    def gc(self):
        self.close()

    @abstractmethod
    def _log(self, timestamp, message, depth, level): pass

    def _log_low(self, timestamp, message, depth, level, std_level):
        # open
        if not self.open(): return
        
        # log
        if level >= self.enabled_level:
            if self._log_lock:
                with self._log_lock: self._log(timestamp, message, depth, std_level)
            else:
                self._log(timestamp, message, depth, std_level)

    def log(self, message, depth=0, level=MessageLevel.GENERAL):
        self._log_low(time.time(), message, depth, level, MessageLevel.GENERAL)

    def debug(self, message, depth=0, level=MessageLevel.DEBUG):
        self._log_low(time.time(), message, depth, level, MessageLevel.DEBUG)

    def info(self, message, depth=0, level=MessageLevel.INFO):
        self._log_low(time.time(), message, depth, level, MessageLevel.INFO)

    def warning(self, message, depth=0, level=MessageLevel.WARNING):
        self._log_low(time.time(), message, depth, level, MessageLevel.WARNING)

    def error(self, message, depth=0, level=MessageLevel.ERROR):
        self._log_low(time.time(), message, depth, level, MessageLevel.ERROR)

    def critical(self, message, depth=0, level=MessageLevel.CRITICAL):
        self._log_low(time.time(), message, depth, level, MessageLevel.CRITICAL)

    def separator(self, ch="=", width=80, level=MessageLevel.SEPARATOR):
        message = ch * width if width > 0 else ch
        self._log_low(time.time(), message, 0, level, MessageLevel.SEPARATOR)

    def exception(self, ex, depth=0, level=MessageLevel.DEBUG):
        message = "EXCEPTION: " + str(ex) + "\n"
        message += traceback.format_exc()
        self._log_low(time.time(), message, depth, level, MessageLevel.GENERAL)

class TextLogger(Logger):
    def __init__(self):
        Logger.__init__(self)

        # settings
        self.include_timestamp = True  # whether to include timestamp
        self.use_utc = False  # whether to use UTC or local time
        self.indent_size = 4  # size of indent
        self.vline = "|"  # vertical line for indent

    def format_output(self, timestamp, message, depth, level):
        # separator
        if level == MessageLevel.SEPARATOR: return message

        # create timestamp text
        ts_text = ""
        if self.include_timestamp:
            if self.use_utc:
                ts_text = time.strftime("%Y-%m-%d %H:%M:%SZ ", time.gmtime(timestamp))
            else:
                ts_text = time.strftime("%Y-%m-%d %H:%M:%S ", time.localtime(timestamp))

        # create message text
        message_text = ""
        if level == MessageLevel.DEBUG:
            message_text = message
        elif level == MessageLevel.INFO:
            message_text = "INFO: " + message
        elif level == MessageLevel.WARNING:
            message_text = "WARNING: " + message
        elif level == MessageLevel.ERROR:
            message_text = "ERROR: " + message
        elif level == MessageLevel.CRITICAL:
            message_text = "CRITICAL: " + message
        else:
            message_text = message
        message_lines = message_text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
        if len(message_lines) == 0: return ts_text

        # create indent text
        indent_size = self.indent_size
        indent_text = ""
        if depth < 0: depth = 0
        if indent_size < 0: indent_size = 0
        if indent_size < 3:
            indent_text = " " * indent_size
        else:
            if len(self.vline) == 1:
                indent_text = self.vline + " " * (indent_size - 1)
            else:
                indent_text = " " * indent_size

        # format output
        output_text = ""
        for i in range(0, len(message_lines)):
            if i == 0:
                output_text = ts_text + indent_text * depth + message_lines[i]
            else:
                output_text += "\n" + " " * len(ts_text) + indent_text * depth + message_lines[i]

        #
        return output_text

class ConsoleLogger(TextLogger):
    def __init__(self):
        TextLogger.__init__(self)

    def _log(self, timestamp, message, depth, level):
        output_text = self.format_output(timestamp, message, depth, level)
        print(output_text)

class TextFileLogger(TextLogger):
    def __init__(self):
        TextLogger.__init__(self)

        # settings
        self.encoding = "utf-8"  # text file encoding
        self.auto_flush = True  # whether to flush content immediately

        # control
        self._open_mode = "a"
        self._files = []

    def close(self):
        # close all files
        for f in self._files:
            if f is not None: f.close()
        self._files.clear()

        #
        TextLogger.close(self)

    @abstractmethod
    def _get_file(self, timestamp, message, depth, level): pass

    def _log(self, timestamp, message, depth, level):
        f = self._get_file(timestamp, message, depth, level)
        if f is None: return
        output_text = self.format_output(timestamp, message, depth, level)
        print(output_text, file=f)
        if self.auto_flush: f.flush()

class FileLogger(TextFileLogger):
    def __init__(self, filepath, reset=False):
        TextFileLogger.__init__(self)

        # control
        self._filepath = filepath
        if reset: self._open_mode = "w"

    def open(self):
        if self._state is not None: return True
        if not TextFileLogger.open(self): return False
        self._files = [None]
        return True        

    def _get_file(self, timestamp, message, depth, level):
        try:
            f = self._files[0]
            if f: return f
            f = open(self._filepath, mode=self._open_mode, encoding=self.encoding)
            if f: self._files[0] = f
            return f
        except:
            return None
        
    @classmethod
    def generate_filename(cls, prefix=None, use_utc=False):
        timestamp = time.time()
        filename = time.strftime(
            "%Y%m%d%H%M%S.log",
            time.gmtime(timestamp) if use_utc else time.localtime(timestamp))
        return (prefix + filename) if prefix else filename

class DatedFileLogger(TextFileLogger):
    def __init__(self, folderpath):
        TextFileLogger.__init__(self)

        # control
        self._folderpath = folderpath
        self._current_filepath = ""

    def open(self):
        if self._state is not None: return True
        if not TextFileLogger.open(self): return False
        self._files = [None]
        return True        

    def _get_file(self, timestamp, message, depth, level):
        # get file path
        filename = time.strftime(
            "%Y-%m-%d.log",
            time.gmtime(timestamp) if self.use_utc else time.localtime(timestamp))
        filepath = os.path.join(self._folderpath, filename)
        if filepath == self._current_filepath: return self._files[0]

        # close current file
        if self._files[0]:
            self._files[0].close()
            self._files[0] = None
            self._current_filepath = ""

        # open file
        try:
            f = open(filepath, mode=self._open_mode, encoding=self.encoding)
            if f:
                self._files[0] = f
                self._current_filepath = filepath
            return f
        except:
            return None

class Loggers(ManagedObjects):
    def __init__(self):
        ManagedObjects.__init__(self)

    def register_logger(self, logger):
        self.register_object(logger, Logger)

    def close(self):
        for obj in self: obj.close()
        self.clear()

    def log(self, message, depth=0, level=MessageLevel.GENERAL):
        for logger in self: logger.log(message, depth, level)

    def debug(self, message, depth=0, level=MessageLevel.DEBUG):
        for logger in self: logger.debug(message, depth, level)

    def info(self, message, depth=0, level=MessageLevel.INFO):
        for logger in self: logger.info(message, depth, level)

    def warning(self, message, depth=0, level=MessageLevel.WARNING):
        for logger in self: logger.warning(message, depth, level)

    def error(self, message, depth=0, level=MessageLevel.ERROR):
        for logger in self: logger.error(message, depth, level)

    def critical(self, message, depth=0, level=MessageLevel.CRITICAL):
        for logger in self: logger.critical(message, depth, level)

    def separator(self, ch="=", width=80, level=MessageLevel.SEPARATOR):
        for logger in self: logger.separator(ch, width, level)

    def exception(self, ex, depth=0, level=MessageLevel.DEBUG):
        for logger in self: logger.exception(ex, depth, level)

class LoggerHelper:
    def __init__(self):
        self._logger = None

    @property
    def logger(self):
        return self._logger

    def bind_logger(self, logger):
        self._logger = logger

    def log(self, message, depth=0, level=MessageLevel.GENERAL):
        if self._logger: self._logger.log(message, depth, level)

    def debug(self, message, depth=0, level=MessageLevel.DEBUG):
        if self._logger: self._logger.debug(message, depth, level)

    def info(self, message, depth=0, level=MessageLevel.INFO):
        if self._logger: self._logger.info(message, depth, level)

    def warning(self, message, depth=0, level=MessageLevel.WARNING):
        if self._logger: self._logger.warning(message, depth, level)

    def error(self, message, depth=0, level=MessageLevel.ERROR):
        if self._logger: self._logger.error(message, depth, level)

    def critical(self, message, depth=0, level=MessageLevel.CRITICAL):
        if self._logger: self._logger.critical(message, depth, level)

    def separator(self, ch="=", width=80, level=MessageLevel.SEPARATOR):
        if self._logger: self._logger.separator(ch, width, level)

    def exception(self, ex, depth=0, level=MessageLevel.DEBUG):
        if self._logger: self._logger.exception(ex, depth, level)

    def error_x(self, x, message, depth=0, level=MessageLevel.ERROR):
        self.error(message, depth, level)
        return x

    def exception_x(self, x, ex, depth=0, level=MessageLevel.DEBUG):
        self.exception(ex, depth, level)
        return x