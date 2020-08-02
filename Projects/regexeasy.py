# regex with less code

import re
        
message = 'Call me 415-555-1011 tomorrow, or at 765-254-2222'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # add parentheses to group them
mo = phoneNumRegex.search(message) # to search for one
print(mo.group()) # to list out the search result
print(mo.group(1)) # to get the area code
#print(phoneNumRegex.findall(message)) # to find all occurrences

# pipe character use (to match groups)

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
