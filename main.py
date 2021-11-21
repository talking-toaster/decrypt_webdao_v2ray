import datetime
import base64
import requests


def get_raw_link():
    url = 'https://raw.githubusercontent.com/webdao/v2ray/master/nodes.txt'

    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(response.text)
            raise Exception("Network Error")
    except:
        print("Cannot connect to raw.githubusercontent.com")
        exit()

    return response.text


def get_key(date: datetime.date = datetime.date.today()):
    yyyymmdd = str(date.year)+str(date.month)+str(date.day)
    return yyyymmdd*4


def decrypt(key: str, ciphertext: str or bytes):
    '''
    XOR
    '''
    b64_cipher = base64.b64decode(ciphertext).decode()
    plaintext = ''
    for i in range(len(b64_cipher)):
        plaintext += chr(ord(b64_cipher[i]) ^ ord(key[i % len(key)]))
    return plaintext

if __name__=="__main__":
    link = decrypt(get_key(), get_raw_link())
    print(link)
