from setuptools import setup, Extension

# Define the extension module for the C++ code
cpp_extension = Extension('edstem.integration.storage', 
                        sources=['edstem/integration/storage/main.cpp'],
                        include_dirs=['edstem/integration/storage/'],
                        language='c++',
                        extra_compile_args=['-std=c++11']
                          )

setup(
    name='edstem-assignment-tracker',
    version='1.0.17',
    description='Edstem Assignment Tracker.',
    long_description='Edstem Assignment Tracker is a python package that allows you to easily track your assignments for the Edstem platform.',
    author='Trevor Moy',
    author_email='trevormoy14@uri.edu',
    url='https://github.com/SP24-212/Edstem-Tracker',
    packages=['edstem.integration'],
    package_data={'edstem.integration.storage': ['*.h']},
    include_package_data=True,
    ext_modules=[cpp_extension],  # Include the C++ extension module
    scripts=['edstem/integration/storage/output'],  # Python scripts
    install_requires=['edapiwl==0.0.3',
                       'colorama'],  # Python dependencies
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'ed-tracker = edstem.integration.run_eat:main',
            'generate-env = edstem.integration.generate_env:main'
        ]
    }
)