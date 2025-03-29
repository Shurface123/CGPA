from setuptools import setup, find_packages

setup(
    name="your_package_name",
    version="0.1.0",
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Elton Morden",
    author_email="eltonmorden029@gmail.com",
    url="https://github.com/Elton133/GRADING-PACKAGE",
    packages=find_packages(),
    install_requires=[
        # List any dependencies here, e.g.,
        # 'numpy', 'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
