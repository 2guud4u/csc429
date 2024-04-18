import check_functionality
import requests
import time
import random
import json
import re

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Get the webhook URL from the configuration
webhook_url = config.get('webhook_url')

message = {
    'text': "<!everyone> The server is currently down. CHECK THE SERVER IMMEDIATELY!"
}

def main():
    target = "http://64.23.209.18/submit.php"
    target2 = "http://64.23.209.18"
    try:
        ping_test(target) 
        check_functionality.ui_test(target2)
    except Exception as e:
        # send notification
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print("Failed to send notification. Status code: {status_code}".format(status_code=response.status_code))
        return False


def ping_test(target):
    random_number = random.randint(0, 999)
    payload = {'firstName': 'test', 
            'lastName': 'test',
            'phoneNumber': random_number, 
            'item': 'Wand'}
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    try:
        r=requests.post(target, headers=header, data=payload)
        t = time.localtime()
        pattern = re.compile(r'^[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}$')
        t_id = r.text[-12:]
        if len(r.text) == 66 and bool(pattern.match(t_id)):
            current_time = time.strftime("%H:%M:%S", t)
            print("{time}: {id}".format(time=current_time, id=t_id))
        else:
            raise("Ping test failed.")
    except Exception as e:
        raise("Ping test failed.", e)


if __name__ == "__main__":
    main()