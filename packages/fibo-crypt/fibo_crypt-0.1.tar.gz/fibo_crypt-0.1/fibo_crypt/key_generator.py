import time
import re
import hashlib

def f(n):
    sum_n = sum(map(int, str(n)))
    if sum_n > 9:
        return f(sum_n)
    return sum_n

def generate_key():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    sum_time = re.findall(r'\d+', current_time)
    key = sum([int(num) for num in sum_time])
    key = f(key)
    return key

def export_key(key, file_path):
    with open(file_path, 'w') as file:
        key = str(key)
        file.write(hashlib.md5(key.encode()).hexdigest())