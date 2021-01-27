name = input("What is your name? ")
condit_answer = input("Do you have cancer, chronic kidney disease, heart conditions, severe obesity, sickle cell disease, organ transplantation, diabetes, asthma, hypertension COPD, do you smoke, or are you pregnant? Answer Yes or No  ")
age= int(input("%s what is your age? " % name))

if condit_answer == "Yes":
  print("Stay in, it's not safe for you. There's a higher chance you could end up in the hospital from Covid-19 according to the CDC")
elif age > 65:
  print("You should stay away from people until you receive a vaccine. There's a high chance you could be hospitalized or worse if you contract Covid-19. Everyone else is not going to take responsibility if you get sick.")
else:
    print("There's a lower chance you would end up in the hospital, get back to work!")



