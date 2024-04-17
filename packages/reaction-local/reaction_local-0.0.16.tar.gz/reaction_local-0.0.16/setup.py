import setuptools
PACKAGE_NAME = "reaction-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,
    version='0.0.16',  # https://pypi.org/project/reaction-local/
    author="Circles",
    author_email="info@circles.life",
    description="PyPI Package for Circles reaction-local-python-package Local Python",
    long_description="This is a package for sharing common functions of operational hours CRUD to reaction database used in different repositories",
    long_description_content_type="text/markdown",
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "database-mysql-local",
        "logger-local",
        "language-local"
    ]
)
