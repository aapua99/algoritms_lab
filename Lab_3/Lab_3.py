def search(k, result, i):
    lenght = len(k)
    j = 0
    while j < len(k):
        if (k[j][0] == i):
            n = k[j][1]
            if (n % 2 == 0):
                result[0].append(n)
            else:
                result[1].append(n)
            k.pop(j)
            search(k, result, n)
            j = 0
        else:
            j += 1
    return result


if __name__ == "__main__":
    n = input()
    plem = []
    list_pairs = []
    for i in range(0, int(n)):
        var = input().split()
        list_pairs.append([int(var[0]), int(var[1])])
    while (len(list_pairs) > 0):
        result = [[], []]
        if (list_pairs[0][0] % 2 == 0):
            result[0].append(list_pairs[0][0])
        else:
            result[1].append(list_pairs[0][0])
        result = search(list_pairs, result, list_pairs[0][0])
        plem.append(result)
    print(plem)
    result_pairs = []
    for i in range(0, len(plem)):
        for k in range(0, len(plem[i][0])):
            for j in range(0, len(plem)):
                if i != j:
                    for b in range(0, len(plem[j][1])):
                        result_pairs.append([plem[j][1][b], plem[i][0][k]])
    print(len(result_pairs))
    print(result_pairs)
