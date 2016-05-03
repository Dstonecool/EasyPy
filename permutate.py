
def permutate(array):
    if len(array) < 2:
        return [array]

    a = array[0]
    b = array[1:]
    subs = permutate(b)
    r =[]
    for s in subs:
        for i in range(len(s)+1):
            n = s[:]
            n.insert(i,a)
            r.append(n)
    return r

if __name__ == "__main__":
    array = range(10)
    for line in permutate(array):
        print line
