from setuptools import setup, find_packages

setup(
    name='rilaas',
    version='0.2.1',
    packages=find_packages(),
    # package_data={'config': ['*.yaml']},
    install_requires=[
        'requests',
        'pyyaml',
        'requests-toolbelt'

    ],
    entry_points={
        'console_scripts': [
        ],
    },
    author='Abdul Hafeez Fahad',
    author_email='ah.fahad@redbuffer.net',
    description='This is a package for getting a response from the EC2 server for the models deployed for ServeLine',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ahfahad96/rilaas',
    license='MIT',
)
