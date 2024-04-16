import check_functionality
import requests

def main():
    target = "http://test.csc429.io"
    if(check_functionality.check()):
        #do nothing
        print("All functionality is working fine")
    else:
        #send report
        print("Some functionality is not working")


def ping_test(target):
    try:
        requests.get(target)
        return True
    except:
        # insert code that runs when site is down here
        return False

    