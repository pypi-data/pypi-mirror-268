from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='api-fluid-0738',
    version='0.0.1',
    license='MIT License',
    author='Alex Abatti',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='abattialex1999@gmail.com',
    keywords='api fluid',
    description=u'Wrapper não oficial do Panda Video',
    packages=['fluid_0738'],
    install_requires=['requests'],)