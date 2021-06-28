'''Input:
ant magenta magnate tan gnamate
Output: 3
Explanation
Anagram strings(1) - ant, tan
Anagram strings(2) - magenta, magnate,
                     gnamate
Thus, only second subset have largest
size i.e., 3
'''

from collections import Counter
def maxAnagramSize(input):
    # split input string separated by space
    input = input.split(" ")

    # sort each string in given list of strings
    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))

    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    freqDict = Counter(input)

    # get maximum value of frequency
    print(max(freqDict.values()))
    print(max(freqDict.items()))


if __name__ == "__main__":
    input = 'ant magenta magnate tan gnamate'
    maxAnagramSize(input)