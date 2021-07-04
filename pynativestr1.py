#https://pynative.com/python-string-exercise/
#Exercise Question 1: Given a string of odd length greater 7,
#return a string made of the middle three chars of a given String
def sep(str1):
    mid = len(str1)//2
    return str1[mid-1]+str1[mid]+str1[mid+1]
str1 = 'JhonDipPeta'
print("Middle Three characters are:",sep(str1))