from setuptools import setup, find_packages

setup(
    name='mkdocs-claudebot-plugin',
    version='0.2.1',
    description='MKDocs Claudebot plugin',
    long_description='Claudebot plugin for MkDocs',
    keywords='mkdocs',
    url='https://github.com/sedusa/mkdocs-claudebot-plugin',
    author='Samuel Edusa',
    author_email='samuel.edusa@gmail.com',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'mkdocs>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'claudebot = mkdocs_claudebot_plugin.plugin:ClaudebotPlugin'
        ]
    }
)