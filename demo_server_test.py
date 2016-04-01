#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from demo_server import DemoServer


class DemoServerTest(unittest.TestCase):

    def setUp(self):
        self._app = DemoServer()._test_client()

    def test_minimal(self):
        rv = self._app.get('/')
        self.assertTrue(rv.status.startswith('200 '))
        self.assertEqual(rv.data, b'Hello world!\n')


if __name__ == '__main__':
    unittest.main()
