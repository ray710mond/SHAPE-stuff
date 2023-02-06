## is it a palindrome

test_string = "kayak"

def is_palindrome(test_string):
    stack = []
    for i in range(0, len(test_string)//2):
        stack.append(test_string[i])

    if len(test_string) % 2 != 0:
        while(len(stack) > 0):
            i+=1
            if stack.pop() == test_string[i]:
                return False
        return True

print(is_palindrome(test_string))

