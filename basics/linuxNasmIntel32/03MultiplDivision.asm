
;;;;;;;;;;;;;;;;;;;;;;
;;;;; MUL ; IMUL ;;;;;
;;;;;;;;;;;;;;;;;;;;;;

; commands for multiplication
; MUL - for unsigned numbers
; IMUL - for signed numbers
; first operand - regiter type only. Also used as save point. May e used register pairs (couples, two) like DX:AX or EDX:EAX
; second opernd - register or memory ( [x] ) type
; AL - 1byte regiter, AX - 2byte, EAX - 4byte
; flags MUL & IMUL sets CF & OF to zero if high part o the result eql zero
; Other flags are not determined


;;;;;;;;;;;;;;;;;;;;;;
;;;;; DIV ; IDIV ;;;;;
;;;;;;;;;;;;;;;;;;;;;;

; DIV - unsigned division
; IDIV - signed div
; rounding: unsigned - down, signed - up.
; flags - not determined

;;;;;;;;;;;;;;;;;;
;;;;; SAVING ;;;;;
;;;;;;;;;;;;;;;;;;

; if both multipliers are 1byte:
; result saved to AX (2byte register)
; if 2byte multipls:
; result saved to DX:AX pair
; and so on...

; dividend - delimoe
; quotient ( of division) - chastnoe
; remainder ( of division ) - ostatok
; Fmultiplr - first multiplier ( register type only )

;---------------------------------------------------------------+
;     |	multiplication	   |	division			|
; bits+--------------------+--------------------------------	|
;     |	Fmultiplr | result |	dividend | quotient | remainder |
;-----+--------------------+------------------------------------|
; 8   |	AL	    AX	   |	AX	   AL	      AH	|
; 16  |	AX	    DX:AX  |	DX:AX	   AX	      DX	|
; 32  |	EAX	    EDX:EAX|	EDX:EAX	   EAX	      EDX	|
;---------------------------------------------------------------+


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; termination error ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

div ax, [x]	; where !x = 0! & ax - any
; or
div ax, [y]	; where y = 2 & !ax = 2^36!
