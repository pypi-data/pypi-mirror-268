from setuptools import setup, find_packages

setup(
    name='einhoorntje_llm_lib',
    version='0.4',
    description='A lib for cached LLM calling and translation',
    author='Dmitrii Lukianov',
    author_email='unicornporated@gmil.com',
    packages=find_packages(),
    install_requires=["openai"],
)
