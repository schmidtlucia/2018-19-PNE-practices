# Example of reading a file located in our local filesystem

Name = 'mynotes.txt'

# Open the file
myfile = open(Name, 'r')

# myfile is an object, not a variable

print('File opened: {}'.format(myfile.name))

contents = myfile.read()

print('The file contents are: {}'.format(contents))

myfile.close()

f = open(Name, 'a')
f.write('THIS IS A TEXT EXAMPLE FOR ADDING TO MYFILE')
f.close()
print('The end')