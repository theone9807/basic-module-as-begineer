"""This is the basic module created by me as a python developer begineer"""

def time_and_work(a,b):
    """this func. is used to calculate days in which a+b can do a work
       a = days in which a can complete a work
       b=days in whis b can complete a work"""

    w1 = (1/a)+(1/b)
    w2 = 1/w1
    w3 = round(w2,2)
    return w3

def matrix_multiplication_2x2(a11,a12,a21,a22,b11,b12,b21,b22):
    """This funstion is to calculae matrix multiplication"""
    print(f'[{((a11*b11)+(a12*b21))}   {((a11*b12)+(a12*b22))}]')
    print(f'[{((a21*b11)+(a22*b21))}   {((a21*b12)+(a22*b22))}]')
    

def nth_term_of_ap(a,n,d):
    """This funstion is to calculte nth term of AP"""
    tn = a + (n-1)*d
    return tn

def sum_of_n_terms_of_ap(n,a,d):
    """This funstion is to calculte sum of nth term of AP"""
    Sn = (n/2)*((2*a) + (n - 1)*d)
    return Sn

def nth_term_of_gp(a,r,n):
    """This funstion is to calculte nth term of GP"""  
    tn = a*(r)**(n-1)
    return tn

def an_diff_bn(a,b,n):
    #calulates an - bn
    return (a**n)-(b**n)


def roots_of_quadratic_eq(a,b,c):
    """This funstion is to calculte rootes of quaderatic equation"""
    x1 = (-b + ((b)**2 - (4*a*c))**(0.5))/(2*a)
    x2 = (-b - ((b)**2 - (4*a*c))**(0.5))/(2*a) 
    
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    
    

def no_of_diagonals_in_polygon(s):              #here n = number of sides 
    """This funstion is to calculte no. of diagonals in polygon"""
    d = (s*(s-3))/2
    return d

dictionary = {'A':'Ampere','AC':"Alternating Current",'ADC':'Analog to digital converter'}


