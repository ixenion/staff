
; Coputations which are made at assembling stage


; allowed operations:
; sorted by prior (from high to low). order may changed by "()"

; unary operations: "-"&"+" and "~"; then * /(%) //(%%);then "+"&"-"; then <<, >>, &, ^, finaly |
; unary "-" : shift sign symbol; "+" does nothing
; * : multipliation; / ( or %) division for unsigned, // for signed
; "+", "-" : addition and subtraction
; << bit shift to the left, >> to the right
; & bit operation "and"
; ^ xor
; | or


mov eax, label		; wrong
label:	...

mov eax, dword label	; right
label:	...




; expressions as part of the executive address

mov eax, [5*ebx]
mov eax, [ebx+4*ecx+5*x+y]



