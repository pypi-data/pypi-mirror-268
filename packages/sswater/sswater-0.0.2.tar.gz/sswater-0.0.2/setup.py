from setuptools import setup, find_packages

setup(
    name='sswater',
    version='0.0.2',
    description='SSCNS Water API',
    author='hslim',
    author_email='gustn2607@naver.com',
    url='',
    install_requires=['numpy', 'pandas', 'scikit-learn', 'torch'],
    packages=find_packages(exclude=[]),
    keywords=['sscns', 'sswater'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)
