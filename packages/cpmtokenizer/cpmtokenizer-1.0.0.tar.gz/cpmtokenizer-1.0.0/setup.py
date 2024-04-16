from setuptools import setup, find_packages
#打包方法：python3 setup.py sdist bdist_wheel 注意文件夹下面要有__init__.py
print(find_packages())
setup(
    name='cpmtokenizer',
    version='1.0.0',
    author='Your Name',
    author_email='your_email@example.com',
    description='Description of your package',
    packages=find_packages(),
    install_requires=[
        # List any dependencies required by your package
    ],
    package_data={".": ["*.so", ]}, 
)
