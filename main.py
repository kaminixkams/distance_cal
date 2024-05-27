while True:
    print("DISTANCE CALCULATOR!!!!")
    x1,y1=list(map(int,input("Enter point 1's co-ordinates: ").split()))
    x2,y2=list(map(int,input("Enter point 2's co-ordinates: ").split()))
    equ=((x2-x1)**2+(y2-y1)**2)**(1/2)
    print("Distance between 2 points: ",equ)
    k=input("Do you want to continue or exit? (y/n): ")

    if k=="n":
        print("Thank you for using this calculator!!")
        break
