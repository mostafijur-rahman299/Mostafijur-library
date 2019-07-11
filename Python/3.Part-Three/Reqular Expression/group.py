import re
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('this is my phone number buddy 458-95587-8595 yeah byddy')
print(mo.group())


phoneNumberRegex = re.compile(r'\d{3}-\d{5}-\d{4}')
mo = phoneNumberRegex.search('this is my phone number buddy 458-95587-8595 yeah byddy')
print(mo.group())


phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d\d\d)-(\d\d\d\d)')
mo = phoneNumberRegex.search('this is my phone number buddy 458-95587-8595 yeah byddy')
print(mo.group(1))
print(mo.group(2))
print(mo.group(3))
print(mo.group(0))


phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('this is my phone number buddy 458-95587-8595 yeah byddy')
print(mo.groups())
areaCode, maniNumber = mo.groups()

