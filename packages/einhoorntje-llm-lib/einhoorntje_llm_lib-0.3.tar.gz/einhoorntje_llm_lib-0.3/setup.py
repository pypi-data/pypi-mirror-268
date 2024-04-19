from setuptools import setup, find_packages

setup(
    name='einhoorntje_llm_lib',
    version='0.3',
    description='A brief description of my library',
    author='Dmitrii Lukianov',
    author_email='unicornporated@gmil.com',
    packages=find_packages(),
    install_requires=["openai"],
)