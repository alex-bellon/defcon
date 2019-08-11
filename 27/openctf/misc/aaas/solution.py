import string, itertools, socket

def generate_strings(length=3):
    chars = string.ascii_letters + string.digits + '@.'
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

def main():

    for i in range(50):
        gen = generate_strings(i)
        for string in gen:
            s = socket.socket()
            host = 'challenges.openctf.cat'
            port = 9011
            s.connect((host, port))

            r = s.recv(1024).decode('ascii')
            #print(r)

            resp = string + '\n'
            s.send(resp.encode('ascii'))

            text = ''
            for j in range(20):
                r = s.recv(9999999999).decode('ascii')
                text += r

            num = text.split('\n')[-2:][0]
            print(num)

            try:
                num = int(num)
                if abs(num - 987654321) <= 10000:
                    print('\n\nFOUND: ' + string + ': ' + str(num) + '\n\n')
                if num == 987654321:
                    print('\n\nFOUND: ' + string + ': ' + str(num) + '\n\n')
                    return
            except:
                pass


            #return
            s.close()
main()
