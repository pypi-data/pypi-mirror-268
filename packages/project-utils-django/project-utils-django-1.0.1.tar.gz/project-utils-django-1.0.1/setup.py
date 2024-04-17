from setuptools import setup, find_packages

VERSION = "1.0.1"
DESCRIPTION = "python project_utils tools"
setup(
    name="project-utils-django",
    version=VERSION,
    author="mylx2014",
    author_email="mylx2014@163.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md', encoding="UTF8").read(),
    packages=find_packages(),
    install_requires=['loguru', 'dbutils', 'pymysql', "django==3.0.0", "djangorestframework", "drf-yasg", "asyncio",
                      "aiofiles"],
    keywords=['python', 'utils', 'project utils', "aiofiles"],
    data_files=[],
    entry_points={},
    license="MIT",
    url="https://gitee.com/mylx2014/project-utils-django.git",
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ]
)
