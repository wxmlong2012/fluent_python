# replace a character in a string text without using .replace() function
def replace_str(text, old, new):
    result = ""
    for s in text:
        if s == old:
            s = new
        result += s
    return result

text = "D t C mpBl ckFrid yS le"
old = " "
new = "a"

replace_str(text, old, new)

# Use .replace() function
text = "D t C mpBl ckFrid yS le"
text.replace(old, new)


"""
Given a positive integer num, write a function that returns True if num is a perfect square else False.
"""
def perfect_square(num):
    num_sqrt = int(num**0.5)
    result = num == num_sqrt**2
    return result

perfect_square(25)
perfect_square(10)


"""
without using any package
Given an integer n, return the number of trailing zeroes in n factorial n!
"""
def factorial_training_zeros(n):
    fact = n
    while n > 1:
        fact *= n - 1
        n -= 1

    count = 0
    for s in str(fact)[::-1]:
        if s == "0":
            count += 1
        else:
            break
    return count


"""
You are provided with a large string and a dictionary of the words. 
You have to find if the input string can be segmented into words using the dictionary or not.
"""

def word_segmentation(word, dictionary):

    for i in range(1, len(word)+1):
        word1 = word[0:i]
        if word1 in dictionary:
            word2 = word[i:]
            if (word2 in dictionary) \
                    or (not word2) \
                    or word_segmentation(word2, dictionary):
                return True
    return False

w1 = "shank3cancauseautism"
w2 = "shank3cannotcauseautism"
dictionary = ["shank3", "can", "cause", "autism", "cam", "lack"]

word_segmentation(w1, dictionary)

"""
remove duplicates from a list or array
"""
list1 = [1,1,2,3,3]
list2 = [1,1,1,2,2,2,3,3,4,5,6,7,8]
list(set(list1))
list(set(list2))

def remove_dups(array):
    new_array = [array[0]]
    for i in array:
        if i != new_array[-1]:
            new_array.append(i)
    return new_array

# just count the number of unique values (list are ordered)
def count_unique(array):
    n_unique = 0
    for i in range(len(array) - 1):
        if array[i] != array[i+1]:
            n_unique += 1
    return n_unique

remove_dups(list1)
remove_dups(list2)
count_unique(list1)
count_unique(list2)




"""
How to sort a list?
"""
l1 = [1, 2, 5, 6, 4,4, 7, 9, 10, 8, 10]
sorted(l1)

def sort_list(l):
    new_l = [l[0]]
    for i in l[1:]:
        if i <= new_l[0]:
            new_l.insert(0, i)
        elif i >= new_l[-1]:
            new_l.append(i)
        else:
            for j in range(1, len(new_l) - 1):
                if i >= new_l[j] and i <= new_l[j+1]:
                    new_l.insert(j+1, i)
                    break
    return new_l

sort_list(l1)

"""
Write a function that returns True if there is a Pythagorean triplet that satisfies a2+ b2 = c2
"""

def pythagorean(l):
    l1 = [i**2 for i in l]
    l1.sort()
    