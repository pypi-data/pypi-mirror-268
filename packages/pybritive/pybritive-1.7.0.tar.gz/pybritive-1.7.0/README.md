# Britive CLI - Pure Python Implementation

PyBritive is intended to be used as a CLI application for communicating with the Britive Platform.

## Installation

`pybritive` will be installed via Python `pip`. 

~~~bash
pip install pybritive
~~~

Or you can always pull the latest version directly from GitHub using one of the following commands.

~~~
pip install $(curl -s https://api.github.com/repos/britive/python-cli/releases/latest | jq -r '.assets[] | select(.content_type == "application/x-gzip") | .browser_download_url')

OR

pip install $(curl -s https://api.github.com/repos/britive/python-cli/releases/latest | grep "browser_download_url.*.tar.gz" | cut -d : -f 2,3 | tr -d \")
~~~

The end user is free to install the CLI into a virtual environment or in the global scope, so it is available
everywhere.


## Documentation

https://britive.github.io/python-cli/


## Community Projects

Note: Britive, Inc. does not provide support for community projects. Community projects are also not considered when ensuring backwards compatibility for releases. The list below is provided as-is and use of these projects is subject to the licensing/restrictions of each individual project.

* `vim-britive`: https://github.com/pbnj/vim-britive

