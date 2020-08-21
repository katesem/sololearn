s = ''.join(input().split('x')) 
print('ALARM'if  ('$T' in s) or  ('T$' in s)\
       else 'quiet')
