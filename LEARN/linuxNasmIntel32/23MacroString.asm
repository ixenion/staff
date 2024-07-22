

; assign length of string to variable. sl=9
%strlen sl 'my string'

; extract specified symbol from string
%substr var1 'abcd' 1
%substr var2 'abcd' 2
%substr var3 'abcd' 3
; var1=a, var2=b, var3=c
; same as:
%define var1 'a'
%define var2 'b'
%define var3 'c'

; all macro processed before compilation




