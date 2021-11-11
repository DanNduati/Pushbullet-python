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

def main():
    fp = read_file("numbers.txt")
    print(get_numbers(fp))

if __name__ == "__main__":
    main()
