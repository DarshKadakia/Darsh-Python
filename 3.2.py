def strup(strings: str) -> None:
    result = ""
    for char in strings:
        if "a" <= char <= "z":  
            result += chr(ord(char) - 32)  
        else:
            result += char  
    print(result)
    
def strdown(strings: str) -> None:
    result = ""
    for char in strings:
        if "A" <= char <= "Z":  
            result += chr(ord(char) + 32)  
        else:
            result += char  
    print(result)
    
def strtoggle(strings: str) -> None:
    result = ""
    for char in strings:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
             result += chr(ord(char) + 32)
    print(result)
    
strings = input("Enter string: ")
strup(strings)
strdown(strings)
strtoggle(strings)