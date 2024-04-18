#!/usr/bin/env python
import socket
import httpx
import codefast as cf
from codefast.utils import timeout
import os
import sys
import subprocess
import argparse
from .utils import get_system_info


class FastPing(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description='Ping a host.')
        self.add_argument('host', type=str, help='hostname or IP address')
        self.add_argument('-c', '--count', type=int, default=9,
                          help='number of packets to send')

    @property
    def os(self):
        return get_system_info()['system']

    @property
    def cmd(self):
        args = self.parse_args()
        os_name = self.os.lower()
        if 'darwin' in os_name:
            return "ping -c {} -i 0.1 -W 1 {}".format(args.count, args.host)
        elif 'linux' in os_name:
            return "ping -c {} -4 -i 0.1 -W 1 {}".format(args.count, args.host)

    @staticmethod
    def entrypoint():
        response = os.system(FastPing().cmd)
        return response == 0


class Cufo(object):
    @staticmethod
    def entrypoint():
        return os.system(
            "curl cufo.cc"
        )


class ProxyCheck(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(description='Check if a proxy is working.')
        self.add_argument('host', type=str, help='hostname or IP address')
        self.add_argument('port', type=int, help='port number')
        self.args = self.parse_args()

    def is_reachable(self):
        try:
            socket.gethostbyname(self.args.host)
            return True
        except socket.error:
            return False

    def is_port_open(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        try:
            sock.connect((self.args.host, self.args.port))
            sock.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False
        finally:
            sock.close()

    def is_socks5_working(self):
        proxies = {
            'http://': 'socks5://{}:{}'.format(self.args.host, self.args.port),
            'https://': 'socks5://{}:{}'.format(self.args.host, self.args.port)
        }

        @timeout(5)
        def _worker():
            with httpx.Client(proxies=proxies) as client:
                response = client.get('http://www.google.com')
                return response.status_code == 200

        try:
            return _worker()
        except Exception:
            return False

    def is_http_working(self):
        proxies = {'http://': 'http://{}:{}'.format(self.args.host, self.args.port),
                   'https://': 'http://{}:{}'.format(self.args.host, self.args.port)}
        with httpx.Client(proxies=proxies) as client:
            try:
                response = client.get('http://www.google.com')
                return response.status_code == 200
            except:
                return False

    @staticmethod
    def entrypoint():
        pc = ProxyCheck()
        msgs = [
            ("Is [HOST] reachable", pc.is_reachable),
            ("Is [PORT] open", pc.is_port_open),
            ("Is [SOCKS5] proxy working", pc.is_socks5_working),
            ("Is [HTTP] proxy working", pc.is_http_working)
        ]
        for msg, f in msgs:
            b = f()
            btext = cf.fp.green(b) if b else cf.fp.red(b)
            print(f"{msg:<{30}}: {btext}")
