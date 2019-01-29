
# def reverse(s):
#     return s[::-1];
#
# def isPalindrome(str):
#     revStr = reverse(str);
#     print(revStr);
#     if str == revStr:
#         print("String is Palindrome");
#         return True
#     print("String is not Palindrome");
#     return False;
#
# str = "abc";
# isPalindrome(str);
# str1 = "aba"
# isPalindrome(str1);

# --------------------------------- Using loop ----------------------------


def isStrPalindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False;
        return True;

str = "abc";
print(isStrPalindrome(str));
str1 = "aba"
print(isStrPalindrome(str1));
