CSEG segment
org 100h

Begin:
	
	mov ah,9
	mov dx,offset Message
	int 21h

	int 20h

Message db 'Hello world!$'
CSEG ends
end Begin







