def Linear_search(ele,tar):
    for i in ele:
        if i == tar:
            print(True)
            return True
    print(False)
    
ele = list(map(int,input().split())) 
tar = int(input())
Linear_search(ele,tar)