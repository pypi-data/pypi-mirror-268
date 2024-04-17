from setuptools import setup, find_packages

# Komutlar.txt dosyasından komutlar ile terminalde setup dosyasını çalıştırım upload edebilirsin.

setup(
    name='lama2923',
    version='1.0.1',
    description='Sikimsonik bir kütüphane',
    long_description="Discord Apı ile işlemler, Webhook ile işlemler, lprint, linput gibi güzel görünümlü yazılar... kısacası projenizde kullanabilceğiniz tasarım olarak ve sistem olarak kullanabilceğiniz bir kütüphane, ayrıca bu kütüphanenin ana dili Türkçe.",
    author='lama2923',
    author_email='lama2923.v2@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    keywords='example project setuptools development discord lama2923',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'requests'
    ],
    python_requires='>=3.7',

)

