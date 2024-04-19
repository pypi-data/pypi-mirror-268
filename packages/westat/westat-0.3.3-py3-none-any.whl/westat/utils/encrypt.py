def get_md5(text):    
    import hashlib
    md5  =hashlib.md5(text.encode('utf-8'))
    result=md5.hexdigest()
    return result

def get_sha1(text):    
    import hashlib
    sha1 = hashlib.sha1(text.encode('utf-8'))
    result = sha1.hexdigest()
    return result

