; specify and fill in array with "@" symbol


global _start

section .bss
array resb 256	; 256 bytes array

section .text
_start
	mov ecx, 256	; the number of elements to the counter ecx
	mov edi, array	; array addr to edi
	mov al, '@'	; symbol to the single byte AL reg
again:  mov [edi], al	; get symbol to the address
	inc edi		; inrement address
	dec ecx		; decrease counter
	jnz again	; if ecx!=0 - repeat cycle
	

	mov eax, 0x01
	mov ebx, 0
	int 0x80
