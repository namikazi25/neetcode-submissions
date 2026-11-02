class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        record = []
        for i in operations:
            if i != "+" and i != 'D' and i != 'C':
                print("if: " + str(i))
                x.append(int(i))
                record.append(int(i))
            else:
                if i == "+":
                    a = record[-1]
                    b = record[-2]
                    c = a + b
                    record.append(c)
                if i == "D":
                    a = record[-1]
                    c = a * 2
                    record.append(c)
                if i == 'C':
                    record.pop()

        return sum(record)