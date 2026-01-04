from ncclient import manager
#import logging
# This will log the actual XML content to your console
#logging.basicConfig(level=logging.DEBUG)

# Configuration XML to enable ethernet-1/1
# Namespace verified for SR Linux 2025/2026
config_data = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interface xmlns="urn:nokia.com:srlinux:chassis:interfaces">
        <name>ethernet-1/1</name>
        <admin-state>enable</admin-state>
    </interface>
</config>
"""

with manager.connect(
    host='172.20.20.6', 
    port=830, 
    username='admin', 
    password='NokiaSrl1!',
    hostkey_verify=False
) as m:
    # 1. Push config to candidate datastore
    m.edit_config(target='candidate', config=config_data)
    
    # 2. Commit the changes to make them active in 'running'
    #m.commit()
    #print("Interface ethernet-1/1 enabled and committed.")

