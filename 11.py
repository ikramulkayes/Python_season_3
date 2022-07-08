def to_camel_case(text):
    import string

    text = [x.replace('-', ' ') for x in text]
    text = [x.replace('_', ' ') for x in text]
    k = ''.join(str(i) for i in text)
    k = k.split()
    f = []
    if len(k)>1:
        if k[0][0].isupper():
            flag = False
        else:
            flag = True
    for word in k:
        if flag:
            f.append(word)
            flag = False
        else:

            i = word.capitalize()
            f.append(i)
    final = ''.join(str(i) for i in f)
    
    return final

print(to_camel_case(""))