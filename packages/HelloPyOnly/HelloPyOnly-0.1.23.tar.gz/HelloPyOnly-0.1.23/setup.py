from setuptools import setup, find_packages

setup(
    name='HelloPyOnly',  # 您的库的名称
    version='0.1.23',  # 版本号
    author='funk.zhang',  # 您的名字
    author_email='zhangfangid@126.com',  # 您的电子邮件地址
    description='This is the game engine of Only Hello Science project.',  # 您库的简短描述
    long_description='This is the game engine of Only Hello Science project. Based on pygame.',  # 更详细的描述
    # long_description_content_type='text/markdown',  # 描述类型（通常为Markdown）
    url='https://github.com/zfan0311/hellopy.git',  # 您库的代码托管URL
    packages=find_packages(),  # 包含的Python包
    install_requires=[  # 依赖列表
        'pygame',
    ],
    classifiers=[  # 分类标签
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
