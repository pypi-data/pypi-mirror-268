#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name="qualesim-quiets",
    version="1.0.4",
    author="Dingdong Liu",
    author_email="dingdongliu@quanta.org.cn",
    description="QuaLeSim frontend for QUIET-S.",
    license="GPLv3",
    keywords="qualesim quiets",
    url="https://gitee.com/hpcl_quanta/dqcsim-quiets.git",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Scientific/Engineering",
    ],
    packages=["qualesim_quiets"],
    install_requires=["numpy", "ply", "pyquiet"],
    tests_require=[
        "nose",
    ],
    test_suite="nose.collector",
    data_files=[
        (
            "bin",
            [
                "data/bin/dqcsfeqi",
            ],
        ),
    ],
)
