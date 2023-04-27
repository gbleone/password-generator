import random as rd
import dictionary as dic

# set the difficulty of password generated.
easy = 5
normal = 9
hard = 13

# transforms a heterogenous (strings and integers) list into a string.
def combination(strings_and_integers):
    password = ''.join(str(b) for b in strings_and_integers)
    return password


# an empty list to store values.
list = []

# generates a random-set of alphebtical values.
for i in range(normal):
    list.append(rd.choice(dic.alphabet))

# generates a random-set of symbolic values.
for i in range(normal):
    list.append(rd.choice(dic.symbols))

# generates a random-set of numerical values.
for i in range(normal):
    list.append(rd.randint(0, 100))



print(list)




# final_password = combination(list)

# print(f'--- Password --- \n"{final_password}"')



