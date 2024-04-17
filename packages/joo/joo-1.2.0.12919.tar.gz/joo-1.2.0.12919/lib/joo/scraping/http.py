"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import requests
import joo.sysutil as sysutil
from joo.scraping import Session as SessionBase

class Session(SessionBase):
    def __init__(self):
        SessionBase.__init__(self)

        # settings
        self.user_agent = None
        self.ok_status_codes = [200]

    def open(self, **kwargs):
        try:
            if self._handle: return self._handle
            self.debug("Opening HTTP session...")
            self._handle = requests.Session()
            self._state = "opened"
            return self._handle
        except Exception as ex:
            self.exception(ex)
            self._handle = None
            self._state = None
            return None

    def close(self):
        if self._handle:
            self.debug("Closing HTTP session...")
            self._handle = None
            self._state = None

    def response_is_ok(self, response):
        if response:
            return response.status_code in self.ok_status_codes
        else:
            return False

    def request(self, method, url, **kwargs):
        # check method
        if method not in ["GET", "POST"]: return None

        # check mode
        if "retries" in kwargs:
            # request with retries
            retries = kwargs.pop("retries", 0)
            if retries < 0: return None

            retry_wait = kwargs.pop("retry_wait", 0)

            response = self.request(method, url, **kwargs)
            retry_count = 0
            while True:
                if response:
                    if response.status_code in self.ok_status_codes: break
                if retry_count >= retries: return None
                retry_count += 1
                if retry_wait > 0: self.wait(retry_wait)
                kwargs["call_tag"] = "retry {}/{}".format(retry_count, retries)
                response = self.request(method, url, **kwargs)
            return response
        else:
            # request without retry
            try:
                if url is None: return None
                if url == "": return None

                s = self.handle
                if self.user_agent: s.headers["User-Agent"] = self.user_agent

                call_tag = kwargs.pop("call_tag", None)
                if call_tag:
                    self.debug("HTTP {} ({}): {}".format(method, call_tag, url))
                else:
                    self.debug("HTTP {}: {}".format(method, url))

                if method == "GET":
                    response = s.get(url, **kwargs)
                elif method == "POST":
                    response = s.post(url,
                                      data=kwargs.pop("data", None),
                                      json=kwargs.pop("json", None),
                                      **kwargs)
                else:
                    response = None
                self.debug("method={}\nurl={}\nstatus={}".format(method, url, response.status_code), 1)

                return response
            except Exception as ex:
                self.exception(ex)
                return None

    def get(self, url, retries=0, **kwargs):
        kwargs["retries"] = retries
        return self.request("GET", url, **kwargs)

    def post(self, url, data=None, json=None, retries=0, **kwargs):
        kwargs["data"] = data
        kwargs["json"] = json
        kwargs["retries"] = retries
        return self.request("POST", url, **kwargs)

    def _get_page(self, url, cache, format, **kwargs):
        if format == "html":
            # read from cache
            if cache:
                key = sysutil.Cache.make_key(url)
                content = cache.get(key)
                if content: return self.bytes_str(content)

            # read from online
            retries = kwargs.pop("retries", 0)
            response = self.get(url, retries, **kwargs)
            if response:
                if response.status_code == 200:
                    if cache:
                        key = sysutil.Cache.make_key(url)
                        cache.set(key, response.content)
                    return self.bytes_str(response.content, response.encoding)

        #
        return None

    @classmethod
    def download(cls, url, filepath, retries=0, create_parent=True, **kwargs):
        success = False
        session = Session()
        try:
            response = session.get(url, retries, **kwargs)
            if response:
                if response.status_code == 200:
                    success = sysutil.save_file_bytes(filepath, response.content, create_parent)
        except:
            pass
        finally:
            session.close()
        return success