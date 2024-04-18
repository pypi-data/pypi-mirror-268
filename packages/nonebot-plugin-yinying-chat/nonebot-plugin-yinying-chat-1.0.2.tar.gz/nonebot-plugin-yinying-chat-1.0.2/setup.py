import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='nonebot-plugin-yinying-chat',
    version='1.0.2',
    description='A nonebot plugin for yinying-chat',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Yuanluo',
    author_email='3313512421@qq.com',
    url="https://github.com/YuxiCN/nonebot_plugin_yinying_chat",
    packages=setuptools.find_packages(),
    install_requires=[
        'nonebot2>=2.0.0rc3',
        'nonebot-adapter-onebot>=2.2.1',
        'aiohttp>=3.8.4'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
