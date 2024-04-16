# =============================================================================
# <copyright>
# Copyright (c) 2023 3LC Inc. All rights reserved.
#
# All rights are reserved. Reproduction or transmission in whole or in part, in
# any form or by any means, electronic, mechanical or otherwise, is prohibited
# without the prior written permission of the copyright owner.
# </copyright>
# =============================================================================

"""Configure the `tlc` package and Object Service

When importing the tlc package from a Jupyter notebook (e.g. `import tlc`), the default configuration will be picked
from the config file and environment variables (if set). If the users wants to override these values, one can import the
`tlcconfig` module and set the configuration options before importing the `tlc` package.

:Example Usage:

```python

import tlcconfig.options
import tlcconfig.option_loader

# Create a new OptionLoader instance. Pass false to constructor to prevent
# options being loaded from default configuration file and environment variables.
myOptionLoader = tlcconfig.option_loader.OptionLoader(initialize=False)

# Set an option:
scan_urls = ["s3://bucket/path/to/tables", "file://home/data/tables"]
myOptionLoader.set(tlcconfig.options.TABLE_SCAN_URLS, scan_urls)

# Set the global OptionLoader instance to the one we just created.
OptionLoader.setInstance(myOptionLoader)

import tlc # This will use the options set above

# Use tlc package with your custom options
```

"""

from .version import _PACKAGE_GIT_REVISION, _PACKAGE_NAME, _PACKAGE_VERSION  # noqa: F401

__version__ = _PACKAGE_VERSION
__git_revision__ = _PACKAGE_GIT_REVISION
