# SDRCAP

A software defined radio recording library in python.

Organized as a Python Pip Poetry project. Currently only limited support for RTL-SDR with others to be added.

## Setup

### Installing

Obtain pyproject.toml & poetry.lock
in root of project run
```
poetry install
```
Both toml and lock files are currently version controlled
TODO: understand best strategies for application developers having their own lock files and just providing a toml.

### Running

Try out the example!
```
poetry run python examples/example_usage.py
```

In general, the library is organized around you calling the 
<b>library -> hardware device interface -> functions</b>
We define the hardware device interface in the python file and class name:

For RTLSDRv4 devices:
```
from sdrcap import rtl_interface 
```

### Output

Currently the output is stored in plain text csv format.
TODO: Output into a higher data format filetype like hd5

### Dependencies
setuptool is needed for MACOS to import packages 

A environment setting script is set to bind the poetry environments rtlsdrlib but shouldn't be necessary if you are explicitly doing:

```
poetry run python ${target}
```
instead of:
```
poetry shell
python ${target}
```
due to differences in potential python environments.
If you want to use it run:
```
source set_env.sh
```
then run:
```
sudo -E python ${target}
```
where -E attached to sudo retains the environment variable you sourced from the shell script.

### TODO's
 For RTLSDR:
 0. Support multiple devices
 1. Support all rtlsdr.rtlsdr.BaseRtlSdr API options
 2. Support asyncio streaming
 3. Support/ expand TCP server client functions -> rtlsdr.rtlsdrtcp
 4. Add compliant encryption for data at rest, data in air
 5. Add on more advanced data transformation, interpolation, sniffing and analysis features

