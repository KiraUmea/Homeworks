python_gr = {'Ivan', 'Evgen', 'Yuri'}
java_gr = {'Ivan', 'Maria', 'Alex', 'Anna'}
frontend_gr = {'Elena', 'Anna', 'Evgen'}
fullstack_gr = {'Elena', 'Alex', 'Anna'}

print("There are students who learn at least in 2 groups:\n")
two_group_st = [python_gr & java_gr, python_gr & frontend_gr, python_gr & fullstack_gr, frontend_gr & fullstack_gr, java_gr & frontend_gr, java_gr & fullstack_gr]
sorted(two_group_st)
print(two_group_st)

not_frontend = (python_gr | java_gr | fullstack_gr) - frontend_gr

print(f"There are students, who don't learn frontend:\n {not_frontend}")

print(f"There are students who learn python or java:\n {python_gr | java_gr}")

