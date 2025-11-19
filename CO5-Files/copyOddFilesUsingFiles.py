with open("abc.txt", "r+") as abc:
    with open("pqr.txt", "w") as pqr:
        for rownum, row in enumerate(abc):
            if rownum % 2 == 0:
                pqr.write(row)
            else:
                continue
