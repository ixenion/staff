
section .data
msg db "Hello world", 0xa
msglen equ $-msg
errmsg db "error", 0xa
errlen equ $-errmsg
ssmsg db "success"
sslen equ $-ssmsg

section .text
global _start

_start:
	mov edx, msglen
	mov ecx, msg
	mov ebx, 1
	mov eax, 4
	int 0x80

	cmp eax, 0
	jns success

error:
	mov edx, errlen
        mov ecx, errmsg
        mov ebx, 1
        mov eax, 4
        int 0x80
	jmp exit

success:
	mov edx, sslen
        mov ecx, ssmsg
        mov ebx, 1
        mov eax, 4
        int 0x80

exit:
	mov ebx, 0
	mov eax, 1
	int 0x80




