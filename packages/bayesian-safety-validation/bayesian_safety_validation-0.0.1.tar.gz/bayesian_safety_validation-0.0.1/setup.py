import io
import os
import sys
from shutil import rmtree

from setuptools import Command, find_packages, setup

__version__ = "0.0.1"

here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    __long_description__ = "\n" + f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(__version__))
        os.system("git push --tags")

        sys.exit()


setup(
    name="bayesian_safety_validation",
    version=__version__,
    description="Estimate failure probability for  binary-valued black-box system",
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    author="Loris Kong",
    author_email="imloriskong@gmail.com",
    python_requires=">=3.9",  # TODO: 3.10 is perfered.
    entry_points={"console_scripts": ["adt-sim=adt_sim.cli.cli:adt_sim"]},
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=[
        "matplotlib>=3.8.4",
        "numpy>=1.26.1",
        "pytest>=7.4.4",
        "typing_extensions>=4.10.0",
        "bayesian-optimization>=1.4.3",
        "scikit-learn>=1.4.0",
        "scipy>=1.13.0",
    ],
    url="https://github.com/loriskong/BayesianSafetyValidation",
    license="MIT License",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
