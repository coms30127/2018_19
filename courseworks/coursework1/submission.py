#this will be the programme for creating your submission document
#it is not finished yet

class Submission:
    def __init__(self,filename):
        self.document=open(filename+".tex",'w')

    def header(self,candidate_name):
        self.document.write("\\documentclass[a4paper,fontsize=12pt]{scrartcl}\n")
        self.document.write("\\begin{document}\n")
        self.document.write("\\section*{"+candidate_name+"}\n")

    def section(self,section_name):
        self.document.write("\\subsection*{"+section_name+"}\n")
        
    def matrix_print(self,matrix_name,matrix):
        n=len(matrix)
        r=len(matrix[0])
        self.document.write("$$ "+matrix_name+"=\\left(\\begin{array}{")
        for i in range(0,r):
            self.document.write("c")
        self.document.write("}\n")
        for j in range(0,n):
            for i in range(0,r):
                self.document.write(str(matrix[j][i]))
                if i!=r-1:
                    self.document.write("&")
            self.document.write("\\\\")
        self.document.write("\\end{array}\\right)$$")

        
    def bottomer(self):
        self.document.write("\\end{document}")
        self.document.close()


if __name__ == '__main__':

    matrix=[[i+j for j in range(0,4)] for i in range(0,3)]
        
    submission=Submission("test")
    submission.header("Aoife Citizen")
    submission.section("matrix")
    submission.matrix_print("C",matrix)
    submission.bottomer()
    
        
