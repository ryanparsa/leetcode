def encoder(data: list[str]) -> str:
    a = []
    for i in data:
        a.append(len(i))

    return ','.join(map(str, a)) + "#" + ''.join(data)


def decoder(encoded_str: str) -> list[str]:
    length_str, data_str = encoded_str.split('#', 1)
    lengths = list(map(int, length_str.split(',')))

    data = []
    index = 0
    for length in lengths:
        data.append(data_str[index:index + length])
        index += length

    return data


s1 = encoder(["user", "###", "data", "path#", "cisco"])
print(s1)
# 4,3,4,5,5#user###datapath#cisco
s2 = decoder(s1)
print(s2)
# ['user', '###', 'data', 'path#', 'cisco']
