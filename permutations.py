import itertools   #iterable as input
n=input ("Enter the number")
P=list (itertools. permutations(n)) #function to generate the permutations, f
print(*[''.join (p) for p in P]) #The join method is used to join the characters in each permutation into a single string.
