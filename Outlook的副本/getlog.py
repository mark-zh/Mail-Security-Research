#coding=utf-8
import os
import re

def get_log():
    httplog = os.popen('cat /var/log/apache2/access.log')
    return httplog.read()

def main():
    str = get_log()
    pattern = re.compile(r'GET /(.*?)HTTP')
    key = re.findall(pattern,str)
    print key

if __name__ == '__main__':
    main()