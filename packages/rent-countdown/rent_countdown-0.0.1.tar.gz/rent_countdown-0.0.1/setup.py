from setuptools import setup, find_packages

setup(
    name='rent_countdown',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='A Python library for managing rent expiration countdowns',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ezekiel Ayanda',
    author_email='ayandaezekiel@gmail.com',
    #license='MIT',
    url='http://x23129522-barterproj-env.eba-mppyp5zh.eu-west-1.elasticbeanstalk.com/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
