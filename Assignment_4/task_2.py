file1 = open('output.txt','a')

writing_file = file1.write('Learning file handling in Python. \n')
print(writing_file)
file1.close()

file1 = open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()