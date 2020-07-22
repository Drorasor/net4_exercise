import random
from time import sleep

facbook = 100
instegram = 50

print("wellcome to our advertisment machin \n")
total_budget = int(input("hello... what is your campaign budget? \n"))
time_face = int(input("ok...for how long do you want your facebook campaign?\n"))
time_inst = int(input("and for how long wuld you want yor instergram campaign\n"))
i_cost = (instegram * 3.5) * (time_inst) * 1.17
f_cost = (facbook* 3.5) * (time_face) * 1.17
print("your cost on facbook will be:\n ")
sleep(2)
print(str(f_cost) + " NIS\n")
print("your cost on instegram will be:\n")
sleep(2)
print(str(i_cost) + " NIS including tax")

sum_budget = f_cost + i_cost
print("your total price offer is\n " + str(sum_budget))
if int(total_budget)>= sum_budget:
    print("succsfull and you got another:\n " + str( total_budget - sum_budget)+ "S")
else:
    print("your budget is not enough, you need to add: " + str(sum_budget-total_budget) + "$")

