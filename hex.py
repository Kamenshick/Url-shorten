import hashlib
class Hex:
    @staticmethod
    def hrefToString(stringHref):
        hash_object = hashlib.sha256(stringHref.encode('utf-8'))
        return hash_object.hexdigest()