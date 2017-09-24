import requests
import form_replication
import sys

def attempt_login(url, uname, passw):
    key = requests.get(url).text.split("hashLoginPassword(this, '")[1].split("'")[0]
    print(key)
    requests.post(url, data={
        'user': uname,
        'passwrd': passw,
        'cookielength': '60',
        'hash_passwrd': form_replication.hashLoginPassword(uname, passw, key),
    }).text
    # do your stuff here

def main():
    attempt_login(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()
