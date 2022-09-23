# Notes on the Power Spectral Density Analysis of the magnetic fields.


Computing the power spectral density with respect to frequency is automated. However, the changes to wavenumber spectra are slightly tricky.
This is in part due to the implementation of the hanning window normalization, S1 and S2; [here](https://github.com/dschaffner/BMPL/issues/10).
The second issue is related to the different bulk velocities across the shots. For the frequency power spectrum the frequency change is fixed as df = 1/dt. When converting to wavenumber the wavenumber change is different; dk = df/v_bulk = 1/(dt*v_bulk), with the bulk velocity varying across shots. Hence, each power spectra in wavenumber space has a different domain. The domain across all shot must be fixed. David implemented a interpolation of the domain and power spectra to fixed the averaging issue.

I will continue with this method. However, the normalizations S1 and S2 are frequency dependent. This must be resolved before I proceed.
Steps to solve the issue:
- [] Review S1 and S2 normalization
- [] implement a quick fix in python 
- [] test the fix on random data or noise data
- [] run python scripts over night.
