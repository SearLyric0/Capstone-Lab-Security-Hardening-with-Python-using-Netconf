#import the ncclient which allows us to use NETCONF with our devices
from ncclient import manager

#define our router with correct settings
router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False,
    "device_params": {"name": "csr"},
}

#set the hostname of our device using XML with the YANG model
hostname_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>SecuredDevice</hostname>
  </native>
</config>
"""
#set a VLAN 20 on device using XML with the YANG model
subinterface_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <GigabitEthernet>
        <name>1.20</name>
        <description>NETCONF_SUBIF_VLAN20</description>
        <encapsulation>
          <dot1Q>
            <vlan-id>20</vlan-id>
          </dot1Q>
        </encapsulation>
        <ip>
          <address>
            <primary>
              <address>192.168.20.1</address>
              <mask>255.255.255.0</mask>
            </primary>
          </address>
        </ip>
      </GigabitEthernet>
    </interface>
  </native>
</config>
"""


#defining a domain name on our router using XML with the YANG model
domain_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <ip>
      <domain>
        <name>cisco.com</name>
      </domain>
    </ip>
  </native>
</config>
"""

#This logic unpacks the code writen above
with manager.connect(**router) as m:
   #add a simple comment to confirm code has ran
    print("Connected to device")

    #These lines run our configurations on our target device
    print(m.edit_config(target="running", config=hostname_config))
    print(m.edit_config(target="running", config=subinterface_config))
    print(m.edit_config(target="running", config=domain_config))

#run one last line of code to make sure our code doesn't break before we finish all configurations
print("\nAll tasks completed successfully.")
