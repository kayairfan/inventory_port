# 03.04.2024 
# Discovery + envanter projesi
# 


import pandas as pd
from pprint import pprint
from netmiko import ConnectHandler
from netmiko import ReadTimeout
import asyncio
import telnetlib3
import time
from JobsSqlLogging import *
from pprint import pprint
import re
from concurrent.futures import ThreadPoolExecutor
import threading

list_hostname = []
list_devtype = []
list_sfp_port = []
list_ipaddress = []
list_sfp_serial = []
list_sfp_product = []
list_card_slot = []
list_sfp_speed = []

list_hostname_temp = []
list_devtype_temp = []
list_sfp_port_temp = []
list_ipaddress_temp = []
list_sfp_serial_temp = []
list_sfp_product_temp = []
list_card_slot_temp = []
list_sfp_speed_temp = []


def cisco_xe_3725(device_name, device_type, device_ip): #3725 ŞİFRE HATASI
    print("CISCO_XE / 3725")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []
    
    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            output = connection_main.send_command_timing("show inventory oid ", read_timeout=100, cmd_verify=True)

            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]
            
            port = "#"
            serial_number = "#"
            product_number = "#"           
            
            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                        except:
                            port = "undefined"
                            pass

                        try:
                            serial_number = serial_number_line.split("SN: ")[1].strip()
                        except:
                            serial_number = "undefined"
                            pass

                        try:
                            if "^" in serial_number_line.split()[1].strip():
                                product_number = "undefined"
                            else:
                                product_number = serial_number_line.split()[1].strip()
                        except:
                            product_number = "undefined"
                            pass

                        list_card_slot.append("device")
                        list_ipaddress.append(device_ip)
                        list_sfp_port.append(port)
                        list_sfp_serial.append(serial_number)
                        list_sfp_product.append(product_number)
                        list_hostname.append(device_name)
                        list_devtype.append(device_type)
                        list_sfp_speed.append("#")

                        list_card_slot_temp.append("device")
                        list_ipaddress_temp.append(device_ip)
                        list_sfp_port_temp.append(port)
                        list_sfp_serial_temp.append(serial_number)
                        list_sfp_product_temp.append(product_number)
                        list_hostname_temp.append(device_name)
                        list_devtype_temp.append(device_type)
                        list_sfp_speed_temp.append("#")

                        # print("***************************************************")
                        # print(list_ipaddress_temp)
                        # print("---------------------------------------------------")
                        # print(list_hostname_temp)
                        # print("---------------------------------------------------")
                        # print(list_devtype_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_port_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_serial_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_product_temp)
                        # print("---------------------------------------------------")
                        # print(list_card_slot_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_speed_temp)
                        # print("---------------------------------------------------")
                        # print("list_ipaddress: " + str(len(list_ipaddress)))
                        # print("list_hostname: " + str(len(list_hostname)))
                        # print("list_devtype: " + str(len(list_devtype)))
                        # print("list_sfp_port: " + str(len(list_sfp_port)))
                        # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                        # print("list_sfp_product: " + str(len(list_sfp_product)))
                        # print("list_card_slot: " + str(len(list_card_slot)))
                        # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                        # print("***************************************************")
                        # print("\n\n\n")

                       

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xr_n540(device_name, device_type, device_ip): #3725 ŞİFRE HATASI
    print("CISCO_XR / 540")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_xr',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal monitor disable ", read_timeout=100, cmd_verify=True)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)

            for SplitItem in output_desc.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"
                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                    port = SplitItem.split()[0]

                    if "." not in port and "/" in port:
                        port_temp = port.replace("Gi","")
                        port_temp = port_temp.replace("Te","")
                        port_temp = port_temp.replace("TF","")
                        port_temp = port_temp.replace("Hu","")

                        output = connection_main.send_command_timing("show inventory | begin " +"'"+ str(port_temp) +'"'+"'", read_timeout=100, cmd_verify=True)
                        # print("show inventory | begin " +"'"+ str(port_temp) +'"'+"'")  


                        # Split the text by empty lines
                        lines = [segment.strip() for segment in output.strip().split('\n\n')][0]

                        if (str(port_temp) +'"') in output:
                            lines = output.strip().split('\n')
                            for i, line in enumerate(lines):
                                if (str(port_temp) +'"') in line:
                                    
                                    serial_number_line = lines[i + 1]

                                    try:
                                        serial_number = serial_number_line.split("SN: ")[1].strip()
                                    except:
                                        serial_number = "undefined"
                                        pass

                                    try:
                                        if "^" in serial_number_line.split()[1].strip():
                                            product_number = "undefined"
                                        else:
                                            product_number = serial_number_line.split()[1].strip()
                                    except:
                                        product_number = "undefined"
                                        pass

                                    list_card_slot.append("device")
                                    list_ipaddress.append(device_ip)
                                    list_sfp_port.append(port)
                                    list_sfp_serial.append(serial_number)
                                    list_sfp_product.append(product_number)
                                    list_hostname.append(device_name)
                                    list_devtype.append(device_type)
                                    list_sfp_speed.append("#")

                                    list_card_slot_temp.append("device")
                                    list_ipaddress_temp.append(device_ip)
                                    list_sfp_port_temp.append(port)
                                    list_sfp_serial_temp.append(serial_number)
                                    list_sfp_product_temp.append(product_number)
                                    list_hostname_temp.append(device_name)
                                    list_devtype_temp.append(device_type)
                                    list_sfp_speed_temp.append("#")

                                    
                        else:
                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)

                        # print("***************************************************")
                        # print(list_ipaddress_temp)
                        # print("---------------------------------------------------")
                        # print(list_hostname_temp)
                        # print("---------------------------------------------------")
                        # print(list_devtype_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_port_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_serial_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_product_temp)
                        # print("---------------------------------------------------")
                        # print(list_card_slot_temp)
                        # print("---------------------------------------------------")
                        # print(list_sfp_speed_temp)
                        # print("---------------------------------------------------")
                        # print("list_ipaddress: " + str(len(list_ipaddress)))
                        # print("list_hostname: " + str(len(list_hostname)))
                        # print("list_devtype: " + str(len(list_devtype)))
                        # print("list_sfp_port: " + str(len(list_sfp_port)))
                        # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                        # print("list_sfp_product: " + str(len(list_sfp_product)))
                        # print("list_card_slot: " + str(len(list_card_slot)))
                        # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                        # print("***************************************************")
                        # print("\n\n\n")                           

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xe_a901_6cz_f_d(device_name, device_type, device_ip): #A901-6CZ-F-D
    print("CISCO_XE / A901-6CZ-F-D")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command("terminal length 0", read_timeout=200,cmd_verify=True)
            output = connection_main.send_command("show inventory oid ", read_timeout=200, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)

            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]

            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                            port = port.replace("TenGigabitEthernet ", "Te")
                            port = port.replace("GigabitEthernet ", "Gi")
                            
                        except:
                            port = "undefined"
                            pass

                        if "/" in port and "." not in port:
                            output_speed = connection_main.send_command_timing("show interfaces "+ str(port), read_timeout=100, cmd_verify=True)
                        
                            for SplitItemX in output_speed.split("\n"):
                                if "Mbps" in SplitItemX and "media type" in SplitItemX:
                                    speed = SplitItemX.split()[2]
                                    speed = speed.replace(",","")

                            try:
                                serial_number = serial_number_line.split("SN: ")[1].strip()
                            except:
                                serial_number = "undefined"
                                pass

                            try:
                                if "^" in serial_number_line.split()[1].strip():
                                    product_number = "undefined"
                                else:
                                    product_number = serial_number_line.split()[1].strip()
                            except:
                                product_number = "undefined"
                                pass
                            

                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)


                            list_card_slot_temp.append("device")
                            list_ipaddress_temp.append(device_ip)
                            list_sfp_port_temp.append(port)
                            list_sfp_serial_temp.append(serial_number)
                            list_sfp_product_temp.append(product_number)
                            list_hostname_temp.append(device_name)
                            list_devtype_temp.append(device_type)
                            list_sfp_speed_temp.append(speed)


                            for SplitItem in output_desc.split("\n"):
                                port = "#"
                                serial_number = "#"
                                product_number = "#" 
                                speed = "#"
                                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                                    port = SplitItem.split()[0]
                                    if port not in list_sfp_port_temp and "/" in port and "." not in port:
                                        list_card_slot.append("device")
                                        list_ipaddress.append(device_ip)
                                        list_sfp_port.append(port)
                                        list_sfp_serial.append(serial_number)
                                        list_sfp_product.append(product_number)
                                        list_hostname.append(device_name)
                                        list_devtype.append(device_type)
                                        list_sfp_speed.append(speed)

                            # print("***************************************************")
                            # print(list_ipaddress_temp)
                            # print("---------------------------------------------------")
                            # print(list_hostname_temp)
                            # print("---------------------------------------------------")
                            # print(list_devtype_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_port_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_serial_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_product_temp)
                            # print("---------------------------------------------------")
                            # print(list_card_slot_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_speed_temp)
                            # print("---------------------------------------------------")
                            # print("list_ipaddress: " + str(len(list_ipaddress)))
                            # print("list_hostname: " + str(len(list_hostname)))
                            # print("list_devtype: " + str(len(list_devtype)))
                            # print("list_sfp_port: " + str(len(list_sfp_port)))
                            # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                            # print("list_sfp_product: " + str(len(list_sfp_product)))
                            # print("list_card_slot: " + str(len(list_card_slot)))
                            # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                            # print("***************************************************")
                            # print("\n\n\n")           



            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xe_a901_12c_f_d(device_name, device_type, device_ip): #A901-12C-F-D
    print("CISCO_XE / A901-6CZ-F-D")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command("terminal length 0", read_timeout=200,cmd_verify=True)
            output = connection_main.send_command("show inventory oid ", read_timeout=200, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)

            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]

            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                            port = port.replace("TenGigabitEthernet ", "Te")
                            port = port.replace("GigabitEthernet ", "Gi")
                            
                        except:
                            port = "undefined"
                            pass

                        if "/" in port and "." not in port:
                            output_speed = connection_main.send_command_timing("show interfaces "+ str(port), read_timeout=100, cmd_verify=True)
                        
                            for SplitItemX in output_speed.split("\n"):
                                if "Mbps" in SplitItemX and "media type" in SplitItemX:
                                    speed = SplitItemX.split()[2]
                                    speed = speed.replace(",","")

                            try:
                                serial_number = serial_number_line.split("SN: ")[1].strip()
                            except:
                                serial_number = "undefined"
                                pass

                            try:
                                if "^" in serial_number_line.split()[1].strip():
                                    product_number = "undefined"
                                else:
                                    product_number = serial_number_line.split()[1].strip()
                            except:
                                product_number = "undefined"
                                pass

                       
                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)


                            list_card_slot_temp.append("device")
                            list_ipaddress_temp.append(device_ip)
                            list_sfp_port_temp.append(port)
                            list_sfp_serial_temp.append(serial_number)
                            list_sfp_product_temp.append(product_number)
                            list_hostname_temp.append(device_name)
                            list_devtype_temp.append(device_type)
                            list_sfp_speed_temp.append(speed)


                            for SplitItem in output_desc.split("\n"):
                                port = "#"
                                serial_number = "#"
                                product_number = "#" 
                                speed = "#"
                                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                                    port = SplitItem.split()[0]
                                    if port not in list_sfp_port_temp and "/" in port and "." not in port:
                                        list_card_slot.append("device")
                                        list_ipaddress.append(device_ip)
                                        list_sfp_port.append(port)
                                        list_sfp_serial.append(serial_number)
                                        list_sfp_product.append(product_number)
                                        list_hostname.append(device_name)
                                        list_devtype.append(device_type)
                                        list_sfp_speed.append(speed)

                            # print("***************************************************")
                            # print(list_ipaddress_temp)
                            # print("---------------------------------------------------")
                            # print(list_hostname_temp)
                            # print("---------------------------------------------------")
                            # print(list_devtype_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_port_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_serial_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_product_temp)
                            # print("---------------------------------------------------")
                            # print(list_card_slot_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_speed_temp)
                            # print("---------------------------------------------------")
                            # print("list_ipaddress: " + str(len(list_ipaddress)))
                            # print("list_hostname: " + str(len(list_hostname)))
                            # print("list_devtype: " + str(len(list_devtype)))
                            # print("list_sfp_port: " + str(len(list_sfp_port)))
                            # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                            # print("list_sfp_product: " + str(len(list_sfp_product)))
                            # print("list_card_slot: " + str(len(list_card_slot)))
                            # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                            # print("***************************************************")
                            # print("\n\n\n")           



            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xe_asr_920_24sz_m(device_name, device_type, device_ip): #ASR-920-24SZ-M
    print("CISCO_XE / ASR-920-24SZ-M")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            output = connection_main.send_command_timing("show inventory oid ", read_timeout=100, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)
            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]
            
            port = "#"
            serial_number = "#"
            product_number = "#"           
            
            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                            last_digit = port.split()[-1]
                            port = port.replace(" transceiver ","/")
                            if int(last_digit) <24:
                                port = port.replace("subslot ","Gi")
                            else:
                                port = port.replace("subslot ","Te")
                        except:
                            port = "undefined"
                            pass

                        if "/" in port and "." not in port:
                            output_speed = connection_main.send_command_timing("show interfaces "+ str(port), read_timeout=100, cmd_verify=True)
                        
                            for SplitItemX in output_speed.split("\n"):
                                if "Mbps" in SplitItemX and "link type" in SplitItemX and "media type" in SplitItemX:
                                    speed = SplitItemX.split()[2]
                                    speed = speed.replace(",","")
                                    speed = speed.replace("a-","")
                                    
                            try:
                                serial_number = serial_number_line.split("SN: ")[1].strip()
                            except:
                                serial_number = "undefined"
                                pass

                            try:
                                if "^" in serial_number_line:
                                    product_number = "undefined"
                                else:
                                    product_number = serial_number_line.split()[1].strip()
                                    product_number =  product_number.replace("\x7f", "")
                            except:
                                product_number = "undefined"
                                pass

                            
                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)


                            list_card_slot_temp.append("device")
                            list_ipaddress_temp.append(device_ip)
                            list_sfp_port_temp.append(port)
                            list_sfp_serial_temp.append(serial_number)
                            list_sfp_product_temp.append(product_number)
                            list_hostname_temp.append(device_name)
                            list_devtype_temp.append(device_type)
                            list_sfp_speed_temp.append(speed)

                            for SplitItem in output_desc.split("\n"):
                                port = "#"
                                serial_number = "#"
                                product_number = "#" 
                                speed = "#"
                                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                                    port = SplitItem.split()[0]
                                    if port not in list_sfp_port_temp and "/" in port and "." not in port:
                                        list_card_slot.append("device")
                                        list_ipaddress.append(device_ip)
                                        list_sfp_port.append(port)
                                        list_sfp_serial.append(serial_number)
                                        list_sfp_product.append(product_number)
                                        list_hostname.append(device_name)
                                        list_devtype.append(device_type)
                                        list_sfp_speed.append(speed)

                            # print("***************************************************")
                            # print(list_ipaddress_temp)
                            # print("---------------------------------------------------")
                            # print(list_hostname_temp)
                            # print("---------------------------------------------------")
                            # print(list_devtype_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_port_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_serial_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_product_temp)
                            # print("---------------------------------------------------")
                            # print(list_card_slot_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_speed_temp)
                            # print("---------------------------------------------------")
                            # print("list_ipaddress: " + str(len(list_ipaddress)))
                            # print("list_hostname: " + str(len(list_hostname)))
                            # print("list_devtype: " + str(len(list_devtype)))
                            # print("list_sfp_port: " + str(len(list_sfp_port)))
                            # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                            # print("list_sfp_product: " + str(len(list_sfp_product)))
                            # print("list_card_slot: " + str(len(list_card_slot)))
                            # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                            # print("***************************************************")
                            # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xe_asr_920_4sz_d(device_name, device_type, device_ip): #ASR-920-4SZ-D
    print("CISCO_XE / ASR-920-4SZ-D")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            output = connection_main.send_command_timing("show inventory oid ", read_timeout=100, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)

            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]
            
            port = "#"
            serial_number = "#"
            product_number = "#"           
            
            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                            last_digit = port.split()[-1]
                            port = port.replace(" transceiver ","/")
                            if int(last_digit) < 2:
                                port = port.replace("subslot ","Gi")
                            else:
                                port = port.replace("subslot ","Te")
                        except:
                            port = "undefined"
                            pass

                        if "/" in port and "." not in port:
                            output_speed = connection_main.send_command_timing("show interfaces "+ str(port), read_timeout=100, cmd_verify=True)
                        
                            for SplitItemX in output_speed.split("\n"):
                                if "Mbps" in SplitItemX and "link type" in SplitItemX and "media type" in SplitItemX:
                                    speed = SplitItemX.split()[2]
                                    speed = speed.replace(",","")

                            try:
                                serial_number = serial_number_line.split("SN: ")[1].strip()
                            except:
                                serial_number = "undefined"
                                pass

                            try:
                                if "^" in serial_number_line.split()[1].strip():
                                    product_number = "undefined"
                                else:
                                    product_number = serial_number_line.split()[1].strip()
                            except:
                                product_number = "undefined"
                                pass

                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)


                            list_card_slot_temp.append("device")
                            list_ipaddress_temp.append(device_ip)
                            list_sfp_port_temp.append(port)
                            list_sfp_serial_temp.append(serial_number)
                            list_sfp_product_temp.append(product_number)
                            list_hostname_temp.append(device_name)
                            list_devtype_temp.append(device_type)
                            list_sfp_speed_temp.append(speed)
                            
                            for SplitItem in output_desc.split("\n"):
                                port = "#"
                                serial_number = "#"
                                product_number = "#" 
                                speed = "#"
                                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                                    port = SplitItem.split()[0]
                                    if port not in list_sfp_port_temp and "/" in port and "." not in port:
                                        list_card_slot.append("device")
                                        list_ipaddress.append(device_ip)
                                        list_sfp_port.append(port)
                                        list_sfp_serial.append(serial_number)
                                        list_sfp_product.append(product_number)
                                        list_hostname.append(device_name)
                                        list_devtype.append(device_type)
                                        list_sfp_speed.append(speed)

                            # print("***************************************************")
                            # print(list_ipaddress_temp)
                            # print("---------------------------------------------------")
                            # print(list_hostname_temp)
                            # print("---------------------------------------------------")
                            # print(list_devtype_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_port_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_serial_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_product_temp)
                            # print("---------------------------------------------------")
                            # print(list_card_slot_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_speed_temp)
                            # print("---------------------------------------------------")
                            # print("list_ipaddress: " + str(len(list_ipaddress)))
                            # print("list_hostname: " + str(len(list_hostname)))
                            # print("list_devtype: " + str(len(list_devtype)))
                            # print("list_sfp_port: " + str(len(list_sfp_port)))
                            # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                            # print("list_sfp_product: " + str(len(list_sfp_product)))
                            # print("list_card_slot: " + str(len(list_card_slot)))
                            # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                            # print("***************************************************")
                            # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def cisco_xe_asr_920_12cz_d(device_name, device_type, device_ip): #ASR-920-12CZ-D
    print("CISCO_XE / ASR-920-12CZ-D")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            output = connection_main.send_command_timing("show inventory oid ", read_timeout=100, cmd_verify=True)
            output_desc = connection_main.send_command("show interfaces description ", read_timeout=200, cmd_verify=True)

            oid_list = ["1.3.6.1.4.1.9.12.3.1.9.51","1.3.6.1.4.1.9.12.3.1.9.76","1.3.6.1.4.1.9.12.3.1.9.93","1.3.6.1.4.1.9.12.3.1.9.117","1.3.6.1.4.1.9.12.3.1.9.118","1.3.6.1.4.1.9.12.3.1.9.122","1.3.6.1.4.1.9.12.3.1.9.68"]
            
            port = "#"
            serial_number = "#"
            product_number = "#"           
            
            lines = output.strip().split('\n')
            for i, line in enumerate(lines):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                for oid in oid_list:
                    if oid in line:
                        serial_number_line = lines[i - 1]
                        port_line = lines[i - 2]

                        try:
                            port = port_line.split('"')[1].strip()
                            last_digit = port.split()[-1]
                            port = port.replace(" transceiver ","/")
                            if int(last_digit) <12:
                                port = port.replace("subslot ","Gi")
                            else:
                                port = port.replace("subslot ","Te")
                        except:
                            port = "undefined"
                            pass

                        if "/" in port and "." not in port:
                            output_speed = connection_main.send_command_timing("show interfaces "+ str(port), read_timeout=100, cmd_verify=True)
                        
                            for SplitItemX in output_speed.split("\n"):
                                if "Mbps" in SplitItemX and "link type" in SplitItemX and "media type" in SplitItemX:
                                    speed = SplitItemX.split()[2]
                                    speed = speed.replace(",","")

                            try:
                                serial_number = serial_number_line.split("SN: ")[1].strip()
                            except:
                                serial_number = "undefined"
                                pass

                            try:
                                if "^" in serial_number_line.split()[1].strip():
                                    product_number = "undefined"
                                else:
                                    product_number = serial_number_line.split()[1].strip()
                            except:
                                product_number = "undefined"
                                pass

                            list_card_slot.append("device")
                            list_ipaddress.append(device_ip)
                            list_sfp_port.append(port)
                            list_sfp_serial.append(serial_number)
                            list_sfp_product.append(product_number)
                            list_hostname.append(device_name)
                            list_devtype.append(device_type)
                            list_sfp_speed.append(speed)


                            list_card_slot_temp.append("device")
                            list_ipaddress_temp.append(device_ip)
                            list_sfp_port_temp.append(port)
                            list_sfp_serial_temp.append(serial_number)
                            list_sfp_product_temp.append(product_number)
                            list_hostname_temp.append(device_name)
                            list_devtype_temp.append(device_type)
                            list_sfp_speed_temp.append(speed)

                            for SplitItem in output_desc.split("\n"):
                                port = "#"
                                serial_number = "#"
                                product_number = "#" 
                                speed = "#"
                                if "/" in SplitItem and re.search(r'\S+\s+\S+\s+\S+', SplitItem):
                                    port = SplitItem.split()[0]
                                    if port not in list_sfp_port_temp and "/" in port and "." not in port:
                                        list_card_slot.append("device")
                                        list_ipaddress.append(device_ip)
                                        list_sfp_port.append(port)
                                        list_sfp_serial.append(serial_number)
                                        list_sfp_product.append(product_number)
                                        list_hostname.append(device_name)
                                        list_devtype.append(device_type)
                                        list_sfp_speed.append(speed)

                            # print("***************************************************")
                            # print(list_ipaddress_temp)
                            # print("---------------------------------------------------")
                            # print(list_hostname_temp)
                            # print("---------------------------------------------------")
                            # print(list_devtype_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_port_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_serial_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_product_temp)
                            # print("---------------------------------------------------")
                            # print(list_card_slot_temp)
                            # print("---------------------------------------------------")
                            # print(list_sfp_speed_temp)
                            # print("---------------------------------------------------")
                            # print("list_ipaddress: " + str(len(list_ipaddress)))
                            # print("list_hostname: " + str(len(list_hostname)))
                            # print("list_devtype: " + str(len(list_devtype)))
                            # print("list_sfp_port: " + str(len(list_sfp_port)))
                            # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                            # print("list_sfp_product: " + str(len(list_sfp_product)))
                            # print("list_card_slot: " + str(len(list_card_slot)))
                            # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                            # print("***************************************************")
                            # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass
   
