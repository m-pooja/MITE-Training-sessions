# MITE-Training-sessions
dates: 9th July to 21st July 2018
Content covered:
DAY1:-
Fundamentals of Python:
Numbers: Floats, Integers
Arithmetic operations
String, String operations, Slicing
Control statements
range function
.format
print('Insert one string : {}'.format(s))
students = 'Forty'
print('There are %s students in the class.' % students  )
students = 42
print('There are %d students in the class.' % students)

List, List operations, Slicing

P1: WAP to display 'is there' and 'no-more' if a character is there in a string or not. User will provide a string user will provide the   character.

P2:WAP to display an input string  like this:-
'computer'
r				computer
er				compute
ter				comput
uter				compu
puter				comp
mputer			com
omputer			co
computer			c

P3: Ask the user to input a word in English. Make sure the user entered a valid word. Convert the word from English like this:-
Input : SUKUN
Output : UKUNSPK
[(2nd alphabet to end) + 1st alphabet + ‘PK’]. Display the translated result.

P4: input a string, go through it, and if the length of a word is even, print 'Even' else print 'odd'.

P5: WAP that prints the integers from 1to100.  but for multiples of 3 print 'FUZZ' and multiples of 5 print 'BUZZ' for numbers which are multiple of both 3 and 5 print'FIZZBUZZ'.

DAY2:
Fundamentals of Python:
List remaining operations
Tuple, operations, indexing
Dictionaries, operations, indexing
Sets, operations
Booleans
Type conversion
Functions
List comprehension
map()
enumerate()
zip()
filter()
reduce()
lambda expression
import
P1: Display 420 without using integer.
P2: WAP to create a function which takes a sentence as an input if any letter in it is 'A' or 'a' convert it to 'X'. Return the updated sentence.
P3: Finding factorial.
P4: Displays which Letters are in the First String but not in the Second.
P5: Create a function such that where the first occurrence of replace_string in test_string is replaced by bodega.  
Tests:  
replace("Hi how are you?", "you") should return 
"Hi how are bodega?"
P6: Remove the nth index character from a non-empty string.
P7: WAP to detect if two strings are anagrams.
P8: WAP to read a list of words and return the length of the longest one.
P9: Program to check if a number is a palindrome.
P10: Define a function scrabble_score that takes a string word as input  and returns the equivalent scrabble score for that word. Assume your input is only one word  containing no spaces or punctuation.  As mentioned, no need to worry about score multipliers! 
For example: the word "Helix" would score 15points due to the sum of the 
letters: 4 + 1 + 1 + 1 + 8. 
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,"r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,"x": 8, "z": 10}
P11: 'Tour Cost Estimating System'
------------------------------------------------------------------------------
Define a function called 'plane_ride_cost' that takes a string, city, as input.
The function should return a different price depending on the location.
Below are the valid destinations and their corresponding  round-trip prices.
•	"delhi": 2000
•	"chennai": 3400
•	"bangalore": 5400
•	"mumbai": 4750

	Define a function for 'Hotel_cost' based on number of nights stayed and type of room.

	Define a function called rental_car_cost with an argument called days. Calculate the cost of renting the car: Every day you rent the car costs INR40. 	if you rent the car for 7 or more days, you get INR50 off your total. Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 	You cannot get both of the above discounts. Return that cost.
Define a function 'total_trip_cost' which should return the sum of all the costs (plane ride cost, rental car cost, hotel cost)
-------------------------------------------------------------------------------------------
User-side: he/she should only be able to do following:
enter the destination place
enter the type of room required 
enter the number of days for trip
**All the functionalities be hidden from the user.
Note: use 'import'.
P12: 'Shopping cart'
Create three functions one each for vegetables, fruits and milk product. User can pick any item out of these and user will tell the quantity required.
Create another function to calculate the total shopping cost.
if any item is not available, let the user know about it.
keep appending a text file with the cost from each section (vegetable, fruit, milk product).
once the shopping is complete, print back the details of the purchase with total cost and user name/user ID to the user from the text file.

DAY4: Numpy, Scipy titanics dataset.
	creating ndarray
		 using list
		.arrage()
		.random.randint()
		.random.rand()
		.random.randn()
		.zeros()
		.ones()
		.eye()
		.linspace()
.reshape()
.shape
.max(), .min()
.argmax(), .argmix()
Indexing of array, 2d array.
Slicing on array, 2d array.
Conditional selection.
.mean(), .meadian(), .std(), .var(), .sum(), .sum(axis=0)
.sqrt(), .exp()
np.nan()
array broadcasting like array*2
.flags.writeable (making files read-only)
np.getfromtxt('')
.shuffle()
DAY5: Pandas, matplotlib, titanics dataset, drinks dataset.
Creating pandas series 
		with lists, array, dictionaries, labels with data.
		in  line by filling data and index values  
Creating pandas Dataframe
		with lists, array, dictionaries, labels with data.
		using random with index values and column names
Accessing values using indexing and index names.
.idxmax()
.idxmin()
.iloc()
.loc()
.ix()
Checking for type of dataframe and series in it.
Applying conditional slicing on whole dataframe.
Applying conditional slicing on dataframe to access one or more columns.
use | and &.
.reset_index()
Adding a new column in data frame.
.set_index()
Handling missing values using .isnan(), .fillnan(), .dropnan()
.unique()
.duplicates()
.drop_duplicates()
Reading from file :-
		pd.read_csv()
		pd.read_excel()
writing dataframe in a file:-
		.to _csv()
		.to_excel()
plotting dataframe:
		.hist(), .scattermatrix()
importing matplotlib.pyplot
Plotting histogram,  scatter, pie chart, bar chart,boxplots, area plots.
DAY6: Practice session on 'groupby' and '.apply' methods.
 Introduction to Machine Learning.
 Practice session on Feature scalling using sklearn.preprocessing tools on 'iris' dataset,  like 	
	MinMaxNormalizer
	Standardizer 
	Normalizer 
Worked on Principal Component analysis.
DAY7: Supervised learning: Classification and Regression.
Datasets: iris, wine quality prediction, players dataset.
Basic steps to develop a ML model using sklearn
Understanding classification, regression and implementing:-
Linear Regression
Logistic Regression
K-NN Classifier
Naive-Bayes Classifier (MultimonialNB, GaussianNB, BernoulliNB)
Accuracy, MSE, Confusion matrix, AUC
sklearn.metrics for mean_squared_error
sklearn.metric for accuracy-score, confusion matrix
DAY8: Understanding and implementing :-
K-means clustering algorithm and Neural Network
Unit-Test Framework
Technical discussion on projects allotted. 
