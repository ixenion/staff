
; used when there are 2 slightly defferent copies of one programm
; and when found error in one neeed to correct both copies.
; conditional compilation resolves this problem

; example
; debug information

%ifdef DEBUG_PRINT
	PRINT "Entering suspicious section"
	PUTCHAR 10
%endif
;
;	suspicious secction
;
%ifdef DEBUG_PRINT
	PRINT "Leaving suspicious section"
	PUTCHAR 10
%endif

; ifdef - conditional compilation derrective
; it will work (print debug info) only if speify at hte top:
%define DEBUG_PRINNT
; so get next code:
%define DEBUG_PRINT
%ifdef DEBUG_PRINT
        PRINT "Entering suspicious section"
        PUTCHAR 10
%endif
;       suspicious secction
%ifdef DEBUG_PRINT
        PRINT "Leaving suspicious section"
        PUTCHAR 10
%endif


; another way to include cond comp is:
; nasm -f elf -dDEBUG_PRINT prog.asm
; add -dDEBUG_PRINT


; TWO CUSTOMERS
%ifdef FOR_JOHN
;	code part only for John
%elifdef FOR_SAM
;	code part only for Sam
%else
;	if neither John or Sam
;	stop compilation and print error
%error Please define either FOR_JOHN or FOR_SAM
%endif

; opposit of "ifdef" is "ifndef"
; if -dNOT_INCLUDE "ifndef" won't include
; for "elifdef" is "elifndef"



; ifidn - 2 args, compare them as strings, proceed if full equal
%ifidn arg1, arg2
;some stuff
%endif

; ifidni - allow partual equation like:
; foobar, Foobar, FOOBAR are equal
; Both have
; ifnidn, ifnidni
; elifidn, elifidni, elifnidn, elifnidni

; ifmacro - checks is there multiline macros
; have
; ifnmacro, elifmacro, elifnmacro

; ifid - checks is arg a identificator
; ifstr - is arg a string
; ifnum - is arg a number

; ifctx - too difficult

