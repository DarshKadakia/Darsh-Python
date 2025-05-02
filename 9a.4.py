lst = ['madam','Python',"malayalam",12321]

lst_palindrome=list(filter(lambda n:isinstance(n,str) and n[::-1]==n,lst))

print(lst_palindrome)
