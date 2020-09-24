def open_or_senior(data):
    result = []
    for i,x in enumerate(data):
        if data[i][0] >= 55 and data[i][1] > 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result

print (open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))
