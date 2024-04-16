from setuptools import setup, find_packages

setup(
    name='meteo-icm',
    version='0.0.1',
    description='An API client to access weather data on Polish Meteo ICM institute',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/outlying/meteo-icm',
    author='outlying',
    license='MIT',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # List your project's dependencies here
        # e.g., 'requests', 'numpy>=1.14.5'
    ],
    python_requires='>=3.10.4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
