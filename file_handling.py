with open("employees.txt", encoding="utf-8") as f:
    # print(type(f))
    # print(f.read())
    for line in f:
        #print(line, end="")
        print(line.strip())

with open("employees_temp.txt", "a", encoding="utf-8") as f:
    f.write("árvíztűrőtükörfúrógép\n")
    f.write("John Doe\n")
    f.write("Jack Doe\n")
