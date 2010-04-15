#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os
from path import path
import firefox_cookies

if __name__ == '__main__':

    cookiejar=firefox_cookies.get_cookie_jar()


    cookiejar.save("cookies.txt")
