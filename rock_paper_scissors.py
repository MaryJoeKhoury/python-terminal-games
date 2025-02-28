import random

options=['rock','paper','scissors']

user_score=0
opponent_score=0




while user_score<3 and opponent_score<3:
    opponent_option=random.choice(options)
    user_choice=input('Enter your choice(rock,paper,scissors): ')
    while user_choice.lower()!='paper' and user_choice.lower()!='rock' and user_choice.lower()!='scissors':
        user_choice=input('Wrong choice!\n Enter your choice:')
    if user_choice==opponent_option:
        print(f'Draw! you both chose {user_choice}')
    elif  user_choice.lower()=='rock':
        if opponent_option=='scissors':
            print(f'{opponent_option} \nYou win!')
            user_score+=1
        elif opponent_option=='paper':
            print(f'You lost:( Opponent chose {opponent_option}')
            opponent_score+=1
    elif user_choice.lower()=='paper':
        if opponent_option=="rock":
            print(f'{opponent_option} \nYou win!')
            user_score+=1
        elif opponent_option=="scissors":
            print(f'You lost:( Opponent chose {opponent_option}')
            opponent_score+=1
    
    else:
        if opponent_option=="paper":
            print(f'{opponent_option} \nYou win!')
            user_score+=1
        elif opponent_option=="rock":
            print(f'You lost:( Opponent chose {opponent_option}')
            opponent_score+=1
    if user_score==3:
        print(f'YOU WON!\n USER SCORE:{user_score}      OPPONENT SCORE:{opponent_score}')
    elif opponent_score==3:
        print(F'HARDLUCK:/ YOU LOST\n USER SCORE:{user_score}      OPPONENT SCORE:{opponent_score}')




