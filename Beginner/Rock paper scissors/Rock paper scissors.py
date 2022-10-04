def rps():
    pl_1=input("enter your choice r/p/s:")
    pl_2=input("enter your choice r/p/s:")

    if pl_1 == pl_2:
        print('draw')
        
    else:
        if pl_1 =='r':
            if pl_2=='p':
                return 'pl_2 wins'
            else:
                return 'pl_1 wins'
            
        elif pl_1=='s':
            if pl_2=='p':
                return 'pl_1 wins'
            else:
                return 'pl_2 wins'
            
        elif pl_1=='p':
            if pl_2=='s':
                return 'pl_2 wins'
            else:
                return 'pl_1 wins'

print(rps())

    
    

    


