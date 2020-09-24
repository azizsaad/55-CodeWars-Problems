s = "Fred:Corwill;Aziz:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

# upper = list(map(lambda name: reversed(name) ,s.upper().replace(';',' ').replace(':',',').split()))

 # upper = sorted(reversed(s.upper().replace(':',',').split(';')))

# print (upper)

test = ''.join(str('('+c[0]+', '+c[1]+')') for c in sorted([list(reversed(elem.split(','))) for elem in s.upper().replace(':',',').replace(';',' ').split()]))

print (test)

# result = []
#
# for name in upper:
#     result.append(name.split(':'))
'''
for i,x in enumerate(upper):
    x[0],x[1] = x[1],x[0]
'''

'''
sorted_list = sorted(result)

string = ''

for i in sorted_list:
    string = string + '(' + i[0] + ', ' + i[1] + ')'

print (string)
'''
