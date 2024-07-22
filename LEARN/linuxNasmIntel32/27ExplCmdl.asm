; conditional compilation used
; Linux		$nasm -f elf -dOS_LINUX 27ExplCmdl.asm
; FreeBSD	$nasm -f elf -dOS_FREEBSD 27ExplCmdl.asm


section .text
global _start	; must be declared for linker (ld)

strlen:		; arg1 == address of the string
	push ebp
	mov ebp, esp
	push esi
	xor eax, eax
	mov esi, [ebp+8]	; arg1
.lp:	cmp byte [esi], 0
	jz .quit
	inc esi
	inc eax
	jmp short .lp
.quit:	pop esi
	pop ebx
	ret

newline:
	pushad
%ifdef OS_FREEBSD
	push dword 1
	push dword .nwl
	push dword 1	; stdout
	mov eax, 4	; write
	push eax
	int 0x80
	add esp, 16
%elifdef OS_LINUX
	mov edx, 1
	mov ecx, .nwl
	mov ebx, 1
	mov eax, 4
	int 0x80
%else
%error define either OS_FREEBSD or OS_LINUX
%endif
	popad
	ret
.nwl db 10

_start:			; tell linker entry point
	mov ecx, [esp]
	mov esi, esp
	add esi, 4
again:	push dword [esi]
	call strlen
	add esp, 4
	push esi
	push ecx
%ifdef OS_FREEBSD
	push eax
	push dword [esi]
	push dword 1	; stdout
	mov eax, 4
	push eax	; write
	int 0x80
	add esp, 16
%else
	mov edx, eax
	mov ecx, [esi]	; arg1
	mov ebx, 1
	mov eax, 4
	int 0x80
%endif
	call newline
	pop ecx
	pop esi
	add esi, 4
	loop again

%ifdef OS_FREEBSD
	push dword 0
	mov eax, 1	; _exit
	push eax
	int 0x80
%else
	mov ebx, 0
	mov eax, 1
	int 0x80
%endif
	
