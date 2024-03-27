
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; LOOP ; JCXZ ; JECXZ ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; LOOP is short jump
; it decrements ecx register counter
; and jump at label specifyed if ecx!=0
; JCXZ jump if CX=0 without decrementing it
; JECXZ jump if ECX=0 without decrementing it


; example.
; Summ of 1000 random numbers from "array" var

global _start		; init start ?

section .bss		; define reserve section
array resd 1000		; reserve 1000 addresses for "array"

section .text		; define command section
_start			; def programm start ?
	mov ecx 1000	; use ecx as counter. Goes from 1000 to 1
	mov esi, array	; set first addr of "array" to esi reg. esi - source index (also si) used for copy/paste
	mov eax, 0	; set sum to 0
lp:	add eax, [esi]	; loop start. add content of address stored at esi to eax.
	add esi, 4	; inrease address counter by 4 , because double word are used (array resd 1000).
	loop lp		; loop - special jmp works with ecx reg only by decr ecx by 1 and if ecx!=0 - jump at label

	mov eax, 0x01	; graeful
        mov ebx, 0	; exit
        int 0x80



; loop analog may be like:
; dec eax	| which obviously longer
; jnz lp	| and takes more clock counts
;

; or without esi
;
;	mov ecx, 1000
;	mov eax, 0
;lp:	add eax, [array+4*ecx-4]  ; Goes from 999 to 0. Must be only one summand, but at translation stage assembler does array-4.
;	loop lp
;
; here we go from the end of "array", not from top


;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ******************* ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;

;	; fill in ecx
;	jecxz lpq	; check if ecx is already = 0. and pass "lp" cycle if it is. Or lp would be processed 2^32 times
; lp:	; some cycle
;	; ...
;	loop lp
; lpq:
;	; other cycle


;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; LOOPE ; LOOPNE ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;

; LOOPE = loopz - jump if ecx!=0 & ZF=1
; LOOPNE = loopnz - jump if ecx!=0 & ZF=0
