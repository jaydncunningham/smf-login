import sys
import hashlib

def hashLoginPassword(uname, psw, hsh):
    frst_str = uname.lower() + psw
    frst = hashlib.sha1(frst_str.encode()).hexdigest()
    scnd_str = frst + hsh
    scnd = hashlib.sha1(scnd_str.encode()).hexdigest()
    return scnd

def main():
    hashLoginPassword(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()
