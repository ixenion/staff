

; assembller

match:				; subprogram start
	push ebp		; init stack frame
	mov ebp, esp		
	sub esp, 4		; local variable I, will be at [ebp-4] address

	push esi		; save esi & edi regiters
	push edi
	mov esi, [ebp+8]	; load params: string address
	mov edi, [ebp+12]	; pattern address
.again:				; here we return when another symol be collated sopostavlen
	cmp byte [edi], 0	; does pattern end?
	jne .not_end		; jump if not
	cmp byte [esi], 0	; pattern end but does string?
	jne near .false		; if not - return false
	jmp .true		; if ends simultaneusly - return true
.not_end:			; if pattern not ended
	cmp byte [edi], '*'	; is it a star at start?
	jne .not_star		; jump if not
	mov dword [ebp-4], 0	; if yes - start cycle. I := 0
.start_loop:
	mov eax, edi		; prepare to recurs
	inc eax			
	push eax
	mov eax, esi
	add eax, [ebp-4]
	push eax
	call match		; recursion

	add esp, 8		; clear stack after recursion
	test eax, eax		; check what was returned
	jnz .true		; if != 0 (e.i. true) return true
	add eax, [ebp-4]	; if = 0 - need count more symbols on that star
	cmp byte [esi+eax], 0	; but the string may be over?
	je .false		; if = 0 the there is nothing to do
	inc dword [ebp-4]	; else try I := I+1
	jmp .start_loop		; and again

.not_star:
	mov al, [edi]
	cmp al, '?'
	je .quest
	cmp al, [esi]		; if it's not '?' compare two symbols
	jne .false		; if not equal - .false
	jmp .goon		; if equal - continue
.quest:				; pattern symbol is '?' ?
	cmp byte [esi], 0	; only need check that string not over
	jz .false
.goon:
	inc esi
	inc edi
	jmp .again
.true:
	mov eax, 1
	jmp .quit
.false:
	xor eax, eax		; return false
.quit:
	pop edi
	pop esi
	mov esp, ebp
	pop ebx			; result at eax
	ret			; procedure end


; call
push dword pattern
push dword string
call match
add esp, 8






; C language

int match(const char *str, const char *pat)
{
  int i;
  for(;; str++, pat++)
  {
    swith(*pat)
    {
      case 0:
        return *str == 0;
      case '*':
        for(i=0; ; i++)
        {
	  if(match(str+i, pat+1)) return 1;
	  if(!str[i]) return 0;
        }
      case '?':
	if(!*str) return 0;
	break;
      default:
	if(*str != *pat) return 0;
    }
  }
}


