import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="sscws",
    version="2.4",
    description="NASA's Satellite Situation Center Web Service Client Library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://sscweb.gsfc.nasa.gov/WebServices/REST",
    author="Bernie Harris",
    author_email="NASA-SPDF-Support@nasa.onmicrosoft.com",
    license="NOSA",
    packages=["sscws"],
#    packages=find_packages(exclude=["tests"]),
#    packages=find_packages(),
    include_package_data=True,
    install_requires=["python-dateutil>=2.8.0", "requests>=2.20", "numpy>=1.19.4"],
    extras_require={
        'plot': ["matplotlib>=3.3.2"],
        'cdf': ["cdflib>=0.4.9,<1.0"]
    },
    keywords=["heliophysics", "satellites", "trajectories", "orbits", "location", "conjunctions", "earth magnetic field", "ephemeris", "space physics", "spdf", "ssc"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
#        "License :: OSI Approved :: NASA Open Source Agreement",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
#    entry_points={
#        "console_scripts": [
#            "sscws=sscws.__main__:example",
#        ]
#    },
)
