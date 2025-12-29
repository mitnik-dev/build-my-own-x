import re
import random
import requests


url = 'https://raw.githubusercontent.com/codecrafters-io/build-your-own-x/master/README.md'
readme = requests.get(url).text

#with open(readme) as f:
#    text = f.read()

# - We know that all the relevant bullets are between 'Tutorials' and 'Contribute' headings
# - re.search matches 'Tutorial' and 'Contribute' using '()' to capture everything '.*' inbetween, 
# - Match stops at first occurances of 'Contribute' (non-greedy) using '?'
# - .group() returns the all matching text as string
tutorials_section = re.search(r"Tutorials(.*?)Contribute", readme, re.S).group()

# - Now we can be sure all bullets denoted by '*' (markdown) are tutorials
# - re.findall returns a list of all matches in the case of one capturing group (this is what we have)
# - Looking for '*' -> '\*' (escaped the special character) at beginning of line -> '^'
# - Then, match anynumber -> '*' of empty space -> '\s'
# - Finally capture -> '()' one or more characters -> '.+' until end of line (default behavior)
# - Must use flag re.M to specify that '^' will start at beginning of each newline instead of the entire string
tutorials = re.findall(r"^\*\s*(.+)", tutorials_section, re.M)

print(tutorials[random.randrange(0, len(tutorials))])