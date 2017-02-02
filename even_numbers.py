def even_numbers(l):
    for x in l:
        if x % 2 == 0:
            print x
        x += 1
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers(test)
