# -*- coding: utf-8 -*-
#
#  Copyright 2023 sferriol <sferriol@ip2i.in2p3.fr>
"""Utils to init/start/stop crossbar process 
"""
import json
import shutil
import subprocess
import tempfile
from typing import Any, Callable
import os

from sferriol.python import net as sfpy_net
from sferriol.python.dictionary import adict, as_adict


def available():
    return shutil.which('crossbar') is not None
    

def init(cbpath):
    """Run 'crossbar init' command 

    Args:
      cbpath: Path of the Crossbar application base directory
    """
    proc = subprocess.Popen(
        f'crossbar init --appdir {cbpath}'.split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    proc.wait()


def start(cbpath: str) -> subprocess.Popen:
    """Run 'crossbar start' process

    Args:
      cbpath: Path of the Crossbar application directory 

    Returns:
       Crossbar process
    """
    args = f'crossbar start --cbdir {cbpath}'.split()
    p = subprocess.Popen(
        args,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return p


def create_temp_dir(ws_port: int = None,
                    rs_port: int = None) -> tempfile.TemporaryDirectory:
    """Create a temporary base directory for crossbar (see crossbar doc)  

    It includes configuration file .crossbar/config.json containing the value
    of passed parameters

    Args:
      ws_port: Websocket port. If None, an unused port is taken 
      rs_port: Rawsocket port. If None, an unused port is taken 

    Returns:
      A temporary crossbar base directory 
    """
    dir = tempfile.TemporaryDirectory()
    init(dir.name)
    cfgpath = os.path.join(dir.name, '.crossbar/config.json')
    with open(cfgpath) as f:
        cfg = as_adict(json.load(f))
    # put unused rawsocket port
    if rs_port is None:
        rs_port = sfpy_net.unused_port()
    cfg.workers[0].transports[0].endpoint.port = rs_port
    # put unused websocket port
    if ws_port is None:
        ws_port = sfpy_net.unused_port()
    cfg.workers[0].transports[1].endpoint.port = ws_port
    with open(os.path.join(dir.name, 'config.json'), 'a') as f:
        json.dump(cfg, f)
    return dir
