#calculate the equivalent resistance
def calc_Req(R1, R2):
    return (R1*R2)/(R1+R2)

def calculate(R1, R2, n=1):
    #we assume the enough times of iteration is 500 as infinite
    if(n == 500):
        return calc_Req(R1, R2)
    return R1 + calc_Req(R2, calculate(R1, R2, n+1))

R1 = int(input('Please Enter The Value of R1: '))
R2 = int(input('Please Enter The Value of R2: '))

print('The Equivalent Resistance is: ', calculate(R1, R2))