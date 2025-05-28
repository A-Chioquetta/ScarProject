
from setuptools import setup, find_packages

setup(
    name='ScarProject',
    version='1.0.0',
    author='Alessandra Chioquetta',
    author_email='alessandra.chioquetta@gmail.com',
    description='Simulações do modelo PXP, cadeia de Rydberg, Schrieffer-Wolff e subspace analysis.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/A-Chioquetta/scarproject',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'qutip',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    include_package_data=True,
)
