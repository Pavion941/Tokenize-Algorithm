text = "A dog named {target} is {here}. He is SO {{{MEAN}}}. I used \{here} to say the location!"
words = text.split(" ")
# split text into a list of
temp_element = ""
print(words)

for i in range(len(words)):
    # cycle elements in "words" list
    if '{' in words[i] and '}' in words[i]:
        # if braces are present do next thing
        for c in words[i]:
            if c.isalpha() or c.isspace():
                temp_element += c
                # cycle characters in the given element
                # check to see if character is alphanumeric or a space
                # if so, add character to temporary element
        words[i] = temp_element
        # outside of loop, replace old element with contents of temporary element
        temp_element = ""
        # reset temporary element for next round
        print(words[i], "is a keyword")

print(words)