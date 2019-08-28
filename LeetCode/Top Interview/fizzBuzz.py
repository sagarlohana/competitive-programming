class Solution(object):
    # List comprehension and clever use of * operator on strings and "or"
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return ["Fizz" * (not i % 3) + "Buzz" * (not i % 5) or str(i) for i in range (1, n+1)]
    # Standard method using .append on a list
    def fizzBuzz(self, n):
        res = []
        for i in range (1, n+1):
            if not i % 15:
                res.append("FizzBuzz")
            elif not i % 3:
                res.append("Fizz")
            elif not i % 5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    # Standard method, storing modulus results in vars
    def fizzBuzz(self, n):
        res = []
        for i in range (1, n+1):
            div5 = not i % 5
            div3 = not i % 3
            if div5 and div3:
                res.append("FizzBuzz")
            elif div3:
                res.append("Fizz")
            elif div5:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    