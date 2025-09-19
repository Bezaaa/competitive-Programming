class Spreadsheet(object):

    def __init__(self, rows):
        """
        :type rows: int
        """
        self.rows = rows
        self.cols = 26 
        self.hashMap = {}


        for r in range(1, rows + 1):
            for c in range(self.cols):
                cellName = chr(ord('A') + c) + str(r)
                self.hashMap[cellName] = 0
        

    def setCell(self, cell, value):
        if cell in self.hashMap:
            self.hashMap[cell] =value
       
        

    def resetCell(self, cell):
        if cell in self.hashMap:
            self.hashMap[cell] = 0
        

    def getValue(self, formula):
        parts = formula[1:].split("+")
        total = 0

        for p in parts:
            p = p.strip()
            if p.isdigit():  
                total += int(p)
            else:  
                total += self.hashMap.get(p, 0)  
        return total

        
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)