
samp_strng = str(input())
# count a in string
if samp_strng.find('a') > 0 or samp_strng.find('A') > 0:
    vow_a = int(1)
else:
    vow_a = int(0)
# count e in string
if samp_strng.find('e') > 0 or samp_strng.find('E') > 0:
    vow_e = int(1)
else:
    vow_e = int(0)
# count i in string
if samp_strng.find('i') > 0 or samp_strng.find('I') > 0:
    vow_i = int(1)
else:
    vow_i = int(0)
# count o in string
if samp_strng.find('o') > 0 or samp_strng.find('O') > 0:
    vow_o = int(1)
else:
    vow_o = int(0)
# count u in string
if samp_strng.find('u') > 0 or samp_strng.find('U') > 0:
    vow_u = int(1)
else:
    vow_u = int(0)

vowels = vow_a + vow_e + vow_i + vow_o + vow_u

if vowels == 1:
    print('There is only one different vowel in the string.')
else:
    print('There are', vowels, 'different vowels in the string.')
