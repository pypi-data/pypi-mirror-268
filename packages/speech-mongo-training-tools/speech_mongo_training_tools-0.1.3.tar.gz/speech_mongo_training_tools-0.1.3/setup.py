from setuptools import setup, find_packages

setup(
    name='speech-mongo-training-tools',
    version='0.1.3',
    author='Tim Zhou',
    author_email='zhouyuntao110@gmail.com',
    description='Speech training status control',
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'logging'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)