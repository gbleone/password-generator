import random as rd
import dictionary as dic

# a list of the alpabet and symbols.
alphabet_and_symbols = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
                        "j", "k", "l", "m", "n", "o", "p", "q", "r", 
                        "x", "t", "u", "v", "w", "x", "y", "z", "!", 
                        "$", "?", ".", 1 , 2, 3, 4, 5, 6, 7, 8 , 9, 
                        0]


# transforms a heterogenous (strings and integers) list into a string.
def combination(strings_and_integers):
    password = ''.join(str(b) for b in strings_and_integers)
    return password


# an empty list to store values.
list = []

# generates a random-set of alphebtical values.
for i in range(7):
    list.append(rd.choice(alphabet_and_symbols))


print(f"--- List --- \n{list}")

final_password = combination(list)

print(f'--- Password --- \n"{final_password}"')
