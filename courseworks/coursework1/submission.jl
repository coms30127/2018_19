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


f=open("./test.tex","w")

header(f,"Aoife Citizen")
section(f,"A matrix")
bottomer(f)

close(f)
