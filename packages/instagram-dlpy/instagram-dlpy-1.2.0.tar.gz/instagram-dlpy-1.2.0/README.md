![PyPI - Python Version](https://img.shields.io/pypi/pyversions/instagram-dlpy)

# InstagramDL

A python package to download Instagram posts by URL without needing to login.

## Usage

1. Install the package

```bash
$ pip install instagram-dlpy
```

2. Import the package

```python
from instagramdl.api import get_post_data
from instagramdl.parser import parse_api_response
```

3. Get the post info and then parse it

```python
post_url = ""
raw_data = get_post_data(post_url)
parsed_data = parse_api_response(raw_data)
```

4. Download the associated media

```python
parsed_data.download(download_path="./")
```
