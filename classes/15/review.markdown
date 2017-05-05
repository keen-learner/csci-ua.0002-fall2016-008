---
layout: slides
title: Review 
---
<section markdown="block" class="title-slide">
# Functions Review
{% include title-slide-footer.html %}
</section>

<section markdown="block">
### Function Definition

__What's a function?__

<div class="incremental" markdown="block">
A __function__ is a named sequence of statements that performs some _useful_ operation
</div>
</section>

<section markdown="block">
### Method Definition

__What's a method (well... in the context of programming, of course!)?__

<div class="incremental" markdown="block">
A __method__ is an action that an object/_thing_ can do.  It's basically a function that's attached to an object. 
</div>
</section>

<section markdown="block">
### Function Call Definition

__What's a function call?__ 

<div class="incremental" markdown="block">
A __function call__ is the statement that actually executes a function.  It's just the function's name followed by parentheses, with zero or more arguments within those parentheses.
</div>
</section>

<section markdown="block">
### Argument Definition

__What's an argument (again, in the context of functions, of course)?__ 

<div class="incremental" markdown="block">
An __argument__ is a value that's passed in to a function when a function is called.  It's the input!
</div>
</section>

<section markdown="block">
### Parameters

__What's a parameter?__ 

<div class="incremental" markdown="block">
An __parameter__ is a variable that receives an argument that is passed into a function.  It's the name used inside a function to refer to the value which was passed in.
</div>
</section>


<section markdown="block">
### None Definition

__What's None?__

<div class="incremental" markdown="block">
__None__ is a special value in Python that represents the absence of a value.
</div>
</section>

<section markdown="block">
### Function Definition

__What's the syntax for defining a function? &rarr;__

<div class="incremental" markdown="block">
{% highlight python %}
def <function_name>(<zero_or_more_parameters>):
	<statement #1>
	<statement #2>
	.
	.
	<etc.>
	# an optional return statement
	return <some value>
{% endhighlight %}
</div>
</section>


<section markdown="block">
### Return

What does __return__ do?

<div class="incremental" markdown="block">
* it's a statement that... 
	* immediately stops the execution of a function
	* and returns the value specified to the right of it
	* __return "some value"__
</div>
</section>

<section markdown="block">
### Return Continued

__What's value is given back if a function doesn't contain a return statement (that is, there is no explicit return value)?__

<div class="incremental" markdown="block">
__None__ 
</div>
</section>

<section markdown="block">
### Finally, Let's Look at Parameters Again

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	return s

greet_more_input("hey " * 3, math.sqrt(100))
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "hey hey hey"
* num &rarr; 10
</div>
</section>

<section markdown="block">
### And The Tricky One

__Using the following function and function call, what are the values of both greeting and num within the function? &rarr;__

{% highlight python %}
def greet_more_input(greeting, num):
	s = greeting * num
	return s

num = "yo"
greeting = 1
greet_more_input(num, greeting)
{% endhighlight %}

<div class="incremental" markdown="block">
* greeting &rarr; "yo"
* num &rarr; 1
</div>
</section>

<section markdown="block">
## [A Little More About Returning Values](return.html)
</section>
