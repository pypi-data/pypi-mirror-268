# SPDX-FileCopyrightText: 2024 Georg-August-Universität Göttingen
#
# SPDX-License-Identifier: LGPL-3.0-or-later

# this file should contain general utility functions for
# working with tgclient, textgrid metadata and the import
# so the functions here ca move to tgclients itself
# they should be generic and make no assumptions about
# their usage, e.g. have no references to click, jupyter or pandas

import logging

from pathlib import Path
from xml.dom.minidom import parse

from jinja2 import Template

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from tgclients.databinding import Object as TextgridObject

log = logging.getLogger(__name__)

NAMESPACES = {"ore": "http://www.openarchives.org/ore/terms/"}
RDF_RESOURCE = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"

context = XmlContext()
PARSER = XmlParser(context=context)
SERIALIZER = XmlSerializer(context=context, config=SerializerConfig(indent="  "))

def calc_relative_path(filename: str, path: str) -> Path:
    """find the path of 'path' relative to 'filename'
    this could possibly be solved with walk_up=true from python 3.12 on
    https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.relative_to"""
    return Path(path).resolve().relative_to(Path(filename).parent.resolve())

def write_imex(imex_map: dict, filename: str) -> None:
    """write an .imex file which keeps track of local filenames and their related textgrid uris.
    this is useful for reimporting the data with the same uris (or new revisions of them).
    """

    imex_template_string = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<importSpec xmlns="http://textgrid.info/import">
  {% for path, tguri in imex.items() -%}
  <importObject textgrid-uri="{{tguri}}" local-data="{{calc_relative_path(filename, path)}}"/>
  {% endfor %}
</importSpec>
"""
    template = Template(imex_template_string)
    template.globals.update(calc_relative_path=calc_relative_path)
    xml = template.render(imex=imex_map, filename=filename)
    with open(filename, "w") as file:
        file.write(xml)

def imex_to_dict(imex, path_as_key: bool = False) -> dict:
    """parse textgrid_uris and paths from imex file. return a dict with uri as key per default,
    or use path as key if path_as_key is true"""

    imex_map = {}
    imexXML = parse(imex)
    for importObject in imexXML.getElementsByTagName("importObject"):
        textgrid_uri = importObject.getAttribute("textgrid-uri")
        path = importObject.getAttribute("local-data")
        if path_as_key:
            imex_map[path] = textgrid_uri
        else:
            imex_map[textgrid_uri] = path

    return imex_map


def base_uri_from(textgrid_uri: str) -> str:
    return textgrid_uri.split(".")[0]


def is_aggregation(meta: TextgridObject) -> bool:
    return "tg.aggregation" in meta.generic.provided.format


def is_edition(meta: TextgridObject) -> bool:
    return meta.generic.provided.format == "text/tg.edition+tg.aggregation+xml"

