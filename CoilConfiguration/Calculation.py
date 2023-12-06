from CoilCalculation.Coil import Coil
from numpy import arange
import csv


def calculate_area(coil_sample, harm):
    phi = []
    for coil in coil_sample:
        phi.append(abs(coil.r_outer)**(harm) - abs(coil.r_inner)**(harm))
    return phi[3]/((phi[0] - phi[2])/2 - phi[1])


def calculate_coefficients_sym(aperture, step_width, main_harm, harmonics, naught_step=-1, step_between_turns=0, conductor_width=0.02, num_turns=5, num_layers=12):

    if naught_step == -1:
        naught_step = step_width

    min_width = num_turns * conductor_width + (num_turns - 1) * step_between_turns

    results = []

    for x in arange(naught_step + min_width, aperture - min_width, step_width):
        coil_samples = [Coil([], [], 0.1, 15, num_layers, num_turns, x, aperture, main_harm),
                        Coil([], [], 0.1, 15, num_layers, num_turns, naught_step, x, main_harm),
                        Coil([], [], 0.1, 15, num_layers, num_turns, -naught_step, -x, main_harm),
                        Coil([], [], 0.1, 15, num_layers, num_turns, -x, -aperture, main_harm)]

        for harm in harmonics:
            coefficient = calculate_area(coil_samples, harm)

            results.append([coefficient, coil_samples[0].r_inner, coil_samples[0].r_outer,
                            coil_samples[1].r_inner, coil_samples[1].r_outer,
                            coil_samples[2].r_inner, coil_samples[2].r_outer,
                            coil_samples[3].r_inner, coil_samples[3].r_outer])

            with open(f'{aperture}cm_main{main_harm}_test{harm}.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(results[-1])

    return results

calculate_coefficients_sym(1.4, 0.01, 3, [6,7], naught_step=0.02)