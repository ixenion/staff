// from byte to int. Compatile case. No data loss
byte b = 1; // 00000001
int i = b; // 00000000 00000000 00000000 00000001

// won't compile. ut types are compatible
int i = 1;
byte b = i;
// to make it work: (explicit type)
byte b = (byte)i;

// Non-compatible types
string s = "1";
int i = (int)s; // won't compile
// to make it work
int i = Convert.ToInt32(s); // ToByte(), ToInt16(), ToInt32(), ToInt64(), ToBoolean()
int j = int.Parse(s);
