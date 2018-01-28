def getSha1(str):
    from hashlib import sha1
    s1 = sha1()
    s1.update(str.encode())
    return s1.hexdigest()

if __name__ == '__main__':
    print(getSha1('rong'))