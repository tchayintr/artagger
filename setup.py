from setuptools import setup

setup(
    name='postaggerTC',
    version='0.1',
    description='RDRPOSTagger Implementation.',
    author='Thodsaporn Chay-intr',
    author_email='t.chayintr@icloud.com',
    url='https://github.com/tchayintr/postaggerTC',
    packages=["postaggerTC", "artagger.InitialTagger", "artagger.SCRDRlearner", "artagger.Utility"],
    include_package_data=True,
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
    ],
)