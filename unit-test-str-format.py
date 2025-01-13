# created: 2023.07.25
def selfStringReplacement(text = '', *args):
    signStart = '{'
    signEnd = '}'

    # collect indexes pos of replacement signs
    indexArray = []
    i = 0
    while i < len(text):
        if  (i + 1 < len(text) and i + 2 < len(text) and
            text[i] == signStart and text[i+2] == signEnd and text[i+1].isdigit()):
            charIndex = int(text[i+1])
            openBracketIndex = i
            closeBracketIndex = i + 2
            # ({,}, 0)
            indexArray.append( (openBracketIndex, closeBracketIndex, charIndex) )
        i += 1
    else:
        print('while-else:', i)
        print(indexArray)

    # Replace reference index to args' values
    retNewText = ''
    currentText = ''
    previousSubtext = ''
    splitText = text.split(signEnd)
    splitIndex = 0
    signEndRemoving = 1
    for record in indexArray:
        currentText = splitText[splitIndex] + signEnd
        # desructing like {id, name} = object
        # e.g.: (18, 20, 0) => posIndex => pozition of bracketValue {0}
        (startSignIndex, endSignIndex, posIndex) = record
        if len(retNewText) > 0:
            previousSubtext += splitText[splitIndex - 1] + signEnd
            startSignIndex -= len(previousSubtext)
            endSignIndex -= len(previousSubtext)

        retNewText +=  currentText[:startSignIndex]
        # "replacing number to inserting string"
        retNewText +=  str(args[posIndex])
        retNewText +=  currentText[endSignIndex + signEndRemoving:]

        splitIndex += 1

    remainString = splitText[len(splitText)-1]
    retNewText += remainString
    # ternalis: trueValue if condition else falseValue
    return retNewText if retNewText != '' else text


"""text = "I have {0} {1} and {2} {3}."
result = selfStringReplacement(text, 5, "apples", 3, "bananas")
print(result)
exit();
"""

# test cases from chatGPT
def run_tests():
    # Test case 1: Basic replacement
    text = "Hello, my name is {0} and I am {1} years old."
    result = selfStringReplacement(text, "Alice", 30)
    print(result)
    assert result == "Hello, my name is Alice and I am 30 years old."

    # Test case 2: Multiple replacements
    text = "I have {0} {1} and {2} {3}."
    result = selfStringReplacement(text, 5, "apples", 3, "bananas")
    assert result == "I have 5 apples and 3 bananas."

    # Test case 3: Repeated replacement
    text = "{0} is {0} years old."
    result = selfStringReplacement(text, "Alice")
    assert result == "Alice is Alice years old."

    # Test case 4: Empty string input
    text = ""
    result = selfStringReplacement(text, 42)
    assert result == ""

    # Test case 5: No replacements in the text
    text = "This is a plain text."
    result = selfStringReplacement(text, 123)
    assert result == "This is a plain text."

    # Test case 6: Missing arguments
    text = "I have {0}, {1}, but no {2}."
    try:
        result = selfStringReplacement(text, "apples", "bananas")
        assert False, "Expected IndexError"
    except IndexError:
        pass  # Expected IndexError

    # Test case 7: Negative index (Not supported in selfStringReplacement)
    """
    text = "I have {-1}, {0}, and {1}."
    try:
        result = selfStringReplacement(text, "apples", "bananas", "oranges")
        assert False, "Expected IndexError"
    except IndexError:
        pass  # Expected IndexError
    """

    print("=>> All test cases passed!")

if __name__ == "__main__":
    run_tests()
