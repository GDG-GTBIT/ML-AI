print("Wellcome to quiz game !!")
print("Write the answers in small case")
print("")

score = 0
question_no = 0

playing = input('Do you want to play ? (yes/no) ').lower()

if playing == 'yes':
    question_no += 1
    qna = input(f"\n{question_no}. Which is India's largest city by population? ").lower()
    if qna == 'mumbai':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> mumbai')


    question_no += 1
    qna = input(f'\n{question_no}. Which planet is known as morning star or evening star? ').lower()
    
    if qna == 'venus':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> venus')


    question_no += 1
    qna = input(f'\n{question_no}. What does colour of star indicate? ').lower()
    
    if qna == 'temperature':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> temperature')


    question_no += 1
    qna = input(f'\n{question_no}. what does PSU stand for? ').lower()
    
    if qna == 'power supply unit':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> power supply unit')


else:
    print('Exiting the Game.')
    quit()

print(f'\nnumber of question is ',question_no)
print(f'your score is ',score)
