// compile;
// $gcc <src.c> -o <outp>


// allocates some memory on the stack
// and copyes a string into it from the command line

// argc - tne number of params given
// argv - pointer to those variables that one have got (be held in the kernell area (32b only?))
// 500 - 500 haracters long
// strcpy - copies command line params from argv into the buffer
// at the top of stack return address placed, then goes EBP register and then 500 bytes reserved


#include <stdio.h>
#include <string.h>

int main (int argc, char** argv)
{
	char buffer[500];
	strcpy(buffer, argv[1]);

	return 0;
}


// mission is to rewrite ret address

