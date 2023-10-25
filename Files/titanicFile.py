PATH_NAME = '/Users/hellenmarjoriewanyana/Desktop/OOP/Files/titani.csv'

# #part1
# with open(PATH_NAME,encoding = "utf-8") as f:
#     titanic = f.read()

# print(titanic)

# #part2
# with open(PATH_NAME,encoding = "utf-8") as f:
#     lines = f.readlines()

# num_of_lines = 0
# for line in lines:
#     num_of_lines += 1

# print(f"\n Number of lines: {num_of_lines}")

#part3
with open(PATH_NAME,encoding = "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        names = line.strip('"')
        #names = line.split(",")
        print(names)


