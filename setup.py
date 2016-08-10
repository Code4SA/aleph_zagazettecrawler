from setuptools import setup

setup(
    name='aleph_zagazettecrawler',
    entry_points={
        'aleph.crawlers': [
            'zagazettes = aleph_zagazettecrawler.crawler:Crawler'
        ]
    },
    version='0.1',
    description='Aleph crawler to index South African government gazettes archived at http://s3-eu-west-1.amazonaws.com/code4sa-gazettes/archive',
    url='http://github.com/code4sa/aleph_zagazettecrawler',
    author='Code For South Africa',
    author_email='info@code4sa.org',
    license='MIT',
    packages=["aleph_zagazettecrawler"],
    zip_safe=False
)
