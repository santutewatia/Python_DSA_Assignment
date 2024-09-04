#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python DSA  Assignment

Ques 1  Discuss string slicing and provide examples.

Ques 2  Explain the key features of lists in Python.

Ques 3  Describe how to access, modify, and delete elements in a list with examples.

Ques 4  Compare and contrast tuples and lists with examples.

Ques 5  Describe the key features of sets and provide examples of their use.

Ques 6  Discuss the use cases of tuples and sets in Python programming.

Ques 7  Describe how to add, modify, and delete items in a dictionary with examples.

Ques 8  Discuss the importance of dictionary keys being immutable and provide examples.


# In[ ]:


# Ques 1 

Discuss string slicing and provide examples.


String slicing in Python is a method for extracting parts of a string using a range of indices. 
This feature allows you to access and manipulate subsets of a string efficiently.

How String Slicing Works:

The basic syntax for string slicing is:

string[start:end:step]

start: The starting index of the slice (inclusive). If not provided, it defaults to the beginning of the string.

end: The ending index of the slice (exclusive). If not provided, it defaults to the end of the string.

step: The increment between each index for slicing. If not provided, it defaults to 1.


# In[5]:


# Examples of String Slicing
a='hello world'
print(a[0:5])


# In[6]:


#reverse string
a[::-1]


# In[ ]:


Summary

String slicing is a powerful tool in Python that allows you to access, manipulate, and analyze
parts of strings with flexibility.

The basic syntax, string[start:end:step], helps you specify the range and direction of slicing.

Slicing is commonly used for extracting substrings, reversing strings, and more, making it 
a fundamental concept in Python programming.


# In[ ]:


# Ques 2

Explain the key features of lists in Python.

Lists in Python are a versatile and widely-used data structure that allows you to store an ordered
collection of items. Here are the key features of lists in Python:

Key Features of Lists in Python:
    


# In[7]:


# 1 Ordered:

# Lists maintain the order of elements as they are inserted. This means that the elements have
# a specific order or sequence, and each element can be accessed by its index.

fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # Output: "apple"
print(fruits[1])  # Output: "banana"


# In[8]:


# 2 Mutable:

# Lists are mutable, meaning you can change, add, or remove elements after the list has been created

numbers = [1, 2, 3]
numbers[1] = 10  # Changing the second element
print(numbers)   # Output: [1, 10, 3]


# In[9]:


# 3 Dynamic:

# Lists in Python are dynamic, which means they can grow and shrink in size. You can add or remove
# elements at any time.
colors = ['red', 'green']
colors.append('blue')  # Adding an element
print(colors)          # Output: ['red', 'green', 'blue']
colors.remove('red')   # Removing an element
print(colors)          # Output: ['green', 'blue']


# In[10]:


# 4 Heterogeneous Elements:

# Lists can contain elements of different data types, including integers, strings, floats, and even
# other lists (nested lists)
mixed_list = [1, 'apple', 3.14, [2, 4, 6]]
print(mixed_list)  # Output: [1, 'apple', 3.14, [2, 4, 6]]


# In[11]:


# 5 Indexing and Slicing:

# Lists support both positive and negative indexing, making it easy to access elements from both the beginning and the end of the list.
# Slicing allows you to extract a portion of the list.

numbers = [10, 20, 30, 40, 50]
print(numbers[1])    # Output: 20 (positive indexing)
print(numbers[-1])   # Output: 50 (negative indexing)
print(numbers[1:4])  # Output: [20, 30, 40] (slicing)


# In[12]:


# 6 Methods for Manipulation:

# Lists come with several built-in methods to manipulate the elements, such as append(), extend(),
# insert(), remove(), pop(), sort(), reverse(), and more.
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')    # Adds 'date' to the end
print(fruits)            # Output: ['apple', 'banana', 'cherry', 'date']

fruits.sort()            # Sorts the list
print(fruits)            # Output: ['apple', 'banana', 'cherry', 'date']


# In[13]:


# Iteration:

# You can iterate through the elements of a list using loops, such as for and while, which makes 
# it easy to perform operations on each element
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5


