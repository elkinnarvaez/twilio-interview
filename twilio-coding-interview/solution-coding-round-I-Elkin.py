
# Format the text such that each line has exactly `Width` characters and is fully (left and right) justified.
# Add extra spaces between words when necessary so that each line has exactly `Width` characters.
# Extra spaces between words should be distributed as evenly as possible between all the words in a line.
# For the last line of text, it should be left justified and no extra space is inserted between words.
 
# Example:
 
# Width = 25
# Text = "Leaves come in many shapes and sizes. Plants with leaves all year round are evergreens, and those that shed their leaves are deciduous."
 
# Return the formatted lines as:
 
# Leaves   come   in   many //25 chars char: 16 spaces: 9
# shapes  and sizes. Plants
# with   leaves   all  year
# round are evergreens, and
# those   that  shed  their
# leaves are deciduous.

"""
    Description: Function to justify a single line (adding spaces if neccesary)
    Input:
        - currentWords: List of current words that will be included in justified line
        - currentCaracters: Integer of the sum of characters of each word that will be included in justified line
        - width: Integer indicating the width (number of characters) that the line needs to be formatted to
        - isFullyJustified: Boolean that indicates if the line needs to be fully justified
    Output:
        String of the justified line containing all the words specified in the currentWords list
    
    Time complexity: O(n)
"""
def formatLine(currentWords, currentCaracters, width, isFullyJustified):
    spaces = 1
    unevenSpaces = 0
    if isFullyJustified:
        allExtraSpaces = width - currentCaracters
        spaces = (allExtraSpaces // (len(currentWords) - 1))
        unevenSpaces = (allExtraSpaces % (len(currentWords) - 1))
    line = ""
    for j in range(len(currentWords) - 1):      
        line += currentWords[j] + " " * spaces
        if unevenSpaces > 0:
            line += " "
            unevenSpaces -= 1
    line += currentWords[len(currentWords) - 1]
    return line

"""
    Description: Function to justify the text
    Input:
        - text: A string of the text that needs to be justified
        - width: Integer indicating the width (number of characters) that each line needs to be formatted to
    Output:
        A list of strings containing all the fully justified lines (except the last one that is left justified)

    Time complexity: ~ O(n)
"""
def formatText(text, width):
    formattedLines = list()
    words = text.split()
    
    i = 0
    currentWords = list()
    currentCaracters = 0
    while (i < len(words)):
        if (currentCaracters + len(words[i]) <= (width - len(currentWords))):
            currentWords.append(words[i])
            currentCaracters = currentCaracters + len(words[i])
            i += 1
        else:
            formattedLines.append(formatLine(currentWords, currentCaracters, width, True))
            currentWords = list()
            currentCaracters = 0
    formattedLines.append(formatLine(currentWords, currentCaracters, width, False))
    return formattedLines

def main():
    width = 25
    text = "Leaves come in many shapes and sizes. Plants with leaves all year round are evergreens, and those that shed their leaves are deciduous."
    print(formatText(text, width))
main()