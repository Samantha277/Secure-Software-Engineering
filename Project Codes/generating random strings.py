import random
import string
import time

start_time = time.time()
def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """

    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

print("Generating Random String password with letters, digits and special characters ")
print ("First Random String ", randomStringwithDigitsAndSymbols(100000) )
#print ("Second Random String", randomStringwithDigitsAndSymbols(10) )
#print ("Third Random String", randomStringwithDigitsAndSymbols(10) )