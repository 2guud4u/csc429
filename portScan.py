import nmap
import json
import requests
nm = nmap.PortScanner()
nm.scan('64.23.209.18', '1-5000')
result = ""
# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Get the webhook URL from the configuration
webhook_url = config.get('webhook_url')
message = {
    'text': "<!everyone> Warning! Port scan results have changed. CHECK THE SERVER IMMEDIATELY!"
}
with open('scan_results.txt', 'r+') as f:
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
                result += 'port : %s\tstate : %s\n' % (port, nm[host][proto][port]['state'])
    #compare result with original scan results
    if f.read() == result:
        print("No changes in port scan results")
    else:
        print("Changes in port scan results")
        f.seek(0)
        f.write(result)
        f.truncate()
        # alert the user
        message["text"] = message["text"] + "\n" + result
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
