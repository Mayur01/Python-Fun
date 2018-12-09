from collections import OrderedDict
def freq(str):
    # break the string into list of words
    str = str.split()
    str2 = []

    for i in str:
        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)
            dict={str2[i] : str.count(str2[i]) for i in range(0, len(str2))}
    orderedDict = OrderedDict(sorted(dict.items()))
    for k,v in orderedDict.items():
         print(k,":",v)
str=input("Enter your string :")
# str ='New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'
freq(str)
