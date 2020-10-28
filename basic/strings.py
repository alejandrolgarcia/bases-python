# String
s = "Hello, World!"
print(s)

# multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are arrays
print(s[1])

# Slicing
print(s[2:5])

# Negative indexing
print(s[-6:-2])

# Length
print(len(s))

# Methods
y = "  Hello world!!   "
print(y.strip())            # removes any whitespace from the beginning or the end.

print(s.lower())            # returns the string in lower case.

print(s.upper())            # returns the string in upper case.

print(s.replace("H", "J"))  # eplaces a string with another string.

print(s.split(","))

