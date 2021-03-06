---
layout: slides
title: Dictionaries 
---
<section markdown="block" class="title-slide">
# Dictionaries
{% include title-slide-footer.html %}
</section>

<section markdown="block">
###  Remember That Counting Frequency of Dice Rolls Assignment?

* roll two thee sided dice simultaneously 1000 times
* (they exist!  what do you think they [look like](http://suptg.thisisnotatrueending.com/archive/14752803/images/1304091112226.jpg)? 
* count the frequency of the results... 2 through 6
* __let's code that up really quickly__
	* generate two random numbers
	* do this 1000 times
	* keep track of the number of times a two is rolled... a three... up through six
	* use multiple assignment for initializing your counts!
</section>

<section markdown="block">
### Dice Rolls Solution 
{% highlight python %}
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	if roll == 2:
		twos += 1
	if roll == 3:
		threes += 1
	if roll == 4:
		fours += 1
	if roll == 5:
		fives += 1
	if roll == 6:
		sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 
{% endhighlight %}
</section>


<section markdown="block">
### Dice Rolls 

Whew!

That was a long if-else.  What if we had to write one for two twenty-sided dice?  

* that would be pretty lengthy
* and consequently error prone

If there were only a way to dynamically create names and associate values to them.

We'll get to that in a second.  First: __compound types, mapping types and dictionaries__...
</section>

<section markdown="block">
###  Revisiting Compound Types

__Compound types__: values that are made up of other values.  

Sequence types are compound types.  We know three sequence types.  __What are they?__

<div class="incremental" markdown="block">
1. string
2. list
3. tuple
</div>
</section>

<section markdown="block">
###  Mapping Types

Another kind of compound type is a mapping types.  

A __mapping type__ is a data type that is made of a collection of keys (think of names) and their associated values.  The only mapping type in Python is a __dictionary__.
</section>

<section markdown="block">
###  Dictionaries

A __dictionary__ is an __unordered__ collection of key/value pairs.  

* __key__ is an item that is used to _look up_ values in a dictionary; think of keys as names or labels.
* keys must be immutable objects (they're usually strings or ints)
* the values that are associated with keys can be any type!
* in other languages dictionaries are called associative arrays or hash tables 
</section>

<section markdown="block">
###  Dictionaries Syntax

Let's take a look at some examples

{% highlight python %}
{"first_name":"joe", "fav_candy":"cleo's"}
{28:"foo", 6:"bar", "entirely different":["baz"]}
{}
{% endhighlight %}

* dictionaries are delimited by curly braces - { and }
* an empty dictionary is {}
* each key value pair in a dictionary is separated by a comma
* keys and values are linked together by a colon, the key before and the value after

(btw, [cleo's are pretty good](http://www.godairyfree.org/wp-content/uploads/2012/11/gomaxgocleo.jpg))
</section>

<section markdown="block">
###  Dictionaries Syntax Continued

__What are the keys and what type are they? What are the values and what type are they?__
{% highlight python %}
d1 = {"first_name":"joe", "fav_candy":"cleo's"}
d2 = {28:"foo", 6:"bar", "entirely different":["baz"]}
{% endhighlight %}

<div class="incremental" markdown="block">
* d1
	* keys - the strings "first_name" and "fav_food"
	* values - the strings "joe" and "cleo's"
* d2
	* keys - the ints 28 and 6 ...and the string "entirely different" 
	* values - the strings "foo" and "bar" ... and the list ["baz"]
</div>
</section>

<section markdown="block">
### Retrieving Values at Keys 

You can use the key like a list index to retrieve a value at that key.  __What does this code print out?__

{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d["first_name"])
print(d["fav_candy"])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
joe
cleo's
{% endhighlight %}
</div>

</section>

<section markdown="block">
### Keys That Don't Exist!

Let's try that again... but with a key that doesn't exist.  __What do you think will happen here?__

{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d["height"])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'height'
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Retrieval Using the get Method

You can also retrieve a value from a dictionary by calling the __get__ method.  __get__ takes two arguments:

* the key of the element you want to retrieve
* an optional default value in case that key doesn't exist yet

__What do you think this code outputs?__

{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
print(d.get("height", None))
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Key/Value Pairs 

So... things are a bit different when adding keys and values to a dictionary.  There is __no error__ if you use a key that doesn't exist in order to assign a value to it (that is... to create a new key/value pair).

{% highlight python %}
# look ma, no keys!
d = {}
# but I can assign with no probz
d["problems"] = None
d["another key"] = "another value"
{% endhighlight %}
</section>

<section markdown="block">
### Key/Value Pairs Continued

If the key already exists... and you use the assignment operator, you are just associating a new value with an existing key.

__What does this code output?__

{% highlight python %}
d = {}
d["another key"] = "another value"
d["problems"] = None
d["another key"] = "something"
print(d["another key"])
print(d["problems"])
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
something
None
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Dictionaries and Mutability

Based on what we've seen so far... __are dictionaries mutable or immutable?__

<div class="incremental" markdown="block">
Dictionaries are __mutable__!

{% highlight python %}
d = {}
d["did not exist before"] = "some value"
# ok!
{% endhighlight %}
</div>
</section>

<section markdown="block">
### We Can Iterate Over Dictionaries

__Let's run this code.  What would you expect this to print?  Does it match what actually happens?__

{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
for item in d:
  print(item)
{% endhighlight %}
<div class="incremental" markdown="block">

{% highlight python %}
# we only get the keys!
fav_candy
first_name
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Converting a Dictionary to a List of Tuples

Another way to iterate over a dictionary is to convert it to a list of tuples.  The __items__() method returns a list (it's slightly more sophisticated than a list, but it acts like one for iteration) of tuples, w/ the first element in each tuple the key, and the second, the value.

__What type is the type of variable i?  How many iterations are there?  What is the value of i at each iteration?__

{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
t = d.items()
for i in t:
	print(i)
{% endhighlight %}

</section>

<section markdown="block">
### Converting a Dictionary to a List of Tuples Continued

* i is always a tuple
* 2 iterations, with i being a tuple that represents a name value pair 
</section>

<section markdown="block">
### Iterating over a Dictionary Using items()

Now... we have a tuple... __how do we print out each key and value individually (how do we unpack again?)__

<div class="incremental" markdown="block">
{% highlight python %}
d = {"first_name":"joe", "fav_candy":"cleo's"}
for k, v in d.items():
  print(k, v)
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Dictionaries Are Unordered

Unlike sequence types like string, list or tuple, dictionaries are __unordered__.  That means that the order of the key value pairs cannot be guaranteed!  __Let's take a look.  Intuitively, what's the first thing that we think will be printed out?__

{% highlight python %}
d = {"one":"foo", "two":"bar", 3:"baz"}
for k, v in d.items():
  print(k, v)
{% endhighlight %}

<div class="incremental" markdown="block">
{% highlight python %}
# this is actually just one possible ordering!
3 baz
two bar
one foo
{% endhighlight %}
</div>
</section>

<section markdown="block">
### Summary Questions

* how do we construct a string literal?
* how do we create an empty dictionary?
* are dictionaries mutable or immutable?
* are dictionaries ordered or unordered
* how do we access a value at a key... what happens if they key doesn't exist?
* what's the exception to the above?
* what's another way of accessing a value?


</section>
<section markdown="block">
### Summary Answers

* dictionaries are delimited by curly braces, key value pairs are separated by commas, with each key and value joined by a colon
* {}
* they're mutable
* order cannot be guaranteed
* d["some key"], excepion
* assignment
* get method

</section>


<section markdown="block">
### Back to Dice!

__Try reimplementing our dice program so that it uses a dictionary to store the frequency of rolls (each roll as a key, each value as a count).__  By doing this you'll also be able to remove all if statements (hint: use the get method or use a try-except).
{% highlight python %}
import random
twos, threes, fours, fives, sixes = 0, 0, 0, 0, 0
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	if roll == 2:
		twos += 1
	if roll == 3:
		threes += 1
	if roll == 4:
		fours += 1
	if roll == 5:
		fives += 1
	if roll == 6:
		sixes += 1

print("twos: %s, threes: %s, fours: %s, fives: %s, sixes %s" % (twos, threes, fours, fives, sixes)) 
{% endhighlight %}
</section>


<section markdown="block">
### Dice Rolls Solution 
{% highlight python %}
import random
freq_dice_rolls = {}
for i in range(1000):
	roll = random.randint(1,3) + random.randint(1,3)
	freq_dice_rolls[roll] = freq_dice_rolls.get(roll, 0) + 1
print(freq_dice_rolls)
{% endhighlight %}
</section>
