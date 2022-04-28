def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
ans=  (most_frequent('mississippi'))
import operator
print(dict(sorted(ans.items(),key=operator.itemgetter(1))))
