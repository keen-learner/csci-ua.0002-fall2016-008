"""
bauble_boutique.py (15 points) (1 point extra credit)
=====
You're the manager of a tiny boutique that sells Python related gifts and 
knick-knacks (like plush Python stuffed animals, Guido Van Rossum bobble head
dolls, etc. ). Unfortunately, your cash register stopped working, so you 
decide to write your own program to display receipts and print out change.

Here's what your program should do:

1. Ask the cashier for information regarding the items purchased. It will 
   assume that everyone buys exactly three items (!?). For every item:
   a. ask for name of the item
   b. ask for the price (assume that users will always enter a number with a 
      decimal point)
   c. ask for quantity (assume that users will always enter a whole number)
2. Ask the cashier for how much the user paid. Assume that the amount paid
   is at least as much as the total owed 
3. Print out a receipt that contains the following information:
   a. name, price, quantity and total cost per item purchased
   b. the total cost of all of the items
   e. the total amount paid
   f. the change owed, followed by a break down of how many of each 
      denomination will be given back:
      * 10 dollar bills
      * 5 dollar bills
      * 1 dollar bills
      * quarters
      * dimes 
      * nickels 
      * pennies 
   g. it will always print out the number of bills/coins for each denomination, 
        even if the quantity is 0
4. The receipt should be in the following format:
   a. the width of the receipt is 50 characters long total
   b. it has a center aligned title: PREMIER PYTHON PLAZA RECEIPT
   c. followed by a line created by equal signs that's 80 characters long (===)
      * __DO NOT TYPE OUT__ 50 ='s ... use what we learned about Python types,
        operators, etc. to do this
   d. print out the costs per item
   e. print out another line created by equal signs
   f. print out the calculations for total item cost amount paid, and change
   g. print out another line created by equal signs
   h. print out the number of tens, fives, etc. 
   i. "headings" in a line are left justified: item name x quantity ... cost
   j. prices / costs:
      * are right justified
      * have a dollar sign
      * have two decimal places
      * hint: you may have to use format more than once to get the decimal
        places... but then you'll need to add a dollar and format again!
   k. assume that all item names and costs are less than 40 characters long
   l. see the sample interaction below
      * everything after the > (greater than sign) is user input
      * the receipt is at the end
      * __YOUR OUTPUT SHOULD MATCH THE OUTPUT BELOW!__
5. __COMMENT YOUR SOURCE CODE__ by 
   a. briefly describing sections of your program (for example "# calculates the number of quarters, dimes, nickels and pennies" could go above the part of your code that runs those calculations). 
   b. include your name, the date, and your class section at top of your file (above everything else)

What is the name of the first item?
> Guido Van Rossum Bobble Head
How much does the first item cost?
> 30
How many are being purchased?
> 3
What is the name of the second item?
> Python Stuffed Animal
How much does the second item cost?
> 29.99
How many are being purchased?
> 1
What is the name of the third item?
> Hello World T-Shirt
How much does the third item cost?
> 37.50
How many are being purchased?
> 3
How much was paid?
> 2048

           PREMIER PYTHON PLAZA RECEIPT
==================================================
3 x Guido Van Rossum Bobble Head            $90.00
1 x Python Stuffed Animal                   $29.99
3 x Hello World T-Shirt                    $112.50
==================================================
TOTAL COST OF ITEMS                        $232.49
AMOUNT PAID                               $2048.00
CHANGE                                    $1815.51
==================================================
CHANGE:                                           
181 x tens                                        
1 x fives                                         
0 x ones                                          
2 x quarters                                      
0 x dimes                                         
0 x nickels                                       
1 x pennies                                       
==================================================


EXTRA CREDIT 
=====

* __USE CALCULATIONS TO DETERMINE MANY SPACES__ to pad your title with (do not 
  just write out space characters manually)
* you can use the built-in function, len to get the length of a string
* len("hello") --> 5
* remember that the 2nd parameter to the format function is a string that 
  determines how a string is formatted
* can you construct that string dynamically with the length of the title?
"""