def arista_dcs_7280cr3k_32p4_f(device_name, device_type, device_ip): #DCS-7280CR3K-32P4-F
    print("ARISTA / DCS-7280CR3K-32P4-F")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            output = connection_main.send_command_timing("show inventory | begin Port Manufacturer ", read_timeout=100, cmd_verify=True)
            
            
            for SplitItem in output.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                if "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem) and "Arista Networks" not in SplitItem and "MTA HARDWARE" not in SplitItem and "Intel Corp" not in SplitItem and "FINISAR CORP" not in SplitItem and "FINISAR CORP." not in SplitItem and "SOURCE PHOTONICS" not in SplitItem and "Methode Elec." not in SplitItem and "DELL EMC" not in SplitItem and "HG GENUINE" not in SplitItem:
                    port = SplitItem.split()[0]


                    output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2]

                    serial_number = SplitItem.split()[3]
                    product_number = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)

                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

                elif "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem):
                    port = SplitItem.split()[0]

                    output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2] 

                    serial_number = SplitItem.split()[4]
                    product_number = SplitItem.split()[3]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def arista_dcs_7280sr2k_48c6_m_f(device_name, device_type, device_ip): #DCS-7280SR2K-48C6-M-F
    print("ARISTA /  DCS-7280SR2K-48C6-M-F")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            output = connection_main.send_command_timing("show inventory | begin Port Manufacturer ", read_timeout=100, cmd_verify=True)
            
            for SplitItem in output.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                if "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem) and "Arista Networks" not in SplitItem and "MTA HARDWARE" not in SplitItem and "Intel Corp" not in SplitItem and "FINISAR CORP" not in SplitItem and "FINISAR CORP." not in SplitItem and "SOURCE PHOTONICS" not in SplitItem and "Methode Elec." not in SplitItem and "DELL EMC" not in SplitItem and "HG GENUINE" not in SplitItem:
                    port = SplitItem.split()[0]

                    if int(port) < 49:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    else:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +"/1 status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2]
                        speed = speed.replace("a-","")

                    serial_number = SplitItem.split()[3]
                    product_number = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

                elif "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem):
                    port = SplitItem.split()[0]

                    if int(port) < 49:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    else:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +"/1 status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2]
                        speed = speed.replace("a-","")

                    serial_number = SplitItem.split()[4]
                    product_number = SplitItem.split()[3]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def arista_dcs_7280sr3k_48yc8_f(device_name, device_type, device_ip): #DCS-7280SR3K-48YC8-F
    print("ARISTA / DCS-7280SR3K-48YC8-F")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0 ", read_timeout=100, cmd_verify=True)
            output = connection_main.send_command_timing("show inventory | begin Port Manufacturer ", read_timeout=100, cmd_verify=True)            

            for SplitItem in output.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"
                if "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem) and "Arista Networks" not in SplitItem and "MTA HARDWARE" not in SplitItem and "Intel Corp" not in SplitItem and "FINISAR CORP" not in SplitItem and "FINISAR CORP." not in SplitItem and "SOURCE PHOTONICS" not in SplitItem and "Methode Elec." not in SplitItem and "DELL EMC" not in SplitItem and "HG GENUINE" not in SplitItem:
                    port = SplitItem.split()[0]

                    if int(port) < 49:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    else:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +"/1 status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        speed = "#"
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2]
                        
                        speed = speed.replace("a-","")
                        
                        
                    serial_number = SplitItem.split()[3]
                    product_number = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")
                    

                elif "Not Present" not in SplitItem and re.search(r'\s+\d+\s+\S+\s+\S+\s+\S+', SplitItem):
                    port = SplitItem.split()[0]

                    if int(port) < 49:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +" status ", read_timeout=100, cmd_verify=True)
                    else:
                        output_speed = connection_main.send_command_timing("show interfaces ethernet "+ str(port) +"/1 status ", read_timeout=100, cmd_verify=True)
                    
                    for SplitItemX in output_speed.split("\n"):
                        if "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX) and ":" in SplitItemX:
                            speed = SplitItemX.split()[-2]
                        elif "Et" in SplitItemX and ("full" in SplitItemX or "half" in SplitItemX):
                            speed = SplitItemX.split()[-2]

                        speed = speed.replace("a-","")
                        
                    serial_number = SplitItem.split()[4]
                    product_number = SplitItem.split()[3]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zte_m6000_3s_plus(device_name, device_type, device_ip): #M6000-3S-PLUS
    print("ZTE / M6000-3S-PLUS")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            output = connection_main.send_command_timing("show opticalinfo brief | exclude offline ", read_timeout=100, cmd_verify=True)
       
            for SplitItem in output.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                if "gei" in SplitItem and re.search(r'\S+\s+\S+\s+\S+\s+\S+\s+\S+\s', SplitItem):
                    port = SplitItem.split()[0]

                    output_speed = connection_main.send_command_timing("show interfaces "+ str(port)+" | include BW ", read_timeout=100, cmd_verify=True)

                    for SplitItemX in output_speed.split("\n"):
                        if "BW" in SplitItemX and "bit" in SplitItemX:
                            speed = SplitItemX.split("BW ")[2]
                    
                    output_sn = connection_main.send_command_timing("show opticalinfo " + port + " | include Vendor SN  : ", read_timeout=100, cmd_verify=True)
                    for SplitItem_sn in output_sn.split("\n"):
                        if "Vendor SN" in SplitItem_sn:
                            serial_number = SplitItem_sn.split()[-1]
                    
                    output_product = connection_main.send_command_timing("show opticalinfo " + port + " | include Ethernet Compliance Codes: ", read_timeout=100, cmd_verify=True)
                    for SplitItem_product in output_product.split("\n"):
                        if "Ethernet Compliance" in SplitItem_product and "show" not in SplitItem_product:
                            product_number = SplitItem_product.split()[-1]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zte_m6000_8s_plus(device_name, device_type, device_ip): #M6000-8S-PLUS
    print("ZTE / M6000-8S-PLUS")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            output = connection_main.send_command_timing("show opticalinfo brief | exclude offline ", read_timeout=100, cmd_verify=True)
            
            for SplitItem in output.split("\n"):
                port = "#"
                serial_number = "#"
                product_number = "#" 
                speed = "#"

                if "gei" in SplitItem and re.search(r'\S+\s+\S+\s+\S+\s+\S+\s+\S+\s', SplitItem):
                    port = SplitItem.split()[0]

                    output_speed = connection_main.send_command_timing("show interfaces "+ str(port)+" | include BW ", read_timeout=100, cmd_verify=True)

                    for SplitItemX in output_speed.split("\n"):
                        if "BW" in SplitItemX and "bit" in SplitItemX:
                            speed = SplitItemX.split("BW ")[2]

                    output_sn = connection_main.send_command_timing("show opticalinfo " + port + " | include Vendor SN  : ", read_timeout=100, cmd_verify=True)
                    for SplitItem_sn in output_sn.split("\n"):
                        if "Vendor SN" in SplitItem_sn:
                            serial_number = SplitItem_sn.split()[-1]
                    
                    output_product = connection_main.send_command_timing("show opticalinfo " + port + " | include Ethernet Compliance Codes: ", read_timeout=100, cmd_verify=True)
                    for SplitItem_product in output_product.split("\n"):
                        if "Ethernet Compliance" in SplitItem_product and "show" not in SplitItem_product:
                            product_number = SplitItem_product.split()[-1]

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def huawei_m1a(device_name, device_type, device_ip): #M1A
    print("HUAWEI_CHASIS / M1A")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_ios',
                'ip': device_ip,
                'username': 'network.automation', 
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("screen-length 0 temporary", cmd_verify=True)
            output_sn= connection_main.send_command_timing("display elabel optical-module brief ", read_timeout=100, cmd_verify=True)
            
            for SplitItem in output_sn.split("\n"):
                if "/" in SplitItem:
                    serial_number = SplitItem.split()[2]
                    product_number = SplitItem.split()[1]
                    port = SplitItem.split()[0]

                    portx = port = re.sub(r'Int', 'Gi', port)
                    port = re.sub(r'Int', 'GE', port)
                    
                    output_speed = connection_main.send_command_timing("display interface "+ str(portx)+" | include BW ", read_timeout=100, cmd_verify=True)

                    for SplitItemX in output_speed.split("\n"):
                        if "BW" in SplitItemX and "Transceiver" in SplitItemX:
                            speed = SplitItemX.split("")[2]
                            speed = speed.replace(",","")

                    list_ipaddress.append(device_ip)
                    list_sfp_port.append(port)
                    list_sfp_serial.append(serial_number)
                    list_sfp_product.append(product_number)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_card_slot.append("device")
                    list_sfp_speed.append(speed)


                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append(port)
                    list_sfp_serial_temp.append(serial_number)
                    list_sfp_product_temp.append(product_number)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append(speed)

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")
           
            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zte_olt_c600(device_name, device_type, device_ip): #C600
    print("ZTE_OLT / C600")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_xr',
                'ip': device_ip,
                'username': 'network.automation',
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)
            ix = 1
            while ix < 17 :

                if ix in [10,11]:
                    ix +=1
                    continue

                ixx = 1
                while ixx < 2:
                        
                    output_sfp = connection_main.send_command_timing("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx) , cmd_verify=True)
                    # print("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))

                    sfp_pon_serial = "#"
                    product_pon_id = "#"

                    ixxx = 0
                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_pon_serial = SplitItem.split()[1]

                        if "Module-Class" in SplitItem:
                            ixxx += 1
                            if ixxx == 1:
                                product_pon_id = SplitItem.split()[-1]
                    
                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial.append(sfp_pon_serial)
                    list_sfp_product.append(product_pon_id)
                    list_card_slot.append("device")    
                    list_sfp_speed.append("#")      


                    list_card_slot_temp.append("device")
                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append("gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial_temp.append(sfp_pon_serial)
                    list_sfp_product_temp.append(product_pon_id)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

                    ixx += 1

                ix += 1

            iy = 10
            while iy < 12:

                iyy = 1
                while iyy < 5:

                    output_sfp = connection_main.send_command_timing("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy), cmd_verify=True)
                    # print("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy))

                    sfp_eth_serial = "#"
                    product_eth_id = "#"

                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_eth_serial = SplitItem.split()[1]

                        if "Module-Type " in SplitItem:
                            product_eth_id = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial.append(sfp_eth_serial)
                    list_sfp_product.append(product_eth_id)
                    list_card_slot.append("1" + "-" + str(iy))
                    list_sfp_speed.append("#")

                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial_temp.append(sfp_eth_serial)
                    list_sfp_product_temp.append(product_eth_id)
                    list_card_slot_temp.append("1" + "-" + str(iy))
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")
                    

                    iyy += 1

                iy += 1

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zte_olt_c610(device_name, device_type, device_ip): #C610
    print("ZTE_OLT / C610")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_xr',
                'ip': device_ip,
                'username': 'network.automation',
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)

            ix = 3
            while ix < 4:

                ixx = 1
                while ixx < 17:
                        
                    output_sfp = connection_main.send_command_timing("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx) , cmd_verify=True)
                    # print("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))

                    sfp_pon_serial = "#"
                    product_pon_id = "#"

                    ixxx = 0
                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_pon_serial = SplitItem.split()[1]

                        if "Module-Class" in SplitItem:
                            ixxx += 1
                            if ixxx == 1:
                                product_pon_id = SplitItem.split()[-1]
                    
                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("gpon-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial.append(sfp_pon_serial)
                    list_sfp_product.append(product_pon_id)
                    list_card_slot.append("device")
                    list_sfp_speed.append("#")



                    list_card_slot_temp.append("device")
                    list_ipaddress_temp.append(device_ip)
                    list_sfp_port_temp.append("gpon-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial_temp.append(sfp_pon_serial)
                    list_sfp_product_temp.append(product_pon_id)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n")

                    ixx += 1

                ix += 1

            iy = 1
            while iy < 2 :

                iyy = 1
                while iyy < 5:

                    output_sfp = connection_main.send_command_timing("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy), cmd_verify=True)
                    # print("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy))

                    sfp_eth_serial = "#"
                    product_eth_id = "#"

                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_eth_serial = SplitItem.split()[1]

                        if "Module-Type " in SplitItem:
                            product_eth_id = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial.append(sfp_eth_serial)
                    list_sfp_product.append(product_eth_id)
                    list_card_slot.append("1" + "-" + str(iy))
                    list_sfp_speed.append("#")


                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial_temp.append(sfp_eth_serial)
                    list_sfp_product_temp.append(product_eth_id)
                    list_card_slot_temp.append("1" + "-" + str(iy))
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n") 

                    iyy += 1

                iy += 1
            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zte_olt_c650(device_name, device_type, device_ip): #C650
    print("ZTE_OLT / C650")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'cisco_xr',
                'ip': device_ip,
                'username': 'network.automation',
                'password': 'Network34*',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)

            ix = 1
            while ix < 10 : #10

                if ix in [5,6]:
                    ix +=1
                    continue

                ixx = 1
                while ixx < 17: #17
                        
                    output_sfp = connection_main.send_command_timing("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx) , cmd_verify=True)
                    # print("show optical-module-info gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))

                    sfp_pon_serial = "#"
                    product_pon_id = "#"

                    ixxx = 0
                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_pon_serial = SplitItem.split()[1]

                        if "Module-Class" in SplitItem:
                            ixxx += 1
                            if ixxx == 1:
                                product_pon_id = SplitItem.split()[-1]
                    
                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial.append(sfp_pon_serial)
                    list_sfp_product.append(product_pon_id)
                    list_card_slot.append("device")
                    list_sfp_speed.append("#")

                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("gpon_olt-1" + "/" + str(ix) + "/" + str(ixx))
                    list_sfp_serial_temp.append(sfp_pon_serial)
                    list_sfp_product_temp.append(product_pon_id)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n") 

                    ixx += 1

                ix += 1

            iy = 5
            while iy < 7 :

                iyy = 1
                while iyy < 5:

                    output_sfp = connection_main.send_command_timing("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy), cmd_verify=True)
                    # print("show optical-module-info xgei-1/" + str(iy) + "/" + str(iyy))

                    sfp_eth_serial = "#"
                    product_eth_id = "#"

                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Sequence-Number" in SplitItem:
                            sfp_eth_serial = SplitItem.split()[1]

                        if "Module-Type " in SplitItem:
                            product_eth_id = SplitItem.split()[2]

                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial.append(sfp_eth_serial)
                    list_sfp_product.append(product_eth_id)
                    list_card_slot.append("1" + "-" + str(iy))
                    list_sfp_speed.append("#")


                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("xgei-1/" + str(iy) + "/" + str(iyy))
                    list_sfp_serial_temp.append(sfp_eth_serial)
                    list_sfp_product_temp.append(product_eth_id)
                    list_card_slot_temp.append("1" + "-" + str(iy))
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n") 

                    iyy += 1

                iy += 1
            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zyxel_olt_5206(device_name, device_type, device_ip): #5206
    print("ZYXEL_OLT / 5206")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'zyxel_os',
                'ip': device_ip,
                'username': 'operasyon',
                'password': '1234',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            connection_main.send_command_timing("terminal length 0", read_timeout=100, cmd_verify=True)


            ix = 1
            while ix < 7 :

                if ix in [3,4]:
                    ix +=1
                    continue

                ixx = 1
                while ixx < 17:
                    output_sfp = connection_main.send_command_timing("show interface gpon " + str(ix) + "-" + str(ixx) + " ddmi status ", cmd_verify=True)
                    # print("show interface gpon " + str(ix) + "-" + str(ixx) + " ddmi status ")

                    sfp_pon_serial = "#"
                    product_pon_id = "#"

                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Serial Number" in SplitItem:
                            sfp_pon_serial = SplitItem.split()[-1]

                        if "Part Number" in SplitItem:
                            product_pon_id = SplitItem.split()[-1]


                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("gpon " + str(ix) + "-" + str(ixx))
                    list_sfp_serial.append(sfp_pon_serial)
                    list_sfp_product.append(product_pon_id)
                    list_card_slot.append("device")
                    list_sfp_speed.append("#")


                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("gpon " + str(ix) + "-" + str(ixx))
                    list_sfp_serial_temp.append(sfp_pon_serial)
                    list_sfp_product_temp.append(product_pon_id)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n") 

                    ixx += 1

                ix += 1

            iy = 1
            while iy < 9 :
                output_sfp = connection_main.send_command_timing("show interface genni " + str(iy) + " ddmi status ", cmd_verify=True)
                # print("show interface genni " + str(iy) + " ddmi status ")

                sfp_eth_serial = "#"
                product_eth_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "vendor s/n" in SplitItem:
                        sfp_eth_serial = SplitItem.split()[-1]

                    if "vendor p/n" in SplitItem:
                        product_eth_id = SplitItem.split()[-1]

                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("genni " + str(iy))
                list_sfp_serial.append(sfp_eth_serial)
                list_sfp_product.append(product_eth_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")

                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("genni " + str(iy))
                list_sfp_serial_temp.append(sfp_eth_serial)
                list_sfp_product_temp.append(product_eth_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                iy += 1

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zyxel_olt_5212(device_name, device_type, device_ip): #5212
    print("ZYXEL_OLT / 5212")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'zyxel_os',
                'ip': device_ip,
                'username': 'operasyon',
                'password': '1234',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)
            ix = 1
            while ix < 13 :

                if ix in [6,7]:
                    ix +=1
                    continue

                ixx = 1
                while ixx < 17:
                    output_sfp = connection_main.send_command_timing("show interface gpon " + str(ix) + "-" + str(ixx) + " ddmi status ", cmd_verify=True)
                    # print("show interface gpon " + str(ix) + "-" + str(ixx) + " ddmi status ")

                    sfp_pon_serial = "#"
                    product_pon_id = "#"

                    for SplitItem in output_sfp.split("\n"):
                        
                        if "Serial Number" in SplitItem:
                            sfp_pon_serial = SplitItem.split()[-1]
                            if sfp_pon_serial == ":":
                                sfp_pon_serial == "#"

                        if "Part Number" in SplitItem:
                            product_pon_id = SplitItem.split()[-1]
                            if product_pon_id == ":":
                                product_pon_id == "#"


                    list_ipaddress.append(device_ip)
                    list_hostname.append(device_name)
                    list_devtype.append(device_type)
                    list_sfp_port.append("gpon " + str(ix) + "-" + str(ixx))
                    list_sfp_serial.append(sfp_pon_serial)
                    list_sfp_product.append(product_pon_id)
                    list_card_slot.append("device")
                    list_sfp_speed.append("#")


                    list_ipaddress_temp.append(device_ip)
                    list_hostname_temp.append(device_name)
                    list_devtype_temp.append(device_type)
                    list_sfp_port_temp.append("gpon " + str(ix) + "-" + str(ixx))
                    list_sfp_serial_temp.append(sfp_pon_serial)
                    list_sfp_product_temp.append(product_pon_id)
                    list_card_slot_temp.append("device")
                    list_sfp_speed_temp.append("#")

                    # print("***************************************************")
                    # print(list_ipaddress_temp)
                    # print("---------------------------------------------------")
                    # print(list_hostname_temp)
                    # print("---------------------------------------------------")
                    # print(list_devtype_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_port_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_serial_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_product_temp)
                    # print("---------------------------------------------------")
                    # print(list_card_slot_temp)
                    # print("---------------------------------------------------")
                    # print(list_sfp_speed_temp)
                    # print("---------------------------------------------------")
                    # print("list_ipaddress: " + str(len(list_ipaddress)))
                    # print("list_hostname: " + str(len(list_hostname)))
                    # print("list_devtype: " + str(len(list_devtype)))
                    # print("list_sfp_port: " + str(len(list_sfp_port)))
                    # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                    # print("list_sfp_product: " + str(len(list_sfp_product)))
                    # print("list_card_slot: " + str(len(list_card_slot)))
                    # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                    # print("***************************************************")
                    # print("\n\n\n") 

                    ixx += 1

                ix += 1

            iy = 1
            while iy < 9 :
                output_sfp = connection_main.send_command_timing("show interface genni " + str(iy) + " ddmi status ", cmd_verify=True)
                # print("show interface genni " + str(iy) + " ddmi status ")

                sfp_eth_serial = "#"
                product_eth_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "vendor s/n" in SplitItem:
                        sfp_eth_serial = SplitItem.split()[-1]

                    if "vendor p/n" in SplitItem:
                        product_eth_id = SplitItem.split()[-1]

                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("genni " + str(iy))
                list_sfp_serial.append(sfp_eth_serial)
                list_sfp_product.append(product_eth_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")


                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("genni " + str(iy))
                list_sfp_serial_temp.append(sfp_eth_serial)
                list_sfp_product_temp.append(product_eth_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                iy += 1


            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zyxel_olt_1404a(device_name, device_type, device_ip): #1404A
    print("ZYXEL_OLT / 1404A")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'zyxel_os',
                'ip': device_ip,
                'username': 'operasyon',
                'password': '1234',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)

            ix = 1
            while ix < 5 :
                output_sfp = connection_main.send_command_timing("show interfaces transceiver pon-" + str(ix) + " ", cmd_verify=True)
                # print("show interfaces transceiver pon-" + str(ix) + " ")

                sfp_pon_serial = "#"
                product_pon_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "Serial Number" in SplitItem:
                        sfp_pon_serial = SplitItem.split()[-1]

                    if "Part Number" in SplitItem:
                        product_pon_id = SplitItem.split()[-1]


                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("pon-" + str(ix))
                list_sfp_serial.append(sfp_pon_serial)
                list_sfp_product.append(product_pon_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")


                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("pon-" + str(ix))
                list_sfp_serial_temp.append(sfp_pon_serial)
                list_sfp_product_temp.append(product_pon_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                ix += 1

            iy = 1
            while iy < 21 :
                output_sfp = connection_main.send_command_timing("show interfaces transceiver eth-" + str(iy) + " ", cmd_verify=True)
                # print("show interfaces transceiver eth-" + str(iy) + " ")

                sfp_eth_serial = "#"
                product_eth_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "Serial Number" in SplitItem:
                        sfp_eth_serial = SplitItem.split()[-1]

                    if "Part Number" in SplitItem:
                        product_eth_id = SplitItem.split()[-1]

                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("eth-" + str(iy))
                list_sfp_serial.append(sfp_eth_serial)
                list_sfp_product.append(product_eth_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")


                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("eth-" + str(iy))
                list_sfp_serial_temp.append(sfp_eth_serial)
                list_sfp_product_temp.append(product_eth_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                iy += 1

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def zyxel_olt_1408ac(device_name, device_type, device_ip): #1408A-C
    print("ZYXEL_OLT / 1408A-C")

    # list_hostname = []
    # list_devtype = []
    # list_sfp_port = []
    # list_ipaddress = []
    # list_sfp_serial = []
    # list_sfp_product = []
    # list_card_slot = []
    # list_sfp_speed = []

    list_hostname_temp = []
    list_devtype_temp = []
    list_sfp_port_temp = []
    list_ipaddress_temp = []
    list_sfp_serial_temp = []
    list_sfp_product_temp = []
    list_card_slot_temp = []
    list_sfp_speed_temp = []
    software_version = "#"
    license_number = "#"
    software_power = "#"
    try:
        try:
            device = {
                'device_type': 'zyxel_os',
                'ip': device_ip,
                'username': 'operasyon',
                'password': '1234',
                'fast_cli': True,  # Enable fast CLI mode
                'session_timeout': 10
            }
            connection_main = ConnectHandler(**device)

            ix = 1
            while ix < 9 :
                output_sfp = connection_main.send_command_timing("show interfaces transceiver pon-" + str(ix) + " ", cmd_verify=True)
                # print("show interfaces transceiver pon-" + str(ix) + " ")

                sfp_pon_serial = "#"
                product_pon_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "Serial Number" in SplitItem:
                        sfp_pon_serial = SplitItem.split()[-1]

                    if "Part Number" in SplitItem:
                        product_pon_id = SplitItem.split()[-1]


                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("pon-" + str(ix))
                list_sfp_serial.append(sfp_pon_serial)
                list_sfp_product.append(product_pon_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")


                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("pon-" + str(ix))
                list_sfp_serial_temp.append(sfp_pon_serial)
                list_sfp_product_temp.append(product_pon_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                ix += 1

            iy = 1
            while iy < 21 :
                output_sfp = connection_main.send_command_timing("show interfaces transceiver eth-" + str(iy) + " ", cmd_verify=True)
                # print("show interfaces transceiver eth-" + str(iy) + " ")

                sfp_eth_serial = "#"
                product_eth_id = "#"

                for SplitItem in output_sfp.split("\n"):
                    
                    if "Serial Number" in SplitItem:
                        sfp_eth_serial = SplitItem.split()[-1]

                    if "Part Number" in SplitItem:
                        product_eth_id = SplitItem.split()[-1]

                list_ipaddress.append(device_ip)
                list_hostname.append(device_name)
                list_devtype.append(device_type)
                list_sfp_port.append("eth-" + str(iy))
                list_sfp_serial.append(sfp_eth_serial)
                list_sfp_product.append(product_eth_id)
                list_card_slot.append("device")
                list_sfp_speed.append("#")


                list_ipaddress_temp.append(device_ip)
                list_hostname_temp.append(device_name)
                list_devtype_temp.append(device_type)
                list_sfp_port_temp.append("eth-" + str(iy))
                list_sfp_serial_temp.append(sfp_eth_serial)
                list_sfp_product_temp.append(product_eth_id)
                list_card_slot_temp.append("device")
                list_sfp_speed_temp.append("#")

                # print("***************************************************")
                # print(list_ipaddress_temp)
                # print("---------------------------------------------------")
                # print(list_hostname_temp)
                # print("---------------------------------------------------")
                # print(list_devtype_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_port_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_serial_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_product_temp)
                # print("---------------------------------------------------")
                # print(list_card_slot_temp)
                # print("---------------------------------------------------")
                # print(list_sfp_speed_temp)
                # print("---------------------------------------------------")
                # print("list_ipaddress: " + str(len(list_ipaddress)))
                # print("list_hostname: " + str(len(list_hostname)))
                # print("list_devtype: " + str(len(list_devtype)))
                # print("list_sfp_port: " + str(len(list_sfp_port)))
                # print("list_sfp_serial: " + str(len(list_sfp_serial)))
                # print("list_sfp_product: " + str(len(list_sfp_product)))
                # print("list_card_slot: " + str(len(list_card_slot)))
                # print("list_sfp_speed: " + str(len(list_sfp_speed)))
                # print("***************************************************")
                # print("\n\n\n") 

                iy += 1
                

            connection_main.disconnect()

        except:
            pass
    except:
        pass

def mains(device):
    name, dev_type, ip = device
    print("main session: " + ip)
       

    if "DWDM" in dev_type:
        print("~~~~~~ DWDM ~~~~~~ "+ str(ip) +  " ~~~~~~")

    elif "Cisco ROUTER-IOS 3725" in dev_type:
        print("CISCO_XE / 3725 "+ str(ip))
        cisco_xe_3725(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS-XR N540" in dev_type:
        print("CISCO_XR / N540 "+ str(ip))
        cisco_xr_n540(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS A901-6CZ-F-D" in dev_type:
        print("CISCO_XE / A901-6CZ-F-D "+ str(ip))
        cisco_xe_a901_6cz_f_d(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS A901-12C-F-D" in dev_type:
        print("CISCO_XE / A901-12C-F-D "+ str(ip))
        cisco_xe_a901_12c_f_d(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS-XE ASR-920-24SZ-M" in dev_type:
        print("CISCO_XE / ASR-920-24SZ-M "+ str(ip))
        cisco_xe_asr_920_24sz_m(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS-XE ASR-920-4SZ-D" in dev_type:
        print("CISCO_XE / ASR-920-4SZ-D "+ str(ip))
        cisco_xe_asr_920_4sz_d(name,dev_type, ip)
    
    elif "Cisco ROUTER-IOS-XE ASR-920-12CZ-D" in dev_type:
        print("CISCO_XE / ASR-920-4SZ-D "+ str(ip))
        cisco_xe_asr_920_12cz_d(name,dev_type, ip)

    elif "Arista ROUTER-EOS DCS-7280CR3K-32P4-F" in dev_type:
        print("ARISTA / DCS-7280CR3K-32P4-F "+ str(ip))
        arista_dcs_7280cr3k_32p4_f(name,dev_type, ip)
    
    elif "Arista ROUTER-EOS DCS-7280SR2K-48C6-M-F" in dev_type:
        print("ARISTA / DCS-7280SR2K-48C6-M-F "+ str(ip))
        arista_dcs_7280sr2k_48c6_m_f(name,dev_type, ip)
    
    elif "Arista ROUTER-EOS DCS-7280SR3K-48YC8-F" in dev_type:
        print("ARISTA / DCS-7280SR3K-48YC8-F "+ str(ip))
        arista_dcs_7280sr3k_48yc8_f(name,dev_type, ip)
    
    elif "Zte ROUTER-OS M6000-3S-PLUS" in dev_type:
        print("ZTE / M6000-3S-PLUS "+ str(ip))
        zte_m6000_3s_plus(name,dev_type, ip)
    
    elif "Zte ROUTER-OS M6000-8S-PLUS" in dev_type:
        print("ZTE_CHASIS / M6000-8S-PLUS "+ str(ip))
        zte_m6000_8s_plus(name,dev_type, ip)
    
    elif "Huawei ROUTER-VRP M1A" in dev_type:
        print("HUAWEI_CHASIS / M1A "+ str(ip))
        huawei_m1a(name,dev_type, ip)

    elif "Zte OLT-OS C600 T-LEVEL" in dev_type:
        print("ZTE_OLT_CHASIS_1 / C600 "+ str(ip))
        zte_olt_c600(name,dev_type, ip)
    
    elif "Zte OLT-OS C610" in dev_type:
        print("ZTE_OLT_CHASIS_1 / C610 "+ str(ip))
        zte_olt_c610(name,dev_type, ip)

    elif "Zte OLT-OS C650" in dev_type:
        print("ZTE_OLT_CHASIS_1 / C650 "+ str(ip))
        zte_olt_c650(name,dev_type, ip)

    elif "Zyxel OLT-OS IES-5206" in dev_type:
        print("ZYXEL_OLT / 5206 "+ str(ip))
        zyxel_olt_5206(name,dev_type, ip)
    
    elif "Zyxel OLT-OS IES-5212" in dev_type:
        print("ZYXEL_OLT / 5212 "+ str(ip))
        zyxel_olt_5212(name,dev_type, ip)

    elif "Zyxel OLT-OS OLT1404A" in dev_type:
        print("ZYXEL_OLT / 1404A "+ str(ip))
        zyxel_olt_1404a(name,dev_type, ip)

    elif "Zyxel OLT-OS OLT1408A-C" in dev_type:
        print("ZYXEL_OLT / 1408A-C "+ str(ip))
        zyxel_olt_1408ac(name,dev_type, ip)
    
    else:
        print("~~~~~~ UNKNOWN ~~~~~~ "+ str(ip) + " / " +str(dev_type) + " ~~~~~~")
        

    

    


# getDeviceListFromQuigon = sqlReadUpdate("SELECT name, type, ip FROM network_inventory.inv_device", read=True)
getDeviceListFromQuigon = sqlReadUpdate("SELECT name, type, ip FROM network_inventory.inv_device WHERE name LIKE '34_MAHMUTBEY_SOL_RTR01'", read=True)
# getDeviceListFromQuigon = [("x",'Cisco ROUTER-IOS A901-6CZ-F-D','193.192.126.206')]

start = time.time()
print("Script has started " + time.ctime())



# getDescription = [(100456,'193.192.126.183','07_MERKEZ-22_TT_BNG01','Cisco ROUTER-IOS-XE ASR1009-X','Te3','up','up','Google_Uplink','SSH_OK'),
# (100457,'193.192.126.184','07_MERKEZ-22_TT_BNG01','Cisco ROUTER-IOS-XE ASR1009-X','ETH3','up','up','Customer_1_Uplink','SSH_OK'),
# (100458,'193.192.126.184','07_MERKEZ-22_TT_BNG01','Cisco ROUTER-IOS-XE ASR1009-X','ETH5','up','up','Customer_2_Uplink','SSH_OK'),
# (100459,'193.192.126.185','07_MERKEZ-22_TT_BNG01','Cisco ROUTER-IOS-XE ASR1009-X','Gi3','up','up','Back_up_Uplink','SSH_OK')]
getDescription = sqlReadUpdate("SELECT * FROM uranus.nw_interface_description" , read=True)
max_workers = 5

with ThreadPoolExecutor(max_workers=max_workers) as executor:
    executor.map(mains, getDeviceListFromQuigon)

print(" - - - - - -  1  - - - - - ")

print(len(list_hostname))
print(len(list_devtype))
print(len(list_sfp_port))
print(len(list_ipaddress))
print(len(list_sfp_serial))
print(len(list_sfp_product))
print(len(list_card_slot))
print(len(list_sfp_speed))

print(" - - - - - -  2  - - - - - ")

dbConn = sqlConn()

count = 0
while count < len(list_hostname):
    
    if list_card_slot[count] == "device":
        getDeviceInfoByID = sqlReadUpdate("SELECT id FROM network_inventory.inv_device WHERE ip = '"+list_ipaddress[count]+"'", read=True)
        parent_id = getDeviceInfoByID[0][0]
        parent_source = "device"
    else:
        
        getDeviceInfoByID = sqlReadUpdate("SELECT inv.id FROM network_inventory.inv_card AS inv LEFT JOIN network_inventory.inv_device AS dev ON inv.parent = dev.id WHERE dev.ip = '"+list_ipaddress[count]+"' AND inv.port = '"+list_card_slot[count]+"'", read=True)
        parent_id = getDeviceInfoByID[0][0]
        parent_source = "card"
        
    # Description Doldurma Blogu
    newInterface = list_sfp_port[count].replace("GigabitEthernet ", "Gi").replace("TenGigabitEthernet ", "Te").replace("subslot 0/0 transceiver 0", "Gi0/0/0").replace("subslot 0/0 transceiver 1", "Gi0/0/1").replace("subslot 0/0 transceiver 2", "Gi0/0/2").replace("subslot 0/0 transceiver 3", "Gi0/0/3").replace("subslot 0/0 transceiver 4", "Gi0/0/4").replace("subslot 0/0 transceiver 5", "Gi0/0/5").replace("subslot 0/0 transceiver 6", "Gi0/0/6").replace("subslot 0/0 transceiver 7", "Gi0/0/7").replace("subslot 0/0 transceiver 8", "Gi0/0/8").replace("subslot 0/0 transceiver 9", "Gi0/0/9").replace("subslot 0/0 transceiver 10", "Gi0/0/10").replace("subslot 0/0 transceiver 11", "Gi0/0/11").replace("subslot 0/0 transceiver 12", "Gi0/0/12").replace("subslot 0/0 transceiver 13", "Gi0/0/13").replace("subslot 0/0 transceiver 14", "Gi0/0/14").replace("subslot 0/0 transceiver 15", "Gi0/0/15").replace("subslot 0/0 transceiver 16", "Gi0/0/16").replace("subslot 0/0 transceiver 17", "Gi0/0/17").replace("subslot 0/0 transceiver 18", "Gi0/0/18").replace("subslot 0/0 transceiver 19", "Gi0/0/19").replace("subslot 0/0 transceiver 20", "Gi0/0/20").replace("subslot 0/0 transceiver 21", "Gi0/0/21").replace("subslot 0/0 transceiver 22", "Gi0/0/22").replace("subslot 0/0 transceiver 23", "Gi0/0/23").replace("subslot 0/0 transceiver 24", "Te0/0/24").replace("subslot 0/0 transceiver 25", "Te0/0/25").replace("subslot 0/0 transceiver 26", "Te0/0/26").replace("subslot 0/0 transceiver 27", "Te0/0/27")

    if len(getDescription) > 0:
        def get_description(ip, interface):
            for device in getDescription:
                if device[1] == ip and device[4] == interface:
                    return device[7], device[5]  # Return the description from the tuple
            return None, None # Return None if no match is found


        ip = list_ipaddress[count]
        interface = newInterface

        description, status = get_description(ip, interface)

        if description:
            intDesc = description
        else:
            intDesc = "#"


        if status:
            intStat = status
        else:
            intStat = "#"

    
        
    insertNewData = sqlReadUpdate("INSERT INTO network_inventory.inv_port (parent_source, parent, port, serial_no, type, speed, port_desc, port_state) VALUES (\
                                        '"+parent_source+"', \
                                        "+str(parent_id)+", \
                                        '"+list_sfp_port[count]+"', \
                                        '"+list_sfp_serial[count]+"', \
                                        '"+list_sfp_product[count]+"', \
                                        '"+list_sfp_speed[count]+"', \
                                        '"+intDesc+"', \
                                        '"+intStat+"') \
                                    ON DUPLICATE KEY UPDATE \
                                        parent_source='"+parent_source+"', \
                                        parent='"+str(parent_id)+"', \
                                        port='"+list_sfp_port[count]+"', \
                                        serial_no='"+list_sfp_serial[count]+"', \
                                        speed='"+list_sfp_speed[count]+"', \
                                        type='"+list_sfp_product[count]+"', \
                                        port_desc='"+intDesc+"', \
                                        port_state='"+intStat+"' \
                                    ;", read=False)
    count = count + 1



end = time.time()
print("Script has been executed " + time.ctime())
print("Script executed in " + str(end - start) + " seconds")