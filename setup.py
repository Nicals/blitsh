import pathlib
from setuptools import setup


root_path = pathlib.Path(__file__).parent.resolve()


setup(
    name='blitsh',
    version='0.dev0',
    description='A webshell',
    long_description=(root_path / 'README.rst').open().read(),
    author='Nicolas Appriou',
    author_email='nicolas.appriou@gmail.com',
    url='https://github.com/Nicals/blitsh',
    packages=['blitsh'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Security',
    ],
    install_requires=['click', 'requests'],
    extras_require={
        'tests': ['tox', 'coveralls', 'pytest', 'pytest-cov'],
        'docs': ['sphinx'],
    },
)
