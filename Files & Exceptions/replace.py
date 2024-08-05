
"""10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:"""


file = "learning_python.txt"
with open(file) as re:
    lines = re.read()
    print(lines.replace("python", "C"))
