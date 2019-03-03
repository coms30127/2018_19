#this is the programme for creating your submission document

from math import *
import random as rnd

class Submission:
    def __init__(self,filename):
        self.document=open(filename+".tex",'w')
        self.segment_direction={6:"(0,0)--(1,0)",5:"(1.05,0.05)--(1.05,1.05)",4:"(-.05,0.05)--(-.05,1.05)",3:"(0,1.10)--(1,1.10)",2:"(1.05,1.15)--(1.05,2.15)",1:"(-.05,1.15)--(-.05,2.15)",0:"(0,2.20)--(1,2.20)"}

        
    def header(self,candidate_name):
        self.document.write("\\documentclass[a4paper,fontsize=12pt]{scrartcl}\n")
        self.document.write("\\usepackage{tikz}\n")
        self.document.write("\\begin{document}\n")
        self.document.write("\\section*{"+candidate_name+"}\n")

    def section(self,section_name):
        self.document.write("\\subsection*{"+section_name+"}\n")
        
    def matrix_print(self,matrix_name,matrix,rounding=2):
        n=len(matrix)
        r=len(matrix[0])
        self.document.write("$$ "+matrix_name+"=\\left(\\begin{array}{")
        for i in range(0,r):
            self.document.write("c")
        self.document.write("}\n")
        for j in range(0,n):
            for i in range(0,r):
                self.document.write(str(round(matrix[j][i],rounding)))
                if i!=r-1:
                    self.document.write("&")
            self.document.write("\\\\")
        self.document.write("\\end{array}\\right)$$\n")

        
    def seven_segment_display(self,pattern):
        
        self.document.write("\\begin{tikzpicture}\n")
    
        def write_draw(segment_status):

            if segment_status==1:
                self.document.write("\\draw[ultra thick,color=red]")
            else:
                self.document.write("\\draw[thick,color=lightgray]")


        for segment,status in enumerate(pattern):
            write_draw(status)
            self.document.write(self.segment_direction[segment])
            self.document.write(";\n")
        
        self.document.write("\\end{tikzpicture}\n")


    def to_bool(self,a):
        if a==1:
            return True
        return False

    def seven_segment(self,pattern):
        self.seven_segment_display(pattern[0:7])
        number=0
        for i,b in enumerate(map(self.to_bool,pattern[7:11])):
            if b:
                number+=pow(2,i)
        self.document.write(str(int(number))+"\n")

    def cr(self):
        self.document.write("\\\\")

    def print_number(self,number,rounding=3):
        self.document.write(" "+str(round(number,rounding))+" ")

        
    def qquad(self):
        self.document.write("\\qquad\n ")

        
    def bottomer(self):
        self.document.write("\\end{document}")
        self.document.close()


if __name__ == '__main__':

    matrix=[[(i+j)/7.0 for j in range(0,4)] for i in range(0,3)]
    six=[1,1,-1,1,1,1,1,-1,1,1,-1]
    three=[1,-1,1,1,-1,1,1,1,1,-1,-1]
    one=[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

    
    submission=Submission("test")
    
    submission.header("Aoife Citizen")
    
    submission.section("matrix")
    submission.matrix_print("C",matrix)

    submission.section("test patterns")
    submission.seven_segment(six)
    submission.qquad()
    submission.seven_segment(three)
    submission.qquad()
    submission.seven_segment(one)

    submission.section("pretending to evolve the pattern")

    test_pattern=six[:]
    
    for i in range(0,10):
        submission.seven_segment(test_pattern)
        submission.qquad()
        if (i%6)==5:
            submission.cr()
            submission.cr()
        change=rnd.randint(0,len(test_pattern)-1)
        test_pattern[change]*=-1


    submission.section("pretending to evolve the pattern with energies")

    test_pattern=six[:]
    
    for i in range(0,6):
        submission.seven_segment(test_pattern)
        submission.print_number(round(rnd.random(),4))
        submission.qquad()
        if (i%3)==2:
            submission.cr()
            submission.cr()
        change=rnd.randint(0,len(test_pattern)-1)
        test_pattern[change]*=-1

        
    submission.bottomer()
    
        
