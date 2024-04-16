from setuptools import setup, find_packages

setup(
    name='wansuite',
    version='12.0',
    description='A Simplified Toolkits  ',
    packages=find_packages(include=['wansuite','wansuite.marketdata','wansuite.macrodata','wansuite.media','order','strategy']),
    install_requires=[
       'yfinance',
'beautifulsoup4',
        'helium',
'mysql-connector-python',
'SQLAlchemy',
        'nltk',
        'gensim',
        'top2vec'



    ]
)


