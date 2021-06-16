'''
消息鉴权码（二次验证）
'''
import doctest
import sqlite3
import pyotp
import os

def create_db():
    conn = sqlite3.connect('username.db')
    print("Opened database successfully")

    c = conn.cursor()
    c.execute("""CREATE TABLE NAME
           (NAME    TEXT    NOT NULL);""")

    print("Table created successfully")
    conn.commit()
    conn.close()

def insert_data(name):
    conn = sqlite3.connect('username.db')
    c = conn.cursor()
    print("Opened database successfully")

    c.execute("INSERT INTO NAME VALUES ('{}')".format(name))

    conn.commit()
    print("Records created successfully")
    conn.close()
    print("Your name is been inserted in database")

def createcode(seed, SECRET_KEY):
    # 创建hotp对象
    hotp = pyotp.HOTP(SECRET_KEY)
    # 生成一个验证码（鉴权）
    code = hotp.at(0)  # =>验证码：260182
    return code


def vcode(code, seed, SECRET_KEY):
    # 服务上面验证
    hotp = pyotp.HOTP(SECRET_KEY)  # SECRET_KEY是共享密钥
    result = hotp.verify(code, seed)  # 验证通过True
    return result


if __name__ == '__main__':

    #create_db()

    # pyotp提供了一个辅助函数随机生成一个16个字符的base32密钥
    key = pyotp.random_base32()
    # 种子
    seed = 0
    # 鉴权码
    code = createcode(seed, key)

    # 如果改变种子或验证码（鉴权码）则验证不成功
    r = vcode(code, seed, key)
    print("result", r)
    n = input("please input your user name")
    p = input("please input your password")
    print("OTP：", code)
    a = input("please input your opt")

    if a == code:
        print("Authentication is successful")
    else:
        print("Authentication is failed")
    if n =="abc" and p =="abc":
        print("login successfully")

    key = pyotp.random_base32()
    seed = 0
    code = createcode(seed, key)
    x = vcode(code, seed, key)
    n = input("please input your Administrator name")
    p = input("please input your Administrator password")
    print("OTP：", code)
    a = input("please input your opt")

    if a == code:
        print("Authentication is successful")
        insert_data(n)
    else:
        print("Authentication is failed")
    if n == "abc" and p == "abc":
        print("login successfully")


