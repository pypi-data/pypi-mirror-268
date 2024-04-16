from setuptools import setup, find_packages

setup(
  name = 'vector_quantize_pytorch',
  packages = find_packages(),
  version = '1.14.7',
  license='MIT',
  description = 'Vector Quantization - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/vector-quantizer-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'pytorch',
    'quantization'
  ],
  install_requires=[
    'einops>=0.7.0',
    'einx[torch]>=0.1.3',
    'torch'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
