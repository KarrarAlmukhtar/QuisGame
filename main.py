print("Welcome to me computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play:) ")
sorce = 0

answer = input ("whet does CPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Coreect")
    sorce += 1

else:
    print("Incorrect!")
answer = input ("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Coreect")
    sorce += 1

else:
    print("Incorrect!")
answer = input ("What does PSU stand for ")
if answer.lower() == "power suplly":
    print("Coreect")
    sorce += 1
else:
    print("Incorrect!")
answer = input ("What does PSi stand for ")
if answer.lower() == "power":
    print("Coreect")
    sorce += 1

else:
    print("Incorrect!")
print("You got " + str(sorce) + " questions correct!")
print("You got " + str((sorce / 4) * 100) + "%.")

