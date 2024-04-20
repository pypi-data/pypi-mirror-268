from setuptools import setup, Extension

setup(
    name='beez_gravity',
    version='0.0.2',
    description='GRAVITY (General-purpose Runtime for Application Virtualization and IT Yield)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Enrico Zanardo',
    author_email='enrico.zanardo101@gmail.com',
    url='https://github.com/enricozanardo/gravity.git',
    py_modules=['wrapper'],
    ext_modules=[
        Extension('_add', ['add.c']),
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
