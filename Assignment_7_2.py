 # Programmer:         Connor Floyd
 # Course:             CSCI/ISAT B104
 # Assignment:         Programming Exercises 7.2

import csv


baseList = ['Jasmine Rice', 'Brown Rice', 'Cilantro Lime Cauliflower Rice', 'Udon Noodles', 'Yakisoba Noodles', 'Rice Noodles',
         'Zucchini Noodles', 'Butternut Squash Noodles']
proteinList = ['Veggie', 'Tofu', 'Chicken', 'Beef', 'Shrimp']
veggieList = ['Carrots', 'Crimini Mushrooms','Jalapenos', 'Green Peppers', 'Snap Peas', 'Bean Sprouts', 'Broccoli',
           'Purple Cabage', 'Thai Peppers', 'Cabbage', 'Spinach', 'Pineapple', 'Bok Choy', 'Edamame', 'Red Onion',
           'Green Onions', 'Green Beans', 'Tropical Salsa', 'Pad Thai Mix']
sauceList = ['Garlic Ginger & Soy', 'Tropical Pineapple', 'Korean BBQ', 'Tikka Masala', 'Lemongrass Mango Sweet & Sour',
             'Mango Habanero', 'Ginger Teriyaki', 'Yellow Coconut Curry', 'Spicy Peanut', 'Hawaiian BBQ', 'Carribean Jerk',
             'Agave, Ginger & Siracha', 'Korean Gojujang Sauce', 'Jalapeno Green Sauce', 'Blackberry Habanero',
             'Mango Habanero', 'Habanero', 'None']
veggies2 = []
veggies3 = []
veggies4 = []
veggies5 = []

for veggie in range(len(veggieList)):
    for veggie2 in range(len(veggieList)):
        veggies2.append(f"{veggieList[veggie]} + {veggieList[veggie2]}")
        
for veggie in range(len(veggieList)):
    for veggie2 in range(len(veggieList)):
        for veggie3 in range(len(veggieList)):
            veggies3.append(f"{veggieList[veggie]} + {veggieList[veggie2]} + {veggieList[veggie3]}")

for veggie in range(len(veggieList)):
    for veggie2 in range(len(veggieList)):
        for veggie3 in range(len(veggieList)):
            for veggie4 in range(len(veggieList)):
                veggies4.append(f"{veggieList[veggie]} + {veggieList[veggie2]} + {veggieList[veggie3]} + {veggieList[veggie4]}")

for veggie in range(len(veggieList)):
    for veggie2 in range(len(veggieList)):
        for veggie3 in range(len(veggieList)):
            for veggie4 in range(len(veggieList)):
                for veggie5 in range(len(veggieList)):
                    veggies5.append(f"{veggieList[veggie]} + {veggieList[veggie2]} + {veggieList[veggie3]} + {veggieList[veggie4]} + {veggieList[veggie5]}")

veggieTotal = veggieList + veggies2 + veggies3 + veggies4 + veggies5
veggieList.append("None")

with open('C:/Users/cwfloyd/Desktop/B104/urbanwok.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    
    for base in baseList:
        for protein in proteinList:
            for sauce in sauceList:
                for veggie in veggieTotal:
                    row = [base, "and", protein, "with", sauce, "and", veggie]
                    writer.writerow(row)
                    
                    

                        
                   
             
                    