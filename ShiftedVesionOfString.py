#Two string S1 and S2 are given, check whether S1 is a shifted version of S2

def areRotation(str1, str2):
    if len(str1) != len(str2):
        return False;
    temp = str1+str1;
    return temp.count(str2);




#driver code;
string1 = "ABACD"
string2 = "ABACDNN"

print(areRotation(string1, string2));
