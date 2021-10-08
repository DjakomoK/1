from turtle import *
shape('turtle')
pensize(3)
color ('green')
speed(10)
tp = pos()
print (tp)

def K_K (n):
    while n >= 0:
        while True:
            left ( 2 )
            forward( 2 )
            if ( (round(xcor(), 1)), (round(ycor(), 1)) ) == (0.0,0.0):
                print(round(ycor(), 1))
                while True:
                    right ( 2 )
                    forward( 2 )
                    if ( (round(xcor(), 1)), (round(ycor(), 1)) ) == (0.0,0.0):
                        break

                break
        left ( 360/n+15 )
        n-=1

                #while True:
                #    
            #break


K_K (5)
