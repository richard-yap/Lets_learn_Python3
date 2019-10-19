#------------------------------File operations---------------------------------
f = open("file.txt", "r") #reading a File
# "w" write File
# "a" append file

#teacher example:
f = open("test.txt", "w") # write or overwrite it
for i in range(10):
    f.write("This is line {}\n".format(i + 1)) #must write \n if not the text will keep going and going

# you have to do this in order to view the file as the file is still in yr RAM, do this
#and it will go to the hardisk
f.close()

# do it this way if you dw to forget to f.close()
with open("test.csv", "a") as f # this is to add more things to the file (appending)
for i in range(10):
    f.write("This is line {}\n".format(i + 1))

#if you want csv change it to .csv

#getting uniquue words
# save an article into article.txt first
f = open("article.txt), "r")
texr = f.read()

len(set(text.split()))
