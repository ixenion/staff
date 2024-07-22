

;       SHIFT OPERATIONS
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;; SHR ; SHL ; SAL ; SAR ; SHRD ; SHLD ; ROR ; ROL ; RCR ; RCL ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; SHR - have 2 operands. First - To shift (reg or memory type), second - how much (direct number from 1 to 31 or CL register).
; shifts register bits to the right
; SHL - same as abowe. Ashift bits to the left
; Shiting signed numbers no so easy.
; So there are special shift commands to save number sign
; SAL=SHL - shift arithmetic left	-| used for 2^n arithmtics ( * & / )
; SAR	 - shift arithmetic right	-|

; SHRD & SHLD - work through 2 registers
; ROR & ROL - cycle shift
; RCR - cycle shift though CF to the right
; RCL - ycle shift though CF to the left

;
