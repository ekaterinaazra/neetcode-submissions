class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        library = {'(': ')', '{': '}', '[': ']'}

        for element in s:
            if element in library:
                stack.append(element)
            else:
                if len(stack) == 0:
                    return False
                if element == library[stack[-1]]:
                    stack.pop()
                else:
                    return False 
        return len(stack) == 0
