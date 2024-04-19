#
# Pavlin Georgiev, Softel Labs
#
# This is a proprietary file and may not be copied,
# distributed, or modified without express permission
# from the owner. For licensing inquiries, please
# contact pavlin@softel.bg.
#
# 2024
#

import socket

from sciveo.common.tools.logger import *
from sciveo.common.tools.timers import Timer


class NetworkTools:
  def __init__(self, **kwargs):
    self.default_arguments = {
      "timeout": 0.1,
      "localhost": False,
    }

    self.arguments = {}
    for k, v in self.default_arguments.items():
      self.arguments[k] = kwargs.get(k, v)

    self.net_classes = ["192.168.", "10."]
    for i in range(16, 32):
      self.net_classes.append(f"172.{i}.")

  def get_local_nets(self):
    list_local_ips = []
    try:
      import netifaces
      interfaces = netifaces.interfaces()
      for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
          ip = addrs[netifaces.AF_INET][0]['addr']
          for net_class in self.net_classes:
            if ip.startswith(net_class):
              list_local_ips.append(ip)
    except Exception as e:
      warning(type(self).__name__, "netifaces not installed")
    return list_local_ips

  def generate_ip_list(self, base_ip):
    octets = base_ip.split('.')
    network_prefix = '.'.join(octets[:3])
    return [f'{network_prefix}.{i}' for i in range(1, 255)]

  def scan_port(self, port=22):
    t = Timer()
    result = []
    list_local_ips = self.get_local_nets()
    debug(type(self).__name__, "scan_port", "list_local_ips", list_local_ips)
    for local_ip in list_local_ips:
      list_ip = self.generate_ip_list(local_ip)
      result += self.scan_port_hosts(list_ip, port)
    if self.arguments["localhost"]:
      result += self.scan_port_hosts(["127.0.0.1"], port)
    debug(type(self).__name__, "scan_port elapsed time", t.stop(), "result", result)
    return result

  def scan_port_hosts(self, list_ip, port=22):
    list_hosts = []
    timeout = self.arguments["timeout"]
    for ip in list_ip:
      try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
          sock.settimeout(timeout)
          result = sock.connect_ex((ip, port))
          if result == 0:
            list_hosts.append(ip)
          # debug(type(self).__name__, "scan_ports", ip, port, result)
      except socket.error:
        pass
    return list_hosts


if __name__ == "__main__":
  net = NetworkTools(timeout=0.01, localhost=True)
  list_hosts = net.scan_port(port=22)
  print(list_hosts)
