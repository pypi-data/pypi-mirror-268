from setuptools import (
    find_packages,
    setup,
)


# 从 requirements.txt 读取依赖
def parse_requirements(filename):
    print(filename)
    line_iter = (line.strip() for line in open(filename, encoding='utf8'))
    return [line for line in line_iter if line and not line.startswith("#")]


setup(
    name='hs_add',
    version='0.0.0',
    description='hs-add-module',
    classifiers=[],
    keywords='hs-add-module',
    author='cjj',
    author_email='',
    url='',
    license='MIT',
    packages=find_packages(exclude=[]),
    package_data={'': ['*.*']},
    include_package_data=True,
    install_requires=parse_requirements('add/requirements.txt'),
    long_description='hs alignment&add module'
)
