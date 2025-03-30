try:
    file1 = open('sample.txt', 'r')
    reading_file = file1.read()
    print(reading_file)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
finally:
    if 'file1' in locals() and not file1.closed:
        file1.close()