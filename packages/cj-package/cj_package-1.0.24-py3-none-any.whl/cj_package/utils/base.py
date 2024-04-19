import hashlib
import base64
from typing import Any

def md5_encrypt(input_string: str, salt: Any = None):
    """
    对输入字符串进行md5加密

    :param input_string: 输入字符串
    :param salt: 盐值，可以不填
    """
    use_salt_bool = False

    if salt is not None:
        try:
            salt = str(salt)
        except Exception as e:
            raise Exception(f"salt转化为字符串失败, {e}")
        use_salt_bool = True

    md5 = hashlib.md5()
    if use_salt_bool:
        salt = salt.encode('utf-8')
        md5.update(input_string.encode('utf-8') + salt)
    else:
        md5.update(input_string.encode('utf-8'))
    return md5.hexdigest()

def base64_encode(input_string: str):
    """
    对输入字符串进行base64编码

    :param input_string: 输入字符串
    """
    # 将字符串编码为字节
    input_bytes = input_string.encode('utf-8')
    # 对字节进行 Base64 编码
    encoded_bytes = base64.b64encode(input_bytes)
    # 将编码后的字节转换为字符串并返回
    return encoded_bytes.decode('utf-8')

def base64_decode(encoded_string: str):
    """
    对输入字符串进行base64解码

    :param encoded_string: 输入字符串
    """
    # 将字符串转换为字节
    encoded_bytes = encoded_string.encode('utf-8')
    # 对字节进行 Base64 解码
    decoded_bytes = base64.b64decode(encoded_bytes)
    # 将解码后的字节转换为字符串并返回
    return decoded_bytes.decode('utf-8')
