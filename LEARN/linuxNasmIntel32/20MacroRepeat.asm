
; rep - repetition
; endrep - exit rep
; exitrep - brake rep ahead of schedule

; example
db 50
db 51
db 52
; ...
db 148
db 149
; or
%assign n 50
%rep 100
	db n
%assing n n+1
%endrep


; example 2.
fibonacci
	%assign i 1
	%assign j 1
	%rep 100000
	  %if j > 100000
	   %exitrep
	  %endif
	
	  dd j
	
	  %assign k j+i
	  %assign i j
	  %assign j k
	%endrep
fib_count equ ($-fibonacci)/4


; example 3.1
array resw 128
%assign a array
%rep 128
	inc word [a]
%assign a a+2
%endrep

; example 3.2
	mov ecx, 128
lp:	inc word [array + ecx*2 -2]
	loop lp

; 3.1 - faster, uses more memory
; 3.2 - slower (~1.5), uses less memory

%rep %0 (?)
