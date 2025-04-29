#================================================
#Farhad Ghaherdoost data analysis
#================================================
import streamlit
# Function for fibonacci
def fibonacci(n):
    #Fibonaccis formula f(n) = f(n-1) + f(n-2) and if n>= 2 then f(0) = 0, f(1) = 1
    sqnce = [0,1]
    for _ in range(2,n):

        next_num = sqnce[-1] + sqnce[-2]

        sqnce.append(next_num)

    return sqnce
#be asure about the user enter the right value for input
try:
    #input
    n = streamlit.chat_input('enter a number(such as 7)')
    seq = fibonacci(int(n))

    #output
    streamlit.write(result := ",".join(str(i) for i in seq))
    
except:
    #warning
    streamlit.warning('!!!(Input must be a number, Try Again.)!!!')

