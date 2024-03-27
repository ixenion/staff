# stdout & stderr

ls -la 1>file1.txt 2>file2.txt
#      result      errors


# make one file to store stdout & stderr
ls -la >file3.txt 2>&1



