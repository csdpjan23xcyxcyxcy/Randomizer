import random

prompted_times = input("How many times you want to throw?")
candidates_names = ['TS','TKL','NKS']


def dice_throw(ttimes):
    return [random.choice(candidates_names) for i in range(ttimes)]


# throw the dice
throw = dice_throw(int(prompted_times))


# count the results
count_of_results = [throw.count(candidates_names[ii]) for ii in range(len(candidates_names))]


# stuff the results with the candidate names into a dict
my_results = {}
for key, value in zip(candidates_names, count_of_results):
    my_results[key] = value

# to tell who win
the_max = max(my_results, key=lambda k: my_results[k])

print(f"The results are {my_results}")
print(f"The winner is {the_max}")