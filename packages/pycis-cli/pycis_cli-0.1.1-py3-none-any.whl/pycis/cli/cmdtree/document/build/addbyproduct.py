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

HELP_PRODUCT = "Sets the 'product' field of the new by-product entry."
HELP_PLATFORM = "Sets the 'platform' field of the new by-product entry."
HELP_ARCH = "Sets the 'arch' field of the new by-product entry."
HELP_BUILDNO = "Sets the 'buildno' field of the new by-product entry."
HELP_FLAVOR = "Sets the 'flavor' field of the new by-product entry."
HELP_PACKAGE = "Sets the 'package' field of the new by-product entry."
HELP_VERSION = "Sets the 'version' field of the new by-product entry."

@click.command("add-by-product")
@click.option("--product", required=True, type=NORMALIZED_STRING, help=HELP_PRODUCT)
@click.option("--platform", required=True, type=NORMALIZED_STRING, help=HELP_PLATFORM)
@click.option("--arch", required=False, type=NORMALIZED_STRING, help=HELP_ARCH)
@click.option("--buildno", required=True, type=NORMALIZED_STRING, help=HELP_BUILDNO)
@click.option("--flavor", required=True, type=NORMALIZED_STRING, help=HELP_FLAVOR)
@click.option("--package", required=True, type=NORMALIZED_STRING, help=HELP_PACKAGE)
@click.option("--version", required=True, type=NORMALIZED_STRING, help=HELP_VERSION)
@click.argument('filename', metavar='<build document>', type=click.Path(dir_okay=False))
def command_pycis_document_build_addbyproduct(
    product: str, platform: str, arch: str, buildno: str, flavor: str,
    package: str, version: str, filename: str):
    
    filename = os.path.abspath(os.path.expandvars(os.path.expanduser(filename)))
    if not os.path.exists(filename):
        errmsg = f"The specified build document was not found. filename={filename}"
        raise FileNotFoundError(errmsg)

    buildobj = None

    with open(filename, 'r') as bdf:
        buildobj = json.load(bdf)
    
    if 'byproducts' not in buildobj:
        errmsg = "The 'byproducts' list entry was not found, did you initialize the build document."
        raise click.BadParameter(errmsg)
    
    byproducts = buildobj["byproducts"]

    byproducts.append({
        "product": product,
        "platform": platform,
        "arch": arch,
        "buildno": buildno,
        "flavor": flavor,
        "package": package,
        "version": version
    })

    with open(filename, 'w') as bdf:
        json.dump(buildobj, bdf, indent=4)

    return
