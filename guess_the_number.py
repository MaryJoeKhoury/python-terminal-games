import random



y=True
while y:
    choice=input('Choose your level:\na-Easy(1 to 10)\nb-Medium(1 to 100)\nc-Hard(-500 to 500)\nd-Exit\n')
    print('awal shi bl outer most loop')
    if choice.lower()=='a':    
        random_number=random.randint(1,10)
        print(random_number)
        counter=0
        while counter<5:
            user_guess=input('enter a number between 1 and 10\n')
            print(f'counter: {counter}')
            counter+=1
            if int(user_guess)>random_number:
                    print('number less than that')
            elif int(user_guess)<random_number:
                    print('number greater than that')
            else:
                    # x=False
                    print(f'You have guessed the number({random_number})!\n')
                    break
                
        if counter==5:    
             print(f'You have lost the game. The number was {random_number}\n')
            # x=False
        
           

    elif choice.lower()=='b':
        random_number=random.randint(1,100)
        print(random_number)
        counter=0
        while counter<7:
            user_guess=input('enter a number between 1 and 100\n')
            print(counter)
            counter+=1
            if int(user_guess)>random_number:
                print('number less than that')
            elif int(user_guess)<random_number:
                 print('number greater than that')
            else:
                x=False
                print(f'You have guessed the number({random_number})!\n')
                break
        if counter==7:
            print(f'You have lost the game. The number was {random_number}\n')
            
    elif choice.lower()=='c':
            random_number=random.randint(-500,500)
            counter=0
            while counter<10:
                user_guess=input('enter a number between -500 and 500\n')
                print(counter)
                counter+=1
                if int(user_guess)>random_number:
                    print('number less than that')
                elif int(user_guess)<random_number:
                    print('number greater than that')
                else:
                    x=False
                    print(f'You have guessed the number({random_number})!\n')
                    break
                    
            if counter==10:
                 print(f'You have lost the game. The number was {random_number}\n')
            
    elif choice.lower()=='d':
        break
    # else:
    #     print('Wrong choice')
    #    break
       