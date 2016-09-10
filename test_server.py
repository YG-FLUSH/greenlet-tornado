#!/usr/bin/env python
# coding=utf-8

import logging
from tornado.log import app_log
import tornado
import tornado.httpserver
import tornado.web
from greenlet_tornado.greenlet_tornado import greenlet_sleep, greenlet_asynchronous

class SleepHandler(tornado.web.RequestHandler):

    @greenlet_asynchronous
    def get(self):
        greenlet_sleep(5)
        self.write("Sleep: hello world")

class NormalHandler(tornado.web.RequestHandler):

    @greenlet_asynchronous
    def get(self):
        self.write("Normal: hello world")

handlers = [
        (r'/sleep', SleepHandler),
        (r'/normal', NormalHandler),
        ]

app = tornado.web.Application(handlers, autoreload=True)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(9010, "0.0.0.0")
logging.warning('start server')
tornado.ioloop.IOLoop.instance().start()
