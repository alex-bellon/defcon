from Crypto.PublicKey import RSA

public = open('key.pub', 'r')
key = RSA.importKey(public.read())
print('n: ' + str(key.n))
print('\ne: ' + str(key.e))
