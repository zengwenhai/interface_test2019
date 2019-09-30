import hashlib


def encrypt(string, salt='', encrypt_way='MD5'):

    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encrypt_way.upper() == 'SHA1':
        hash_string = hashlib.sha1()
    else:
        return False


def sign(sing_dict, private_key=None, encrypt_way='MD5'):

    dict_keys = sing_dict.keys()
    list(dict_keys).sort()
    print(list(dict_keys))

    string = ''
    for key in dict_keys:
        if sing_dict[key] != None:
            string += '{0}={1}&'.format(key, sing_dict[key])
    string = string[0:len(string) - 1]
    string = string.replace('', '')
    return encrypt(string, salt=private_key,encrypt_way=encrypt_way)


if __name__ == '__main__':
    dict1 = {'name': 'zengwenhai', 'password': 123456}
    print(sign(dict1, private_key='111aandf23', encrypt_way='MD5'))
    print(encrypt('100000307111111'))