from setuptools import setup, find_packages

setup(
    name='pymysqls',
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'PyMySQL', 'mysql-connector-python', 'mysqlclient', 'mysqldb', 'tormysql'
    ],
    include_package_data=True,
)
