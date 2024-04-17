<h1 align="center">
<img src="https://raw.githubusercontent.com/heatingma/OpenVideo/main/docs/assets/openvideo-logo2.png" width="600">
</h1><br>

``OpenVideo`` is a Python package designed to facilitate the downloading, data streaming, data cleaning, and captioning of various videos from free, royalty-free video websites. It provides a set of functions and classes that enable seamless integration with these websites and streamline video-related data processing tasks. `OpenVideo` has the following features:

- ``Video Downloading``: downloading of videos from free, royalty-free video websites.

- ``Video Streaming``: Implementing data flow between HuggingFace and ModelScope.

- ``Video Cleaning``: video integrity, scene segmentation, extracting keyframes from videos, etc.

- ``Video Captioning``: Not yet implemented.

## Installation

You can install the stable release on PyPI:

```bash
$ pip install openvideo
```

or get the latest version by running:

```bash
$ pip install -U https://github.com/heatingma/OpenVideo/archive/master.zip # with --user for user install (no root)
```

The following packages are required, and shall be automatically installed by ``pip``:

```
huggingface_hub>=0.22.2
tqdm>=4.66.1
wget>=3.2
requests>=2.31.0
aiohttp>=3.9.3
async_timeout>=4.0.3
moviepy>=1.0.3
opencv-python>=4.9.0.80
selenium>=4.19.0
scenedetect>=0.6.3
texttable>=1.7.0
bs4>=0.0.2
```

## Video Downloading

| website | windows | macos | linux |
| :-----: | :-----: | :---: | :---: |
| [Pexels](https://www.pexels.com) | ✔ | 📆 | 📆 |
| [Mazwai](https://mazwai.com/stock-video-footage) | 📆 | 📆 | 📆 |
| [Mixkit](https://mixkit.co/free-stock-video) | ✔ | 📆 | ✔ |
| [Pixabay](https://pixabay.com/videos/search/?order=ec) | ✔ | 📆 | 📆 |
| [Coverr](https://coverr.co/stock-video-footage) | 📆 | 📆 | 📆 |
| [Youtube](https://www.youtube.com/) | ✔ | ✔ | ✔ |