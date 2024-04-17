"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import pymysql
import datetime
from joo.db import Connection as _BaseConnection
import joo.db.sqlbuilder as sqlbuilder

class Connection(_BaseConnection):
    def __init__(self, **kwargs):
        _BaseConnection.__init__(self, **kwargs)

        # settings
        self.default_host = kwargs.get("host", None)
        self.default_port = kwargs.get("port", 3306)
        self.default_user = kwargs.get("user", None)
        self.default_password = kwargs.get("password", None)
        self.default_database = kwargs.get("database", None)
        self.default_chatset = kwargs.get("charset", "utf8")
        self.log_request = kwargs.get("log_request", False)
        self.commit_before_query = kwargs.get("commit_before_query", True)

        # control
        self._connect_params = None

    def _open(self, **kwargs):
        # NOTE: called by framework
        try:
            self._connect_params = {
                "host": kwargs.pop("host", self.default_host),
                "port": kwargs.pop("port", self.default_port),
                "user": kwargs.pop("user", self.default_user),
                "password": kwargs.pop("password", self.default_password),
                "database": kwargs.pop("database", self.default_database),
                "charset": kwargs.pop("charset", self.default_chatset)
            }
            params = self._connect_params
            self.debug("Connecting database...")
            self.debug("host={} port={} user={} database={}".format(
                params["host"],
                params["port"],
                params["user"],
                params["database"]), 1)
            return pymysql.connect(**self._connect_params)
        except Exception as ex:
            self.exception(ex)
            self._connect_params = None
            return None
    
    def _close(self, handle):
        # NOTE: called by framework
        try:
            if handle:
                self.debug("Disconnecting database...")
                handle.close()
                self._connect_params = None
        except Exception as ex:
            self.exception(ex)

    def _reconnect_on_error(self, ex, auto_reconnect):
        if not auto_reconnect: return False
        if self._state == "linked": 
            return self._owner[0]._reconnect_on_error(ex, auto_reconnect)
        if self._state != "opened": return False
        
        # check error
        if type(ex) == pymysql.OperationalError:
            errcode = ex.args[0]
            if errcode not in [2006, 2013]: return False
        elif type(ex) == pymysql.err.InterfaceError:
            pass
        else: return False

        # reconnect
        try:
            # close connection
            self._close(self._handle)
            self._handle = None

            # reconnect
            self.debug("Reconnecting database...")
            self._handle = pymysql.connect(**self._connect_params)
            return (self._handle is not None)
        except Exception as ex:
            self.exception(ex)
            return False
    
    def _execute(self,
                 sql_or_script,
                 commit_before_execute,
                 commit_after_execute,
                 fetch_rows,
                 auto_reconnect):
        if self._state == "linked":
            return self._owner[0]._execute(
                sql_or_script, 
                commit_before_execute,
                commit_after_execute,
                fetch_rows,
                auto_reconnect)
        if self._state != "opened": return None

        # check sql/script
        if isinstance(sql_or_script, str): sql_list = [sql_or_script]
        elif isinstance(sql_or_script, list): sql_list = sql_or_script
        elif isinstance(sql_or_script, tuple): sql_list = sql_or_script
        else: return None
        if len(sql_list) == 0: return None

        # get connection
        handle = self.handle
        if handle is None: return None

        # execute
        reconnect = False
        cursor = None
        try:
            # commit before execute
            if commit_before_execute: handle.commit()

            # open cursor
            cursor = handle.cursor()

            # execute SQL(s)
            for sql in sql_list:
                if self.log_request:
                    self.debug("Executing SQL...")
                    self.debug(sql, 1)
                affected_rows = cursor.execute(sql)

            # get result
            if fetch_rows < 0:
                results = affected_rows  # result from last SQL
            elif fetch_rows == 0:
                results = cursor.fetchall()
            else:
                results = cursor.fetchmany(fetch_rows)

            # close cursor
            cursor.close()
            cursor = None

            # commit after execute
            if commit_after_execute: handle.commit()

            #
            return results
        except Exception as ex:
            self.exception(ex)
            if cursor: handle.rollback()
            reconnect = self._reconnect_on_error(ex, auto_reconnect)
        finally:
            if cursor: cursor.close()
        if reconnect:
            return self._execute(
                sql_or_script,
                commit_before_execute,
                commit_after_execute,
                fetch_rows,
                auto_reconnect=False)
        
        #
        return None

    def execute(self, sql_or_script, commit=True):
        return self._execute(
            sql_or_script,
            commit_before_execute=False,
            commit_after_execute=commit,
            fetch_rows=-1,
            auto_reconnect=True)
    
    def query(self, sql, fetch_rows=0):
        return self._execute(
            sql,
            commit_before_execute=self.commit_before_query,
            commit_after_execute=False,
            fetch_rows=fetch_rows,
            auto_reconnect=True
        )

    def query_one(self, sql):
        rs = self.query(sql, 1)
        if rs is None: return None
        if len(rs) < 1: return None
        return rs[0]
    
    def query_value(self, sql):
        r = self.query_one(sql)
        if r is None: return None
        return r[0]
    
    def query_values(self, sql):
        rs = self.query(sql)
        if rs is None: return None
        values = []
        for r in rs: values.append(r[0])
        return values

    def get_db_info(self, key):
        if key == "version": sql = "SELECT VERSION();"
        elif key == "os": sql = "SELECT @@version_compile_os;"
        elif key == "basedir": sql = "SELECT @@basedir;"
        elif key == "datadir": sql = "SELECT @@datadir;"
        elif key == "database": sql = "SELECT DATABASE();"
        elif key == "user": sql = "SELECT USER();"
        elif key == "connections": sql = "SHOW STATUS WHERE variable_name='Threads_connected';"
        else: return None
        return self.query_value(sql)
    
    def list_databases(self):
        return self.query_values("SHOW DATABASES;")
    
    def list_tables(self, database_name=None):
        table_names = []
        if database_name is None:
            db_names = self.list_databases()
            if db_names is None: return None
            for db_name in db_names:
                if db_name in ["sys", "mysql", "information_schema", "performance_schema"]: continue
                t = self.list_tables(db_name)
                if t is None: return None
                table_names += t
        else:
            rs = self.query("SHOW TABLES IN {}".format(database_name))
            if rs is None: return None
            for r in rs:
                table_names.append(database_name + "." + r[0])
        return table_names
    
    def list_processes(self, user=None):
        sql = "SELECT user, host, db, command, time, state "
        sql += "FROM information_schema.processlist"
        rs = self.query(sql)
        if rs is None: return None
        results = []
        for r in rs:
            if user:
                if r[0] != user: continue
            results.append({
                "user": r[0],
                "host": r[1],
                "db": r[2],
                "command": r[3],
                "time": r[4],
                "state": r[5]
            })
        return results

