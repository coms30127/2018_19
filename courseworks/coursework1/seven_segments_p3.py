#for the submission uncomment the submission statements
#so submission.README

from math import *

#from submission import *

def seven_segment(pattern):

    def to_bool(a):
        if a==1:
            return True
        return False
    

    def hor(d):
        if d:
            print(" _ ")
        else:
            print("   ")
    
    def vert(d1,d2,d3):
        word=""

        if d1:
            word="|"
        else:
            word=" "
        
        if d3:
            word+="_"
        else:
            word+=" "
        
        if d2:
            word+="|"
        else:
            word+=" "
        
        print(word)

    

    pattern_b=list(map(to_bool,pattern))

    hor(pattern_b[0])
    vert(pattern_b[1],pattern_b[2],pattern_b[3])
    vert(pattern_b[4],pattern_b[5],pattern_b[6])

    number=0
    for i in range(0,4):
        if pattern_b[7+i]:
            number+=pow(2,i)
    print(int(number))
        
#submission=Submission("your_name")
#submission.header("Your Name")

six=[1,1,-1,1,1,1,1,-1,1,1,-1]
three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

##this assumes you have called your weight matrix "weight_matrix"
#submission.section("Weight matrix")
#submission.matrix_print("W",weight_matrix)

print("test1")
#submission.section("Test 1")

test=[1,-1,1,1,-1,1,1,-1,-1,-1,-1]


seven_segment(test)
#submission.seven_segment(test)
##for COMSM0027

##where energy is the energy of test
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step

print("test2")

test=[1,1,1,1,1,1,1,-1,-1,-1,-1]
#submission.section("Test 1")

seven_segment(test)


#submission.seven_segment(test)

##for COMSM0027
##where energy is the energy of test
#submission.print_number(energy)

##this prints a space
#submission.qquad()

#here the network should run printing at each step
#for the final submission it should also output to submission on each step


#submission.bottomer()



