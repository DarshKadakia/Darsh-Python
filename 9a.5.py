lst=["Aryabhatta","Jay","Vaidik","bhuvneshwerkumar","smit","Chankya","Shivraman","Pavish"]

lst_name=list(filter(lambda x:isinstance(x,str) and len(x)>8,lst))

print(lst_name)
