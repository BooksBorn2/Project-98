def swapData():
    data_a = open("sample1.txt", 'r')
    data_b = open("sample2.txt", 'r')
    with open("sample2.txt", 'w') as a:
        a.write(data_a)
    with open("sample1.txt", 'w') as b:
        b.write(data_b)

swapData()