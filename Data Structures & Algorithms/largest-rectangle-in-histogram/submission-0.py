class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []


        ## so this is to iterate through it fully from left to right
        for i,h in enumerate(heights):
            ## them we have to start from our first index
            start = i
            ## and we check is the stack not empty and the stack we have greater than the next height
            while stack and stack[-1][1] > h:
                ## pop it if it is and then assign the values index and heihgt
                index, height = stack.pop()
                ## get that MAX AREA (i - index) = width
                maxArea = max(maxArea, height * (i - index))
                ## make that new square the start of the stack
                start = index
            ## then we have to append the index and height to the stack
            stack.append((start, h))
        
        ## iterate through the stack to find the ones that aren't popped and check 
        ## if they are biggerr the max area:
    
        for i,h in stack:
            ## why len(heights?) because thats how LONG the rectangle is!!
            ## those are the ones that are left
            maxArea = max(maxArea, h * (len(heights) - i ))
        return maxArea









