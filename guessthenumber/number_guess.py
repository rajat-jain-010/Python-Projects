import random
import colorama
num = random.randint(1,100)
counter = 0
while True :
    print(colorama.Fore.GREEN,f"tries left {12 - counter}")
    a = int(input("guess the number between 1-100 :-) "))
    if counter > 12:
        print("you have lost :-(")
    if a == num :
        print(f"Wohooo! you guessed it in {counter + 1 } tries ")
        break
    elif a > num :
        print("a little smaller ")
    elif a < num :
        print("a little bit higher ")
        
    counter += 1