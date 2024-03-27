
; psedocommands
; db, dw, dd, dq, dt resb, resw, resq, rest...
; q - "quadro" 8 bytes, t - "ten" 10 bytes element

; float number: usual exactness (dd), double exactness (dq), extended exactness (dt)

; EQU
; makes constants
four equ 4
mov eax, four
; equal to
mov eax, 4

; get array length
msg db "Hello", 10, 0
msglen equ $-msg		; "$" minus msg. msg - start address. $ - current address right after line above
; value $-msg will be calulated right at assembling


; TIMES
; set 4096 bytes with '*'
stars times 4096 db '*'


; INCBIN
; copy files from external file

