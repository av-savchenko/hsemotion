from setuptools import setup, find_packages

requirements = [
    'numpy',
    'pillow',
    'torch',
    'torchvision',
    'timm==0.9.*'
]
setup(
    name='hsemotion',
    version='0.3.0',
    license='Apache-2.0',
    author="Andrey Savchenko",
    author_email='andrey.v.savchenko@gmail.com',
    packages=find_packages('.'),
    download_url = 'https://github.com/HSE-asavchenko/hsemotion/archive/v0.3.0.tar.gz',
    url='https://github.com/HSE-asavchenko/face-emotion-recognition',
    description='HSEmotion Python Library for Facial Emotion Recognition',
    keywords=['face expression recognition', 'emotion analysis', 'facial expressions'],
    install_requires=requirements,
)
