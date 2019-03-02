
# Function to convert decimal to binary 
def decimal_to_binary(dec): 
    decimal = int(dec) 
    # Prints equivalent decimal 
    return bin(decimal).replace("0b","")
  
# Function to convert decimal to octal 
def decimal_to_octal(dec): 
    decimal = int(dec)
    # Prints equivalent decimal 
    return oct(decimal).replace("0o","")
  
# Function to convert decimal to hexadecimal 
def decimal_to_hexadecimal(dec): 
    decimal = int(dec) 
    # Prints equivalent decimal 
    return hex(decimal).replace("0x","")
  
def print_formatted(num):
    # your code goes here
    e = len(str(decimal_to_binary(num)))
    for number in range(1, num+1):
        n = str(number)
        n = (e-len(n))* " " + n
        b = str(decimal_to_binary(number))
        b = (e-len(b) )*" " + b
        o = str(decimal_to_octal(number))
        o = (e-len(o))*" " + o
        h = str(decimal_to_hexadecimal(number)).upper()
        h = (e-len(h))*" " + h

        print("%s %s %s %s" % (n, o, h, b))
    
    

if __name__ == '__main__':
