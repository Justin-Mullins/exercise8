'''

Excercise 8
Sorting a string

In this exercise, you’ll explore this idea by writing a function, strsort , that takes a
single string as its input and returns a string. The returned string should contain the
same characters as the input, except that its characters should be sorted in order, from
the lowest Unicode value to the highest Unicode value. For example, the result of
invoking strsort('cba') will be the string abc.

''' 

def strsort(string):
     return ''.join(sorted(string))

print(strsort('lA*k11lldky0lLKSN1i018792ii9'))