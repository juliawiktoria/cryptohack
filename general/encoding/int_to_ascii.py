def array_to_ascii(arr):
    result = []

    for i in range(0, len(arr)):
        result.append(chr(arr[i]))
    result = ''.join(result)
    return result

inp = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

print(array_to_ascii(inp))