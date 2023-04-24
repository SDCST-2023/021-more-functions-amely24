#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""

def triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    else:
        sides = sorted([a, b, c])
        a, b, c = sides
        if a**2 + b**2 == c**2:
            return 2
        cos = (a**2 + b**2 - c**2) / (2*a*b)
        if cos < 0:
            return 3
        
        return 1

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
