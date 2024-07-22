

; main concept - LIFO - last in first out

; PUSH - push th evalue (have only on operand) to the stack.
; only word & dword may be pushed.
; Operand type - register, memory and dirrect number.
push eax
push word [x]
push dword [y]
push word 42
push dword 42000000

; Retreave value with
; POP
; Operand type - register or memory
push eax
; do some staf
pop eax

; pop and push retreaves/push value from stack top and shifts that top (ESP - stack pointer)
; to retreave value without ESP shifting:
mov eax, [esp]


; example
; there is symbolic string in memory with random length. last byte=0
; need to reverce and write to the same memory location it using stack
; 0 byte stays still (at thee and)

	xor ebx, ebx
	xor ecx, ecx
lp:	mov bl, [esi+ecx]	; esi - source index (index to stored string)
	cmp bl, 0		; check if this is the end?
	je lpquit		; if yes - jump
	push bx
	inc ecx
	jmp lp
lpquit:	jecxz done		; if string is empty - quit
	mov edi, esi		; edi - destination index
lp2:	pop bx
	mov [edi], bl
	inc edi
	loop lp2
done:



; addition
;;;;; PUSHAD ; POPAD ;;;;;
; these commands stores at stack following flags:
; EAX ECX EDX EBX ESP EBP ESI EDI
; right exact order (first eax then ecx)


