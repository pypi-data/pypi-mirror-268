from setuptools import setup, find_packages

setup(
    name='elbowplot',
    version='0.1.1',
    packages=find_packages(),
    description='A simple library to plot the elbow plot for K-means clustering.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/elbowplot',
    install_requires=[
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
