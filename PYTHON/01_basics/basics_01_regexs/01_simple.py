import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

# find all lines with "dot"
pattern = re.compile(r'\.', re.I)
# from 'Ha HaHa AhHa' returns 'true true false'
pattern = re.compile(r'\bHa', re.I)
# from 'Ha HaHa AhHa' returns 'false true true'
pattern = re.compile(r'\BHa', re.I)
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
# or
pattern = re.compile(r'\d{3}.\d{3}.\d{4}', re.I)
matches = pattern.finditer(text_to_search)
# clear output
# just list of matches
matches_clear = pattern.findall(text_to_search)

# only dash or dot
# 321-555-4321
# 123.555.1234
# 800-555-1234
# 900-555-1234
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
matches = pattern.finditer(text_to_search)

# 800-555-1234
# 900-555-1234
pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d', re.I)
matches = pattern.finditer(text_to_search)

# match digits between 1 and 5
pattern = re.compile(r'[1-5]\d\d[-.]\d\d\d[-.]\d\d\d\d', re.I)
matches = pattern.finditer(text_to_search)

# optional dot

# Mr. Schafer
# Mr Smith
# Mrs. Robinson
# Mr. T
pattern = re.compile(r'Mr\.?', re.I)
matches = pattern.finditer(text_to_search)

# Mr. Schafer
# Mr Smith
# Mr. T
pattern = re.compile(r'Mr\.?\s[A-Z]\w*', re.I)
matches = pattern.finditer(text_to_search)

# Mr. Schafer
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*', re.I)
matches = pattern.finditer(text_to_search)

for match in matches_clear:
    print(match)

# only match beginning of the string
# re.I - ignore case flag
pattern = re.compile(r'start', re.I)
matches = pattern.match(sentence)
# match at entire sentence
matches = pattern.search(sentence)
print(matches)

# from 50_data.txt
with open ('50_data.txt', 'r') as f:
    data = f.read()

    # parse phone numbers
    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d', re.I)
    matches = pattern.finditer(data)
    # for match in matches:
    #     print(match)


