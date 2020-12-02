#open the file and parse it into a list of strings on newlines
text_file = open("input.txt", "r")
lines = text_file.read().split('\n')

#every input text file has an empty newline at the end, delete it
lines.pop(-1)

#convert every string in the list to an int
for i in range(0, len(lines)): 
    lines[i] = int(lines[i]) 

#define the main loop
#iterate through every int in the list
#for every int on the list iterate through every int after the current int in the list
#add the main int and the second int together, check if they sum to 2020
#if sum is 2020, multiply them together and return
def main_loop():
    for i in range(0, len(lines)):
        for j in range(i + 1, len(lines)):
            if lines[i] + lines[j] == 2020:
                return (lines[i] * lines[j])

#run the main loop, print the output
print(main_loop())
