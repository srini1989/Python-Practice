import re

text = "Hello, The documentation can be found at python:org"
match = re.search(r"Python:\w\w\w", text)

if match:
    print("Found", match.group())
else:
    print("Did not found a match")


def print_status(pattern, expression):
    match = re.search(pattern, expression)
    if match:
        print("Found {}".format(match.group()))
    else:
        print("Not Found")


print_status(r"iii", "piiig")

ex_string = "purple alice@test.com, blah monkey bob@abc.com blah dishwasher"
print(re.sub(r"([\w.-]+)@([\w\.-+])", "test", ex_string))
