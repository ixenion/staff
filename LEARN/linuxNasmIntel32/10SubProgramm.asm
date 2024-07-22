
; CALL ; RET

; call - works as jump but with subprogramms. Arguments are: label, register or memory.
; call have only on form - near (nor short nor far)
; ret - return from subprogram
; ret work - reads 4 bytes from stack top & stores them at EIP (instrution pointer)

; example
; fill memory (edi=address, ecx=length, al=value)
fill_memory:
	jecxz fm_q
fm_lp:	mov [edi], al
	inc edi
	loop fm_lp
fm_q:	ret


; to appeal obratit'sa this code (function?)
mov edi, my_array
mov ecx, 256
mov al, '@'
call fill_memory
