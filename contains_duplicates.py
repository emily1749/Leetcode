def containsDuplicate(self, nums):
    myDict = {}
    for numb in nums:
        if numb in myDict:
            return True
        else:
            myDict[numb] = True

    return False