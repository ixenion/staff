; WRITE 
; syscall num - 4
; first param - 1  (standart output)
; seond param is start address of the text
; third is text length

; hello world OS Linux

global _start

section .data
msg db "Hello World!", 10
msg_len equ $-msg

section .text
_start
	mov eax, 4
	mov ebx, 1
	mov ecx, msg
	mov edx, msg_len
	int 0x80

	mov eax, 1
	mov ebx, 0
	int 0x80

; error processing
; error result returns into eax within range fffff000h & ffffffffh
; zero - no error ?


; hello world OS FreeBSD

global _start

section .data
msg db "Hello World!", 10
msg_len equ $-msg

section .text
_start
	push dword msg_len
	push dword msg
	push dword 1
	mov eax, 4
	push eax
	int 80h
	add esp 16

	push dword 0
	mov eax, 1
	push eax
	int 80h

; error processing
; if CF=0 - no error. use jnc to check
; if CF=1 - error occurs. use jc to check




; READ

; both from files and user input
; syscall number - 3
; first param - input descriptor - 0 for standart input
; second - start address (label to store)
; third - number of input bytes

; third = 200
; but actually 15 only were inputed
; then eax store num 15 (positive)
; helps to separate data from garbage

; if eax = 0 - end file situation (keyboard imitation Ctrl+D)

; if eax < 0 - error


; in FreeBSD
; CF=1 - error



; Standart Streams
; 0 - inpput (read)
; 1 - output (write)
; 2 - used for error msg (write)




; OPEN
; used to work with files before read/write
; syscall num - 5
; first param - address of text line whih defines file name. At the end must be 0byte
; second - usage mode (read/write/etc). See table 4.1
; example: to create and open file to write (or if it present - open and errise it content) Linux - 241h, FreeBSD - 601h
; C analog - O_WRONLY|O_CREATE|O_TRUNK
; third param - used only when make file and sets permissions (0666q)

; error
; eax < 0 - Linux
; CF=1 - FreeBSD

; success
; eax contains file descriptor (241h)
; and that descriptou should be used as first param at read & write
; better to copy that number somewhere at memory



; CLOSE
; when file work done that file should be cloecd
; syscall num - 6
; first (and last) param - file descriptor (241h)



; GETPID
; to get pid of current process (proogram)
; syscall 20 (Linux & FBSD)
; no params
; result be at eax

; GETPPID
; get parent pricess id
; syscall 64 for Linux & 39 for FBSD
; no params
; result be at eax


; KILL
; syscall - 37
; first param - target pid (or group of pids or even all system pids)
; second - signal number. 15(SIGTERM) - end of process, may be ignored or delayed by target pid.
;			   9(SIGKILL) - kills process, can't be ignored o delayed.



