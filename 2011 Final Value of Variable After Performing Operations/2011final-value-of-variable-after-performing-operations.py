class Solution(object):
    def finalValueAfterOperations(self, arr):

        X=0
        for index in range(len(arr)):
            if (arr[index] == "X++") or (arr[index] == "++X"):
                X +=1
            else:
                X -=1
        return X