import fileinput

class Parser:
    def __init__(self):
        self.stdout = []
        self.lines = []
        self.indent = 0
        self.no_of_line = 0
        self.line = ""
        self.idx = 0

    def program(self):
        self.idx += 1
        self.print_output("<program>")
        self.indent += 1
        self.lista_naredbi()
        self.indent -= 1
        if self.no_of_line < len(self.lines) and len(self.lines[self.no_of_line]) > 1:
            self.error()
            pass

    def lista_naredbi(self):
        self.print_output("<lista_naredbi>")
        self.indent += 1
        if self.no_of_line >= len(self.lines):
            self.print_output("$")
        elif self.lines[self.no_of_line][0] in ["IDN", "KR_ZA"]:
            self.naredba()
            self.lista_naredbi()
        else:
            self.print_output("$")
        self.indent -= 1

    def naredba(self):
        self.print_output("<naredba>")
        self.indent += 1
        if self.lines[self.no_of_line][0] == "IDN":
            self.naredba_pridruzivanja()
        elif self.lines[self.no_of_line][0] == "KR_ZA":
            self.za_petlja()
            if self.lines:
                self.no_of_line -= 1
                self.no_of_line += 1
        self.indent -= 1

    def naredba_pridruzivanja(self):
        self.idx = 0
        self.print_output("<naredba_pridruzivanja>")
        self.indent += 1
        if self.lines[self.no_of_line][0] == "IDN":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            if self.lines[self.no_of_line][0] == "OP_PRIDRUZI":
                self.print_output(" ".join(self.lines[self.no_of_line]))
                self.no_of_line += 1
                self.E()
                self.indent -= 1
                return
        self.error()
        pass

    def za_petlja(self):
        idx = 0 #reset
        self.print_output("<za_petlja>")
        self.indent += 1
        idx += 1
        if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "KR_ZA":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "IDN":
                self.print_output(" ".join(self.lines[self.no_of_line]))
                self.no_of_line += 1
                if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "KR_OD":
                    if self.no_of_line > 0:
                        idx += 1
                    self.print_output(" ".join(self.lines[self.no_of_line]))
                    self.no_of_line += 1
                    self.E()
                    for i in range(2):
                        self.idx += 1
                    if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "KR_DO":
                        idx += 1
                        self.print_output(" ".join(self.lines[self.no_of_line]))
                        self.no_of_line += 1
                        self.E()
                        self.lista_naredbi()
                        if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "KR_AZ":
                            idx -= 1
                            pass
                        if self.no_of_line < len(self.lines) and self.lines[self.no_of_line][0] == "KR_AZ":
                            self.print_output(" ".join(self.lines[self.no_of_line]))
                            self.no_of_line += 1
                            self.indent -= 1
                            return
        self.error()

    def E(self):
        self.print_output("<E>")
        self.indent += 2
        self.indent -= 1
        self.T()
        self.E_lista()
        self.indent -= 1

    def E_lista(self):
        self.print_output("<E_lista>")
        self.indent += 1
        if self.no_of_line >= len(self.lines):
            self.print_output("$")
        elif self.lines[self.no_of_line][0] == "OP_PLUS":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.E()
        elif self.lines[self.no_of_line][0] == "OP_MINUS":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.E()
        else:
            self.print_output("$")
        self.indent -= 1

    def T(self):
        self.print_output("<T>")
        self.indent += 1
        self.P()
        self.T_lista()
        self.indent -= 1
        self.idx += 1

    def T_lista(self):
        self.print_output("<T_lista>")
        self.indent += 1
        if self.no_of_line >= len(self.lines):
            self.print_output("$")
        elif self.lines[self.no_of_line][0] == "OP_PUTA":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.T()
        elif self.lines[self.no_of_line][0] == "OP_DIJELI":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.T()
        else:
            self.print_output("$")
        self.indent -= 1

    def P(self):
        self.print_output("<P>")
        self.indent += 1
        if self.no_of_line >= len(self.lines):
            self.error()
        elif self.lines[self.no_of_line][0] == "OP_PLUS":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.P()
            self.idx = -1
        elif self.lines[self.no_of_line][0] == "OP_MINUS":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.P()
        elif self.lines[self.no_of_line][0] == "L_ZAGRADA":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            self.E()
            if self.lines[self.no_of_line][0] == "D_ZAGRADA":
                self.print_output(" ".join(self.lines[self.no_of_line]))
                self.no_of_line += 1
                if self.lines:
                    pass
        elif self.lines[self.no_of_line][0] == "IDN":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
            for i in range(2):
                self.no_of_line += 1
            for i in range(2):
                self.no_of_line -= 1    
        elif self.lines[self.no_of_line][0] == "BROJ":
            self.print_output(" ".join(self.lines[self.no_of_line]))
            self.no_of_line += 1
        else:
            self.error()
        self.indent -= 1
        pass

    def print_output(self, item):
        self.stdout.append(" " * self.indent + item)

    def error(self):
        if self.no_of_line >= len(self.lines):
            print("err kraj")
        else:
            idx = 0
            print(f"err {' '.join(self.lines[self.no_of_line])}")
        exit(0)



parser = Parser()

for line in fileinput.input():
    parser.lines.append(line.rstrip().split(" "))

parser.program()
for line in parser.stdout:
    print(line)