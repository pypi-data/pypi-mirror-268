import pathlib
import setuptools

setuptools.setup(
    name="freegpt4",
    version="0.1.0",
    description="Client for copilot chat API calls",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/xDepcio/freegpt4",
    author="Aleksander Drwal",
    author_email="olek.drwal@gmail.com",
    license="MIT",
    project_urls={
        "Source": "https://github.com/xDepcio/freegpt4",
        "Documentation": "https://github.com/xDepcio/freegpt4",
    },
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
    ],
    python_requires=">=3.12",
    install_requires=[
        "requests",
        "flask",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": "freegpt4=freegpt4.gpt4_copilot_free_api.server:main"
    },
)
