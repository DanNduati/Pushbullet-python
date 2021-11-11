import os
from os.path import join,dirname
from dotenv import load_dotenv
from pushbullet import Pushbullet

dotenv_path = join(dirname(__file__),".env")
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY","default")

#Authentication
pb = Pushbullet(api_key)

#get all devices the current user has access to
#print(pb.devices)

# read numbers file and return file pointer
def read_file(file_name):
    try:
        fp = open(file_name,"r")
    except IOError:
        print(f"Unable to open {filename}")
    else:
        return fp

# generate a list of phone numbers from the file
def get_numbers(fp):
    numbers = []
    for line in fp:
        line.strip()
        numbers = line.split(",")
    return numbers

# function to select device to be used to send text msg from devices configured by account
def select_device(index):
    try:
        if pb.devices == "":
            raise ValueError("No devices currently configured for this account!")
    except ValueError as e:
        print(e.args)
    else:
        device = pb.devices[index]
    return device

def send_message(device,number_list,message):
    for i,number in enumerate(number_list):
        print(f"Sending message to: {number_list[i]}")
        push = pb.push_sms(device,number_list[i],message)

def main():
    success = False
    message = str(input("Please input the message: "))
    fp = read_file("numbers.txt")
    number_list = get_numbers(fp)
    devices = dict()
    for i,x in enumerate(pb.devices):
        devices[i] = x
    print(f"Devices currently in your account: {devices}")
    while not success:
        try:
            index = int(input("Please select a mobile device from the list: "))
            if index not in range(len(devices)):
                raise ValueError("Please select a number within the range!")
        except ValueError as e:
            print(e)
        else:
            send_message(select_device(index),number_list,message)
            success = True
if __name__ == "__main__":
    main()
