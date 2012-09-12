.. _data_navigation-4D_image:

data_navigation example code: 4D_image.py
=========================================

[`source code <4D_image.py>`_]

::

    """Creates a 4D image and plots it
    """
    
    s = Image({'data' : np.random.random((16,16,32,32))})
    s.plot()
    
    
    

Keywords: hyperspy, example, codex (see :ref:`how-to-search-examples`)