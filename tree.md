# Tree

## What is a Tree?
A Tree is a **non-linear** data structure. What this means is that the
data inserted in the tree doesn't have to be ordered sequentially. When
we have a list, or a set, or a stack we can go through every item inside
of it in a single run. With a Tree, this may not be possible and will
frequently use recursion to treverse the Tree.

*example:* Lets imagine an apple tree (yes a physical tree). You are 
asked to pick all the apples from this tree starting at the base of the
tree, or the **root**. After climbing to the first branch you see an 
you see an apple so you start following the branch (lets call this a 
**subtree**). After picking an apple from it's **leaf** You will follow
the subtree backwards and either follow a different path from the branch 
to a new leaf, or you will go back to the root and find a new subtree.

## How a tree works
A tree is similar to a linked list by using nodes that are connected 
together by pointers. However, a tree is not limited to only one node. 
A great example is the binary tree which can have at most 2 nodes 
branching off of one node. The start of the binary tree is the root 
and there can only ever be one root. That root can produce up to two 
nodes coming off of it, these are refered to as **child** nodes. If 
these nodes in turn branch off into more nodes, then that child is now
a subtree and also a **parent** because it has new nodes branching off.
Only when we reach a node that doesn't have any childern do we call it
a leaf. 

<!-- insert image here. -->

## Why do trees matter
To answer this question lets talk about the binary search tree. It has 
all of the characteristics of a binary tree, but a binary search tree is 
organized. If we have the numbers 1-10 and the root is 5 then we will 
have the higher numbers branch off in one direction and the lower numbers
branch off into a different direction, then we will create new subtrees to
further divide the elements until each node has a single value. In terms of
efficiency, we are looking at Olog(n) because our list of possibilities is 
reduced by half with each child we follow.


# Problem
I have a binary search tree and would like to see how far down it goes, or
what the max amount of steps I will need to take to retrieve a node from 
this tree. Recursion will be used here to test out each possibility.