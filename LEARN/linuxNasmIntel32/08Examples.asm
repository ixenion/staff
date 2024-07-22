
; 16 elements (from 0 to 15) each element has 32 bits (512 units total)
; units are numbered in order (0,1,2,3,...,45,...,251...511)
; problem - convert unit number to element with it's bit (arrays?)

; prepare example
; same problem but with 256 units instead of 512
mov dx, bx
and bx, 11111b
shr dx, 5
mov bh, dl
; or shorter:
shl bx, 3	; now bh has quotient
shr bl, 3	; and bl has remainder

; return to the problem:
section .bss
set512 resd 16	; dword = 32bits

section .text
; fill reserved space with 0
	xor eax, eax	; eax :=0
	mov ecx, 15
	mov esi, set512
lp:	mov [esi+4*ecx], eax
	loop lp

; Set (make bit=1) particular unit at set512
; let X stored at ebx
	mov cl, bl		; store bit number at CL
	and cl, 11111b		; purge of 3 high bits of CL
	mov eax, 1		; set eax := 1
	shl eax, cl		; create mask
	mov edx, ebx		; store ebx value to edx
	shr edx, 5		; and divide it by 32 just shifting to the right
	or [set512+4*edx], eax	; apply mask

; Reset (make bit=0) particular unit at set512
	mov cl, bl
	and cl, 11111b
	mov eax, 1
	shl eax, cl
	not eax
	mov edx, ebx
	shr edx, 5
	or [set512+4*edx], eax

; Check particular unit at set512 (bit0|1)
	mov cl, bl
	and cl, 11111b
	mov eax, 1
	shl eax, cl
	mov edx, ebx
	shr edx, 5
	test [set512+4*edx], eax	; if ZF=0 - unit missing (=0), ZF=1 - unit present (=1)

; Count how many units are =1
	xor ebx, ebx		; ebx:=0
	mov ecx, 15		; ecx as counter
lp:	mov eax, [set512+4*ecx]	; load element (0-15)
lp2:	test eax, 1		; check if low bit = 1 ?
	jz notone		; if not - jump
	inc ebx			; if yes - increase oneCounter
notone:	shr eax, 1		; shift eax
	test eax, eax		; check does eax contain anything exept zero
	jnz lp2			; if yes - jump
	jecxz quit		; if ecx=0 - exit
	dec ecx			; if not - decrease by one
	jmp lp			; and continue lp cycle
quit:				; now have number of ones at ebx





