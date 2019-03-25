import textwrap
def ui(s):
    a = ""
    for i in s:
        if i not in a:
            a += i
    return a
    
def merge_the_tools(string, k):
    # your code goes here
    num =  k
    li = textwrap.wrap(string, num)
    for i in li:
        print("".join(ui(i)))

if __name__ == '__main__':
