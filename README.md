# pylint
A simple, plugin-based linter for HTML files.

# Please note
This thing is currently nothing but a quick-and-dirty proof-of-concept software. Expect errors and expect them to be horrible!

# What this is supposed to be
pylint is supposed to be a simple, but flexible linter for HTML files. I got the idea when I was testing a script at work and had to parse some HTML in order to do so. I noticed how easily I could check for things like missing id attributes and so on and wanted to improve our software's overall quality.

But each developer has different requirements and thus needs different checks. So I figured that I'd use plugins (which would be very easy to create) in order to enable each developer to lint in their own fashion.

# How it works
Copy any plugin you want (see `title_plugin` for an example) to pylint's default plugin directory (which is `~/.pylint/plugins`). It will automatically be executed.

# Requirements
pylint requires BeautifulSoup4, pluginbase and pprint

# Execute
`python pylint.py`
