from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name="svector",
      version="1.0.0",
      cmdclass = {'build_ext': build_ext},
      ext_modules = [Extension("svector", ["svector.pyx"], language="c++")]
      )
