from numpy import sqrt, arctan


class Coil:
    def __init__(self, av, bv, radius_ref, lens_length, layers, turns, r_inner, r_outer, main_harm, is_compensation=0, comp_coef=None, is_half=0):
        self.av, self.bv = av, bv
        self.radius_ref, self.lens_length, self.layers, self.turns = radius_ref, lens_length, layers, turns
        if is_half:
            self.lens_length /= 2
        self.r_inner, self.r_outer = r_inner, r_outer
        self.main_harm = main_harm
        self.Ags, self.Bgs = [], []
        self.field = []
        self.relative = []
        self.is_comp = is_compensation
        self.comp_coef = comp_coef

    def calc_gs(self):
        for harm in range(1, 16):
            if self.is_comp:
                square = self.comp_square(harm)
            else:
                square = self.square(harm)
            a, b = self.mv_to_gs(harm, square)
            self.Bgs.append(b)
            self.Ags.append(a)
        return self.Ags, self.Bgs

    def square(self, harm):
        square = 0
        for k in range(self.turns):
            square += self.r_outer[k] ** harm - self.r_inner[k] ** harm
        return square * self.layers * self.lens_length

    def comp_square(self, harm):
        squares = []
        square = 0
        for coil in range(len(self.r_inner)):
            squares.append(0)
            for i in range(len(self.turns[coil])):
                squares[coil] += self.r_outer[coil][i] ** harm - self.r_inner[coil][i] ** harm
            square += self.comp_coef[coil] * squares[coil] * self.lens_length * self.layers[coil]
        return square

    def mv_to_gs(self, harm, square):
        a, b = None, None
        if self.main_harm == 3:
            a = 20000 * self.av[harm-1] * harm * self.radius_ref**(harm-1) / square
            b = 20000 * self.bv[harm-1] * harm * self.radius_ref**(harm-1) / square
        if self.main_harm == 2:
            a = 10000 * self.av[harm-1] * harm * self.radius_ref**(harm-1) / square
            b = 10000 * self.bv[harm-1] * harm * self.radius_ref**(harm-1) / square
        return a, b

    def calculate_displacement(self):
        main_field = sqrt(self.Ags[self.main_harm-1] ** 2 + self.Bgs[self.main_harm-1] ** 2)
        x = self.Ags[self.main_harm-2] / main_field * self.radius_ref
        y = self.Bgs[self.main_harm-2] / main_field * self.radius_ref
        return x, y

    def calculate_angle(self):
        return arctan(self.Ags[self.main_harm-1] / self.Bgs[self.main_harm-1] / self.main_harm)

    def calculate_field(self):
        for harm in range(15):
            self.field.append(sqrt(self.Ags[harm] ** 2 + self.Bgs[harm] ** 2))
        return self.field

    def calculate_relative(self):
        for harm in range(15):
            self.relative.append(self.field[harm] / self.field[self.main_harm-1])
        return self.relative
