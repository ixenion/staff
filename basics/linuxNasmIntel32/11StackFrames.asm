

; when subbprogramm has some local variables theere is a problem of storing them
; to enter subprocess:
push ebp		; push ebp value to esp (stack pointer). To not to loose ebp data
mov ebp, esp		; mov esp top to ebp, so return address (from subprocess) be [ebp+4]. 4 - couse 32bit system (32b=4bytes)
			; thus we freeded esp and may use it as stack pointer again.
sub esp, 16		; reserve 16 bytes (not bits) as local variable

; to leave subprocess:
mov esp, ebp
pop ebp
ret



; alias:
; to enter:
enter 16, 0
; to return:
leave
ret

; advantage of these aliases - use less memory
; disadvantage - slower compare to push/mov/sub


