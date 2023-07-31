#Story intro 

print("** A Trip to the Cholocate Factory **")
print("    (May be based on true events) ")
print()
print("Congrats! After a long search you have found a golden ticket in your chocolate bar!")
print()
print("You are visiting Willy Wonka's Chocolate Factory!")
print()

#Intro to scenarios
print("You are outside of the factory waiting with the other lucky few that found a ticket.")
print()
print("You really want to make some new friends. You meet three possible candidates.")
print("  A. Augustus Gloop")
print("  B. Violet Beauregarde")
print("  C. Veruca Salt")

#Prompt user for first adventure choice and save their choice in a variable
userChoice = input("Who will you talk to first? Please select option A through C: ")
print()

#Control flow statements to present selected story
#First, we present what would happen if A. Augustus Gloop is chosen
if(userChoice == "A"):
  print("You say hi to Augustus Gloop. He seems nice.")
  print("Augustus tells you his favorite food is chocolate & he loves swimming.")
  print("Augustus would like to venture out through the factory with you.")
  print("He is very excited to check all the rooms in the factory.")
  print()
  print("What path do you think you and Augustus should take?")
  print("  A.The Oompa Loompa living quarters.")
  print("  B.The magical lollipop room.")
  print("  C.The chocolate river with its beautiful hard-candy boats.")

  #Prompt user for their choice and store it in a variable
  withAugustus = input("Plese select option A through C: ")

  #Check if user entered right answer 'C'
  if(withAugustus == "C"):
    #Success message
    print()
    print("You and Augustus follow the path to the river. It is so fun!")
    print("You swim with Augustus until the Oompa Loompas drag you out of the river for cross-contamination.")
    print("Your new bestfriend, Augustus, shares with you his phone number.")
    print("He wants to hang out again. Congrats on making a new friend!")
    
  #Scenario if user enters anything other than 'C'
  else:
    print()
    print("Blegh! Augustus finds that incredibly boring. He asks Violet to hang out instead. Sorry, pal.")

#Scenario if user chooses B. Violet Beuauregarde
elif(userChoice == "B"):
  print()
  print("You say hi to Violet Beauregarde. She seems sporty and fun.")
  print("Violet is very competitive and likes sports. Her favorite is karate.")
  print("Violet loves chewing too, it helps her performance anxiety at competitions.")
  print("She agrees to hang out with you for a bit but you must guess her favorite candy first.")
  print()

  #Prompt user to enter an answer
  violetsFave = input("Please enter your guess for Violet's favorite candy: ")

  #Scenario if user guesses right
  if(violetsFave == "Gum"):
    print()
    print("Wow! It's like you get her already. She declares you her new best friend!")
    print("Make sure to help your new friend stay out of trouble and keep her from turning blue.")

  #Scenario if user guesses wrong
  else:
    print()
    print("You just don't get her! Violet must keep her eyes on the prize and has no time to chat anymore.")
    print("Bad luck, sport!")

#Last Scenario - C. Veruca Salt
else:
  print()
  print("You say hi to Veruca Salt. She seems put together and quiet.")
  print("Uh-oh. She's a bit snobby because she's heir to a huge fortune.")
  print("Veruca's dad buys her whatever she wants. She has 13 pets.")
  print("She would like two new pets and would like your help choosing.")
  print("She would prefer for the new pets to be indoor animals. Maybe common household pets since her other ones are very exotic. Her new pets can be two of the same.")
  print()

  #Prompt user and store values in two variables
  firstPet = input("Enter first suggestion: ")
  secondPet = input("Enter your second suggestion: ")
  print()

  #It's allowed to have two of the same pets, but this also serves so that the order the answer is put in does not affect the outcome
  firstChoice = (firstPet == "Cat") or (firstPet == "Dog")
  secondChoice = (firstPet == "Cat") or (firstPet == "Dog")

  #Validate input - AND because they both must be a match
  if(firstChoice and secondChoice):
    print("Violet thinks your idea is great! She invites you to meet her new pets sometime.")
    print("Violet's dad is extactic that she made a friend. He writes you a check for $500 and will pay for your travel to come visit.")

  #Scenario if user inputs something else
  else:
    print("Violet was not happy with your response. She already has 5 of each. She walks away with her dad in disgust.")
    print("Sometimes you win, sometimes you don't. Better luck next time.")

  