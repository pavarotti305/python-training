print('')
print('''Here is the structure:
if expression: like on this example if var1 is true that means = 1 print the value of true expression
statement(s)
else: else var1 is false that means = 0 print the value of false expression
statement(s)''')

truevalue = 1
if truevalue:
    print("1 - Got a true expression value")
    print(truevalue)
else:
    print("1 - Got a false expression value")
    print(truevalue)

falsevalue = 0
if falsevalue:
    print("2 - Got a true expression value")
    print(falsevalue)
else:
    print("2 - Got a false expression value")
    print(falsevalue)

print("Good bye!")
print('')

print('''Here is the second structure with elif:
if expression1:
elif expression2:
   statement(s)
elif expression3:
   statement(s)
else:
statement(s)''')

var = 100
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Corresponding to a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)

print("Good bye!")

print('''Python operators:
+ Addition Adds values on either side of the operator.
- Subtraction Subtracts right hand operand from left hand operand.
* Multiplication Multiplies values on either side of the operator
/ Division Divides left hand operand by right hand operand
% Modulus Divides left hand operand by right hand operand and returns remainder
** Exponent Performs exponential (power) calculation on operators
// 	Floor Division - The division of operands where the result is the quotient in which the digits after
the decimal point are removed. like 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0
== If the values of two operands are equal, then the condition becomes true.
!= If values of two operands are not equal, then condition becomes true.
<> If values of two operands are not equal, then condition becomes true.
> If the value of left operand is greater than the value of right operand, then condition becomes true.
< If the value of left operand is less than the value of right operand, then condition becomes true.
>= If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
<= If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
= Assigns values from right side operands to left side operand c = a + b assigns value of a + b into c
+= It adds right operand to the left operand and assign the result to left operand c += a is equivalent to c = c + a
-= Subtract AND subtracts right operand from the left operand and assign the result to left operand c -= a = c = c - a
*= Multiply AND c *= a is equivalent to c = c * a
/= Divide AND c /= a is equivalent to c = c / a
%= Modulus AND c %= a is equivalent to c = c % a
**= Exponent AND c **= a is equivalent to c = c ** a
//= Floor Division c //= a is equivalent to c = c // a''')
