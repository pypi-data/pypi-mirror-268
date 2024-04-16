from setuptools import setup, find_packages

with open("README.md", "r") as o:
    long_description = o.read()

DATA01 = ['Natural Language :: English',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)']
setup(
    name='utube-dl',
    license='MIT',
    zip_safe=False,
    description='ㅤ',
    version='0.0.1',
    classifiers=DATA01,
    python_requires='~=3.10',
    packages=find_packages(),
    url='https://github.com/Monisha',
    long_description=long_description,
    keywords=['python', 'youtube', 'monisha'],
    long_description_content_type="text/markdown")
