import re
import requests
import pyperclip

url = "https://www.alldatasheet.com/view.jsp?Searchword="

chip_reference = input("CHIP REFERENCE : ").strip()

while chip_reference != "" :

    resp = requests.get(url + chip_reference)
    pattern = 'Datasheet (.*?) -'
    res = re.findall(pattern, resp.text)
    pyperclip.copy(res[0])
    print(res[0])
    chip_reference = input("CHIP REFERENCE : ").strip()
    
print("No Match Found!")
