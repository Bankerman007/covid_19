name = input("What is your name? ")
condit_answer = input("Do you have cancer, chronic kidney disease, hear conditions, severe obesity,are pregnant , sickle cell disease, organ transplantation, diabetes, smoke, asthma, hypertension or COPD? Answer Yes or No  ")
age= int(input("name what is your age? "))


if condit_answer == "Yes":
  print("Stay in it's not safe for you.  Theres a higher chance you could end up in the hospital from Covid-19 according to the CDC")
elif age > 65:
  print("You should stay away from people until you receive a vacine.  There's a high chance you could be hospitilized or worse if you contract Covid-19.  Everyone else is not going to take responsibility if you get sick.")
else:
    print("There's a lower chance you would end up in the hospital, get back to work!")



