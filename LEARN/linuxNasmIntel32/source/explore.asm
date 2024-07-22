
; macro to simplify system calls

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



section .data
err1msg db "error", 10
err1len equ $-err1msg
succmsg db "success", 10
succlen equ $-succmsg

;msg db "H"
;msg dd 0x44444422
;msglen equ $-msg


section .bss
msg resd 1
msglen equ 5	; in bytes

section .text
global _start
_start:
	nop		; 90
	nop
	nop
	nop
	;xor eax, eax	; 31c0
		
	
	nop
	nop
	nop
	nop

	;mov eax, dword 0x33333333
	;mov [msg], esp
	;mov [msg], dword 0x33334444
	;mov eax, msg
	;add eax, dword 0x1
	;mov msg, eax
	
	;add msg, dword 0x1
	mov dword [msg+4], 0xa

	syscall 4, 1, msg-8208, msglen
	cmp eax, 0
	jns success
error:
	syscall 4, 1, err1msg, err1len
	jmp exit
success:
	syscall 4, 1, succmsg, succlen
exit:
	syscall 1, 0

