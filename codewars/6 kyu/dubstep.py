song = "WUBWUBAWUBWUBWUBBBWUBWUBWUBCDEWUBWUB"
song2 = ' '.join(song.split('WUB'))
print (song2)
newlist = []
for i,char in enumerate(song2):
    if (i + 1) < len(song2):
        if char == song2[i+1] and char == ' ':
            continue
    if char == ' ' and len(newlist)==0:
            continue
    if char == ' ' and i == len(song2)-1:
            break

    newlist.append(char)

print(newlist)
print(''.join(newlist))