def template_sql_insert(table_name, data_record, excludings=[]):
    return "INSERT INTO {} ({}) VALUES ({})".format(
        table_name,
        sqlbuilder.parts_str(sqlbuilder.fn, data_record, excludings),
        sqlbuilder.parts_str(sqlbuilder.fp, data_record, excludings)
    )

def template_sql_replace(table_name, data_record, excludings=[]):
    return "REPLACE INTO {} ({}) VALUES ({})".format(
        table_name,
        sqlbuilder.parts_str(sqlbuilder.fn, data_record, excludings),
        sqlbuilder.parts_str(sqlbuilder.fp, data_record, excludings)
    )

def template_sql_insert_or_update(table_name, data_record,
                                  excludings_update,
                                  excludings_insert=[]):
    return "INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {}".format(
        table_name,
        sqlbuilder.parts_str(sqlbuilder.fn, data_record, excludings_insert),
        sqlbuilder.parts_str(sqlbuilder.fp, data_record, excludings_insert),
        sqlbuilder.parts_str(sqlbuilder.fn_fn, data_record, excludings_update,
                             format_left="{}", format_right="VALUES({})")
    )

def template_sql_insert_or_update_v8(table_name, data_record,
                                     excludings_update,
                                     excludings_insert=[]):
    # https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html
    return "INSERT INTO {} ({}) VALUES ({}) as t ON DUPLICATE KEY UPDATE {}".format(
        table_name,
        sqlbuilder.parts_str(sqlbuilder.fn, data_record, excludings_insert),
        sqlbuilder.parts_str(sqlbuilder.fp, data_record, excludings_insert),
        sqlbuilder.parts_str(sqlbuilder.fn_fn, data_record, excludings_update,
                             format_left="{}", format_right="t.{}")
    )

def render_sql_with_values(template, data_record):
    r = {}
    for key, value in data_record.items():
        if value is None:
            r[key] = "NULL"
        elif type(value) == str:
            r[key] = '"' + pymysql.converters.escape_string(value) + '"'
        elif type(value) == datetime.datetime:
            r[key] = '"' + value.strftime("%Y-%m-%d %H:%M:%S") + '"'
        else:
            r[key] = value
    return template.format(**r)

