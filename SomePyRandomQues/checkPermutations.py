from collections import Counter
def is_permutation(a,b):
  if len(a)!=len(b):
    return False
  counting = Counter()
  for items in a:
    counting[items] += 1
  for items in b:
    if counting[items]== 0:
      return False
    counting[items] -= 1
  return True
a = input()
b = input()
print(is_permutation(a,b))


    
  
