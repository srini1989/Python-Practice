uFile = open("Py3.9-Programs/for.py", "r")  # open a file in read mode
uFile = open("Py3.9-Programs/for.py", "w")  # open a file in write mode
uFile = open("Py3.9-Programs/for.py", "a")  # open a file in append mode
uFile.readline()

open("Py3.9-Programs/for.py", "a").read()
open("Py3.9-Programs/for.py", "a").readlines()
open("Py3.9-Programs/for.py", "a").readline()

uFile = open("Py3.9-Programs/for.py", "w")
uFile.write("a\nb\nc")
uFile.close()


def charcount(filename):
    return len(open(filename).read())


def wordcount(filename):
    return len(open(filename).read().split())


def linecount(filename):
    return len(open(filename).readlines())
