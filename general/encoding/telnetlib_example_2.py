import telnetlib
import json
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
from binascii import unhexlify


HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def array_to_ascii(arr):
    result = []

    for i in range(0, len(arr)):
        result.append(chr(arr[i]))
    result = ''.join(result)
    return result

# loop for the 100 levels
for i in range(1, 101):
    print('Loop #{}'.format(i))
    received = json_recv()

    print("-> Received type: {}".format(received["type"]))
    print("-> Received encoded value: {}".format(received["encoded"]))

    encoding = received['type']
    word = received['encoded']

    # decode according to the type of encoding
    if encoding == 'hex':
        decoded = bytearray.fromhex(word).decode()
    elif encoding == 'base64':
        decoded = base64.b64decode(word).decode()
    elif encoding == 'rot13':
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == 'bigint':
        decoded = unhexlify(word.replace('0x', '')).decode().replace("'", '"')
    elif encoding == 'utf-8':
        decoded = array_to_ascii(word)
    else:
        decoded = 'aaa'

    print("-> Decoded value: {}".format(decoded))
    print("-> Decoded type: {}".format(type(decoded)))

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)

flag = json_recv()

print('-> FLAG: {}'.format(flag["flag"]))
