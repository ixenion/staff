

; macro
%macro zeromem 2	; two params: 1-address & 2-length
	push ecx
	push esi
	push dword %2
	push dword %1
	pop esi
	pop ecx
%%lp:	mov byte [esi], 0
	inc esi
	loop %%lp
	pop esi
	pop ecx
%endmacro



; usage:
section .bss
array resb 256
arr_len equ $-array

section .text
; ...
	mov ecx, array
	mov esi, arr_len
	zeromem ecx, esi
; ...

; zeromem ecx, esi would be:


