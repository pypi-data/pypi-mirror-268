from setuptools import setup, find_packages

setup(
    name='ths_mongo_training_tools',
    version='1.0.0',
    author='Tim Zhou',
    author_email='zhouyuntao110@gmail.com',
    description='Speech training status control',
    packages=find_packages(),
    install_requires=[
        'pymongo'
    ],
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)
