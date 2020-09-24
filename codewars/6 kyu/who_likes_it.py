def likes(names):
    if len(names) == 0: return 'no one likes this'
    if len(names) == 1: return '{} likes this'.format(''.join(names))
    if len(names) == 2: return '{} and {} like this'.format(''.join(names[0]),''.join(names[1]))
    if len(names) == 3: return '{}, {} and {} like this'.format(''.join(names[0]),''.join(names[1]),''.join(names[2]))
    if len(names) > 3: return '{}, {} and {} others like this'.format(''.join(names[0]),''.join(names[1]),int(len(names)-2))

print (likes(['mark','jacob','hello','pussio']))




#
# Test.assert_equals(likes([]), 'no one likes this')
# Test.assert_equals(likes(['Peter']), 'Peter likes this')
# Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
# Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
# Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
#
# for i in names:
#     print (i + 'likes this.')
