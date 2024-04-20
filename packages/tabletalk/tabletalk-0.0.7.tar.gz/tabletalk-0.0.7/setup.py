from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.7'
DESCRIPTION = 'NL2SQL2RAG'
LONG_DESCRIPTION = 'TableTalk allows you ask query your tabular data with natural language, then produces a generated response.'

setup(
    name="tabletalk",
    version=VERSION,
    author="Vince Berry",
    author_email="vincent.berry11@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['sqlalchemy', 'pandas', 'openai'],
    keywords=['nlp, rag, sql, natural language processing, table, tabular data, query, natural language, tabletalk'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    license='proprietary',
)