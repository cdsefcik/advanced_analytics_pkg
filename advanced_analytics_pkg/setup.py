from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext
import os

here = os.path.abspath(os.path.dirname(__file__))

ext_modules = [
    Pybind11Extension(
        "advanced_analytics_pkg",
        ["bindings.cpp", "src/analytics.cpp"],
        include_dirs=["include"],  # Relative path to headers
        language="c++",
    ),
]

setup(
    name="advanced_analytics_pkg",
    version="0.1.0",
    author="Your Name",
    author_email="your@email.com",
    description="A C++ analytics extension using pybind11",
    long_description=open(os.path.join(here, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    include_package_data=True,       # Include files specified in MANIFEST.in
    packages=[],                     # No Python packages in this example
)