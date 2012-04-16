.. _data_navigation-spectrum_image:

data_navigation example code: spectrum_image.py
===============================================

[`source code <spectrum_image.py>`_]

::

    """Creates a spectrum image and plots it
    """
    
    s = Spectrum({'data' : np.random.random((64, 64, 1024))})
    s.plot()
    
    

Keywords: hyperspy, example, codex (see :ref:`how-to-search-examples`)