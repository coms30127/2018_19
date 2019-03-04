#submission file for julia, not finished obviously

function header(document::IOStream,candidate_name::String)
    write(document,"\\documentclass[a4paper,fontsize=12pt]{scrartcl}\n")
    write(document,"\\usepackage{tikz}\n")
    write(document,"\\begin{document}\n")
    write(document,"\\section*{$candidate_name}\n")
end

function section(document::IOStream,section_name::String)
    write(document,"\\subsection*{$section_name}\n")
end

function bottomer(document::IOStream)
    write(document,"\\end{document}")
end

function seven_segment_display(document::IOStream,pattern::Vector{Int64})
        
    write(document,"\\begin{tikzpicture}\n")

    segment_direction=Dict(7=>"(0,0)--(1,0)",6=>"(1.05,0.05)--(1.05,1.05)",5=>"(-.05,0.05)--(-.05,1.05)",4=>"(0,1.10)--(1,1.10)",3=>"(1.05,1.15)--(1.05,2.15)",2=>"(-.05,1.15)--(-.05,2.15)",1=>"(0,2.20)--(1,2.20)")
    
    function write_draw(segment_status)
        if segment_status==1
            write(document,"\\draw[ultra thick,color=red]")
        else
            write(document,"\\draw[thick,color=lightgray]")
        end
    end

    for (segment,status) in enumerate(pattern)
        write_draw(status)
        write(document,segment_direction[segment])
        write(document,";\n")
    end

    write(document,"\\end{tikzpicture}\n")

end


        
function  matrix_print(document,matrix_name,matrix,rounding=2)
    (n,r)=size(matrix)
    write(document,"\$\$ $matrix_name=\\left(\\begin{array}{")
    for i in 1:r
        write(document,"c")
    end
    write(document,"}\n")
    for j in 1:n
        for i in 1:r
            entry=string(round(matrix[j,i],rounding))
            println(entry)
            write(document,entry)
            if i!=r
                write(document,"&")
            end
        end
        write(document,"\\\\")
    end
    write(document,"\\end{array}\\right)\$\$\n")
end

function seven_segment(document::IOStream,pattern::Vector{Int64})
    seven_segment_display(document,pattern[1:7])

    number=0::Int64

    function to_bool(a)
        if a==1
            true
        else
            false
        end
    end
    
    for (i,b) in enumerate(map(to_bool,pattern[8:11]))
        if b
            number+=2^(i-1)
        end
    end

    write(document,"$number\n")

end



f=open("./test.tex","w")

header(f,"Aoife Citizen")
section(f,"A matrix")
example_matrix=rand(-1.0:0.01:2.0, 3, 4)
matrix_print(f,"C",example_matrix)

six=Int64[1,1,-1,1,1,1,1,-1,1,1,-1]
three=Int64[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=Int64[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(f,three)



bottomer(f)

close(f)

