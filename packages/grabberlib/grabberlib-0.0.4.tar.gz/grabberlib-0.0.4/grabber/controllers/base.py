from cement import Controller, ex
from cement.utils.version import get_version_banner

from grabber.core.sources.graph import get_for_telegraph
from grabber.core.sources.khd import get_sources_for_4khd
from grabber.core.utils import upload_folders_to_telegraph

from ..core.version import get_version

VERSION_BANNER = """
MyApp Does Amazing Things! %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = "base"

        # text displayed at the top of --help output
        description = "MyApp Does Amazing Things!"

        # text displayed at the bottom of --help output
        epilog = "Usage: test command1 --foo bar"

        # controller level arguments. ex: 'test --version'
        arguments = [
            ### add a version banner
            (
                ["-e", "--entity"],
                {
                    "dest": "entity",
                    "type": str,
                    "help": "Webtsite name from where it will be download",
                },
            ),
            (
                ["-s", "--sources"],
                {
                    "dest": "sources",
                    "type": str,
                    "help": "List of links",
                    "nargs": "+",
                },
            ),
            (
                ["-f", "--folder"],
                {
                    "dest": "folder",
                    "default": "",
                    "type": str,
                    "help": "Folder where to save",
                },
            ),
            (
                ["-p", "--publish"],
                {
                    "dest": "publish",
                    "action": "store_true",
                    "help": "Publish page to telegraph",
                },
            ),
            (
                ["-u", "--upload"],
                {
                    "dest": "upload",
                    "action": "store_true",
                    "help": "Upload and publish folders to telegraph",
                },
            ),
        ]

    @ex(hide=True)
    def _default(self):
        """Default action if no sub-command is passed."""

        entity = self.app.pargs.entity
        sources = self.app.pargs.sources
        folder = self.app.pargs.folder
        publish = self.app.pargs.publish
        upload = self.app.pargs.upload

        getter_mapping = {
            "4khd": get_sources_for_4khd,
            "telegraph": get_for_telegraph,
        }

        if upload:
            upload_folders_to_telegraph(folder_name=folder)
        else:
            getter_images = getter_mapping.get(entity, get_for_telegraph)
            getter_images(
                sources=sources,
                entity=entity,
                final_dest=folder,
                save_to_telegraph=publish,
            )
