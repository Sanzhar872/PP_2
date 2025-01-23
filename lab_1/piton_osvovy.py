list = ["var1", "var2", "var3"]

a, b, c = list
print(a)
print(b)
print(c)


q = 1    # int
w = 2.8  # float
e = 1j   # complex

print(type(q))
print(type(w))
print(type(e))

x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# it can be used for strings too
s = str(2)  # s will be "2"
s_1 = str(3.0)  # s_1 will be "3.0"

# strings

str_1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(str_1)  # You can use three double quotes """" for multiline string or three single quotes '''

# to check if a certain phrase or character is present in a string, we can use the keyword in
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print("YES")

# slicing strings

b = "Saparkhan"
print(b[2:5])  # Get the characters from position 2 to position 5 (not included)
print(b[:5])  # Get the characters from the start to position 5 (not included)
print(b[2:])  # Get the characters from position 2, and all the way to the end
print(b[-5:-2])  # starts from r(-5th position) to a(-2th position)

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # / is Escape Character
