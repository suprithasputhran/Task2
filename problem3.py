def main():
    str=input("")
    palindrome = longestPalindrome(str)
    print(palindrome)

def longestPalindrome(s):
    len_palindrome = 0
    palindrome = ""
    len_s = len(s)
    if(len_s < 2):
        return s
    p_table = [[False for row in range(len_s)] for col in range(len_s)]
    for i in range(len_s):
        p_table[i][i] = True
        if(len(s[i:i+1]) > len_palindrome):
            len_palindrome = len(s[i:i+1])
            palindrome = s[i:i+1]
            for i in range(len_s -2,-1,-1):
                for j in range(i+1, len_s):
                    if(s[i] == s[j]):
                        if((j - i == 1) or (p_table[i+1][j-1])):
                            p_table[i][j] = True
                        if len_palindrome < j - i + 1:
                            len_palindrome = j - i + 1
                            palindrome = s[i: j+1]
    return palindrome

if __name__ == "__main__":
    main()