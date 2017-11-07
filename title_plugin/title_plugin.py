config_map = {}

def execute(soup):
    ret_map = {
        "info": [],
        "warn": [],
        "error": [],
        "config":config_map
    }

    if soup is None:
        return ret_map

    title = soup.title
    if title is None:
        ret_map["error"].append("Site has no title")
    elif title.string is None or len(title.string) == 0:
        ret_map["warn"].append("Site's title is empty")
    else:
        ret_map["info"].append("Site's title is '%s'" % title.string)

    return ret_map
