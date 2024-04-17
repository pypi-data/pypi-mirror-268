"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import os
from joo.logging import LoggerHelper, Loggers
from joo.sysutil import FileSystemDataStore

class CLIApp(LoggerHelper):
    def __init__(self, simple_main_proc=None):
        LoggerHelper.__init__(self)

        # initialize workspace
        self.workspace = FileSystemDataStore()

        # initialize loggers
        self.loggers = Loggers()
        self.bind_logger(self.loggers)

        # simple app
        self.simple_main_proc = simple_main_proc
        if simple_main_proc: self.main()

    def register_logger(self, logger):
        self.loggers.register_logger(logger)

    def init_app(self): return True

    def determine_workflow(self): return "default"

    def _globals(self):
        """Global namespace for workflow handler searching.

        When dispatching workflow, if the handler is not found within
        the members, it could alternatively search in a global namespace,
        so that the workflow handler could be as a regular function.
        If application needs to have this capability, simple implement
        this with below code:

            def _globals(self): return globals()
        """
        return None

    def run_workflow(self, workflow_name):
        try:
            #handler name
            handler_name = "workflow_" + workflow_name

            #find handler in members
            if hasattr(self, handler_name):
                f = getattr(self, handler_name)
                if callable(f): return f()

            #find handler in globals
            x_globals = self._globals()
            if x_globals:
                f = x_globals.get(handler_name)
                if callable(f): return f(self)

            #
            return 1
        except Exception as ex:
            self.exception(ex)
            return 1

    def workflow_default(self):
        return self.simple_main_proc(self) if self.simple_main_proc else 0

    def cleanup_app(self):
        #cleanup loggers
        self.loggers.close()

    def main(self):
        exit_code = 1
        try:
            #initialize application
            if not self.init_app(): raise Exception()

            #determine workflow
            workflow_name = self.determine_workflow()
            if workflow_name is None: raise Exception()

            #run workflow
            exit_code = self.run_workflow(workflow_name)
        except Exception as ex:
            self.exception(ex)
        finally:
            #cleanup application
            self.cleanup_app()
        os._exit(exit_code)