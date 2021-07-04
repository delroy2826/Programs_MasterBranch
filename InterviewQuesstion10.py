
def SimpleSymbols(str1):
    for i in str1:
        if i.isalpha():
            if "+"+i+"+" in str1:
                a=True
            else:
                return False
    return a

# keep this function call here
print(SimpleSymbols("==a+"))