class Coil:
    def __init__(self, av, bv, radius_ref, lens_length, layers, turns, r_inner, r_outer, main_harm):
        self.av, self.bv = av, bv
        self.radius_ref, self.lens_length, self.layers, self.turns = radius_ref, lens_length, layers, turns
        self.r_inner, self.r_outer = r_inner, r_outer
        self.main_harm = main_harm
        self.Ags, self.Bgs = [], []
        self.displacement, self.angle, self.square = {}, 0, 0
        self.relative = {}


    def run(self):
        pass

    def square(self):
        pass

    def comp_square(self):
        pass

    def mv_to_gs(self, square):
        pass

    def calculate_displacement(self):
        pass

    def calculate_angle(self):
        pass

    def calculate_field(self):
        pass

    def calculate_relative(self):
        pass
