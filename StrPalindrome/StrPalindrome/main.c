//
//  main.c
//  StrPalindrome
//
//  Created by Suryakant on 10/7/18.
//  Copyright © 2018 Suryakant. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isPalRec(char s[], int startIndex, int endIndex){
    if (startIndex == endIndex)
        return  true;
    if (s[startIndex] != s[endIndex]){
        return false;
    }
    if (startIndex < endIndex + 1)
    return isPalRec(s, startIndex + 1 , endIndex - 1);
    
    return true;
}

bool isPalindrome(char str[]){
    int len = strlen(str);
    if (len == 0)
        return true;
    return isPalRec(str, 0 , len-1);

}


int main(int argc, const char * argv[]) {
    // insert code here...
    char str[] = "geeg";
    
    if (isPalindrome(str))
        printf("Yes");
    else
        printf("No");
    printf("\n");
    return 0;
}
