def xor_with_int(word, integer):
    result = []

    for i in range(len(word)):
        result.append(chr(ord(word[i])^integer))
    print(result)
    return ''.join(result)

word = 'label'
number = 13

print(xor_with_int(word, number))