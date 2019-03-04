
include("submission.jl")

f=open("./test.tex","w")

header(f,"Aoife Citizen")
section(f,"A matrix")
example_matrix=rand(-1.0:0.01:2.0, 3, 4)
matrix_print(f,"C",example_matrix)

section(f,"Some seven segment patterns")

six=Int64[1,1,-1,1,1,1,1,-1,1,1,-1]
three=Int64[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=Int64[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(f,three)
qquad(f)

seven_segment(f,three)
qquad(f)

seven_segment(f,three)
cr(f)

section(f,"Practise printing out the energy for MSc student question")
seven_segment(f,three)
qquad(f)
print_number(f,3.2111)
cr(f)

bottomer(f)

close(f)
