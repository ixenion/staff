import struct
from hexdump import hexdump

# hex_response = "583495E13C770201BD6F"
hex_response = "1D583495E13C770201BD6F"
byte_array = bytes.fromhex(hex_response)
print(hexdump(byte_array))
timestamp = struct.unpack('<BBBBBBBI', byte_array)
print(timestamp)
