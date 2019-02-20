
#CTI-110
#P3HWI- MealTipTax
#Antwon Brown
#2/19/2019

#User inputs price of meal
#Caculated cost per meal with tips of 15%, 18%, 20%
#Display the meal amount


#User inputs meal price

meal_price = float(input("Please enter meal price $\n "))

#User caculates cost per meal with tips of 15%, 18%, 20%

print("Pease tip your server the following\n")

print("Your total if you tip your server 15%", meal_price * .15)

print("Your total if you tip your server 18%", meal_price * .18)

print("Your total if you tip your server 20%", meal_price * .20)
