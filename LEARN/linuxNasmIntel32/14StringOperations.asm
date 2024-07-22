
; to simplify array's operations exist string operations
; these are the commands that uses edi & esi registers
; these commands use DF flag.	if DF=0 - memory direcion is from left to right (address increase)
;				if DF=1 - memory diretion is from right to left (address decrase)

; DF may be set by STD (set direction) & reset by CLD (clear direction)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; STOSB ; STOSW ; STOSD ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; STOSB - fill in address (byte) stored at edi with value stored at AL register & increase edi by 1
; STOSW - word, AX, edi+2
; STOSD - dword, eax, edi+4

; example

buf resb 1024

xor al, al
mov edi, buf		; array's start address
mov ecx, 1024		; length of the array
cld			; work in the forward direction
lp:	stosb		; al -> edi, inc edi
	loop lp

; another useful command - REP
; instead of:
lp:	stosb
	loop lp
; may be:
rep stosb
; command stosb will be repeated as many times as ecx value


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; LODSB ; LODSW ; LODSD ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; LODSB - reads byte stored at esi address & put that into AL
; LODSW - word, ax
; LODSD - dword, eax

; useless:
rep lodsb
; rep repeats only first command?

; example. comput sum of array's elements

array resd 256

xor ebx, ebx		; sum storage
mov esi, array
mov ecx, 256
cld
lp:	lodsd
	add ebx, eax
	loop lp


; lods + stos example. inrease all array's elements y one

array resd 256

	mov esi, array
	mov edi, esi
	mov ecx, 256
	cld
lp:	lodsd
	inc eax
	stosd
	loop lp


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; MOVSB ; MOVSW ; MOVSD ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; movsb - copy byte from address stored at esi to edi & inc [esi] and [edi]
; movsw - word
; movsd - dword

; example:

buf1 resb 1024
buf2 resb 1024

mov ecx, 1024
mov esi, buf1
mov edi, buf2
cld
rep movsb

; example2 partially overlapped memory. From strings "This is a string" and "long" make one string "This is a long string"
; buf1 contains frase: "This is a string", buf2 contains "long".

std			; set reverse direction (from high to low memry address)
mov edi, buf1+17+5	; set last symbol address which will get after insert
mov esi, buf1+17
mov ecx, 8
rep movsb		; shift "string" word to the right
mov esi, buf2+4
mov ecx, 5
rep movsb


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; cmpsb, cmpsw, cmpsd - compare [esi] with [edi] and set appropriate flags and inrease/decrease esi & edi
; scasb, scasw, scasd - compare eax|ax|al with db|dw|dd [edi] and set appropriate flags like cmp and inc/dec edi
; suitable prefixes - repz(=repe) & repnz(=repne). Apart dec ecx and check ecx=0 (or cx=0) also check ZF
; repz - continue if ZF=1
; repnz - continue if ZF=0

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; for signed numbers
; cbw - extend number from al to ax (fill in ah with sign bit)
; cwd - extend ax to dx:ax
; cwde - ax to eax
; cdq - eax to edx:eax

; movsx - move signed extension & movzx - move zro extension
; allows to combine copying with increasing bit depth.
; movsx - fills in missinng bits with sign bit
; movzx - with zero

; nop - no operation

