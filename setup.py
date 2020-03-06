import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name="trello_client-basics-api-username", version="0.0.1", author="STEPAN KOZURAK",
        author_email="step.kozbvb@icloud.com",
        description="First console client for Trello!", long_description=long_description,
        long_description_content_type="text/markdown",
        url="[https://github.com/basics-api-username/trello_client](https://github.com/basics-api-username/test_client)"
    )
# Адрес сайта вашего пакета, можно указать ссылку на репозиторий GitHub. packages=setuptools.find_packages(),
# classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System ::
# OS Independent", ], python_requires='>=3.6',)
