import base64
import argparse
import hashlib

parser = argparse.ArgumentParser(description="Niki's password generator")
parser.add_argument('-l', type=int, help='max_length')

if __name__ == '__main__':
    args = parser.parse_args()
    max_length = args.l
    private = input('Master password: ')
    public = input('Service: ')
    keyword = public + private + public
    transformed = hashlib.sha256(keyword.encode('utf-8')).hexdigest()
    rearranged = base64.b64encode(transformed.encode('utf-8')).decode('utf-8').strip('=')
    length = str(int(str(len(keyword) + len(transformed) + len(rearranged)), base=int(32 % len(private) + 10)))
    password = rearranged.swapcase() + '_' + length
    if max_length:
        password = password[len(password) - max_length:]
    print(password, len(password))



