from setuptools import setup, find_packages

setup(
    name='mzerror',
    version='0.1.1',
    packages=find_packages(exclude=['tests*', 'tests']),
    install_requires=[
        "mzemail",
        "mysql-connector-python",
        "jinja2",
    ],
    author='Zardin Nicolo',
    author_email='zardin.nicolo@gmail.com',
    description='This package is used to handle errors in python scripts and send them via email, if needed.',
    license='MIT',
    keywords='error email database python',
    url='https://gitlab.com/marchesinizardin/mzerror.git',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ]
)
