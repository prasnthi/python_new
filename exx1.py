def minimum(x):
    mini = x[0]
    for i in x[0:]:
        if i > mini:
            mini = i
    return(mini)
b = [565,897,231,48,5456,897,444]
print minimum(b)
