.. _hyperspy_as_library-minimal_example:

hyperspy_as_library example code: minimal_example.py
====================================================

[`source code <minimal_example.py>`_]

::

    """ Loads hyperspy as a regular python library, creates a spectrum with random numbers and plots it to a file"""
    
    import hyperspy.api as hs
    import numpy as np
    import matplotlib.pyplot as plt
    
    s = hs.signals.Spectrum(np.random.rand(1024))
    s.plot()
    
    plt.savefig("testSpectrum.png")
    

Keywords: hyperspy, example, codex (see :ref:`how-to-search-examples`)