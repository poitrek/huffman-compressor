import bisect





if __name__ == '__main__':
    # ar1 = [10, 20, 30, 35, 37, 39, 45, 50, 100]
    ar1 = list(range(0, 100, 2))
    print(bisect.bisect_right(ar1, 40))

