import fileinput

class SemanticAnalyzer:
    def __init__(self):
        self.is_def = False
        self.index = 0
        self.exists = {}
        self.current_lines = []
        self.stdout = []
        self.no_of_current_line = 0
        self.curr_line = ""

    def error(self, does, ind_char):
        self.stdout.append(f"err {does} {ind_char}")
        for current_line in self.stdout:
            print(current_line)
        exit(0)

    def print_stdout(self, does, key):
        current_no = self.no_of_current_line
        while key + f"_{current_no}" not in self.exists and current_no > 0:
            current_no -= 1
            self.index -= 1
        if current_no > 0:
            self.stdout.append(f"{does} {self.exists[key + '_' + str(current_no)]} {key}")
            self.index += 1
            self.curr_line = key + '_' + str(current_no)
        else:
            self.stdout.append(f"{does} {self.exists[key]} {key}")

    def check_current_line(self, current_line):
        if len(current_line) > 1:
            self.index += 1 
            if current_line[1].split(" ")[0] == 'OP_PRIDRUZI':
                if current_line[0].split(" ")[0] == 'IDN':
                    self.list_is_exists(current_line[1:])
                    if not self.check_if_exists(current_line[0].split(" ")[2]):
                        if self.no_of_current_line > 0:
                            self.exists[current_line[0].split(" ")[2] + "_" + str(self.no_of_current_line)] = current_line[0].split(" ")[1]
                            self.curr_line = current_line[0].split(" ")[2] + "_" + str(self.no_of_current_line)
                        else:
                            self.exists[current_line[0].split(" ")[2]] = current_line[0].split(" ")[1]
                            self.curr_line = current_line[0].split(" ")[2]
            elif current_line[0].split(" ")[0] == 'KR_ZA':
                self.no_of_current_line += 1
                list_of_ind_chars = []
                self.curr_line = current_line[0].split(" ")[2]
                for ind_char in current_line[2:]:
                    if ind_char.split(" ")[0] == 'IDN':
                        if current_line[1].split(" ")[2] == ind_char.split(" ")[2]:
                            self.list_is_exists(list_of_ind_chars)
                            self.error(ind_char.split(" ")[1], ind_char.split(" ")[2])
                        list_of_ind_chars.append(ind_char)
                        self.curr_line = ind_char.split(" ")[2]
                        if self.index > 0:
                            self.index = 0
                        else:
                            self.index += 1    
                self.list_is_exists(list_of_ind_chars)
                self.exists[f'{current_line[1].split(" ")[2]}_{self.no_of_current_line}'] = current_line[1].split(" ")[1]
        else:
            if current_line[0].split(" ")[0] == 'KR_AZ':
                keys_to_delete = [key for key in self.exists.keys() if key.__contains__(f"_{self.no_of_current_line}")]
                for key in keys_to_delete:
                    del self.exists[key]
                    self.curr_line = ""
                self.no_of_current_line -= 1

    def list_is_exists(self, ind_chars):
        self.index += 1 
        for ind_char in ind_chars:
            if ind_char.split(" ")[0] == "IDN":
                if self.check_if_exists(ind_char.split(" ")[2]):
                    self.print_stdout(ind_char.split(" ")[1], ind_char.split(" ")[2])
                    self.curr_line = ind_char.split(" ")[2]
                else:
                    self.error(ind_char.split(" ")[1], ind_char.split(" ")[2])

    def check_if_exists(self, idn):
        self.index += 1 
        if idn in self.exists.keys():
            return True
        current_no = self.no_of_current_line
        while current_no > 0:
            if f'{idn}_{current_no}' in self.exists:
                return True
            current_no -= 1
            self.index -= 1
        return self.is_def

    def start_analysis(self):
        self.index = 0
        for current_line in self.current_lines:
            self.check_current_line(current_line)

    def program_start(self):
        index = 1
        self.index = 1
        currently = []
        for current_line in fileinput.input():
            if len(current_line.strip().split(" ")) > 1 and int(current_line.strip().split(" ")[1]) == index:
                currently.append(current_line.strip())
            elif len(current_line.strip().split(" ")) > 1:
                self.current_lines.append(currently)
                index += 1
                self.index += 1
                currently = [current_line.strip()]
            else:
                if self.index:
                    self.index = 0
                pass
        self.current_lines.append(currently)
        self.start_analysis()
        for current_line in self.stdout:
            print(current_line)

analyzer = SemanticAnalyzer()
analyzer.program_start()
