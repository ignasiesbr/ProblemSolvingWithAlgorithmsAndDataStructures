# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
# recursively
#reverse a list
def reverse(l):
   if len(l) == 1:
      return [l[0]]
   else:
      return reverse(l[1:]) + [l[0]]

#reverse a string

def revString(str):
   if len(str) == 1:
      return str
   else:
      return revString(str[1:]) + str[0]

# Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
# recursively

def isPal(str, s, e):
   if s == e:
      return True
   elif str[s] != str[e]:
      return False
   else:
      return isPal(str, s + 1, e - 1)

def isPalindrome(str):
   s = removeWhitespace(str)
   return isPal(s, 0, len(s) - 1)

def removeWhitespace(str):
   return str.replace(" ","")


