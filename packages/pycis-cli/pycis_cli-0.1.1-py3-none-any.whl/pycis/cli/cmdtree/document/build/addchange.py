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

HELP_COMMIT = "Sets the 'commit' field of the new change entry."
HELP_TITLE = "Sets the 'title' field of the new change entry."
HELP_DESCRIPTION = "Sets the 'description' field of the new change entry."
HELP_AUTHOR = "Sets the 'author' field of the new change entry."
HELP_DATE = "Sets the 'date' field of the new change entry."

@click.command("add-change")
@click.option("--commit", required=True, type=NORMALIZED_STRING, help=HELP_COMMIT)
@click.option("--title", required=True, type=NORMALIZED_STRING, help=HELP_TITLE)
@click.option("--description", required=False, type=NORMALIZED_STRING, help=HELP_DESCRIPTION)
@click.option("--author", required=True, type=NORMALIZED_STRING, help=HELP_AUTHOR)
@click.option("--date", required=True, type=NORMALIZED_STRING, help=HELP_DATE)
@click.argument('filename', metavar='<build document>', type=click.Path(dir_okay=False))
def command_pycis_document_build_addchange(
    commit: str, title: str, description: str, author: str,
    date: str, filename: str):
    
    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    if not os.path.exists(filename):
        errmsg = f"The specified build document was not found. filename={filename}"
        raise FileNotFoundError(errmsg)

    buildobj = None

    with open(filename, 'r') as bdf:
        buildobj = json.load(bdf)
    
    if 'changelist' not in buildobj:
        errmsg = "The 'changelist' list entry was not found, did you initialize the build document."
        raise click.BadParameter(errmsg)
    
    changelist = buildobj["changelist"]

    changelist.append({
        "commit": commit,
        "title": title,
        "description": description,
        "author": author,
        "date": date
    })

    with open(filename, 'w') as bdf:
        json.dump(buildobj, bdf, indent=4)

    return

