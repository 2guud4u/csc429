import check_functionality

def main():
    if(check_functionality.check()):
        #do nothing
        print("All functionality is working fine")
    else:
        #send report
        print("Some functionality is not working")