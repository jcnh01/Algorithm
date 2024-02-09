word = input()

a = 0

for i in range(len(word)) :
    if word[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='] :
        a = a + 1;
    if word[i:i+3] in ['dz='] :
        a = a + 1;

print(len(word) - a)