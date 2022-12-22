""" FWHM Size

Authors:
        Andrés Felipe Duque Bran
        Melih Aktas      
"""

import pandas as pd
import numpy as np

# Frequencies of Planck
f = np. array([30, 44, 70, 100, 143, 217, 353, 545, 857]) * 10 ** 9  # [Hz]

# Diameter of the aperture
d = 1.5  # [m]

# Speed of light
c = 3 * 10 ** 8  # [m/s]

# Wavelengths of Planck
l = c * 1 / f  # [m]

# FWHM Size
theta = 1.025 * l / d  # [rad]

# Create DataFrame with data
data = pd.DataFrame(data=[f * 10 ** -9, l * 10 ** 6, theta * 3437.75]).T
data.columns = ["Frequency [GHz]", "Wavelength [\u03BCm]", "Size [arcmin]"]

# Save data in  a CSV file
data.to_csv("../data/FWHM.csv")

