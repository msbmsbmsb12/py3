from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want this, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w') # w 新建会覆盖原文件
#   以写模式 打开test.txt  
#   w代表写模式打开文件  
#   r代表读模式打开文件  
#   wr代表读写模式打开文件  
#   w+代表读写模式打开文件  
#   r+代表读写模式打开文件  
#   a+代表读写模式打开文件 

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close

# a+可读可写，追加内容；

# r+可读可写，覆盖内容；

# w+可读可写，情况内容，但是它的意义是可以边写边读啊，w只能写，不能读。

# 你可以直接执行下面的例子：

# f=open('testPythonFile.txt','w+')

# f.write('1234567890-')

# f.flush()

# f.seek(0)

# str= f.readline() #写完了，我还能读取

# print str

# f.close();