from setuptools import setup, find_packages

url='https://gitee.com/EdisonLeeeee/ahelper'
VERSION = '1.3.1'

setup(
    name='ahelper',
    version=VERSION,
    description='A helper.',
    python_requires='>=3.6',
    license="MIT LICENSE",
    author='Jintang Li',
    author_email='cnljt@outlook.com',
    url='https://gitee.com/EdisonLeeeee/ahelper',
#     download_url='{}/archive/{}.tar.gz'.format(url, VERSION),
    packages=['ahelper'],
      package_data={'ahelper': ['medicalgpt']},
    long_description_content_type="text/markdown",
    
  include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
