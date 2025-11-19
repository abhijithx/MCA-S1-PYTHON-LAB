
with open('input.txt', 'r') as source:

    with open('output.txt', 'w') as dest:
        
        lines = source.readlines()
        
        
        for i in range(0, len(lines), 2):
            dest.write(lines[i])