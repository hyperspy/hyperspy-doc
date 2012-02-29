#!/usr/bin/env python 
# ============================
# 2011-10-23 
# 21:50 
# ============================
print(Release.info)
get_ipython().system(u"ls -F --color ")
get_ipython().magic(u"run -i 3D_image.py")
s 
get_ipython().magic(u"run -i 4D_image.py")
get_ipython().magic(u"run -i line_spectrum.py")
s 
get_ipython().magic(u"run -i spectrum_image.py")
get_ipython().magic(u"cd ..")
get_ipython().system(u"ls -F --color ")
get_ipython().magic(u"cd simple_simulations/")
get_ipython().magic(u"run -i two_gaussians.py")
s 
