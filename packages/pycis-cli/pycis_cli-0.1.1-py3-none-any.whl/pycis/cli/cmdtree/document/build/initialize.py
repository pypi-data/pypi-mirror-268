__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import json
import os

import click

from mojo.xmods.xclick import NORMALIZED_STRING

HELP_ID = "Sets the 'id' field of the build document."
HELP_START = "Sets the 'start' field of the build document."
HELP_STOP = "Sets the 'stop' field of the build document."
HELP_BRANCH = "Sets the 'branch' field of the build document."
HELP_REVISION = "Sets the 'revision' field of the build document."
HELP_RELEASE = "Sets the 'release' field of the build document."
HELP_ARCHIVE = "Sets the 'archive' field of the build document."

@click.command("initialize")
@click.option("--id", required=True, type=NORMALIZED_STRING, help=HELP_ID)
@click.option("--start", required=True, type=NORMALIZED_STRING, help=HELP_START)
@click.option("--stop", required=False, type=NORMALIZED_STRING, default="", help=HELP_STOP)
@click.option("--branch", required=True, type=NORMALIZED_STRING, help=HELP_BRANCH)
@click.option("--revision", required=True, type=NORMALIZED_STRING, help=HELP_REVISION)
@click.option("--release", required=True, type=NORMALIZED_STRING, help=HELP_RELEASE)
@click.option("--archive", required=False, type=NORMALIZED_STRING, default="", help=HELP_ARCHIVE)
@click.argument('filename', metavar='<build document>', type=click.Path(dir_okay=False))
def command_pycis_document_build_initialize(
    id: str, start: str, stop: str, branch: str, revision: str,
    release: str, archive: str, filename: str):
    
    buildobj = {
        "_id": id,
        "dtype": "build",
        "dversion": "1.0",
        "start": start,
        "stop": stop,
        "branch": branch,
        "revision": revision,
        "release": release,
        "job" : {},
        "byproducts": [],
        "changelist": [],
        "archive": archive
    }

    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    if os.path.exists(filename):
      
        with open(filename, 'r') as bdf:
            foundobj = json.load(bdf)
        
        if isinstance(foundobj, dict):
            keys = [k for k in buildobj.keys()]

            keyfound = None
            for nxtkey in keys:
                if nxtkey in foundobj:
                    keyfound = nxtkey
                    break

            if keyfound is not None:
                errmsg = f"Attempt to re-initialize the target document, it contains the key '{keyfound}'."
                raise click.BadParameter(errmsg)

    with open(filename, 'w') as bdf:
        json.dump(buildobj, bdf, indent=4)

    return
