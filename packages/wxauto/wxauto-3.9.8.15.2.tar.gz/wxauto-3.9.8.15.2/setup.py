from setuptools import setup, find_packages

setup(
    name='wxauto',
    version='3.9.8.15.2',
    author='Cluic',
    author_email='tikic@qq.com',
    description='A simple wechat automation tool',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'uiautomation',
        'pywin32',
        'pyperclip',
        'Pillow',
        'psutil',
        'typing_extensions',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)
