import random, time

randomNumber = random.randrange(1, 100)
userNumber = 0
attempts = 0
numbers = []
print ("Liczba: " + str(randomNumber))

while True:
    userNumber = int(input("Podaj liczbę: "))
    numbers.append(userNumber)
    attempts += 1
    if userNumber > randomNumber:
        print("Twoja liczba jest za duża! Podaj mniejszą: ")
    elif userNumber < randomNumber:
        print("Twoja liczba jest za mała! Podaj większą: ")
    elif userNumber == randomNumber:
        print("Udało Ci się odgadnąć liczbę!!!")
        print("Liczba, którą szukałeś to: " + str(randomNumber))
        print("Oto ilość Twoich prób: " + str(attempts))
        print("Poprzednie liczby: " + str(numbers))
        time.sleep(10)
        break