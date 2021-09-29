import os
from python_socks.sync import Proxy

def inc(x):
    return x + 1


def test_answer():
    os.mkdir("potatopath")
    proxy = Proxy.from_url('socks5://user:password@127.0.0.1:1080')
    assert inc(3) == 4
