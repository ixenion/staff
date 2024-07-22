
// overflow
byte number = 255
number = number + 1; // 0

// instead of overflowing throws an exception error and breaks code
checked
{
	byte number = 255;
	number = number + 1;
}
