#Implemented following exs:
#10. NAND NOR XOR
#11 half-adder


class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter the value of the pin A for the gate " + self.getLabel() + "--->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter the value of the pin B for the gate " + self.getLabel() + "--->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("No empty Pins -- ERROR ")


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if (self.pin == None):
            return int(input("Enter the value of the pin for the gate " + self.getLabel() + "--->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("No empty Pins -- ERROR ")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):
    def __init__(self, n):
        AndGate.__init__(self, n)

    def performGateLogic(self):
        a = AndGate.performGateLogic(self)
        if a == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):
    def __init__(self, n):
        OrGate.__init__(self, n)

    def performGateLogic(self):
        a = OrGate.performGateLogic(self)
        if a == 1:
            return 0
        else:
            return 1

class XorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1

class HalfAdder(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            SUM = 0
        else:
            SUM = 1
        if a == 1 and b == 1:
            CARRY = 1
        else:
            CARRY = 0
        return SUM, CARRY




class NotGate(UnaryGate):
    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromGate = fgate
        self.toGate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromGate

    def getTo(self):
        return self.toGate


def main():
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    output1 = g4.getOutput()
    g5 = NandGate("G5")
    g6 = NandGate("G6")
    g7 = AndGate("G7")
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    output2 = g7.getOutput()
    print(output1 == output2)


#main()


