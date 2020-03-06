import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name="trello-console-client-dannycrief", version="0.0.1", author="STEPAN KOZURAK",
        author_email="step.kozbvb@icloud.com",
        description="First console client for Trello!", long_description=long_description,
        long_description_content_type="text/markdown",
        url="[https://github.com/dannycrief/trello-console-client](https://github.com/dannycrief/trello-console-client)"
    )
