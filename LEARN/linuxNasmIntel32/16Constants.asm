
; NUMBERS

; decimal - 10, 5, 99. Are by defaul
; hex - 2a3fh (add h), or 0x2a3f (add 0x), or $2a3f (add $) (but if num is f3a - $0f3a, add $0)
; binary 1101b
; octo - 634o (add o), or 754q (add q)
; 1 != 1.0	1.0=3f800000h=1065353216dec


; SYMBOL and STRING const

; symbol string <= dword (4bytes)
; 'abcd' or "abcd"
; 'abcd' = 64636261h: 64h=d, 63h=c e.h. In memory string reverced