# In[ ]:


Summary

Lists in Python are ordered, mutable, and dynamic, making them suitable for a wide range of applications.

They can hold heterogeneous elements, allowing you to store data of various types in a single collection.

Lists support indexing, slicing, and numerous methods for manipulation, making them a powerful and flexible tool for handling sequences of data in Python.


# In[ ]:


# Ques 3

Describe how to access, modify and delete elements in a list with examples.

In Python, lists are a versatile data structure that allows you to easily access, modify, and delete
elements. Here's how you can perform these operations with examples:


# In[14]:


# 1 Accessing Elements in a List
# You can access elements in a list using their index. Python lists are zero-indexed, meaning the
# first element is at index 0.
fruits = ['apple', 'banana', 'cherry', 'date']

# Access the first element
print(fruits[0])  # Output: 'apple'

# Access the third element
print(fruits[2])  # Output: 'cherry'

# Access the last element using a negative index
print(fruits[-1])  # Output: 'date'




# In[15]:


# 2 Modifying Elements in a List
# You can modify elements by accessing them via their index and assigning a new value.
numbers = [10, 20, 30, 40]

# Modify the second element
numbers[1] = 25
print(numbers)  # Output: [10, 25, 30, 40]

# Modify the last element using a negative index
numbers[-1] = 50
print(numbers)  # Output: [10, 25, 30, 50]


# In[16]:


# 4 Deleting Elements from a List
# You can delete elements from a list using various methods like del, remove(), and pop()
animals = ['cat', 'dog', 'rabbit', 'hamster']

# Delete the second element
del animals[1]
print(animals)  # Output: ['cat', 'rabbit', 'hamster']

# Delete a range of elements
del animals[1:3]
print(animals)  # Output: ['cat']


# In[17]:


# 5 Using remove() Method:

# remove() deletes the first occurrence of a specified value.
colors = ['red', 'green', 'blue', 'green']

# Remove the first occurrence of 'green'
colors.remove('green')
print(colors)  # Output: ['red', 'blue', 'green']


# In[18]:


# 6 Using pop() Method:

# pop() removes an element at a specified index and returns it. If no index is specified, it 
# removes and returns the last element.

languages = ['Python', 'Java', 'C++', 'Ruby']

# Remove and return the last element
last_language = languages.pop()
print(last_language)  # Output: 'Ruby'
print(languages)      # Output: ['Python', 'Java', 'C++']

# Remove and return the element at index 1
second_language = languages.pop(1)
print(second_language)  # Output: 'Java'
print(languages)        # Output: ['Python', 'C++']


# In[ ]:


Summary

Accessing Elements: Use square brackets [] with the index to access elements.
    
Modifying Elements: Assign a new value to a specific index using list[index] = new_value.
    
Deleting Elements: Use del to remove by index or slice, remove() to delete by value, and pop() to remove by index and return the removed element.


# In[ ]:


# Ques 4

Compare and contrast tuples and lists with examples.

Tuples and lists are both data structures in Python used to store collections of items, but they 
have some key differences in terms of mutability, syntax, and use cases. Here’s a comparison of tuples and lists with examples:

1. Mutability

Lists: are mutable, meaning you can change, add, or remove elements after the list is created.

Tuples: are immutable, meaning once they are created, their elements cannot be changed, added, or removed.


# In[19]:


# List (Mutable):
fruits = ['apple', 'banana', 'cherry']
fruits[1] = 'orange'  # Modifying an element
print(fruits)  # Output: ['apple', 'orange', 'cherry']


# In[20]:


# Tuple (Immutable):
fruits = ('apple', 'banana', 'cherry')
# Attempting to modify an element will raise an error
# fruits[1] = 'orange'  # TypeError: 'tuple' object does not support item assignment


# In[ ]:


2 Syntax

Lists are defined using square brackets [].

Tuples are defined using parentheses ().


# In[ ]:


3 Use Cases

Lists are used when you need a collection of items that can be modified. They are ideal for tasks
where data needs to change dynamically, such as data manipulation, sorting, or storing collections
that frequently change.

