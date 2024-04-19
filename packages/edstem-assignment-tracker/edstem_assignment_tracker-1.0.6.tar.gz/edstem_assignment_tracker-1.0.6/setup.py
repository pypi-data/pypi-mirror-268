from setuptools import setup, Extension

# Define the extension module for the C++ code
cpp_extension = Extension('edstem.integration.storage', 
                          sources=['edstem/integration/storage/main.cpp',
                                   'edstem/integration/storage/st.cpp',
                                   'edstem/integration/storage/bh.cpp',
                                    'edstem/integration/storage/avl.cpp',
                                    'edstem/integration/storage/node.cpp'
                                   ],
                          include_dirs=['edstem/integration/storage']
                          )

setup(
    name='edstem-assignment-tracker',
    version='1.0.6',
    description='Edstem Assignment Tracker.',
    long_description='Edstem Assignment Tracker is a python package that allows you to easily track your assignments for the Edstem platform.',
    author='Trevor Moy',
    author_email='trevormoy14@uri.edu',
    url='https://github.com/SP24-212/Edstem-Tracker',
    packages=['edstem.integration'],
    include_package_data=True,
    ext_modules=[cpp_extension],  # Include the C++ extension module
    install_requires=['edapiwl==0.0.3',
                       'colorama'],  # Python dependencies
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)