# Your solution may ONLY use the python modules listed below
# program: Lab1main.py
# author:  Harjaspreet Singh
# date:4/09/2022    
# purpose: Creating a function which will draw a pyramid and ThreeNumber combinations




def drawPyramid(rows):
    for i in range (rows):
        letters = string.ascii_letters[:i +1]
        space = " " * (rows-i-1)
        space += letters[0 : i + 1] + ''.join(reversed(letters[:len(letters)-1]))
        print(space)
   
def threeNumberCombinations(num):
    for a in range(1, num+1):    # this is a range from 1 to num which is specified and the +1 is because the index of an array starts at 0.
        for b in range(1, num+1):
            for c in range(1, num+1):
                
                threeCombo= str(a) + str(b) + str(c)
                print(threeCombo)
                    



