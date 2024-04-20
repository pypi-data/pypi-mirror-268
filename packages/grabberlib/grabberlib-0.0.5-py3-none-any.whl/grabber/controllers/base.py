from cement import Controller, ex
from cement.utils.version import get_version_banner

from grabber.core.sources.graph import get_for_telegraph
from grabber.core.sources.khd import get_sources_for_4khd
from grabber.core.sources.xiuren import get_sources_for_xiuren
from grabber.core.utils import upload_folders_to_telegraph

from ..core.version import get_version

VERSION_BANNER = """
A beautiful CLI utility to download images from the web! %s
%s
""" % (get_version(), get_version_banner())


class Base(Controller):
    class Meta:
        label = "base"

        # text displayed at the top of --help output
        description = "A beautiful CLI utility to download images from the web"

        # text displayed at the bottom of --help output
        epilog = "Usage: grabber --entity 4khd --folder 4khd --publish --sources <list of links>"

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
                ["-l", "--limit"],
                {
                    "dest": "limit",
                    "type": int,
                    "help": "Limit the amount of posts retrieved (used altogether with --tag)",
                    "default": 0,
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
            (
                ["-t", "--tag"],
                {
                    "dest": "is_tag",
                    "action": "store_true",
                    "help": "Indicates that the link(s) passed is a tag in which the posts are paginated",
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
        is_tag = self.app.pargs.is_tag
        limit = self.app.pargs.limit

        getter_mapping = {
            "4khd": get_sources_for_4khd,
            "telegraph": get_for_telegraph,
            "xiuren": get_sources_for_xiuren,
        }

        if upload:
            upload_folders_to_telegraph(folder_name=folder, limit=limit)
        else:
            getter_images = getter_mapping.get(entity, get_for_telegraph)
            getter_images(
                sources=sources,
                entity=entity,
                final_dest=folder,
                save_to_telegraph=publish,
                is_tag=is_tag,
                limit=limit,
            )
