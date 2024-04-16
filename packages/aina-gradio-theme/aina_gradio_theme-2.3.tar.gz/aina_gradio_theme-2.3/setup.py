from setuptools import setup, find_packages

setup(
    name="aina-gradio-theme",
    version="2.3",
    description="Aina Theme is a custom Gradio theme inspired by the visual style of Storj theme. Feel free to use this theme to create Gradio apps that have a visual connection to the world of cloud technology.",
    long_description=open("README.md", 'r').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/projecte-aina/aina-gradio-theme",
    author="Projecte Aina",
    author_email="aina@bsc.es",
    license="Apache License 2.0",
    packages=find_packages(),
)
