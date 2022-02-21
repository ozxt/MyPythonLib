#coding:utf-8
from KMP import kmp_match

if __name__ == '__main__':
    # print(kmp_match("abcdfgtasdasdfgr","dfgr"))
    # print(kmp_match("aaaaa","bba"))
    # print(_bulid_LPS("aaaa"))
    # print(_bulid_LPS("abcabadjabca"))
                      # 000121001234
    # print(_bulid_LPS("abcaabcaaaacjiabcaabc"))
                      # 000112345110001234567
    # print(_bulid_LPS("aaacaaaa"))
   	print(kmp_match("","")==0)
   	print(kmp_match("abc","")==0)
   	print(kmp_match("","a")==-1)
   	print(kmp_match("aaa","a")==0)
   	print(kmp_match("aaaab","ab")==3)
   	print(kmp_match("asddidhdd","dd")==2)
   	print(kmp_match("dddddd","ddd")==0)