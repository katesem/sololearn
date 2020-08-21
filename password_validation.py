import re

s = input()
if len((re.findall("\d",s)))< 2 or len(s)< 7  or\
    len((re.findall("[!@#$%&*]",s)))< 2:
     print('Weak')
else:
    print('Strong')
