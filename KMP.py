#coding:utf-8
#KMP

def _bulid_LPS(s):
    # LPS:longest proper suffix which is also prefix.
    # 真前缀和真后缀相等且最长
    # A proper prefix is prefix with whole string not allowed.
    # "ABC" 's proper prefix are "A","AB".
    # lps[0] must be 0
    # lps[i] indicates length of LPS on s[0,i].
    # "AAABAAAA" : lps=[0,1,2,0,1,2,3,3]
    lps = [0] * len(s)
    i = 0  # index for prefix
    j = 1  # index for suffix
    # print(lps)
    while j<len(s):
        if s[i]==s[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            # step one
            if i==0:
                lps[j] = 0
                j += 1
            # 考虑这种情况:
            # AAABAAAA i=3,j=7
            #
            # 另一个情况 AABAACAABAAD i=5,j=11
            # 此时lps=[0,1,0,1,2,0,1,2,3,4,5]
            # i能走到5，说明s[0,j-1]存在一个长度为5的LPS
            # 即s[0,i-1]==s[j-i,j-1],即s[0,4]==s[6,10]
            # 而lps[i-1]即lps[4]为2，说明s[0,4]中有一个LPS，
            # 也即s[6,10]中有个同样的LPS。
            # lps[4]为2，说明这个LPS的长度是2，
            # 即s[0,1]==s[3,4]==s[6,7]==s[9,10]
            # 那下次我们就可从i=2,j=11比较
            else:
                i = lps[i-1]
        # print(lps)
    return lps


def kmp_match(s, pattern):
    # 在s中搜索pattern
    # 若能匹配，返回从左到右最先匹配的串的起点索引
    # 若无，返回-1

    if not pattern:
        return 0
    if not s:
        return -1
    lps = _bulid_LPS(pattern)
    M,N = len(pattern),len(s)
    i = 0 # index for pattern
    j = 0 # index for s
    while j<N and i<M:
        if pattern[i] == s[j]:
            i += 1
            j += 1

            if i==M:
                return j-M
        else:
            if i==0:
                j += 1
            else:
                i = lps[i-1]

    return -1
