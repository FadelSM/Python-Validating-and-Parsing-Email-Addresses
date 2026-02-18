import re
import email.utils

# Number of email entries
n = int(input())

# Regex pattern for valid email addresses
pattern = re.compile(r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

for _ in range(n):
    line = input().strip()
    
    # Parse the name and email using email.utils
    name, addr = email.utils.parseaddr(line)
    
    # Check if the email address matches the pattern
    if pattern.match(addr):
        print(email.utils.formataddr((name, addr)))