Tuples are used when you need a collection of items that should not be modified. They are ideal 
for fixed data structures like coordinates (x, y), RGB values, or when you want to ensure the data
remains constant throughout the program.


# In[21]:


# List Use Case:
shopping_list = ['milk', 'eggs', 'bread']
shopping_list.append('butter')  # Modifying the list
print(shopping_list)  # Output: ['milk', 'eggs', 'bread', 'butter']


# In[22]:


# Tuple Use Case:
coordinates = (10, 20)  # Fixed coordinate point
# coordinates[0] = 15  # This would raise an error because tuples are immutable
print(coordinates)  # Output: (10, 20)


# In[23]:


# Performance
# Tuples are generally faster than lists because they are immutable and thus have a smaller memory
# footprint. Python can optimize them more effectively.
# Lists are slower because they are mutable and need additional memory to accommodate changes.

import timeit

# Time for list creation
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
print(f"List creation time: {list_time}")

# Time for tuple creation
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print(f"Tuple creation time: {tuple_time}")


# In[ ]:


Summary                               

Feature :         Lists                                Tuples                                 

Mutability:      Mutable (can change)                  Immutable (cannot change)
    
Syntax :         Square brackets []                    Parentheses () 

Use Cases :      Dynamic, modifiable data,             constant data collections


Performance:     Slower due to mutability              Faster due to immutability

Methods   :      More methods available               Fewer methods (count(), index())
                (append(), remove(), etc.)
                                                       Uses less memory
Memory   :      Uses more memory 
usage


Tuples and lists serve different purposes, and choosing between them depends on whether you need
a mutable or immutable data structure.


# In[ ]:


# Ques 5

Describe the key features of sets and provide examples of their use

Sets in Python are an unordered collection of unique elements. They are similar to lists and tuples 
but have some distinct features that make them suitable for specific use cases. Here are the key
features of sets and examples of their use:

Key Features of Sets


# In[24]:


# 1 Unordered:

# Sets do not maintain any specific order of elements. When you print a set or iterate through it,
# the elements may appear in any order.
my_set = {3, 1, 4, 1, 5, 9}
print(my_set)  # Output could be {1, 3, 4, 5, 9}


# In[25]:


# 2 Unique Elements:

# Sets automatically remove duplicate elements. Each element in a set must be unique, meaning no two
# elements can have the same value.
my_set = {1, 2, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}


# In[26]:


# 3 Mutable:

# Sets are mutable, meaning you can add or remove elements from a set after it has been created
#  However, the elements themselves must be immutable (e.g., numbers, strings, tuples).
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


# In[27]:


#  4 No Indexing or Slicing:

# Because sets are unordered, they do not support indexing or slicing like lists or tuples.
# You cannot access elements by index.
my_set = {1, 2, 3}
# my_set[0]  # This will raise a TypeError


# In[28]:


# 5 Set Operations:

# Sets support various mathematical operations like union, intersection, difference, and symmetric
# difference, which are useful for comparing collections of data.
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union: Elements present in either set
print(set_a | set_b)  # Output: {1, 2, 3, 4, 5}

# Intersection: Elements present in both sets
print(set_a & set_b)  # Output: {3}

# Difference: Elements in set_a but not in set_b
print(set_a - set_b)  # Output: {1, 2}

# Symmetric Difference: Elements in either set_a or set_b, but not in both
print(set_a ^ set_b)  # Output: {1, 2, 4, 5}


# In[29]:


# 6 Immutability of Set Elements:

# Elements inside a set must be immutable, meaning you cannot have lists or dictionaries as elements
# of a set. However, you can have tuples as elements because tuples are immutable.
valid_set = {1, (2, 3), 'apple'}
print(valid_set)  # Output: {1, (2, 3), 'apple'}

# invalid_set = {[1, 2], 3}  # This will raise a TypeError: unhashable type: 'list'


# In[ ]:


Summary

Sets in Python are collections of unique, unordered elements that are mutable.

Sets are highly efficient for membership testing, removing duplicates, and performing mathematical 
set operations.
They are suitable for use cases that involve uniqueness, fast lookups, and mathematical set operations.


