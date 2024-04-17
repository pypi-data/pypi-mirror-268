"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import time
import requests
import chardet
import json
from joo import ManagedObject
from joo.logging import LoggerHelper

class HttpAPISession(ManagedObject, LoggerHelper):
    def __init__(self):
        ManagedObject.__init__(self)
        LoggerHelper.__init__(self)

        # control
        self._handle = None

        # settings
        self.parse_response_data = True
        self.log_request = False
        self.log_response = False

    def __del__(self):
        self.close()
        ManagedObject.__del__(self)

    @property
    def handle(self):
        return self.open()

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

    def headers(self):
        return {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

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

    def request(self, method, url, **kwargs):
        # check method
        if method not in ["GET", "POST"]: return None

        # get headers
        headers = kwargs.pop("headers") if "headers" in kwargs else self.headers()

        # get retries/retry_wait
        retries = kwargs.pop("retries", 0)
        retry_wait = kwargs.pop("retry_wait", 0)

        # request
        retry_index = 0
        while True:
            # make a request
            last_status_code = -1
            try:
                # log request
                if self.log_request:
                    if retry_index == 0:
                        self.debug("HTTP {}: {}".format(method, url))
                    else:
                        self.debug("HTTP {} (retry {}/{}): {}".format(method, retry_index, retries, url))

                    request_data = kwargs.get("data", None)
                    if request_data:
                        self.debug(json.dumps(request_data, indent=2), 1)

                    request_json = kwargs.get("json", None)
                    if request_json:
                        request_data = json.loads(request_json)
                        self.debug(json.dumps(request_data, indent=2), 1)

                # request
                if method == "GET":
                    response = self.handle.get(url, headers=headers, **kwargs)
                else:
                    response = self.handle.post(url, 
                                                data=kwargs.get("data", None),
                                                json=kwargs.post("json", None),
                                                headers=headers, 
                                                **kwargs)
                last_status_code = response.status_code
                   
                # log response
                if self.log_response:
                    self.debug("method={}\nurl={}\nstatus={}".format(method, url, response.status_code), 1)

                # check response
                if response.status_code == 200:
                    # parse response
                    content = self.bytes_str(response.content, response.encoding)
                    if self.parse_response_data:
                        response_data = json.loads(content)  # in data
                        if self.log_response:
                            self.debug(json.dumps(response_data, indent=2), 1)
                    else:
                        response_data = content  # in json
                        if self.log_response:
                            self.debug(response_data, 1)
                    
                    # return response                    
                    return (True, response_data)

            except Exception as ex:
                self.exception(ex)
            
            # check retry
            time.sleep(retry_wait)
            retry_index += 1
            if retry_index > retries: return (False, last_status_code)  # return error