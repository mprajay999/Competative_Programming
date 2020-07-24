#################################################################################################################################################
                        #######################        Longest Common Subsequence (LCS)         ###############################

'''
def lcs(arr1,arr2,m,n):

    if m==0 or n==0:
        return 0

    if arr1[m-1]==arr2[n-1]:
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
##################  Printing LCS #################
'''
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
'''

#################################################################################################################################################
                        #######################        Longest Common Substring         ###############################

'''
def lcst(arr1,arr2,m,n,ans=0):

    if m==0 or n==0:
        return 0

    if arr1[m-1]==arr2[n-1]:
        return lcs(arr1,arr2,m-1,n-1,ans+1)

    else:
        return max(ans,lcst(arr1,arr2,m-1,n,ans),lcst(arr1,arr2,m,n-1,ans))
'''

'''
def lcstdp(arr1,arr2,m,n):

    dp=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr1[i-1]==arr2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=0

    return max(max(i) for i in dp)
''' 

#################################################################################################################################################
                        #######################        Shortest Common SuperSequence        ###############################


'''
# SUM OF LENGTHS OF TWO SUBSEQUENCE M AND N -   LCS(M,N)                     LEN(M+N)-LCS(M,N)

'''

####### PRINTING SES ########

'''
def printses(arr1,arr2,m,n):
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
                ans+=arr2[j-1]
                j-=1
            else:
                ans+=arr1[i-1]
                i-=1

    ans+=arr1[:i][::-1]
    ans+=arr2[:j][::-1]

    print(ans[::-1])
'''


#################################################################################################################################################
                        ################ Minimum Number of Insertion and Deletion to convert String a to String b ##############

'''
# INSERTIONS = LEN(B)-LCS(A,B)   DELETIONS= LEN(A)-LCS(A,B)
'''


#################################################################################################################################################
                        #######################        Longest Palindromic Subsequence        ###############################

'''
# LCS(A,A[::-1])
'''

#################################################################################################################################################
          #######################  Minimum number of deletion / insertion in a string to make it a palindrome  #############################

'''
# LEN(A)-LCS(A,A[::-1])
'''
#################################################################################################################################################
                        #######################       Longest repeating subsequence       ###############################

'''
def lrsdp(arr1,arr2,m,n):

    dp=[[0 for i in range(n+1)] for i in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if arr1[i-1]==arr2[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    return dp[-1][-1]
''' 

#################################################################################################################################################
                        #######################       Sequence Pattern Matching     ###############################

'''
     # TO CHECK IF A IS SUBSEQUENCE OF B
     # TRUE IF LCS(A,B)=MIN(LEN(A),LEN(B))

'''