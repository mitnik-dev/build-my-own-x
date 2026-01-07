import re, random, requests

url = 'https://raw.githubusercontent.com/codecrafters-io/build-your-own-x/master/README.md'
readme = requests.get(url).text

tutorials_section = re.search(r"^##\sTutorials(.*?)^##\s", readme, re.S | re.M).group(1)
tutorials = re.findall(r"^\*\s*(.+)", tutorials_section, re.M)

print(tutorials[random.randrange(0, len(tutorials))])