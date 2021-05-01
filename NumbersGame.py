def joda_joda(num):
    x = [int(d) for d in str(num)]
    return x

def find_in_two_numbers(first,second):
    a = joda_joda(first)
    b = joda_joda(second)
    if len(a) == len(b):
        av = " "
        for i in range(len(a)):
            for j in range(len(b)):
                if (a[i] == b[j]):
                    if i == j:
                        av = av + "1"
                        break
                    else:
                        av = av + "2"
                        break
                else:
                    av = av + "0"
                    break
    return (av)

print (find_in_two_numbers(1232,1432))
