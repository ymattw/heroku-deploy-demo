#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response


class DemoServer(object):

    def __init__(self, host='127.0.0.1', port=8080):
        self._host = host
        self._port = port
        self._app = Flask(__name__)
        self._add_routes()

    def index(self):
        return 'Hello world!\n'

    def run(self):
        self._app.run(host=self._host, port=self._port)

    def _add_routes(self):
        self._app.add_url_rule('/', endpoint='index', view_func=self.index)

    def _test_client(self):
        return self._app.test_client()


if __name__ == '__main__':  # pragma: no cover
    from optparse import OptionParser

    parser = OptionParser(usage='%prog [options]')
    parser.add_option('-b', '--bind', default='127.0.0.1',
                      help=('Bind address, default 127.0.0.1, use '
                            '"0.0.0.0" for all'))
    parser.add_option('-p', '--port', type='int', default=8080,
                      help='Listen port, default is 8080')
    opts, _ = parser.parse_args()

    server = DemoServer(host=opts.bind, port=opts.port)
    server.run()
