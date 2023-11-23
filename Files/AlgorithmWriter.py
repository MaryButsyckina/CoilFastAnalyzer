class AlgorithmWriter:
    def __init__(self, file):
        self.file = file

    def write_measurement(self, meas_num):
        self.file.writelines([f"Measurement: {meas_num}\n"])

    def write_current(self, power_type, current):
        if power_type == 'main':
            self.file.writelines([f"Current: {current}\n"])
        elif power_type == 'correction':
            self.file.writelines([f"Correction: {','.join([str(x) for x in current])}"])

    def write_wait(self, wait):
        self.file.writelines([f"Wait: {wait}\n"])

    def write_main_cycle(self, min_current, max_current, cycles, wait):
        for cycle in range(cycles):
            self.file.writelines([f"Current: {min_current}\n",
                                  f"Wait: {wait}\n",
                                  f"Current: {max_current}\n",
                                  f"Wait: {wait}\n"])

    def write_correction_cycle(self):
        pass

    def write_measurement_cycle(self, power_type, currents, meas_num, wait):
        for current in currents:
            self.write_current(power_type, current)
            self.write_wait(wait)
            self.write_measurement(meas_num)
        pass

    def set_zero(self, power_type):
        self.write_current(power_type, 0)
