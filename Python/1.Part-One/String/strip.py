#without strip
name="     Mr.x     "
print(name)

#with underscore
concate="_"+name+"_"
print(concate)

#with left strip
concate="_"+name.lstrip()+"_"
print(concate)
#with right strip
concate="_"+name.rstrip()+"_"
print(concate)


#with r and l strip
concate="_"+name.lstrip().rstrip()+"_"
print(concate)
#with strip
concate="_"+name.strip()+"_"
print(concate)
