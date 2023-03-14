import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
pw_length = 6

def generate_password(pw_length):
    mypw = ""
    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2)
        mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]

    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2,len(mypw))
        mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]
    return mypw

while True:
    print("Your password is", generate_password(pw_length))
    inp = input()
    if not inp:
        break
import string
import random

def generate_password(pw_length):
    charsets = []
    # take 1 or 2 numbers
    for i in range(random.randrange(1,3)):
        charsets.append(string.digits)
    # take 1 or 2 uppercase
    for i in range(random.randrange(1,3)):
        charsets.append(string.ascii_uppercase)
    # fill up with lowercase up to pw_length
    while len(charsets) < pw_length:
        charsets.append(string.ascii_lowercase)
    # generate password of charsets
    random.shuffle(charsets)
    return ''.join(random.choice(cs) for cs in charsets)

while True:
    print("Your password is", generate_password(pw_length))
    inp = input()
    if not inp:
        break