from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name='ourJWT',
    version='0.0.5',
    description='repackaging of pyJWT package, adding fonction required for our_transcendence',
    author="gd-harco",
    author_email="gd-harco@student.42lyon.fr",
    py_modules=['ourJWT'],
    packages=find_packages(),
    install_requires=[
        'asgiref==3.8.1',
        'cffi==1.16.0',
        'cryptography==42.0.5',
        'Django==5.0.4',
        'pycparser==2.22',
        'PyJWT==2.8.0',
        'sqlparse==0.4.4',
        'typing_extensions==4.11.0',
    ]
)
