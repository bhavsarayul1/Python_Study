# create new file name as output.txt

fh = open("output.txt","wt")
fh.write("Hello World")
fh.close()

#append additional data from user input

user_input = input("Enter about yourself:  \n")

fh = open("output.txt","at")
fh.write("\n"+user_input)
fh.close()
fh.close()
fh = open("output.txt","at")
fh.close()

# read and display final content of line

fh = open("output.txt","rt")
content = fh.read()
fh.close()
print(content)

