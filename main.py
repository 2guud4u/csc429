import check_functionality
import requests
import time
import random

def main():
    target = "http://64.23.209.18/submit.php"
    try:
        ping_test(target) 
    except:
        # send notification
        return False
    

    


def ping_test(target):
    while True:
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

        time.sleep(30)

if __name__ == "__main__":
    main()