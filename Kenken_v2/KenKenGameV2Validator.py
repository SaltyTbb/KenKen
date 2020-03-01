class Validator(object):
    def validatePlus(self,answer,expectedAnswer):
        total = 0
        for num in answer:
            total += int(num)
        return total == expectedAnswer
    def validateMinus(self,answer,expectedAnswer):
        num1 = int(answer[0])
        num2 = int(answer[1])
        return abs(num1-num2) == expectedAnswer
        """
        the abs() can be replaced by
        return num1-num2==expectedAnswer or num2-num1==expectedAnser
        """

    def validateMulitply(self,answer,expectedAnswer):
        total = 1
        for num in answer:
            total *= int(num)
        return total == expectedAnswer

    def validateDivision(self,answer,expectedAnswer):
        num1 = int(answer[0])
        num2 = int(answer[1])
        if(num1/num2 == expectedAnswer or num2/num1 == expectedAnswer):
            return True
        return False  # using else does the same thing here


    def validateAnswer(self,answer, rule):
        # answer: list of string of user input|| rule: string of rule
        operater = rule[-1]
        expectedAnswer = int(rule[:-1])
        if(operater == '+'):
            return self.validatePlus(answer,expectedAnswer)

            """
            the for-loop can be replaced by
            return sum(list(map(lambda x: int(x), answer))) == expectedAnswer
            """

        elif(operater == '-'):
            return self.validateMinus(answer,expectedAnswer)

        elif(operater == '*'):
            return self.validateMulitply(answer,expectedAnswer)

        elif(operater == '/'):
            return self.validateDivision(answer,expectedAnswer)
        return False # this line should never be reached