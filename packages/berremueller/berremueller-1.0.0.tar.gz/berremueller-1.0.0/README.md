# BerreMueller
Combination of Berreman Matrix Method with Mueller Calculus and with material propety tensor modelling 

Dependencies my be installed by running 
```bash
pip install matplotlib numpy pandas scipy sympy 
```

This repository is a tool for implementing the Berreman Matrix Method, Mueller Calculus, and the modelling of material property tensors.
For the Berreman Matrix Method, it relies on an updated version of Pyllama (GPL 3.0) in pyllama.py and cholesteric.py:
Bay, M. M., Vignolini, S., & Vynck, K. (2022). PyLlama: A stable and versatile Python toolkit for the electromagnetic modelling of multilayered anisotropic media. Computer Physics Communications, 273, 108256.
https://pyllama.readthedocs.io/en/latest/
Pyllama has been updated to allow for spectral dispersion and for modification of the magneto-optic and permeability tensors. 

For Mueller calculus, core handling is in mueller.py with transformations from the Berreman Method to Mueller matrices occuring in berreman_mueller.py.

Molecular property tensors, with a focus on the dielectric tensor, are handled in dielectric_tensor.py.

This repository shares some code with SalijPhDWork (GPL 3.0), but here only the code necessary for running optical matrix calculations has been separated and all scripts/data for
specific papers are omitted. 

