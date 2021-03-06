from pluginbase import PluginBase
#from util import get_user_home, get_pylint_home, get_plugins_directory, ensure_pylint_home, ensure_pylint_plugins_dir, check_os
from util import *
from os import path
import logging
from pprint import pprint
import argparse
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PyLint:
    def __init__(self, soup, plugin_source, cli_args):
        self.args = cli_args
        self.soup = soup
        self.plugin_source = plugin_source

    def run(self):
        for plugin_name in self.plugin_source.list_plugins():
            plugin = self.plugin_source.load_plugin(plugin_name)

            logger.debug("Loaded plugin '%s'" % plugin_name)
            plugin.config_map = {'html_file': 'index.html'}

            result = plugin.execute(self.soup)

            for info in result["info"]:
                s("[%s] %s" % (result["config"]["html_file"], info))
            for warning in result["warn"]:
                w("[%s] %s" % (result["config"]["html_file"], warning))
            for error in result["error"]:
                e("[%s] %s" % (result["config"]["html_file"], error))


def main(args):
    pylint_home = get_pylint_home()
    plugins_dir = get_plugins_directory()

    ensure_pylint_home()
    ensure_pylint_plugins_dir()

    plugin_base = PluginBase(package='pylint.plugins', searchpath=[plugins_dir])

    plugin_source = plugin_base.make_plugin_source(searchpath=[plugins_dir])

    # Taken from BS4 documentation
    html_doc = """
<html><head></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
    soup = BeautifulSoup(html_doc, 'html.parser')

    pylint = PyLint(soup, plugin_source, args)
    pylint.run()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="PyLint - Plugin-based HTML linter")
    parser.add_argument("-f", "--file", dest="file", required=False, help="Path to the file to lint")
    parser.add_argument("-d", "--dir", dest="directory", required=False, help="Path to the directory to parse for files to lint")
    parser.add_argument("-u", "--url", dest="url", required=False, help="URL to the file to lint (will be downloaded, then parsed)")
    args = parser.parse_args()
    main(args)
