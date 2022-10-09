def recall(n):
    if n==0:
        print('stop')
    else:
        recall(n-1)
        print(f'function called {n}')
        
        
        
recall(5)
