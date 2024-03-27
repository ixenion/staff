global _start

section .text
_start

	mov eax, 0x4
	mov ecx, 1
	mov ecx, output1
	mov edx, output1_length
	int 0x80

	; grasefully exit
	mov eax, 0x1
	mov edx, 0
	int 0x80

section .data
	output1 db "[memcell]", 0xA
	output1_length equ $-output1


section .bss
	memcell resd 2

