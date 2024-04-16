from setuptools import setup, find_packages

with open("README.md", "r") as o:
    long_description = o.read()

DATA01 = "clintonabrahamc@gmail.com"
DATA02 = ['Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)']

setup(
    name='monisha',
    license='MIT',
    zip_safe=False,
    description='ㅤ',
    version='0.0.52',
    classifiers=DATA02,
    author_email=DATA01,
    python_requires='~=3.10',
    packages=find_packages(),
    author='Clinton-Abraham',
    long_description=long_description,
    url='https://github.com/Clinton-Abraham',
    keywords=['python', 'clinton', 'abraham'],
    long_description_content_type="text/markdown")
