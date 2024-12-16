Input:
This program takes an input array of numbers as key word parameter.
Output:
This program outputs a string with decision if the array is Prime number array or not using iteration and recursion methods.

Approach:
It is solved using both iteration and recursion.

For iteration algorithm:
I am looping through the array using a function "is_array_prime_iter"  and taking each element  for Prime and first check with base condition then test for divisors.
    1. if element is less than equal to 1 then "Not Prime" then it exits out
    2. if element is 2 or 3 then Prime and save the result = "true" in a variable and append in list "results" to check
    for each elemnt if they are all "true" then it will return the "final" as "true".
    3. Nested loop continously divide the element for different numbers less than equal to round(math.sqrt(i))+1 and see if
    remainder is 0. Here I am starting to divide by a high number and coming down to 2. If the remainder is 0 for any scenario
    then the element has a divisor and not a prime number. I am saving the result as "true" or "false" for each element test
    and saving in an array "results". If any result is "false" then the array is not a Prime number array. That final result is written in "final" variable.
    4. The decision for the entire array to be Prime or not is coming from "final" variable.
    5. "main" function calls the "is_array_prime_recur" function and saves result in "final_iter" variable.

For recursion algorithm:
I am using two functions :
    is_array_prime_recur - to loop through each element and saves the result of the array check in "final" variable.
    It calculates "final" variable value from "results" array where each element's check result is stored.
    is_prime_recur  - to check individual element. This function returns "result" variable with the result of "true" or "false" for each element check.
For recursion we start from low, the divisor = 2 and go until math.sqrt(i) each time increment by 1 and divide to check if remainder is 0.

TODO:
There is a bug in the code which makes 567 number to return as Prime="true" although it is supposed to be false.
I think it is an edge case and has to do with the math formula I am using "math.sqrt(i)"