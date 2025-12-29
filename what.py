import re
import random
import requests

url = 'https://raw.githubusercontent.com/codecrafters-io/build-your-own-x/master/README.md'
readme = requests.get(url).text

# - We know that all the relevant bullets are under level-2 heading '## Tutorials' until the next level-2 heading '##'
# - re.search starts matching at '## Tutorials' using '()' to capture every following character '.*' including newlines (re.S ensures that '.' does not stop at newlines)
# - Match stops at first occurance of the next level-2 heading (this is called a lazy capture, denoted by '?')
# - Level-2 heading is found by the begining of line '^' followed by exactly two '#' then a space '\s', this prevents level-3 or more heading from stopping the capture
# - .group(1) returns the first (and in this case only) capturing group '(.*?)' (here means everything between '## Tutorials' and next "##")
tutorials_section = re.search(r"^##\sTutorials(.*?)^##\s", readme, re.S | re.M).group(1)

# - Now we can be sure all bullets denoted by '*' (markdown) are tutorials
# - re.findall returns a list[str] of all matches in the case of one capturing group (this is what we have)
# - First, we need to match the bullet characters to know we are on a line that lists a tutorial
# - So, we match the markdown bullet character ('*') at beginning of the line ('^') ('\' is need to escape the special character "*" which means 0 or more in regex)
# - Then, match any number ('*') of empty space ('\s')
# - Finally capture using '()' one or more characters ('.+') until end of line
# - Must use flag re.M to specify that '^' will start at beginning of each newline instead of the entire string
tutorials = re.findall(r"^\*\s*(.+)", tutorials_section, re.M)

print(tutorials[random.randrange(0, len(tutorials))])