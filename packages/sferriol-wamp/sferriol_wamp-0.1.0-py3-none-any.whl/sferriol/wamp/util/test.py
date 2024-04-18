# -*- coding: utf-8 -*-
#
#  Copyright 2023 sferriol <sferriol@ip2i.in2p3.fr>
"""Unittest utilities
"""
import asyncio
import functools
import unittest

from autobahn.wamp.component import _run
from autobahn.asyncio.component import Component, run
import sferriol.python as sfpy
import sferriol.python.net as sfpy_net

from . import crossbar


class Wamp_TestCase(unittest.IsolatedAsyncioTestCase):
    """TestCase class for WAMP unittests

    Crossbar application is executed in setUpClass with an unused Websocket port.
    """
    async def asyncSetUp(self):
        # create internal component
        comp = self.new_component()
        await self.start_component('internal', comp)

    async def asyncTearDown(self):
        await self.stop_component('internal')

    @classmethod
    def new_component(cls):
        """Create a new WAMP component"""
        comp = Component(transports=cls.ws_url)
        return comp

    async def start_component(self, name: str, comp: Component):
        """Start a WAMP component and it is registered with the specified name
        
        It waits until component has joined the Crossbar WAMP broker
        
        Args:
          name: Name of the component
          comp: The WAMP component
        """
        if not hasattr(self, 'components'):
            self.components = dict()
        elif name in self.components:
            raise KeyError(f'component {name} is already registered')

        joined = asyncio.Event()

        @comp.on_join
        def _(session, details):
            comp.session = session
            joined.set()

        loop = asyncio.get_event_loop()
        def done_callback(reactor, arg):
            pass
        d = _run(loop, [comp], done_callback)

        await joined.wait()
        self.components[name] = (comp, d)

    async def stop_component(self, name):
        """Stop a WAMP component
        
        Args:
          name: Name of the component
        """
        if hasattr(self, 'components') and name in self.components:
            (comp, d) = self.components[name]
            await comp.stop()
            await d
            del self.components[name]

    async def call(self, uri, *args, **kwargs):
        (comp, _) = self.components['internal']
        ret = await comp.session.call(uri, *args, **kwargs)
        return ret

    @classmethod
    def setUpClass(cls):
        if not crossbar.available():
            unittest.TestCase.skipTest(cls, 'crossbar applisation is not available')
        cls.ws_port = sfpy_net.unused_port()
        cls.ws_url = f'ws://localhost:{cls.ws_port}/ws'
        cls.realm = 'realm1'
        cls.cbdir = crossbar.create_temp_dir(cls.ws_port)
        cls.proc = crossbar.start(cls.cbdir.name)
        # wait crossbar application ready
        sfpy.loop_until(fct=functools.partial(sfpy_net.is_port_in_use,
                                              cls.ws_port),
                        ret=True,
                        every=0.01,
                        timeout=5)

    @classmethod
    def tearDownClass(cls):
        cls.proc.terminate()
        cls.proc.wait()
        cls.cbdir.cleanup()
