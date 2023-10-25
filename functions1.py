#functions in python
#string  transform functions
#capitalize
message = "hi, how are you?"
print(message.capitalize())

#title
name = "deva naidu29"
print(name.title())

#upper
name = "deva naidu29"
print(name.upper())

#lower
name = "deva naidu29"
print(name.lower())

#casefold
name = "DEVAPRIYAM"
print(name.casefold())

#swapcase
name = "DEVAPRIYAM"
print(name.swapcase())

name = "DEVAPRIYAM"
print(name.swapcase())

#string check functions

#isnumeric
a = "12234"
print(a.isnumeric())

#isalnum
a = "naidu29"
print(a.isalnum())
b = "naidu"
print(b.isalnum())

#isdigit
a = "235"
print(a.isdigit())

#isasscii
a = "G4G"
print(a.isascii())

#isupper
a = "DEVAPRIYAM"
print(a.isupper())

#islower
a = "devapriyam"
print(a.islower())

#isspace
a = " "
print(a.isspace())

b = "priyam"
print(b.isspace())

#isidentifier
a = "devapriyam29"
print(a.isidentifier())

#isprintable
a = "devapriyam 42"
print(a.isprintable())

#istitle
a = "Hello, Welcome!"
print(a.istitle())

#string len function
name = "devapriyam29"
print(len(name))

#string search functions

#index
email = "devapriyam29"
print(email.index("2"))
print(email.index("9"))

#rindex
email = "devapriyam5@gmail.com"
print(email.rindex("5"))
print(email.rindex("@"))

#find
email = "devapriyam25@gmail.com"
print(email.find("3"))
print(email.find("b"))

email = "devapriy25am@gmail.com"
print(email.find("2"))
print(email.find("@"))

#rfind
email = "devapriyam25@gmail.com"
print(email.rfind("2"))
print(email.rfind("@"))

#startswith
email = "devapriyam25@gmail.com"
print(email.startswith("deva"))
print(email.startswith("25"))

#endswith
email = "devapriyam25@gmail.com"
print(email.endswith("deva"))
print(email.endswith(".com"))

#CRUD functions
#create/add data
#append
lst = []
lst.append("deva")
lst.append("25")
print(lst)

#insert
names = ["a", "b", "c"]
names.insert(2, "deva")
print(names)

#read
names = ["a", "b", "c"]
print(names.index("b"))

#count
names = ["a", "b", "c", "a"]
print(names.count("a"))

#extend
names = ["a", "b", "c"]
num = ["1", "2", "3"]
names.extend(num)
print(names)

#remove
names = ["deva", "priyam", "25"]
names.remove("priyam")
print(names)

#pop with index
names = ["priyam", "deva", "25"]
names.pop(2)
print(names)

#pop without index
names = ["deva", "priyam", "25"]
names.pop()
names.pop()
print(names)

#clear
names = ["deva", "priyam", "25"]
names.clear()
print(names)

#sort
num = [8, 3, 5, 2, 6, 1]
num.sort()
print(num)

#reverse
num = [8, 3, 5, 2, 6, 1]
num.reverse()
print(num)