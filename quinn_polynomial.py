# Tyler Quinn
# CPSC 21000 - Programming Fundamentals

#The purpose of this program is to accurately solve a custom polynomial of the user's choosing 



# Centered heading 
print('*'* 60)
print('*%58s*' % "POLYNOMIAL PLOTTER".center(58))
print('*'* 60)

print('')


#Ask the user for the degree of the polynomial they want to calculate 

polynomial_degree = 0
polynomial_degree_selector = 0
go_again = 0
first_degree = 0
second_degree = 0
third_degree = 0
fourth_degree = 0
constant_term = 0
starting_x = 0
ending_x = 0
a = 0
b = 0
c = 0
x = 0

while go_again == 0:
    polynomial_degree = 0
    polynomial_degree_selector = 0
    first_degree = 0
    second_degree = 0
    third_degree = 0
    fourth_degree = 0
    constant_term = 0
    starting_x = 0
    ending_x = 0
    a = 0
    b = 0
    c = 0
    x = 0


    while polynomial_degree == 0:

        print('Select your polynomial degree: ')
        print('1')
        print('2')
        print('3')
        print('4')
        polynomial_degree = float(input('Enter the degree of your polynomial: '))
        polynomial_degree_selector = polynomial_degree


    #Ask the user for the coefficients of the terms that are relevant for that degree

    #Identify mathematical statement 

    while polynomial_degree_selector == 1:

        first_degree = float(input('Select the coefficient for the first degree term (x): '))
        constant_term = float(input('Select the coefficient for the constant term: '))
        mathematical_statement = ('%.2fx + %.2f' %(first_degree, constant_term))
        polynomial_degree_selector = 5
        

    while polynomial_degree_selector == 2:

        second_degree = float(input('Select the coefficient for the second degree term (x^2): '))
        first_degree = float(input('Select the coefficient for the first degree term (x): '))
        constant_term = float(input('Select the coefficient for the constant term: '))
        mathematical_statement = ('%.2fx^2 + %.2fx + %.2f' %(second_degree, first_degree, constant_term))
        polynomial_degree_selector = 5
        
    

    while polynomial_degree_selector == 3:

        third_degree = float(input('Select the coefficient for the third degree term (x^3): '))
        second_degree = float(input('Select the coefficient for the second degree term (x^2): '))
        first_degree = float(input('Select the coefficient for the first degree term (x): '))
        constant_term = float(input('Select the coefficient for the constant term: '))
        mathematical_statement = ('%.2fx^3 + %.2fx^2 + %.2fx + %.2f' %(third_degree, second_degree, first_degree, constant_term))
        polynomial_degree_selector = 5
    
        

    while polynomial_degree_selector == 4:

        fourth_degree = float(input('Select the coefficient for the fourth degree term (x^4): '))
        third_degree = float(input('Select the coefficient for the third degree term (x^3): '))
        second_degree = float(input('Select the coefficient for the second degree term (x^2): '))
        first_degree = float(input('Select the coefficient for the first degree term (x): '))
        constant_term = float(input('Select the coefficient for the constant term: '))
        mathematical_statement = ('%.2fx^4 + %.2fx^3 + %.2fx^2 + %.2fx + %.2f' %(fourth_degree, third_degree, second_degree, first_degree, constant_term))
        polynomial_degree_selector = 5
        
        


    #Ask the user for the starting and ending values of x 

    starting_x = int(input('Select the starting value of x: '))
    ending_x = int(input('Select the ending value of x: '))

    print('')
    print('')

    #Print evaluative statement 

    evaluative_statement = ('Here is f(x) = %s over domain [%.2f,%.2f]' %(mathematical_statement, starting_x, ending_x))

    print(evaluative_statement)

    print('')

    #Table Header

    print('-'*20)

    print('|%s | %s|' % ('x'.center(8),'f(x)'.center(8)))
    print('-'*20)

    #Find the number of items going to be solved for 

    domain_list = [starting_x, ending_x + 1]

    for x in range(starting_x, ending_x + 1): 
        #print('%.2f' %(x))
        

    #Solve for x

        if polynomial_degree == 1:
            solution_output = first_degree * (x) + constant_term
            print('|%8.2f | %8.2f |' %(x,solution_output))

        if polynomial_degree == 2: 
            solution_output = second_degree * (x * x) + first_degree * (x) + constant_term 
            #print(solution_output)
            #print ('f(x) at %.2f is %.2f' %(x,solution_output))
            print('|%8.2f | %8.2f |' %(x,solution_output))

        if polynomial_degree == 3: 
            solution_output = third_degree * (x * x * x) + second_degree * (x * x) + first_degree * (x) + constant_term 
            print('|%8.2f | %8.2f |' %(x,solution_output))

        if polynomial_degree == 4: 
            solution_output = fourth_degree * (x * x * x * x) + third_degree * (x * x * x) + second_degree * (x * x) + first_degree * (x) + constant_term
            print('|%8.2f | %8.2f |' %(x,solution_output))

    print('-'*22)
    print('')
    print('')
    print('Would you like to go again?')
    print('')
    print('')
    print('0: I would like to go again')
    print('1: I am finished')
    print('')
    go_again = float(input('Enter the number which applies: '))

while go_again == 1: 
    print('')
    print('Thank you for using this program.')
    go_again = 2
    








