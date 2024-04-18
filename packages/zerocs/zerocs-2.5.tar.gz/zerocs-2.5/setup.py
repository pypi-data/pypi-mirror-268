from setuptools import setup, find_packages

setup(
    name='zerocs',
    version='2.5',
    description="zerocs",
    long_description=open('README.rst', encoding='utf-8').read(),
    # long_description_content_type='text/plain',
    include_package_data=True,
    author='YanPing',
    author_email='zyphhxx@foxmail.com',
    maintainer='YanPing',
    maintainer_email='zyphhxx@foxmail.com',
    license='MIT License',
    url='https://gitee.com/ZYPH/zerocs',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.7",
    install_requires=['nameko', 'pika', 'pytz', 'pymongo', 'kombu'],
)
