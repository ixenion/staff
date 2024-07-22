# MEMORY ADDRESS

section .data
count dd 0			; create variable "count". The name "count" is memory address.

section .text
_start
	mov [count], eax	; move value from eax to count var
	mov edx, [count]	; from count to edx register
	int 0x80		; again. count - address (40f2a008), [count] - value stored at 40f2a008 (0)
	
	mov ebx, [eax]		; use eax as address & go to memory with this address & and take val stored at this adr & save it in ebx
	
	;copy/past like this:
	mov eax, [x]
	mov [y], eax
	; but not like this:
	mov [y], [x]

	; assign value to var
	mov [x], dword 25
	; or
	mov dword [x], 25
	; but not like this. error
	mov [x], 25

	; calculate memr addr without address conversation (obrashenie)
	lea eax, x	; mov x addr to eax. x - marker (mark)
	lea eax, [1000+ebx+8*ecx]

	; grasefully exit	
	mov eax, 0x1
	mov ebx, 0
	int 0x80


;	INTEGER ARITHMETIC (celochislennaya)
mov eax, ebx	; eax + ebx | stored at eax (first summand)
sub [x], ecx	; for example x = 5 (mov [x], 5). 5 - ecx | x=x-ecx (stored at x addr)
add dword [x], 12
; flags used
; when ans (answer)
; ans = 0 - ZF=1
; ans > 0 - SF=0
; ans < 0 - SF=1
; ans overflow - OF=1 (no mean to unsign numbers)
; ans int overflow CF=1 (no meaning to sigh numbers)

add eax, ecx	; add low parts
adc edx, ebx	; add high parts taking into account CF
; adc then sets CF according it's result
; same with substraction
sub eax, ecx
sbb edx, ebx

