alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

def print_rangoli(size):
    # top
    top = ""
    for j in range(size-1):
        line = ""
        dashes = (size-j-1)*2
        for d in range(dashes):
            line += "-"
        pos = size  - 1
        for i in range(j+1):
            line += alpha[pos] 
            if i != j:
                line += "-"
            pos -= 1
        line += "".join(reversed(line[:len(line)-1])) + "\n"
        top += line
    # the center code
    center = ""
    pos = size - 1
    for i in range(size-1):
        center += alpha[pos] + "-"
        pos -= 1
    center += 'a' + center[::-1]
    
    ans = top + center + "\n" + "".join(reversed(top[:len(top)-1]))
    
    
    print(ans)

if __name__ == '__main__':
