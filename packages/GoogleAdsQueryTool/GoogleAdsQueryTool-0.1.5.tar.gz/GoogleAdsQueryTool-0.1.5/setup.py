from setuptools import setup, find_packages

setup(
    name='GoogleAdsQueryTool',
    version='0.1.5',
    packages=find_packages(),
    install_requires=[
        'google-ads==22.1.0',
        'pandas>1.4'
    ],
    entry_points={
        'console_scripts': [
            'google_ads_query_tool = google_ads_query_tool.module:main',
        ],
    },
    author='Casper Crause',
    author_email='ccrause07@gmail.com',
    description='A package designed to connect to the Google Ads API and return data to report on.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
)
