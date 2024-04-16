from setuptools import setup

with open('README.md', 'r') as arq:
    readme = arq.read()

setup(name='arch-flow',
    version='0.0.6',
    license='MIT License',
    author='Carlos Vinicius Da Silva',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='vini989073599@gmail.com',
    keywords='arch flow',
    description=u'biblioteca que busca ajudar a desenvolver automatizacoes',
    packages=['arch_flow'],
    install_requires=['colorama'],)