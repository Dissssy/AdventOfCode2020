#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
group = text_file.read().split('\n\n')

count = 0
for i in range(0, len(group)):
    group[i] = group[i].replace('\n', '')
    count += len("".join(set(group[i])))

print(count)
