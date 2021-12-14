# Stack

<!-- Notes for later
USE LESS WORDS!
Include more examples
Spend some more time on the problem to make it understandable -->
## What is a stack?
Stack is a data structure that uses a last-in-first-out system. Think of it like
a stack of plates. The item at the top of the stack, or the plate that was put on last,
is the first item taken off. In this data structure only the top of the stack is accessible.
Everything else inside of the stack cant be accessed besides the top, which means if you
want to get an item from the middle of the stack then you would have to keep taking items
off of the top of the stack until you hit that point.

## How is stack used?
Stack can be a great benefit for any software that wants to quickly access the last element 
added. Think of a deck of cards. Most of the time, only the card at the top of the pile is
needed. All of the cards are still there, but we only ever need the top card. In software we
also have an *undo* button. Imagine creating a house in *The Sims* and you dont like the 
placement of a recent wall. Instead of changing tools to delete it, we can just tell the 
game to take off our most recent item.

## Stack terminology
* Front: This term is used to refer to the bottom of the stack. It is the very first item
added and the very last item to be used.
* Back: This term is used to refer to the top of the stack. This is the last item added to
the stack and will be the first item used.
* Push: Push is used when an item is pushed onto a stack. If I have a stack of people, I 
will use push for each person and that person will be added to the back of the stack.
* Pop: Pop is used to remove the last item of the stack and use it. The last item of the
stack is removed and the size is decreased by one.

## Example
<!-- Put yourself as the person in this scenario. One day, you are coding new software for
your company. You have imported many different libraries into your code and everything
is going well. However just a few days before your deadline, your software is failing.
Your current debugger mentions a function from an imported library, but does not tell
you which one. A simple method you could do is go though your thousands of lines of code
and try to find the problem, or you could put them in order into a stack. The stack 
itself won't break you program and by going through the stack it can tell you exactly 
where the error is occuring. -->

As your tech company has expanded, you have decided that a single server isn't enough
to take care of your companies many needs. To solve this problem you have implemented
a system where your main server will deligate tasks to other servers, which will then
deligate the task again to others until the tasks can be solved seemlessly and the 
information returned. However, one day your main server fails completely because of a
simple bug that was passed down the line then made it back up to the main server. What
you should have done is implement a stack where only the top layer could be effected.

## Problem
Python has built in stuctures that we will be taking advantage of. Instead of a "push",
we will be using append
``` Python
myStack = []
myStack.append(basemap)
myStack.append(roads)
myStack.append(lights)
myStack.append(traffic)
myStack.append(accidents)
```

This is a possible code for adding layers onto a map. A stack is used so the basemap wont
be touched unless everything else is changed first. Now, after creating this the 
programmer realizes that they wanted to add a section for "weather" right after the
basemap but cant change the current code. What would the code look like to implement this
change? (Don't think too hard about this. Just use a series of pops and appends, and don't
forget to add back onto the stack everything that was just taken off.)

<!-- myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
mystack.append(weather)
myStack.append(roads)
myStack.append(lights)
myStack.append(traffic)
myStack.append(accidents) -->

