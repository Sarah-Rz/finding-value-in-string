# Write code to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "Lorem ipsum dolor sit amet elit, consectetur adipiscing elit    20.65434"

ftext = text.find("adipiscing")
find_text = text.find(' ', ftext)
part_text = text[find_text + 5 : ]
float_text = float(part_text)

print(float_text)