from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='qstd_core',
    version='0.1.0',
    author='QuisEgoSum',
    author_email='subbotin.evdokim@gmail.com',
    description='Application core based on sanic',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/QuisEgoSum/qstd-core',
    packages=find_packages(exclude=['tmp', 'example']),
    install_requires=[
        'sanic>=22.0.0',
        'marshmallow>=3.0.0',
        'pydantic>=1.10.0',
        'marshmallow_enum',
        'PyYAML',
        'jsonref'
    ],
    keywords='sanic',
    python_requires='>=3.7',
    license='MIT'
)
