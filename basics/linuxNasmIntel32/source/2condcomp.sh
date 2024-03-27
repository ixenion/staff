
echo "[*] Start"

if [ $1 ]; then
	temp=$(echo $1 | awk -F "." '{print$1}')
	nasm -f elf32 -dOS_LINUX $1
	echo "    nasm done"
	ld -m elf_i386 -o $temp $temp".o"
	echo "    ld done"
	echo "[*] Done"
else
	echo "Usage: $ 2condcomp.sh <if>"
fi
