# V(ersioned) (P)ython

This lightweight utility for Python versioning captures the contents of any file after you run it. To use:

1. Clone this repo
2. Run `pip install .` in the root directory of the repo
3. Any time you run `python ...`, run `vython ...` instead. 

Example: run `vython helloworld.py` in the root directory to get the output:

```
> vython helloworld.py
hello world
```

Versions are saved as json files such as:

```json
{
    "timestamp": "2022-04-12 16:13:34.875372", 
    "filename": "/Users/shreyashankar/Documents/projects/vpython/helloworld.py", 
    "command": "/Users/shreyashankar/miniforge3/envs/hawk/bin/python3.9 helloworld.py", 
    "contents": "print(\"hello world\")\n"
}
```

The default save directory is `Path.home()/.vython`. To override it, set the `VYTHON_SAVE_DIR` environment variable.

TODO:
* Utilities for diffing versions
* Log stdout to the json files
* Integrations with git