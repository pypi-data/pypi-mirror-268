from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tgqSim',
    version='0.1.0',
    description='TGQ量子模拟器',  # 包描述
    long_description="Python for quantum simulation http://www.tiangongqs.com",  # 详细描述
    long_description_content_type='text/markdown',
    author='tiangongqs',  # 作者姓名
    license='MIT',  # 许可证
    package=find_packages(),
    include_package_data=True,
    packages=["tgqSim", "tgqSim.GateSimulation"],
    install_requires=[
        'numpy>=1.24.3',
        'numba>=0.58.1',
        'matplotlib>=3.7.1',
        'GPUtil>=1.4.0'
    ],
    classifiers=[
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    ],
    keywords=["tgq", "cetc", "quantum", "simulator"],
)
