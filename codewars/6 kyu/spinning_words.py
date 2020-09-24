def spin_words(sentence):
    sent2 = sentence.split(' ')
    result = []
    for word in sent2:
        if len(word) >= 5:
            res = word.replace(word,word[::-1])
            result.append(res)
        else:
            result.append(word)
    fin_res = ' '.join(result)
    return fin_res

print (spin_words('hey fellow warriors'))
