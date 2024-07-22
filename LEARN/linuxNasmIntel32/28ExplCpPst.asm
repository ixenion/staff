
%macro syscall 1-*
%rep %0			; %0 - macro params counter
%rotate -1		; rotate to the right by 1. Last becomes first
	push dword %1
%endrep
%ifdef OS_FBSD
	mov eax, [esp]	; why ?. eax be rewriten by next interrupt
	int 80h
	jnc %%sc_ok
	neg eax
%%sc_ok:
	add esp, (%0-1)*4
%elifdef OS_LINUX
	pop eax
  %if %0 > 1
	  pop ebx
    %if %0 > 2
	    pop ecx
      %if %0 > 3
	      pop edx
	%if %0 > 4
		pop esi
	  %if %0 > 5
		  pop edi
	    %if %0 > 6
		    %error "Too many params for Linux syscall"
	    %endif
	  %endif
	%endif
      %endif
    %endif
  %endif
	int 80h
%else
%error Please define either OS_FBSD or OS_LINUX
%endif
%endmacro


; now HELLO WORLD be like:

; section .data
; msg db "Hello world", 10
; msg_len equ $-msg
; section .text
; global _start
; _start: syscall 4, 1, msg, msg_len
; 	  syscall 1, 0




section .bss
buffer	resb 	4096		; copy/past by batches of 4096 byte each
bufsize equ 	$-buffer	; bufer size
fdsrc 	resd 	1		; file descriptor source
fddest 	resd 	1		; file descriptor destination
argc	resd	1		; stores number of params of this whole programm
argvp	resd	1		; stores address of array full of points at these programm params
				; all these variables don't need initial values, thus may be stored at bss section
section .data
helpmsg db 'Usage: copy <src> <dest>', 10
helplen equ $-helpmsg
err1msg db "Couldn't open source file for reading", 10
err1len equ $-err1msg
err2msg db "Couldn't open destination file for writing", 10
err2len equ $-err2msg

section .text
global _start
_start:
	pop dword [argc]
	mov [argvp], esp
	cmp dword [argc], 3
	je .args_count_ok
	syscall 4, 2, helpmsg, helplen
	syscall 1, 1
.args_count_ok:
	mov esi, [argvp]	; Start open source file
	mov edi, [esi+4]
	syscall 5, edi, 0	; O_RDONLY - source file descriptor (here=0)
	cmp eax, 0
	jge .source_open_ok
	syscall 4, 2, err1msg, err1len
	syscall 1, 2
.source_open_ok:
	mov [fdsrc], eax	; End open source file. Save source file descriptor
	mov esi, [argvp]	; Start open destination file
	mov edi, [esi+8]
%ifdef OS_LINUX
	syscall 5, edi, 241h, 0666o	; 666 rw- (?) 
%else					; assume it's FBSD
	syscall 5, edi, 601h, 0666o
%endif
	cmp eax, 0
	jge .dest_open_ok
	syscall 4, 2, err2msg, err2len
	syscall 1, 3
.dest_open_ok:
	mov [fddest], eax

.again: syscall 3, [fdsrc], buffer, bufsize
	cmp eax, 0
	jle .end_of_file
	syscall 4, [fddest], buffer, eax
	jmp .again

.end_of_file:
	syscall 6, [fdsrc]
	syscall 6, [fddest]
	syscall 1, 0

