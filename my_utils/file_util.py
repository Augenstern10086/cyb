# -*- coding:UTF-8 -*-
"""
editor:ChangYingbo
date:2024年 09月 11日
"""
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()

def append_to_file(file_name, data):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.close()

if __name__ == "__main__":
    print_file_info("1231.txt")
    append_to_file("123.txt", "187654321")