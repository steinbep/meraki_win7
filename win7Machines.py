#!/usr/bin/python

import merakidashboard as meraki
import json, csv, pprint, time

#
# Python Script Using Meraki API to find all Window 7/8 clients in Dashboard
#


# Enter User's API Key
apikey = '3b5c4d0c2eb2dd0388f5add825759d285043840f'

# Enter Organization ID Here
organizationid = '133624'

clientMachines = []
win7Machines = []
nondomain = []


#Networks lookup
networks = meraki.getnetworklist(apikey, organizationid, suppressprint=True)


#Loop through Networks 
for row in networks:

    #Lookup all devices in network
    devices = meraki.getclientsAll(apikey, row['id'],'1000', suppressprint=True)

    #For loop to append
    for device in devices:
    
        #Updating the device list to include the network id and name.
        device.update({'network' : row['id'], 'networkName' : row['name']})
        clientMachines.append(device)
        
        '''
        #If you have any networks you want to exclude, uncomment this section and comment out the above 2 lines. 
        if row['id'] == 'Systems Manager Network ID':
            continue
        else:
            device.update({'network' : row['id'], 'networkName' : row['name']})
            clientMachines.append(device)
        '''

#optional if you have multiple networks
#clientMachines.sort(key=lambda i:i['network'])


for client in clientMachines:

    if client['os'] == "Windows 7":
        win7Machines.append(client)
    elif client['os'] == "Windows 7/Vista":
        win7Machines.append(client)
    else:
        pass

print(len(win7Machines))
