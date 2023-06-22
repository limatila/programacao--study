import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

#if in VScode it will check the current workspace values, not the folder it's in to(because off current directory set values in cmd)