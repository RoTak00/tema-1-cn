def poly(x, *alist):
    res = 0

    for ind, el in enumerate(reversed(alist)):
        res += el
        if ind < len(alist) - 1:
            res *= x

    return res


print(poly(3, 1, 2, 3, 4))
