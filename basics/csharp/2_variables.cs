// C# Type ! .NET Type ! Bytes ! Range

// byte ! Byte ! 1 ! 0 to 255
// short ! int16 ! 2 ! -32.768 to 32.767
// int ! int32 ! 4 ! -2.1B to 2.1B
// long ! int64 ! 8 ! ...
// float ! Single ! 4 ! -3.4x10^38 to 3.4x10^38
// double ! Double ! 8 ! ...
// decimal ! Decimal ! 16 ! -7.9x10^28 to 7.9x10^28
// char ! Char ! 2 ! Unicode Characters
// bool ! Boolean ! 1 ! True / False

float num1 = 1.2f;// without "f" at the end compiler woould think this number is double
decimal num2 = 1.2m;// same here. Without "m" program wouldn't compile
