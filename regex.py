import re
my_str = '''A regular expression is a special sequence of characacters that helps you match or find other 
strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions
 are widely used in UNIX world.
this is perfectallyyy number 0301-5902110
The Python module re provides full support for Perl-like regular expressions in Python. The
 re module raises the exception re.error if an error occurs while compiling or using a regular
  expression.'''
# patt = re.compile(r'special')     # anywhere
# patt = re.compile(r'....ence')       #  as much dot as char left side
# patt = re.compile(r'^A')              # ^ start with string
# patt = re.compile(r'.....ssion.$')                  # $ end with string
# patt = re.compile(r'...ly*')                  # * last char zero or many time 
# patt = re.compile(r'ly+')                  # + last char one or many time 
# patt = re.compile(r'........lly{2}')                  # + last char selected time 
# patt = re.compile(r'(ac){2}')                  # () group for selected time 
# patt = re.compile(r'ac{1}|ed')                  # | either or  
# patt = re.compile(r'\bexpre')                  # \b..... start a word
# patt = re.compile(r'thon\b')                  # .....\b end a word  
patt = re.compile(r'\d{4}-\d{7}')                  # \d{n-digit} sign \d{n-digit}------its for numbers not char
matches = patt.finditer(my_str)
for match in matches:
    print(match)

# print(my_str[50:54])
# print(my_str[130:137])