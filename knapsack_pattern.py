
#################################################################################################################################################
                            #######################        0/1 KnapSack         ###############################
'''                                     
def knapsack01(w,v,c,n):

    if c<=0 or n==0:                                              # w=weight array, v= value array,c= capacity , n=length of array
        return 0

    if w[n-1]>j:
        return knapsack01(w,v,c,n-1)
    
    else:
        return max(knapsack01(w,v,c,n-1),v[n-1]+knapsack(w,v,c-w[n-1],n-1))
'''

'''
def knapdp(w,v,c,n):

    dp=[[0 for i in range(c+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,c+1):
            if w[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],v[i-1]+dp[i-1][j-w[i-1]])
'''

#################################################################################################################################################
                        #######################       Subset Sum K        ###############################


'''


def subsetsum(arr,n,k):

    if n==0 or k<0:
        return False
    if k==0:
        return True

    if arr[n-1]>k:
        return subsetsum(arr,n-1,k)
    else:
        return subsetsum(arr,n-1,k) or subsetsum(arr,n-1,k-arr[n-1])
'''

'''
def subsetsumdp(arr,n,k):

    dp=[[i for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=False

    for i in range(n+1):
        dp[i][0]=True

    for  i in range(1,n+1):
        for j in range(1,k+1):
            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[-1][-1]
'''
#################################################################################################################################################
                        #######################       Equal Subset Sum Partition         ###############################

'''
                                             #SUBSET SUM K PROBLEM WHERE K=SUM OF ARRAY DIVIDED BY 2

def equalsumdp(arr,n):

    if sum(arr)%2==1:
        return False
    
    k=sum(arr)//2

    dp=[[-1 for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=False
    for i in range(n+1):
        dp[i][0]=True

    for i in range(1,n+1):
        for j in range(1,k+1):

            if j <arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[-1][-1]
'''

#################################################################################################################################################
                        #######################       Minimum Subset Sum Difference         ###############################

'''
                                             #    EXTENSION OF SUBSET SUM PARTITION 
                                             #    KNOW ALL POSSIBLE SUBSETS AND FIND MINIMUM SUBSET DIFFERENCE

def equalsumdp(arr,n):

    k=sum(arr)

    dp=[[-1 for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=False
    for i in range(n+1):
        dp[i][0]=True

    for i in range(1,n+1):
        for j in range(1,k+1):

            if j <arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    ans=float('inf')

    for j in range(0,k//2+1):
        if dp[-1][j]:
            ans=min(ans,abs(k-2*j))


    return ans
'''
#################################################################################################################################################
                        #######################    Count of   Subset Sum K        ###############################




'''
def countsubsetsum(arr,n,k):

    if k==0:
        return 1

    if n==0 or k<0:
        return 0

    if arr[n-1]>k:
        return countsubsetsum(arr,n-1,k)
    else:
        return countsubsetsum(arr,n-1,k) + countsubsetsum(arr,n-1,k-arr[n-1])

'''
'''

def countsubsetsumdp(arr,n,k):

    dp=[[i for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=0

    for i in range(n+1):
        dp[i][0]=1

    for  i in range(1,n+1):
        for j in range(1,k+1):
            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j] + dp[i-1][j-arr[i-1]]

    return dp[-1][-1]
'''
#################################################################################################################################################
                        #######################    Target Sum K        ###############################

                                 
''' 
                    # QUESTION MODIFIES INTO NO OF SUBSETS WITH DIFFERENCE T
                    # EXTENSION OF SUBSET COUNT K ,WE HAVE TO FIND NO. OF SUBSETS WITH SUM EQUAL (T+S)//2 , X+Y=S,X-Y=T
                        
def targetsum(arr,n,t):
    
    s=sum(arr)
    
    if s<t or (s+t)%2==1:
        return 0

    ans=0
    dp=[[0 for i in range(s+1)] for i in range(n+1)]-
    
    for i in range(s+1):
        dp[0][i]=0
    for i in range(n+1):
        dp[i][0]=1
        
    for i in range(1,n+1):
        for j in range(1,s+1):
            
            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] + dp[i-1][j-arr[i-1]]
         
    return dp[-1][(s+t)//2]
'''







#################################################################################################################################################
                            #######################        Unbounded KnapSack         ###############################
'''                                     
def uknapsack(w,v,c,n):

    if c<=0 or n==0:                                              # w=weight array, v= value array,c= capacity , n=length of array
        return 0

    if w[n-1]>j:
        return uknapsack(w,v,c,n-1)
    
    else:
        return max(uknapsack(w,v,c,n-1),v[n-1]+uknapsack(w,v,c-w[n-1],n))
'''

'''
def uknapdp(w,v,c,n):

    dp=[[0 for i in range(c+1)] for i in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,c+1):
            if w[i-1]>j:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j],v[i-1]+dp[i][j-w[i-1]])
'''

#################################################################################################################################################
                            #######################         Rod Cutting Problem         ###############################
        '''
                                                        SAME AS UNBOUNDED KNAPSACK
                            '''


#################################################################################################################################################
                            #######################    Maximum number of ways to make change         ###############################

'''
def coinchange(arr,n,k):

    if k==0:
        return 1
    
    if n==0 or k<0:
        return 0
    
    if arr[n-1]>k:
        return coinchange(arr,n-1,k)
    
    else:
        return coinchange(arr,n-1,k)+coinchange(arr,n,k-arr[n-1])

'''

'''
def coinchangedp(arr,n,k):

    dp=[[-1 for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=0

    for i in range(n+1):
        dp[i][0]=1

    for  i in range(1,n+1):
        for j in range(1,k+1):

            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j] + dp[i][j-arr[i-1]]

    return dp[-1][-1]

'''

#################################################################################################################################################
                            #######################    Minimum number of coins to make change         ###############################


'''
                                            #initialize columns with infinity as we need infinity coins to make a sum when we have 0 coins
def mincoinchangedp(arr,n,k):

    m=float('inf')
    dp=[[-1 for i in range(k+1)] for i in range(n+1)]

    for i in range(k+1):
        dp[0][i]=m

    for i in range(n+1):
        dp[i][0]=0

    for  i in range(1,n+1):
        for j in range(1,k+1):

            if j<arr[i-1]:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=min(dp[i-1][j],1+ dp[i][j-arr[i-1]])    #use max instead of min for maximum no. of cuts that can be made (maximum ribbon cut)

    if dp[-1][-1]==m:
        return -1
    return dp[-1][-1]
'''