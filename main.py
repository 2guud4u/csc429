import check_functionality
import requests
import time
import random
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Get the webhook URL from the configuration
webhook_url = config.get('webhook_url')

message = {
    'text': "The server is currently down. CHECK THE SERVER IMMEDIATELY!"
}

def main():
    target = "http://64.23.209.18/submit.php"
    try:
        ping_test(target) 
        check_functionality.ui_test(target)
    except:
        # send notification
        response = requests.post(webhook_url, data=json.dumps(message), headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print("Failed to send notification")
        return False
    

    


def ping_test(target):

    try:
        random_number = random.randint(0, 999)
        payload = {'firstName': 'test', 
                'lastName': 'test',
                'phoneNumber': random_number, 
                'item': 'Wand'}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}

        r=requests.post(target, headers=header, data=payload)
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("{time}: {id}".format(time=current_time, id=r.text[-12:]))
        # check r.text is valid id
    except:
        return False

        

if __name__ == "__main__":
    main()