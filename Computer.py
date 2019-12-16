class Computer():
    def __init__(self, intcode, inputs=[], print_output=False):
        self.intcode = intcode
        self.temp_copy = list(self.intcode)
        self.inputs = inputs
        self.inst_code = None
        self.outputs = []
        self.counter = 0
        self.is_finished = False
        self.is_halted = False
        self.relative_base = 0
        self.print_output = print_output

        # Assign extra memory to the computer
        memory = [0] * 10000
        self.temp_copy.extend(memory)

        # param_modes are stored in reverse. 
        # i.e if 3 params, param_modes[i] is the mode of ith param
        self.param_modes = []

    def get_param(self, param_number, is_read_param=False):        
        is_default_mode = (param_number >= len(self.param_modes))
        mode = 0 if is_default_mode else self.param_modes[param_number]
        val = None
        ele = self.temp_copy[self.counter]
        if mode is None or mode == 0:
            val = ele if is_read_param else self.temp_copy[ele]
        elif mode == 1:
            val = ele
        elif mode == 2:
            val = self.relative_base + ele if is_read_param else self.temp_copy[self.relative_base + ele]

        return val

    def updates_inst_code(self, inst_code):
        self.inst_code = inst_code
        self.param_modes = [int(x) for x in str(self.inst_code)[:-2]]
        self.param_modes.reverse()

    def get_read_param(self, param_number):
        param = self.get_param(param_number)
        self.counter += 1
        return param

    def get_write_param(self, param_number):
        param = self.get_param(param_number, True)
        self.counter += 1
        return param

    def add(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)
        param3 = self.get_write_param(2)
        self.temp_copy[param3] = param1 + param2

    def multiply(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)
        param3 = self.get_write_param(2)
        self.temp_copy[param3] = param1 * param2

    def process_input(self):
        if len(self.inputs) > 0:
            self.counter += 1
            param1 = self.get_write_param(0)
            self.temp_copy[param1] = self.inputs.pop(0)
            self.is_halted = False
        else:
            self.is_halted = True 

    def process_output(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        self.outputs.append(param1)
        if self.print_output:
            print(param1)

    def jump_if_true(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)
        if param1 !=0:
            self.counter = param2

    def jump_if_false(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)
        if param1 == 0:
            self.counter = param2

    def less_than(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)        
        param3 = self.get_write_param(2)
        self.temp_copy[param3] = 1 if param1 < param2 else 0

    def equals(self):        
        self.counter += 1
        param1 = self.get_read_param(0)
        param2 = self.get_read_param(1)        
        param3 = self.get_write_param(2)
        self.temp_copy[param3] = 1 if param1 == param2 else 0

    def finish(self):
        self.counter += 1
        self.is_finished = True

    def update_relative_base(self):
        self.counter += 1
        param1 = self.get_read_param(0)
        self.relative_base += param1

    def run_program(self, inputs=None):
        if inputs is not None:
            self.inputs = inputs
        while self.counter < len(self.temp_copy):
            self.updates_inst_code(self.temp_copy[self.counter])
            op_code = self.inst_code - int(self.inst_code / 100) * 100
            if op_code == 1:
                self.add()
            elif op_code == 2:
                self.multiply()
            elif op_code == 3:
                self.process_input()
                if self.is_halted:
                    break
            elif op_code == 4:
                self.process_output()
            elif op_code == 5:
                self.jump_if_true()
            elif op_code == 6:
                self.jump_if_false()
            elif op_code == 7:
                self.less_than()
            elif op_code == 8:
                self.equals()
            elif op_code == 9:
                self.update_relative_base()
            elif op_code == 99:
                self.finish()
                break