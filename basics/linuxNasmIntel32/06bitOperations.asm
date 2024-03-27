
;	LOGIC OPERATIONS

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; AND ; OR ; XOR ; NOT ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; byte per byte operatins
and al, bl	; and bits stored at "al" with bits in "bl"
; same for OR, XOR
not eax		; Not has only one operand. Works only with register or memory type operands
not dword [number]	; With memory type length must be specified.
; all these commands sets ZF, SF, PF according to the result.
; usualy only ZF used.


; NOTE
; very often instead of
mov eax, 0
; may find
xor eax, eax
; because mov takes 5 machine  commands
; and xor only 2
mov eax, -1	; 5 machine commands
; equal to
xor eax, eax	; 2 machine commands
not eax		; 2 machine commands

; to check i the result is = 0
; instad of:
cmp eax, 0
; used
test eax, eax	; takes less memory. faster.


;	SHIFT OPERATIONS
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; SHR ; SHL ;
;;;;;;;;;;;;;;


