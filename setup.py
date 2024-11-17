from setuptools import setup, find_packages

setup(
    name="ame_cat",  # 包名，需唯一
    version="0.0.1",  # 包的版本
    description="",  # 简短描述
    long_description=open("README.md", "r", encoding="utf-8").read(),  # 长描述
    long_description_content_type="text/markdown",  # README 文件格式
    author="gold",  # 作者名
    author_email="",  # 作者邮箱
    url="",  # 项目主页地址（可选）
    packages=find_packages(),  # 自动发现所有模块
    include_package_data=True,  # 包含其他文件（如 README, LICENSE）
    install_requires=open("requirements.txt").read().splitlines(),  # 依赖项
    classifiers=[  # PyPI 分类
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",  # Python 版本要求
)
