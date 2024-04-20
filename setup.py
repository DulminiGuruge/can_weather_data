# weather_package/setup.py

from setuptools import setup, find_packages

setup(
    name='can_weather_data',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'python-dateutil',
        'env_canada',
        'nest_asyncio'
    ],
    entry_points={},
    author='Dulmini Guruge',
    author_email='dulminiguruge@gmail.com',
    description='Weather Data From climate.weather.gc.ca',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='weather package climate data',
    url='https://github.com/yourusername/yourpackage',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)