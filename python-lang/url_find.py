import re
from urllib.request import urlopen
def load_and_save(url, fl):
    with urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            fl.write(line)
# Uncomment the following lines to load the source to file.
#f=open('source.txt','w')
#load_and_save('https://www.python.org',f)
#f.close()

hold = ''        
with open('source.txt') as f:
    hold = f.read()
print(type(hold))
target = hold.split()
# All links
result = [item[6:] for item in target if "href" in item]
# Links starting with http or https
result2 = [item[6:(0 or item.index("\""))] for item in result if item.startswith("http")]
for link in result2:
    print(link)

