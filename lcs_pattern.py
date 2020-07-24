#################################################################################################################################################
                        #######################        Longest Common Subsequence (LCS)         ###############################

'''
def lcs(arr1,arr2,m,n):

    if m==0 or n==0:
        return 0

    if arr1[m]==arr2[n]:
        return 1+lcs(arr1,arr2,m-1,n-1)

    else:
        return max(lcs(arr1,arr2,m-1,n),lcs(arr1,arr2,m,n-1))
'''

'''
def lcsdp(arr1,arr2,m,n):

    dp=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr1[i-1]==arr2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]
''' 
#####  Printing LCS ######

def printlcs(arr1,arr2,m,n):
    dp=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr1[i-1]==arr2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    ans=''
    while i>0 and j>0 :
        if arr1[i-1]==arr2[j-1]:
            ans+=arr1[i-1]
            i-=1
            j-=1
        else:
            if dp[i][j-1]>dp[i-1][j]:
                j-=1
            else:
                i-=1

    print(ans[::-1])


printlcs('abcdaf','acbcf',6,5)



#################################################################################################################################################
                        #######################        Longest Common Substring         ###############################

'''
def lcst(arr1,arr2,m,n,ans=0):

    if m==0 or n==0:
        return 0

    if arr1[m]==arr2[n]:
        return lcs(arr1,arr2,m-1,n-1,ans+1)

    else:
        return max(ans,lcst(arr1,arr2,m-1,n,ans),lcst(arr1,arr2,m,n-1,ans))
'''

'''
def lcstdp(arr1,arr2,m,n):

    dp=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr1[m]==arr2[n]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=0

    return max(max(i) for i in dp)
''' 