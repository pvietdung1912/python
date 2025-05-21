from netmiko import ConnectHandler
# from ntc_templates.parser import parse_output

SW = {
    'device_type': 'cisco_ios',
    'ip': '10.215.27.104',
    'username': 'vnpro',
    'password': 'vnpro#123',
    'secret': 'vnpro#321'
}

net_connect = ConnectHandler(**SW)

# connect mode privallige
net_connect.enable()

# show ip interface brief description
data = net_connect.send_command('show ip int brief')
print(data)

for i in range(10, 31):
    create_vlan = 'vlan {}'.format(i)
    config_vlan = ['int vlan {}'.format(i), 'ip add 172.16.{}.1 255.255.255.0'.format(i), 'no shut']
    output = net_connect.send_config_set(create_vlan)
    output = net_connect.send_config_set(config_vlan)
data = net_connect.send_command('show vlan')
# print(data)


# dataparse = parse_output(platform = 'cisco_ios', command = 'show vlan', data = data)

# for i in dataparse:
#     print(i)
# # disconnect mode privallige
# net_connect.disconnect()
