# read from file
# opening input file and saving each line in a list called 'list_of_cals'
with open("input.txt") as file:
    rucksack_file_list = file.readlines()
    rucksack_file_list = [line.rstrip() for line in rucksack_file_list]

for i in rucksack_file_list:
    firstCompartment = i[:len(i)//2]
    secondCompartment = i[len(i) // 2:]

    print("Current value is:", i)
    print("First Compartment of current value is:", firstCompartment)
    print("Second Compartment of current value is:", secondCompartment)

    for char in range(len(firstCompartment)):
        if firstCompartment[char] == secondCompartment[char]:
            print("Duplicates:", firstCompartment[char])

    print()
