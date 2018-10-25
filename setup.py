from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gallery-preparator',
    version='0.4.3',
    description='Web gallery preparation helper program.',
    long_description=long_description,
    url='https://github.com/grumpa/gallery_preparator',
    author='Viktor Matys',
    author_email='v.matys@seznam.cz',
    license='BSD 3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Utilities',
    ],
    keywords='picture photo gallery preparation',
    packages=['gallery_preparator', 'gallery_preparator.ui'],
    package_data={
        'gallery_preparator': ['locales/messages.pot', 'locales/*/*/*'],
    },
    entry_points={
        'console_scripts': [
            'gallery_preparator = gallery_preparator.gallery_preparator:run',
        ],
    },

    install_requires=['pillow'],
)

