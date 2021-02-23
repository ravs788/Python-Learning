import re

p = re.compile('[aeiou]')

print(p.findall("This is my life, this is my ingdom, this is Sparta"))

p = re.compile('\d+')

print(p.findall("This is the 19th day of Jan 1990. This is the 3rd Friday of the year and the 3rd weekend. The 1st January is a Monday for this year."))

p = re.compile('\w') 
print(p.findall("He said * in some_lang.")) 
  
# \w+ matches to group of alphanumeric character. 
p = re.compile('\w+') 
print(p.findall("I went to him at 11 A.M., he said *** in some_language.")) 
  
# \W matches to non alphanumeric characters. 
p = re.compile('\W') 
print(p.findall("he said *** in some_language.")) 

p = re.compile('ab*') 
print(p.findall("ababbaabbb")) 

print(re.split("\W+","He said * in some_lang."))