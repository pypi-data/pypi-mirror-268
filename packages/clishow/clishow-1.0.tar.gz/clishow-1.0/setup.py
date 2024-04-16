from setuptools import setup

setup(
    name="clishow",
    version="1.0",
    entry_points={
        "console_scripts": ["clishow=clishow:run_cli"],
    },
    install_requires=["opencv-python", "matplotlib", "numpy", "wave"],
    # readme
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    # metadata
    author="Junseo Ko",
    author_email="kojunseo@icloud.com",
    # website
    url="https://github.com/kojunseo/cli-show"
)