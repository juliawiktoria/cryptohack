import codecs

inp = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

hex = codecs.decode(inp, 'hex')

result = codecs.encode(hex, 'base64')

print(result.decode())