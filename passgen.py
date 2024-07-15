import base64
from time import sleep

greeting = '''#############
P A S S   G E N
by blaze_edge
#############'''

print(greeting)
sleep(1)

def base_encode(word: str):
    b = word.encode("UTF-8")
    be = base64.b64encode(b)
    se = be.decode("UTF-8")
    return se

service = input('Enter the service name: ')
year = input('Enter the year of registration: ')

eservice = base_encode(service)
eyear = base_encode(year)

print(f'Generated pass: {eservice.replace("=", "") + eyear.replace("=", "")}')
sleep(5)