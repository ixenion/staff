
; this is comment

global _start

; define the sections that are neccessary
; for this assembly program to run
section .text:
_start:
; see syscall (system call) codes at:
; unistd_32.h (/usr/include/x86_64-linux-gnu/asm/unistd_32.h)
; using intel syntaxis?
	mov eax, 0x4		; use the write syscall
	mov ecx, 1		; use stdout as the fd (file desriptor)
	mov ecx, message	; use the message as the buffer
	mov edx, message_length	; and supply the length
	int 0x80		; invoke the syscall (run). "int" - interrupt

	; now grasefully exit
	mov eax, 0x1		; use the exit syscall
	mov ebx, 0		; return 0
	int 0x80


; create variable
section .data:
	; variable "message". "db" - define bites. "Hello world" - define string. 0xA - new line caracter
	message: db "Hello world!", 0xA
	; equ means "equal to"
	message_length equ $-message

; to compile:
; nasm -f elf32 -o helloworld.o 01helloworld.asm
; make it executable;
; ld -m elf_i386 -o helloworld helloworld.o

