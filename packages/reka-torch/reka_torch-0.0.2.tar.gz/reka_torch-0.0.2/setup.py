# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reka_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'torchvision', 'zetascale']

setup_kwargs = {
    'name': 'reka-torch',
    'version': '0.0.2',
    'description': 'Reka Torch - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Reka Torch\nImplementation of the model: "Reka Core, Flash, and Edge: A Series of Powerful Multimodal Language Models" in PyTorch. [PAPER LINK](https://publications.reka.ai/reka-core-tech-report.pdf)\n\n## Install\n`pip3 install -U reka-torch`\n\n## Usage\n```python\nimport torch  # Importing the torch library\nfrom reka_torch.model import Reka  # Importing the Reka model from the reka_torch package\n\ntext = torch.randint(0, 10000, (2, 512))  # Generating a random tensor of shape (2, 512) with values between 0 and 10000\n\nimg = torch.randn(2, 3, 224, 224)  # Generating a random tensor of shape (2, 3, 224, 224) with values from a normal distribution\n\naudio = torch.randn(2, 1000)  # Generating a random tensor of shape (2, 1000) with values from a normal distribution\n\nvideo = torch.randn(2, 3, 16, 224, 224)  # Generating a random tensor of shape (2, 3, 16, 224, 224) with values from a normal distribution\n\nmodel = Reka(512)  # Creating an instance of the Reka model with input size 512\n\nout = model(text, img, audio, video)  # Forward pass through the model with the input tensors\n\nprint(out.shape)  # Printing the shape of the output tensor\n\n```\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/Reka-Torch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
