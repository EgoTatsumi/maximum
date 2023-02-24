import re
line = input()
answer = re.sub('([A-Z])', r' \1', line).split()
print(answer)
