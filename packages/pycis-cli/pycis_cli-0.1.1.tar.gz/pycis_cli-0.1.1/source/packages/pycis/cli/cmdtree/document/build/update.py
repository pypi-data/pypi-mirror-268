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

HELP_ID = "An optional 'id' value to set in the build document."
HELP_START = "An optional 'start' value to set in the build document."
HELP_STOP = "An optional 'stop' value to set in the build document."
HELP_BRANCH = "An optional 'branch' value to set in the build document."
HELP_REVISION = "An optional 'revision' value to set in the build document."
HELP_RELEASE = "An optional 'release' value to set in the build document."
HELP_ARCHIVE = "An optional 'archive' value to set in the build document."

@click.command("update")
@click.option("--id", required=False, type=NORMALIZED_STRING, default=None, help=HELP_ID)
@click.option("--start", required=False, type=NORMALIZED_STRING, default=None, help=HELP_START)
@click.option("--stop", required=False, type=NORMALIZED_STRING, default=None, help=HELP_STOP)
@click.option("--branch", required=False, type=NORMALIZED_STRING, default=None, help=HELP_BRANCH)
@click.option("--revision", required=False, type=NORMALIZED_STRING, default=None, help=HELP_REVISION)
@click.option("--release", required=False, type=NORMALIZED_STRING, default=None, help=HELP_RELEASE)
@click.option("--archive", required=False, type=NORMALIZED_STRING, default=None, help=HELP_ARCHIVE)
@click.argument('filename', metavar='<build document>', type=click.Path(dir_okay=False))
def command_pycis_document_build_update(
    id: str, start: str, stop: str, branch: str, revision: str,
    release: str, archive: str, filename: str):
    
    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    if not os.path.exists(filename):
        errmsg = f"The specified build document was not found. filename={filename}"
        raise FileNotFoundError(errmsg)

    buildobj = None

    with open(filename, 'r') as bdf:
        buildobj = json.load(bdf)
    
    if id is not None:
        buildobj["id"] = id
    
    if start is not None:
        buildobj["start"] = start

    if stop is not None:
        buildobj["stop"] = stop

    if branch is not None:
        buildobj["branch"] = branch
    
    if revision is not None:
        buildobj["revision"] = revision
    
    if release is not None:
        buildobj["release"] = release
    
    if archive is not None:
        buildobj["archive"] = archive

    with open(filename, 'w') as bdf:
        json.dump(buildobj, bdf, indent=4)

    return
