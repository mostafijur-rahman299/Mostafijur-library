import re

heroRegex = re.compile(r'Batman | sajib')
mo = heroRegex.search('i know that Batman is friend of sajib')
print(mo.group())

mo2 = heroRegex.search('i know that Batma is friend of sajib')
print(mo2.group())
