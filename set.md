# Set

## What is a set?
A set is similar to a list, but does not have any duplicates and the order 
doesn't matter. 

## Why is set?
Lets imagine that you own a toy store. A customer calls and asks if you have
the new buzzlightyear toy in stock. With a set you can look up the item 
instantly and see if it exists. No loops neccesary.

## How is set?
A set works so well becuase of a process called hashing. Hashing in a basic
sense assigns an item to its own location. If we have a set that is made to 
store the values 0-9, but then we create a set with (3, 8, 9), the set could
look like this.
 , , ,3, , , , ,8,9
Instead of a list where each value will be next to each other, a set makes
a specific spot for each value. This results in an O(1) time when we search
for a value within the set.

## When is set?
A set should be used when we want to see all of the individual items in some
kind of list, comaring two sets to find any similarities or differences, or 
combining two sets together while removing any duplicates.

## Example
``` Python
list1 = ["apple", "banana", "watermelon", "cantalope", "banana", "grape"]
set1 = {"pear", "apple", "grape", "peach"}
```

Now we will have a bit of fun manipulating this list and set.
``` Python
set2 = set(list1)      // This will turn the list into a set, removing the duplicates.
set3 = intersection(set1, set2)  // This will be the duplicates between the two sets.
set4 = union(set1, set2)  // This will be the two sets combined together without any duplicates.
items = size(set4)    // This will return the size of set4.
if ("strawberry" in set4):   // Check if there is a strawberry in set4.
    set4.add("orange")       // Add an orange to set4.
    set4.remove("strawberry")  // Remove strawberry from set4.
print(set1)
print(set2)
print(set3)
print(set4)
```

The outcome of this code may look like this:
{'grape', 'pear', 'apple', 'peach'}
{'grape', 'cantalope', 'watermelon', 'banana', 'apple'}
{'grape', 'apple'}
{'grape', 'cantalope', 'pear', 'watermelon', 'peach', 'banana', 'apple'}

Notice that the sets aren't displayed in the same order they were created.

