# palindrome program #
n=input()
i=0
j=len(n)-1
while(i<=j):
    if n[i]==n[j]:
        i+=1
        j-=1
        is_palindrome=True
        break
else:
    is_palindrome=False

print("palindrome" if is_palindrome else "not palindrome")
