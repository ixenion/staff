
; Need to create variables with same name


funtion_1:
	.localVariable
function_2:
	.localVariable

; How it works:
; when assemler sees "." It just adds previous label.

; so it will be:
; function_1.loalVariable
; and
; function_2.localVariable

