class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for o in operations:
            if len(record) >= 2 and o == '+':
                b = record[-1]
                a = record[-2]
                record.append(a + b)
            if len(record) >= 2 and o == 'D':
                b = record[-1]
                a = record[-2]
                record.append(a * b)
            if len(record) >= 2 and o == 'C':
                record.pop()
                record.append(o)
        
        return record[-1]