#* OPERATORS:used to perform operations on variables and values

#   ARITHMETIC OPERATORS :
#*   Operator	    Name	            Example	
#*   +	            Addition	        x + y	
#*   -	            Subtraction	        x - y	
#*   *	            Multiplication	    x * y	
#*   /	            Division	        x / y	
#*   %	            Modulus	            x % y	
#*   **	            Exponentiation	    x ** y	
#*   //	            Floor division	    x // y

# ASSIGNMENT OPERATORS :
#   Operator	Example	        Same As
#*   =	        x = 5	        x = 5	
#*   +=	        x += 3	        x = x + 3	
#*   -=	        x -= 3	        x = x - 3	
#*   *=	        x *= 3	        x = x * 3	
#*   /=	        x /= 3	        x = x / 3	
#*   %=	        x %= 3	        x = x % 3	
#*   //=	    x //= 3	        x = x // 3	
#*   **=	    x **= 3	        x = x ** 3	
#*   &=	        x &= 3	        x = x & 3	
#*   |=	        x |= 3	        x = x | 3	
#*   ^=	        x ^= 3	        x = x ^ 3	
#*   >>=	    x >>= 3	        x = x >> 3	
#*   <<=	    x <<= 3	        x = x << 3	
#*   :=	        print(x:=3)	    x = 3

# COMPARISON OPERATORS :
#    Operator	Name	                    Example
#*   ==	        Equal	                    x == y	
#*   !=	        Not equal	                x != y	
#*   >	        Greater than	            x > y	
#*   <	        Less than	                x < y	
#*   >=	        Greater than or equal to	x >= y	
#*   <=	        Less than or equal to	    x <= y

# LOGICAL OPERAOTR :
# Operator	Description	                                                Example	
#* and 	    Returns True if both statements are true	                x < 5 and  x < 10	
#* or	    Returns True if one of the statements is true	            x < 5 or x < 4	
#* not	    Reverse the result, returns False if the result is true	    not(x < 5 and x < 10)

# IDENTITY OPERATOR :
# Operator	Description	                                                Example
#* is 	    Returns True if both variables are the same object	        x is y	
#* is not	Returns True if both variables are not the same object	    x is not y

# MEMBERSHIP OPERATOR :
# Operator	Description	                                                        Example
#* in 	    Returns True if  the specified value is present in the object	    x in y	
#* not in	Returns True if  the specified value is not present in the object	x not in y

# BITWISE OPERATOR :
# Operator	Name	Description	                                                    Example	Try it
#* & 	    AND	    Sets each bit to 1 if both bits are 1	                        x & y	
#* |	        OR	    Sets each bit to 1 if one of two bits is 1	                    x | y	
#* ^	        XOR	    Sets each bit to 1 if only one of two bits is 1	                x ^ y	
#* ~	        NOT	    Inverts all the bits	                                        ~x	
#* <<	    Zero    Shifts binary to the left, adding zeros, dropping left bits	    x << 2	
#* >>	    Signed  Shifts binary right, copies leftmost bit, drops right bits.  	x >> 2



# PRECEDENCE OPERATOR :describes the order of operations execution.

#* Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
#* print((6 + 3) - (6 + 3))

#* Multiplication * has higher precedence than
#* addition +, and therefor multiplications are
#* evaluated before additions:
#* print(100 + 5 * 3)

#* The precedence order is described in the table below, starting with the highest precedence at the top:

#   Operator	                                    Description
#*  ()	                                            Parentheses	
#   **	                                            Exponentiation	
#*  +x  -x  ~x	                                    Unary plus, unary minus, and bitwise NOT	
#*  * /  //  %	                                    Multiplication, division, floor division, and modulus	
#*  +  -	                                        Addition and subtraction	
#*  <<  >>	                                        Bitwise left and right shifts	
#*  &	                                            Bitwise AND	
#*  ^	                                            Bitwise XOR	
#*  |	                                            Bitwise OR	
#*  ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
#*  not	                                            Logical NOT	
#*  and	                                            AND	
#*  or	                                            OR

#* If two operators have the same precedence, the expression is evaluated from left to right.
#* eg: Addition and subtraction with same precedence so evaluated left to right. print(5+4-7)
