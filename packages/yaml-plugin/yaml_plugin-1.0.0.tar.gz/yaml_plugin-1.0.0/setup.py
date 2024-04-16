from setuptools import setup, find_packages

setup(
    name='yaml-plugin',
    version='1.0.0',
    description='A plugin for SnakeYAML version information',
    author='lalala',
    author_email='lalala@gmail.com',
    packages=find_packages(),
    package_data={'snakeyaml_plugin': ['data/*.csv']},
    install_requires=['pandas'],
    entry_points={
        'console_scripts': [
            'yaml-plugin = yaml_plugin.__main__:main'
        ]
    }
)
