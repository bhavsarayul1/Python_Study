# read txt file and print content line by line

fh = open("sample1.txt","rt")
data = fh.read()
fh.close()
print(data)
print("_"*30)

# Error handling if file not exist
try:
    fh = open("sample.txt","rt")
    data = fh.read()
    fh.close()
except FileNotFoundError as file_error:
    print(f"The file {fh.name} was not found")
