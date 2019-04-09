#!/usr/bin/env python3

from netmiko import ConnectHandler

switches = [{"un":"admin","pw":"alta3","ip":"172.16.2.10","driver":"eos"},{"un":"admin","pw":"alta3","ip":"172.16.2.20","driver":"eos"}]

for switch in switches:
    open_connection = ConnectHandler(device_type=switch.get("driver"),ip=switch.get("ip"),username=switch.get("un"),password=switch.get("pw")
    my_command = open_connection.send_command("show ip int brief")
    print(mycommand)
