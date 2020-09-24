def get_count(input_str):
    return len([i for i in input_str if i in ['a','e','i','o','u']])

print (get_count("o a kak ushakov lil vo kashu kakao"))
