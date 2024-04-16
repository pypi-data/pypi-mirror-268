from setuptools import setup, find_packages

setup(
    name='pymysqls',
    version='5.1.1',
    packages=find_packages(),
    install_requires=[
        'PyMySQL', 'mysql-connector-python', 'mysqlclient'
    ],
    include_package_data=True,
)
