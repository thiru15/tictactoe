l=[["__","__","__"],
    ["__","__","__"],["__","__","__"]]
l1=l
def displayboard(l):
    
    for i in range(len(l)):
         a=l[i]
         print(*a)
         print("\n")
   
def newboard():
    print("want to play a new game enter yes for yes and no for no")
    s=input()
    flag=0
    if s=="yes":
         l=[["__","__","__"],
             ["__","__","__"],["__","__","__"]]
         displayboard(l)
         userinput()
    else:
        print("Game over")
        count=6
         
        exit()

 
            
    



def userinput():
     
    l=[["__","__","__"],
             ["__","__","__"],["__","__","__"]]
    print("enter the symbol of user1")
    p1=input()
    print("enter the symbol of user2")
    p2=input()
    count=0
    
    while count<6:
        print("enter the position where p1 wants to put")
        a,b=map(int,input("enter the positon of a and b").split())
        
        if l[a][b]!="__":
                print("the position is occupied try some other positon")
                a,b=map(int,input("enter the positon of a and b").split())
        l[a][b]=p1
        x=p1
        displayboard(l)
        if (l[0][0]==l[0][1]==l[0][2]==p1) or (l[1][0]==l[1][1]==l[1][2]==p1) or(l[2][0]==l[2][1]==l[2][2]==p1) or (l[0][0]==l[1][1]==l[2][2]==p1) or (l[0][2]==l[1][1]==l[2][0]==p1):
                  print(x+"  wins the game")
                  newboard()
         
        print("enter the position where p2 wants to put")
        a,b=map(int,input("enter the positon of a and b").split())
        if l[a][b]!="__":
                print("the position is occupied try some other positon")
                a,b=map(int,input("enter the positon of a and b").split())
        l[a][b]=p2
        x=p2
        displayboard(l)
        if (l[0][0]==l[0][1]==l[0][2]==p2) or (l[1][0]==l[1][1]==l[1][2]==p2) or(l[2][0]==l[2][1]==l[2][2]==p2) or (l[0][0]==l[1][1]==l[2][2]==p2) or (l[0][2]==l[1][1]==l[2][0]==p2):
                print(x+"wins the game")
                newboard()         
        count+=1
        if count==6:
            print("The Game is a DRAW")
            newboard()
         
displayboard(l)
userinput()