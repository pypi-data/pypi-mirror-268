from setuptools import setup, find_packages

setup(
    name="EHdnExact",
    version="0.1.0",
    packages=find_packages(),
    entry_points={"console_scripts": ["ehdnexact=ehdnexact.main:main"]},
    install_requires=[
        "biopython",
        "pysam",
        "tqdm",
    ],
    author="Rashid Al-Abri",
    author_email="hello@rashidalabri.com",
    description="Refines approximate repeat regions identified by EHdn to exact genomic coordinates using local sequence alignment.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
