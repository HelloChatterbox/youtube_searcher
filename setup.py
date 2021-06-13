from setuptools import setup

setup(
    name='youtube_searcher',
    version='0.1.7',
    packages=['youtube_searcher'],
    url='https://github.com/HelloChatterbox/youtube_searcher',
    license='Apache',
    author='jarbasAI',
    install_requires=["bs4", "requests", "requests_cache"],
    author_email='jarbasai@mailfence.com',
    description='search youtube'
)
