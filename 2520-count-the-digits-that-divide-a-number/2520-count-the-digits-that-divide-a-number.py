class Solution:
    def countDigits(self, num: int) -> int:
        original=num
        counter=0
        while num>0:
            digit=num%10
            if original%digit==0:
                counter+=1
            num=num//10
        return counter
        