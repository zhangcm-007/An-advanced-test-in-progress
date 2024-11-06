import os

### 编写一个Python程序，将一些文本内容写入到文件中，并且能够从文件中读取内容并显示出来。



def read_file(file):
    #读取文件
    f = open(file, "r", encoding='utf_8')
    content = f.read(10)
    print(content)
def write_file(file, content):
    f = open(file, 'w', encoding='utf_8')
    f.write(content)
    f.close()


if __name__ == '__main__':
    file = r'D:\python_data_test\test1.txt'
    # read_file(r'D:\python_data_test\test1.txt')
    write_file(file, '很高兴')
    read_file(file)