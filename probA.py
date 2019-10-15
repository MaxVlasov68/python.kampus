def f():
    import random
    a=['1','2','3']

    while True:
            b=random.choice(a)
            c=input()
            if  b == c :
                print('WIN')
            elif b != c:
                print('Game Over')
            

    
    
