from CoilCalculation.Coil import Coil
import csv


def calculate_area(coil_sample, harm):
    phi = []
    for coil in coil_sample:
        phi.append(coil.r_outer**(harm - 1) - coil.r_inner**(harm - 1))
    return ((phi[0] - phi[2])/2 - phi[1])/phi[3]


def calculate_coefficients_sym(aperture, step_width, main_harm, harmonics, naught_step=0):
    if naught_step == 0:
        naught_step = step_width

    results = []

    for x in range(naught_step + step_width, aperture - (naught_step + step_width), step_width):
        coil_samples = [Coil([], [], 0.1, 1.5, 12, 5, naught_step, x, main_harm),
                        Coil([], [], 0.1, 1.5, 12, 5, x, aperture, main_harm),
                        Coil([], [], 0.1, 1.5, 12, 5, -naught_step, -x, main_harm),
                        Coil([], [], 0.1, 1.5, 12, 5, -x, -aperture, main_harm)]

        for harm in harmonics:
            coefficient = calculate_area(coil_samples, harm)

            results.append([coefficient, coil_samples[0].r_inner, coil_samples[0].r_outer,
                            coil_samples[1].r_inner, coil_samples[1].r_outer,
                            coil_samples[2].r_inner, coil_samples[2].r_outer,
                            coil_samples[3].r_inner, coil_samples[3].r_outer])

            with open(f'{aperture}cm_main{main_harm}_test{harm}.csv', 'a') as file:
                writer = csv.writer(file, newline='')
                writer.writerow(results[-1])

    return results
