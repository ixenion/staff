

;;;;;;;;;;;;;;;;;;;;;
;;;;; ADD ; SUB ;;;;;
;;;;;;;;;;;;;;;;;;;;;

; works both positive and negative nums

; add value stored at edx to eax & store into eax
add eax, ebx

; take 4byte number from x (x - is only an address) and substrct ecx value from it. Save to x address
sub [x], ecx

; increase edx by 12
add edx, 12

; increase 4byte memory cell ( x ) by 12
add dword [x], 12

; depends on result ADD and SUB set these flags:
; OF - Overflow Flag 
; CF - Carry Flag ( only for dual )
; ZF - Zero Flag
; SF - Sign Flag ( only for single )


;;;;;;;;;;;;;;;;;;;;;
;;;;; ADC ; SBB ;;;;;
;;;;;;;;;;;;;;;;;;;;;

; allow work with 64bit nums at 32b system
; example: add two 64b nums:
add eax, ecx	; eax - first number low 32b, ecx - second number low 32b
adc ebx, edx	; ebx - first number high 32b, edx - second number high 32b

; how it works (4bit):
;		|-------|------| -> 8bit number in 4bit system
; when adding	0001        1010 (16+10 in decml)
; and		0010        1001 ( 9 in decml)
; get	       	0100 <-+-(1)0011 (19 in decml)
; first add low bits of numbs & set CF, then add high bits taking into account CF (just adding it to high bits sum)
; left bit of low byte (fifth) represents CF
; and sub CF if operation is SUB


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; INC ; DEC ; NEG ; CMP ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; INC/DEC - increase/decrease by 1. Used only with register & memory type operands
; But may with address type. Need speify operand size (inc dword x)
; flags - ZF, OF, SF

; NEG - sign shift (from 7 to -7 & vice versa)
; flags - ZF, OF, SF , CF

; CMP - compare. Actually same as SUB, but result doesn't stored. Just for flags setting.
; jump commands usualy used next below CMP