# In[ ]:


# Ques 6

Discuss the use cases of tuples and sets in Python programmong.

Tuples and sets are both important data structures in Python, each serving distinct purposes based
on their properties. Here's a discussion of their use cases:

Use Cases of Tuples:


# In[30]:


# 1 Fixed Collections of Items:

# Tuples are ideal when you have a collection of items that should not change throughout the program
#  They are often used to represent fixed collections of related items, like coordinates, RGB color 
# codes, or date and time.
point = (10, 20)  # Coordinate (x, y)
color = (255, 0, 0)  # RGB color code for red
date_of_birth = (1995, 5, 23)  # (Year, Month, Day)


# In[31]:


# 2 Immutable Data Structures:

# Because tuples are immutable, they can be used to create constant data structures. This immutability 
# makes them safer to use in scenarios where data should remain unchanged, such as configuration
# settings or fixed lookup tables.
DAYS_OF_WEEK = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')


# In[32]:


# 3 Data Integrity and Hashability:

# Tuples can be used as keys in dictionaries or elements of sets because they are hashable 
# (unlike lists). This is useful when you need a composite key (a key made up of multiple values).
locations = {
    ('New York', 'USA'): 'NY',
    ('Los Angeles', 'USA'): 'LA',
    ('Tokyo', 'Japan'): 'TYO'
}
print(locations[('New York', 'USA')])  # Output: 'NY'


# In[33]:


# 4 Iterating Over Immutable Data:

# When data needs to be iterated over without the risk of modification, tuples are preferred to ensure 
# data consistency.
immutable_settings = ('high', 'medium', 'low')
for setting in immutable_settings:
    print(setting)


# In[34]:


# Use Cases of Sets

# 1. Removing Duplicates from a Collection:

# Sets automatically eliminate duplicate values, making them useful for tasks that require
# filtering out duplicate entries from a collection.
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = set(items)
print(unique_items)  # Output: {1, 2, 3, 4, 5}


# In[37]:


# 2 Mathematical Set Operations:

# Sets provide built-in methods for union, intersection, difference, and symmetric difference. T
# hese operations are valuable in applications such as data analysis, comparison, and mathematical
# computations.
set_a = {1, 2, 3}
set_b = {2, 3, 4}

union_set = set_a | set_b  # Union
print(union_set)  # Output: {1, 2, 3, 4}

intersection_set = set_a & set_b  # Intersection
print(intersection_set)  # Output: {2, 3}

difference_set = set_a - set_b  # Difference
print(difference_set)  # Output: {1}


# In[38]:


# 3 Removing Duplicates and Aggregating Results:

# Sets are ideal for collecting unique items from multiple sources, such as logs, user inputs,
# or datasets. They simplify the process of aggregation and de-duplication.
emails_from_file1 = {'alice@example.com', 'bob@example.com'}
emails_from_file2 = {'bob@example.com', 'charlie@example.com'}

unique_emails = emails_from_file1 | emails_from_file2  # Union of sets
print(unique_emails)  # Output: {'alice@example.com', 'bob@example.com', 'charlie@example.com'}


# In[ ]:


Summary

Tuples are best used for fixed collections of data, ensuring data integrity, supporting multiple
return values from functions, and hashable key storage in dictionaries.

Sets are ideal for unique collections, efficient membership testing, mathematical operations,
data deduplication, and finding common or unique elements across datasets.

Both tuples and sets provide powerful tools for managing data in Python, allowing developers to select the most appropriate data structure for their specific needs.


# In[ ]:


# Ques 7

Describe how to add, modify, and delete items in a dictionary with examples.

In Python, dictionaries are collections that store data in key-value pairs. 
They are mutable, which means you can add, modify, and delete items after the dictionary
has been created. Here’s how you can perform these operations:



# In[39]:


# 1. Adding Items to a Dictionary
# To add items to a dictionary, you assign a value to a new key. If the key already exists,
# the value will be updated.
# Creating a dictionary
person = {'name': 'Alice', 'age': 25}

# Adding a new key-value pair
person['city'] = 'New York'

