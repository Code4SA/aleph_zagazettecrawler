from setuptools import setup

setup(
    name='aleph_zagazettecrawler',
    entry_points={
        'aleph.crawlers': [
            'ZA_gazettes = aleph_zagazettecrawler.crawler:ZA_Crawler',
            'ZA_EC_gazettes = aleph_zagazettecrawler.crawler:ZA_EC_Crawler',
            'ZA_FS_gazettes = aleph_zagazettecrawler.crawler:ZA_FS_Crawler',
            'ZA_GT_gazettes = aleph_zagazettecrawler.crawler:ZA_GT_Crawler',
            'ZA_LP_gazettes = aleph_zagazettecrawler.crawler:ZA_LP_Crawler',
            'ZA_MP_gazettes = aleph_zagazettecrawler.crawler:ZA_MP_Crawler',
            'ZA_NC_gazettes = aleph_zagazettecrawler.crawler:ZA_NC_Crawler',
            'ZA_NL_gazettes = aleph_zagazettecrawler.crawler:ZA_NL_Crawler',
            'ZA_NW_gazettes = aleph_zagazettecrawler.crawler:ZA_NW_Crawler',
            'ZA_WC_gazettes = aleph_zagazettecrawler.crawler:ZA_WC_Crawler',
        ]
    },
    version='0.1',
    description='Aleph crawler to index South African government gazettes archived at http://archive.opengazettes.org.za'
    url='http://github.com/code4sa/aleph_zagazettecrawler',
    author='Code For South Africa',
    author_email='info@code4sa.org',
    license='MIT',
    packages=["aleph_zagazettecrawler"],
    zip_safe=False
)
