class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        a, b = 3, 5
        for x in range(1, n+1):
            if x % (a*b) == 0:
                arr.append('FizzBuzz')
            elif x % a == 0:
                arr.append('Fizz')
            elif x % b == 0:
                arr.append('Buzz')
            else:
                arr.append(str(x))
        return arr