print(person)  
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}



# In[40]:


# 2. Modifying Items in a Dictionary
# To modify an item in a dictionary, you can update the value associated with an existing
# key by assigning a new value to that key.

# Example:
# Existing dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Modifying the value of an existing key
person['age'] = 30

print(person)  
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# In[41]:


# 3. Deleting Items from a Dictionary
# There are several ways to remove items from a dictionary:

# Using del keyword: Removes a specific key-value pair by key.
# Using .pop() method: Removes a key and returns its value.
# Using .popitem() method: Removes and returns the last key-value pair as a tuple 
# (this is only available in Python 3.7+).
# Using .clear() method: Removes all items from the dictionary.
# Existing dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Deleting a key-value pair using del
del person['city']

print(person)  
# Output: {'name': 'Alice', 'age': 30}


# In[42]:


# 4 Example using .pop():
# Existing dictionary
person = {'name': 'Alice', 'age': 30}

# Deleting a key-value pair using pop
age = person.pop('age')

print(person)  
# Output: {'name': 'Alice'}
print(age)  
# Output: 30 (the removed value)


# In[ ]:


Summary

Adding Items: Assign a value to a new key.
    
Modifying Items: Assign a new value to an existing key.
    
Deleting Items: Use del, .pop(), .popitem(), or .clear() depending on the specific need.


# In[ ]:


# Ques 8

Discuss the importance of dictionary keys being immutable and provide examples.


In Python, dictionary keys must be immutable. This immutability is crucial for the dictionary’s 
functionality, allowing it to maintain data integrity and perform efficiently.
Here’s a detailed discussion on why dictionary keys must be immutable, along with examples


# In[ ]:


Importance of Immutable Dictionary Keys

Hashing and Performance:

Reason: Dictionaries in Python use a hash table for efficient data retrieval. A hash table relies
on the hash value of keys to quickly locate the corresponding value. Immutable objects have a 
fixed hash value, which is essential for maintaining consistent and reliable access to dictionary 
elements.

Example: If you use a mutable object (like a list) as a key, its hash value can change, causing 
the dictionary to lose track of the associated value.


# In[43]:


my_dict = {}
key = [1, 2, 3]  # This is a mutable list and cannot be used as a key.
# my_dict[key] = 'value'  # This will raise a TypeError: unhashable type: 'list'


# In[ ]:


Data Integrity:

Reason: Immutable keys ensure that once a key is used in a dictionary, it remains consistent. 
This guarantees that the dictionary can always find the correct value associated with a key,
as the key’s identity doesn’t change.

Example: Using an immutable tuple as a key ensures that the dictionary remains stable,
even if you accidentally change other parts of your data.


# In[44]:


my_dict = {}
key = (1, 2, 3)  # This is an immutable tuple and can be used as a key.
my_dict[key] = 'value'
print(my_dict)  # Output: {(1, 2, 3): 'value'}


# In[45]:


# Examples of Immutable and Mutable Keys

# Immutable Keys (Allowed):

# Strings:
my_dict = {'key': 'value'}
print(my_dict['key'])  # Output: 'value'



# In[46]:


# Tuples (as long as the tuple only contains immutable elements):

my_dict = {(1, 2): 'value'}
print(my_dict[(1, 2)])  # Output: 'value'


# In[47]:


# Mutable Keys (Not Allowed):

# Lists:
my_dict = {}
key = [1, 2, 3]
# my_dict[key] = 'value'  # This will raise a TypeError: unhashable type: 'list'


# In[48]:


# Dictionaries:
my_dict = {}
key = {'a': 1}  # This is a mutable dictionary
# my_dict[key] = 'value'  # This will raise a TypeError: unhashable type: 'dict'


# In[ ]:


Summary

The immutability of dictionary keys is crucial for ensuring the efficiency, reliability, and

consistency of dictionary operations. Immutable keys guarantee that the dictionary’s internal

structure remains stable and predictable, enabling quick and accurate data retrieval.

Using mutable types as keys would compromise these benefits and lead to unpredictable
and erroneous behavior.


# In[ ]:




