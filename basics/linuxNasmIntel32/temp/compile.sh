#!/bin/bash

# example:
# 01simple.asm <outputFile> <options>
#
# if <outputFile> is not speified - will be used input file name
#
# options:
# d - start delay (just don't start program immidatly after compilation)

echo "[*] Start Assembler..."
if [ $1 ]; then
	tempo=$(echo $1 | awk -F "." '{print$1}')".o"
	echo "    Temp (assembled) file be: "$tempo
	nasm -f elf32 -o $tempo $1
	echo "[*] Done"
	echo

	echo "[*] Start Linker..."
	if [ "$2" != "d" ] && [ -n "$2" ]; then
		outexe=$2
	elif [ "$2" = "d" ]  || [ -z "$2" ]; then
		outexe=$(echo $1 | awk -F "." '{print$1}')
	fi

	echo "    Linked output: "$outexe
	ld -m elf_i386 -o $outexe $tempo
	echo "[*] Done"
	echo
	echo $1
	echo $tempo
	echo $outexe
	echo

	if [ "$2" != "d" ] && [ "$3" != "d" ]; then
		echo "[*]              Start Binary..."
		echo "################################################"
		echo
		../bin/$outexe
	fi


		
else
	echo "No args. Need One at least"
fi
