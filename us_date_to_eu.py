s = input()
if '/' in s:
    s = s.split('/')
    print(('/').join([s[1],s[0],s[2]]))
else:
    d = {
        "January": 1, 
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12   
        }
    s = s.replace(',','').split(' ')
    print(('/').join([s[1], str(d[s[0]]), s[2]]))
 
