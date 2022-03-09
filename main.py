import base64
import argparse
import hashlib
parser = argparse.ArgumentParser(description="Input public and private key pairs:\n")
parser.add_argument('public', type=str)
parser.add_argument('private', type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    public = args.public
    private = args.private
    keyword = public + private + public
    transformed = hashlib.sha256(keyword.encode('utf-8')).hexdigest()
    rearranged = base64.b64encode(transformed.encode('utf-8')).decode('utf-8').strip('=')
    length = str(int(str(len(keyword) + len(transformed) + len(rearranged)), base=int(32 % len(private) + 10)))
    password = rearranged.swapcase() + '_' + length
    print(password)



