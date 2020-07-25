#python3 
# encoding='utf-8'
import math
class Solution:
    def divisorGame(self, N: int) -> bool:
        # 辗转相减      
        #1 B
        #2 1 A
        #3 1 B
        #4 2 1 (2B)   (1A) A
        #5 1 B
        #6 3 2 1 A
        #7 1 B
        #8 4 2 1   A
        #9 3 1 B
        #10 5 2 1 A
        
        return N%2==0