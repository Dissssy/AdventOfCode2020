#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
group = text_file.read().split('\n\n')
group[len(group) - 1] = group[len(group) - 1][:-1]

count = 0
people = []
for i in range(0, len(group)):
    people = group[i].split('\n')
    answers = "".join(set(group[i].replace('\n', '')))
    idkwhat = ""
    for j in range(0, len(people)):
        idkwhat = idkwhat + people[j]
    for j in range(0, len(answers)):
        if(idkwhat.count(answers[j]) == len(people)):
            count += 1

print(count)
