'''Check whether a string has all unique chararcter or not.'''


def unique(string):
    for i in range(0,len(string)-1):
        for j in range(i+1,len(string)):
            if string[i]==string[j]:
                return False
    return True
string = input()
print(unique(string))

----------------------------------------------------
----------------------------------------------------
input example:
abchsje it should return 'True'

abchwwww -> 'False'

12345 -> 'True'

12354324 -> 'False'
