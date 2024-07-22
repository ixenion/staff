
%macro mymacro 1-3
; or
%macro mysecondmacro 2-*

%rotate 1		; rotate to the left by 1
%rotate -1		; rotate to the right by 1


; example:
%macro pcall 1-*
  %rep %0 - 1
    %rotate -1		; rotate to the right by 1
      push dwort %1
  %endrep
  %rotate -1
	call %1
	add esp, (%0 - 1) * 4
%endmacro

; usage:
pcall myproc, eax, myvar, 27

; substitution podstanovka result
push dword 27
push dword myvar
push dword eax
call myproc
add esp, 12





