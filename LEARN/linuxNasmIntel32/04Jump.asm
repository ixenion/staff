
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; Unconditional Jumps ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; There are 3 jump types:
; FAR - to the different segment ( flat memory model currently used, it mans that there is only one segment, so no need for FAR jump)
; NEAR - transferring control to an arbitrary (proizvolnoe) location within (v predelah) a single segment
; It changes EIP flag.
; SHORT - jump 127 bytes ahead & 128 bytes backward. Address shift defined by single byte, herewhy this restric

; defaults
; near - default for unconditional jumps
; short - default for conditional jumps


;;;;;;;;;;;;;;;
;;;;; JMP ;;;;;
;;;;;;;;;;;;;;;

jmp cycle	; jump at "cycle" mark (label)
jmp eax		; at addr stored in eax
jmp [addr]	; jump at addres which stored into "addr" mark
jmp [eax]	; jump address stored at addr which contains eax

; example
label:
	;
	; some commands
	;
	jmp short label


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; Conditional Jumps ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;---------------------------------------------------------------------------------+
;cmnd		      |	jz    |	js    |	jc    |	jo    |	jp    |	jnz   |	& so on...|
;transition condition |	ZF=1  |	SF=1  |	CF=1  |	OF=1  |	PF=1  |	ZF=0  |		  |
;---------------------------------------------------------------------------------+

; usualy used after math:
cmp eax, ebx
jz are_equal

; example: check a < b
; first use cmp a, b
; for SIGNED nums
; equation is true if SF=1 & OF=0 or SF=0 & OF=1
; can check that by jl jump
;
; for UNSIGNED nums
; check for CF and jump by jc, jb, jnae (all same)

;;;;;;;;;;;;;;;;;;;;;
;;;;; JL ; JNGE ;;;;;
;;;;;;; SIGNED ;;;;;;
;;;;;;;;;;;;;;;;;;;;;

; used with signed numbers
; jl - jump if less than
; jnge - jump if not greater or equal
; both commands are same

; thus can check a < b
cmp a, b
jl is_less
; or
jnge is_less


;;;;;;;;;;;;;;;;;;;;;
;;;;; JB ; JNAE ;;;;;
;;;;;; UNSIGNED ;;;;;
;;;;;;;;;;;;;;;;;;;;;

; JB - jump if below
; JNAE - jump if not above or equal
; both are same + jc

; to check a < b
cmp a, b
jb is_less


;-----------------------------------------------+
; cmd	jump if...	exprsn	condtn	synonym |
;-----------------------------------------------|
; je	equal		a=b	ZF=1	jz	|
; jne	not equal	a!=b	ZF=0	jnz	|
;-----------------------------------------------|
;		signed numbers only		|
;-----------------------------------------------|
; jl	less					|
; jnge	NtGrater|eql	a<b	SF!=OF		|
;						|
; jle	less|eql	a<=b	SF!=OF		|
; jng	NtGrater		or ZF=1		|
;						|
; jg	greater		a>b	SF=OF		|
; jnle	NtLess|eql		& ZF=0		|
;						|
; jge	greater|eql	a>=b	SF=OF		|
; jnl	not less				|
;-----------------------------------------------|
;	      unsigned numbers only		|
;-----------------------------------------------|
; jb	below		a<b	CF=1	jc	|
; jnae	NtAbove|eql				|
;						|
; jbe	below|eql	a<=b	CF=1		|
; jna	NtAbove			| ZF=1		|
;						|
; ja	Above		a>b	CF=0&ZF=0	|
; jnbe	NtBlw|eql				|
;						|
; jae	Above|eql	a>=b	CF=0	jnic	|
; jnb	NtBlw					|
;-----------------------------------------------+


