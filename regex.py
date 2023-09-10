colors = ['blue', 'white', 'red', 'yellow']
	
fruit = ['blueberry','apple','cherry','banana']
print(colors[0])

print (colors[0],fruit[0], colors[1], fruit[1], colors[2], fruit[2], colors[3], fruit[3])

import re


print(re.findall(r'[Gg]eek', 'GeeksforGeeks: \
				A computer science portal for geeks'))


# ranges
print('Range',re.search(r'[a-zA-Z]', 'x'))

import re
  
  
print('Geeks:', re.search(r'\bGeeks\b', 'Geeks'))
print('GeeksforGeeks:', re.search(r'\bGeeks\b', 'GeeksforGeeks'))