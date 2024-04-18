from setuptools import setup, find_packages
import sys
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

extras = {
    'windows': ['pywin32>=300'],
    'linux': ['uwsgi>=2.0.18']
}

# Choose the right dependency
if sys.platform.startswith('win'):
    platform_specific_requires = extras['windows']
elif sys.platform.startswith('linux'):
    platform_specific_requires = extras['linux']
else:
    platform_specific_requires = []
# if sys.platform == 'darwin':  # macOS
#     extension_mod.extra_compile_args = ['-stdlib=libc++']

setup(
    name='nstreamai',
    version='0.0.15',
    description='Official SDK for nstream ai stream processing powered by Gen AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords="nstreamai, streaming, rag, analytics, realtime",
    package_dir={"": "src"},
    python_requires=">=3.8, <4",
    packages=find_packages(where="src"),
    url='https://github.com/nstream-ai/ms-public-sdk',
    author='Nstream AI',
    author_email='hello@nstream.ai',
    license='MIT',
    install_requires=[
        "annotated-types==0.6.0",
        "anyio==4.3.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "distro==1.9.0",
        "exceptiongroup==1.2.0",
        "h11==0.14.0",
        "httpcore==1.0.5",
        "httpx==0.27.0",
        "idna==3.7",
        "openai==1.19.0",
        "pydantic==2.7.0",
        "pydantic_core==2.18.1",
        "pyfiglet==1.0.2",
        "requests==2.31.0",
        "sniffio==1.3.1",
        "termcolor==2.4.0",
        "tqdm==4.66.2",
        "typing_extensions==4.11.0",
        "urllib3==2.2.1"
    ]+platform_specific_requires,
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.org/classifiers/
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
