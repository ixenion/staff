
# f key
nasm -f elf
# without 'f' otput file will be just commands in binary, NOT machine commands. That ile couldn't be started
# so called RAW format
# it could be usefull when want to locate programm at boot sector of the disk

# o key
# specifies output file name. By default same as input

# d key
# conditional ompilation
# anther way to use:
nasm -dSIZE=1024
# dSIZER=1024 except o defying 'SIZE' symbol also adds param 1024
# analg:
%define SIZE 1024

# l key
# listing key. shows what memory (cells?) were used.
nasm -f elf -l prog.lst prog.asm

# g key
# force nasm to inlude debug info.
# It adds to .o file information such as: source code name, string number etc
# Helpful when working with step by step debugger "gdb"

# e key
# drive all code through macroprcessor & print result on the screen and nothing else.
# useful for macro debug




