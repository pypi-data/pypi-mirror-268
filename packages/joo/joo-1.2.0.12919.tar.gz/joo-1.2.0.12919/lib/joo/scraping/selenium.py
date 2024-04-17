"""
    This file is part of joo library.
    :copyright: Copyright 1993-2024 Wooloo Studio.  All rights reserved.
    :license: MIT, check LICENSE for details.
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import joo.sysutil as sysutil
from joo.scraping import Session as SessionBase

class Session(SessionBase):
    def __init__(self):
        SessionBase.__init__(self)

        # settings
        self.webdriver = "chrome"
        self.desired_capabilities = None
        self.options = None
        self.default_timeout = 10.0
        self.default_wait = 0.5
        self.default_by = By.XPATH

    def open(self, **kwargs):
        try:
            if self._handle: return self._handle
            self.debug("Opening web driver ({}) session...".format(self.webdriver))
            caps = kwargs.pop("desired_capabilities", None)
            if caps is None: caps = self.desired_capabilities
            options = kwargs.pop("options", None)
            if options is None: options = self.options
            if self.webdriver == "chrome":
                self._handle = webdriver.Chrome(desired_capabilities=caps, options=options, **kwargs)
            elif self.webdriver == "firefox":
                self._handle = webdriver.Firefox(desired_capabilities=caps, options=options, **kwargs)
            elif self.webdriver == "edge":
                self._handle = webdriver.Edge(desired_capabilities=caps, options=options, **kwargs)
            else:
                raise Exception("Invalid webdriver.")
            self._state = "opened"
            return self._handle
        except Exception as ex:
            self.exception(ex)
            self._handle = None
            self._state = None
            return None

    def close(self):
        try:
            if self._handle is None: return
            self.debug("Closing web driver ({}) session...".format(self.webdriver))
            self._handle.close()
            self._handle = None
            self._state = None
        except Exception as ex:
            self.exception(ex)
            self._handle = None
            self._state = None

    def get(self, url):
        try:
            self.debug("Web Driver ({}) GET: {}".format(self.webdriver, url))
            self.handle.get(url)
            return True
        except Exception as ex:
            self.exception(ex)
            return False

    def get_html(self):
        return self.execute("return document.documentElement.outerHTML")

    def get_soup(self):
        try:
            html = self.get_html()
            if html is None: return None
            return BeautifulSoup(html, "html.parser")
        except Exception as ex:
            self.exception(ex)
            return None

    def _get_page(self, url, cache, format, **kwargs):
        if format == "html":
            # read from cache
            if cache:
                key = sysutil.Cache.make_key(url)
                content = cache.get(key, text_format=True)
                if content: return content

            # read from online
            wait = kwargs.pop("wait", 0)
            self.get(url)
            self.wait(wait)
            html = self.get_html()
            if html:
                if cache:
                    key = sysutil.Cache.make_key(url)
                    cache.set(key, html, text_format=True)
                return html

        #
        return None

    def get_url(self, leading_wait=2.0, timeout=None, wait=None):
        if timeout is None: timeout = self.default_timeout
        if wait is None: wait = self.default_wait
        if leading_wait > 0.0: time.sleep(leading_wait)
        ts_0 = time.perf_counter()
        url = None
        while True:
            try:
                url = self.handle.current_url
                if url:
                    self.debug("Current URL is: {}".format(url))
                    return url
            except:
                pass

            if time.perf_counter() - ts_0 > timeout:
                self.debug("WARNING: URL is not obtained!")
                return None

            time.sleep(wait)

    def find_element(self, value, base=None, timeout=None, wait=None, by=None):
        if timeout is None: timeout = self.default_timeout
        if wait is None: wait = self.default_wait
        if by is None: by = self.default_by
        ts_0 = time.perf_counter()
        if base is None: base = self.handle
        while True:
            try:
                element = base.find_element(by, value)
                if element: return element
            except:
                pass

            if time.perf_counter() - ts_0 > timeout:
                self.debug("WARNING: Element '{}' is not found!".format(value))
                return None

            time.sleep(wait)

    def find_elements(self, value, base=None, timeout=None, wait=None, by=None):
        if timeout is None: timeout = self.default_timeout
        if wait is None: wait = self.default_wait
        if by is None: by = self.default_by
        ts_0 = time.perf_counter()
        if base is None: base = self.handle
        while True:
            try:
                elements = base.find_elements(by, value)
                if elements:
                    self.debug("WARNING: {} elements had been found as '{}'.".format(len(elements), value))
                    return elements
            except:
                pass

            if time.perf_counter() - ts_0 > timeout:
                self.debug("WARNING: Element(s) '{}' is not found.".format(value))
                return None

            time.sleep(wait)

    def execute(self, script, *args):
        try:
            return self.handle.execute_script(script, *args)
        except Exception as ex:
            self.exception(ex)
            return None

    def get_sizes(self):
        try:
            script = """
                return {
                    "screen.width": window.screen.width,
                    "screen.height": window.screen.height,
                    "screen.client.width": window.screen.availWidth,
                    "screen.client.height": window.screen.availHeight,
                    "window.width": window.outerWidth,
                    "window.height": window.outerHeight,
                    "window.client.width": window.innerWidth,
                    "window.client.height": window.innerHeight,
                    "page.width": document.documentElement.scrollWidth,
                    "page.height": document.documentElement.scrollHeight,
                    "page.client.width": document.documentElement.clientWidth,
                    "page.client.height": document.documentElement.clientHeight
                }
            """
            sizes = self.execute(script)
            if sizes is None: return None
            sizes["window.border.width"] = sizes["window.width"] - sizes["window.client.width"]
            sizes["window.border.height"] = sizes["window.height"] - sizes["window.client.height"]
            sizes["window.scrollbar.width"] = sizes["window.client.width"] - sizes["page.client.width"]
            sizes["window.scrollbar.height"] = sizes["window.client.height"] - sizes["page.client.height"]
            return sizes
        except:
            return None

    def get_element_path(self, element):
        script = """
            function joo_get_path(node){
                if (node == null) return "";
                if (node.parentNode == null) return "/.";
                return joo_get_path(node.parentNode) + "/" + node.tagName;
            }
            return joo_get_path(arguments[0]);
        """
        return self.execute(script, element)
    
    def resize_for_screenshot(self):
        """Resize browser for screenshot of current page.
        
        To get better result on Chrome, make sure below options are included when opening session:
        1. "--headless", this will remove limitation (screen size) of window size, so that
        a full page could be captured.
        2. "--hide-scrollbars", this will hide scroll bars.
        """
        sizes = self.get_sizes()
        if sizes is None: return
        window_width = sizes["page.width"] + sizes["window.border.width"]
        window_height = sizes["page.height"] + sizes["window.border.height"]
        self.handle.set_window_size(window_width, window_height)

    def save_screenshot(self, filepath, resize=True):
        if resize: self.resize_for_screenshot()
        return self.handle.save_screenshot(filepath)

    def get_screenshot_as_png(self, resize=True):
        if resize: self.resize_for_screenshot()
        return self.handle.get_screenshot_as_png()

    def get_screenshot_as_base64(self, resize=True):
        if resize: self.resize_for_screenshot()
        return self.handle.get_screenshot_as_base64()

    def save_html(self, filepath):
        html = self.get_html()
        if html is None: return False
        return sysutil.save_file_contents(filepath, html)

    def capture_snapshot(self, filename, folderpath=None, with_html=True, with_screenshot=True):
        if folderpath is None: folderpath = os.getcwd()
        filepath = os.path.join(os.path.abspath(folderpath), filename)
        if with_html: self.save_html(sysutil.alter_ext(filepath, ".html"))
        if with_screenshot: self.save_screenshot(sysutil.alter_ext(filepath, ".png"))