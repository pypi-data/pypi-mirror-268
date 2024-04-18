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

HELP_NAME = "Sets the 'name' field of the job detail section for the build document."
HELP_ID = "Sets the 'id' field of the job detail section for the build document."
HELP_INITIATOR = "Sets the 'initiator' field of the job detail section for the build document."
HELP_LABEL = "Sets the 'label' field of the job detail section for the build document."
HELP_OWNER = "Sets the 'owner' field of the job detail section for the build document."
HELP_TYPE = "Sets the 'type' field of the job detail section for the build document."

@click.command("set-job-detail")
@click.option("--name", required=True, type=NORMALIZED_STRING, help=HELP_NAME)
@click.option("--id", required=True, type=NORMALIZED_STRING, help=HELP_ID)
@click.option("--initiator", required=True, type=NORMALIZED_STRING, help=HELP_INITIATOR)
@click.option("--label", required=False, type=NORMALIZED_STRING, default="", help=HELP_LABEL)
@click.option("--owner", required=True, type=NORMALIZED_STRING, help=HELP_OWNER)
@click.option("--type", "jtype", required=True, type=NORMALIZED_STRING, help=HELP_TYPE)
@click.argument('filename', metavar='<build document>', type=click.Path(dir_okay=False))
def command_pycis_document_build_setjobdetail(
    name: str, id: str, initiator: str, label: str,
    owner: str, jtype: str, filename: str):
    
    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    if not os.path.exists(filename):
        errmsg = f"The specified build document was not found. filename={filename}"
        raise FileNotFoundError(errmsg)

    buildobj = None

    with open(filename, 'r') as bdf:
        buildobj = json.load(bdf)
    
    if 'job' not in buildobj:
        errmsg = "The 'job' list entry was not found, did you initialize the build document."
        raise click.BadParameter(errmsg)
    
    jobdetail = buildobj["job"]

    jobdetail["name"] = name
    jobdetail["id"] = id
    jobdetail["initiator"] = initiator
    jobdetail["label"] = label
    jobdetail["owner"] = owner
    jobdetail["type"] = jtype
    
    with open(filename, 'w') as bdf:
        json.dump(buildobj, bdf, indent=4)

    return

