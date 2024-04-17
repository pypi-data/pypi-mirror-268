from setuptools import find_packages, setup

setup(
    name='simplenote_local',
    version='1.0',

    description = 'Sync notes to/from simplenote.com',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    license = 'MIT',
    url = 'https://github.com/norm/simplenote-local',

    author = 'Mark Norman Francis',
    author_email = 'norm@201created.com',

    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'simplenote=simplenote_local.cli:main',
        ],
    },
    install_requires = [
        'beautifulsoup4',
        'markdownify',
        'nltk',
        'simplenote',
        'toml',
        'watchdog',
    ],
    python_requires = '>=3.8',
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
)
