data = {
        'PMTK300,3000,0,0,0,0': 0x1E,
        'PMTK300,5000,0,0,0,0': 0x18,
        }
a = '$PMTK300,3000,0,0,0,0*1E'
b = '$PMTK300,5000,0,0,0,0*18'


import operator
from functools import reduce

def nmea_checksum(sentence: str):
    """
    This function checks the validity of an NMEA string using it's checksum
    """
    sentence = sentence.strip("$\n")
    nmeadata, checksum = sentence.split("*", 1)
    calculated_checksum = reduce(operator.xor, (ord(s) for s in nmeadata), 0)
    ab = hex(calculated_checksum).split('x')[-1]
    print(f'Calculated: {ab}')
    if int(checksum, base=16) == calculated_checksum:
        print(f'Valid checksum')
        return nmeadata
    else:
        print(f'Invalid checksum')
        raise ValueError("The NMEA data does not match it's checksum")


nmea_checksum(a)
