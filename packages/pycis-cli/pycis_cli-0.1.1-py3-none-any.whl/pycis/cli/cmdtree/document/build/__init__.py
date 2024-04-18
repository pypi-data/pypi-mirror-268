
__author__ = "Myron Walker"
__copyright__ = "Copyright 2023, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import click

from pycis.cli.cmdtree.document.build.addbyproduct \
    import command_pycis_document_build_addbyproduct
from pycis.cli.cmdtree.document.build.addchange \
    import command_pycis_document_build_addchange
from pycis.cli.cmdtree.document.build.initialize \
    import command_pycis_document_build_initialize
from pycis.cli.cmdtree.document.build.setjobdetail \
    import command_pycis_document_build_setjobdetail
from pycis.cli.cmdtree.document.build.update \
    import command_pycis_document_build_update



@click.group("build", help="Contains commands for writing data to a pycis 'build' document.")
def group_pycis_document_build():
    return

group_pycis_document_build.add_command(
    command_pycis_document_build_addbyproduct
)
group_pycis_document_build.add_command(
    command_pycis_document_build_addchange
)
group_pycis_document_build.add_command(
    command_pycis_document_build_initialize
)
group_pycis_document_build.add_command(
    command_pycis_document_build_setjobdetail
)
group_pycis_document_build.add_command(
    command_pycis_document_build_update
)
