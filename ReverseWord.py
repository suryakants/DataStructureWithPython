# reverse the string by word
# Input :  "How are you" Output = "you are how";



# class py_solution:
def reverse_words(s):
    print(s.split());
    return ' '.join(reversed(s.split()))


# print(reverse_words('How are you?'))



def reverseTheWorld(s):
    wordArr = s.split();
    print(wordArr);
    reversedArr = reversed(wordArr);
    # print(reversed(wordArr));
    return(' '.join(reversedArr));

print(reverseTheWorld("How are you"));
