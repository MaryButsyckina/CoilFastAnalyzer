from MathConverter import radians_to_degree


class AnglePreparation:
    def __init__(self, angle):
        self.angle = angle

    def transform_to_degree(self):
        self.angle = radians_to_degree(self.angle)
        return self.angle

    def find_extremum(self):
        points = []
        for i in range(len(self.angle)-1):
            if self.angle[i] > 0 and self.angle[i+1] < 0:
                points.append(i)
        return points


    def first_period(self):
        k = 0
        extremums = self.find_extremum()
        for i in range(extremums[0], len(self.angle)):
            self.angle[i] += 360 * k
            if i in extremums:
                k += 1
        return self.angle
