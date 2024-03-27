
; 2 params
%macro pcall1 2		; 2 - param number
	push %2
	call %1
	add esp, 4
%endmacro
; usage
pcall1 proc, eax
; in result we get
push eax
call proc
add esp, 4

; 3 param
%macro pcall2 3
	push %3
	push %2
	call %1
	add esp, 8
%endmacro

; 4 params
%macro pcall3 4
	push %4
	push %3
	push %2
	call %1
	add esp, 12
%endmacro

; 0 args
%macro pcall0 1
	call %1
%endmacro


; single line macro:
%define arg1 ebp+8
%define arg2 ebp+12
%define arg3 ebp+16
%define local1 ebp-4
%define local2 ebp-8
%define local3 ebp-12

%define arg(n) ebp+(4*n)+4
%define local(n) ebp-(4*n)
; usage
mov eax, [arg1]
mov [arg(7))], edx
; rid off []
%define arg1 [ebp+8]
; usage
mov eax, arg1




; macro in macro. Lazy

%define thenumer 25
%define mkvar dd thenumber
var1 mkvar
; var1 dd thenumber
; var1 dd 25
%define thenumber 36
var2 mkvar
; var2 dd thenumer
; var2 dd 36

; macro in macro. Energetic
%define thenumber 25
%xdefine mkvar dd thenumber
var1 mkvar			; var1 dd 25
%define thenumber 36
var2 mkvar			; var2 dd 25. NOT 36


; sngle line macro with computaton
%define thenumber 41
%assign var thenumber+1


