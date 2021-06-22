from collections import Counter

def lengthy_string(str):
    txt=str
    arr=splitFun(txt)
    a = arr=[x.strip(',') for x in arr]
    repeated = first_Repeated_Word(arr)
    return repeated

def splitFun(txt):
    arr= txt.split()
    return arr

def first_Repeated_Word(arr):
    counts=dict()
    arr=tolower(arr)
    for word in arr:
        if word in counts:
            counts[word]+=1
            if counts[word]>1:
                return word
        else:
            counts[word]=1
    return None

def tolower(arr):
    return [x.lower() for x in arr]


first=lengthy_string("Once upon a time, there was a brave princess who...")
print(first)

second=lengthy_string("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only")
print(second)

third=lengthy_string("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..")
print(third)


