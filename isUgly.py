def isUgly(num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num == 0:
            return False
        if num % 2 or num % 3 or num % 5 == 0:
            return True
        return False

if __name__ == '__main__':
    x = isUgly(3)
    print(x)