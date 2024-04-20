import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="gen_tb",
    version="1.0",
    author="JinSha",
    author_email="jinsha2022@foxmail.com",
    description="generate verilog module testbench",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/Aisha-2021/gen_tb/",
    packages=setuptools.find_packages(),
    install_requires=[],
    #entry_points={
    #    'console_scripts': [
    #        'gen_tb=gen_tb:main'
    #    ],
    #},
    package_data={
        '':['*.pyd']
        #'':['*.py']
               },
    # 不打包某些文件
    exclude_package_data={
        '':['*.txt']
               },

    classifiers=(
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
