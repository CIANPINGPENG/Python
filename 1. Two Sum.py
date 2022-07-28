class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #if(len(nums)==2):
        #    return [0,1]


        tmp=nums.copy()
        nums.sort()
        low=0
        high=len(nums)-1
        while(low<high):
            n=nums[low]+nums[high]
            if n==target:
                break
            elif target>n:
                low+=1
            else:
                high-=1

        found_a = False
        found_b = False

        for i in range(0,len(tmp)):

            if tmp[i]==nums[low] and found_a == False:
                a = i
                found_a = True
            elif tmp[i] == nums[high]:
                b = i
                found_b = True
                
            if(found_a == True and found_b == True):
                break


        return [a,b]
