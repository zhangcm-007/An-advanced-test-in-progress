from operation_file import read_file

file = r'D:\python_data_test\test1.txt'

def test_read_file():
    assert read_file(file)
