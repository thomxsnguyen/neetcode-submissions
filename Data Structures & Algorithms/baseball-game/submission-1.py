class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for o in operations:
            if len(record) >= 2 and o == '+':
                b = record[-1]
                a = record[-2]
                record.append(a + b)
            elif len(record) >= 1 and o == 'D':
                a = record[-1]
                record.append(a* 2)
            elif len(record) >= 2 and o == 'C':
                record.pop()
            else:
                record.append(int(o))
        
        return sum(record)