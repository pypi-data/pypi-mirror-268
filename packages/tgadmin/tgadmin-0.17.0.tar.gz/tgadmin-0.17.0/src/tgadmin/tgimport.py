# SPDX-FileCopyrightText: 2024 Georg-August-Universität Göttingen
#
# SPDX-License-Identifier: LGPL-3.0-or-later

import logging
import xml.etree.ElementTree as ET

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import PurePath

from xsdata.exceptions import ConverterWarning

from tgclients import (
    TextgridCrud,
    TextgridCrudException
)
from tgclients.databinding import Object as TextgridObject, MetadataContainerType

from .utils import (
    NAMESPACES,
    PARSER,
    RDF_RESOURCE,
    base_uri_from,
    is_aggregation,
    is_edition,
    write_imex,
)

log = logging.getLogger(__name__)


def aggregation_import(tgcrud: TextgridCrud, sid: str, project_id: str, filename: str, threaded: bool, ignore_warnings: bool):
    """
    Import an TextGrid aggregation (or collection or edition)
    recursively with given tgcrud and sid into specified project

    Args:
        tgcrud (TextgridCrud): an instance of tgcrud
        sid (str): Session ID
        project_id (str): Project ID
        filename (str): path of the aggregation file to import
        threaded (bool): wether to use multiple threads for crud upload

    Raises:
        TextgridImportException: with a human understandable message  in case of
                                 errors (opening files, crud communication, etc)

    Returns:
        dict: results of import process (location of imex file, num objects uploaded, root aggregation uri)
    """
    imex_map = {}

    agg_meta = metafile_to_object(filename, referenced_in=filename)
    if not is_aggregation(agg_meta):
        raise TextgridImportException(f"File '{filename}' is not of type aggregation")

    tguri = handle_aggregation_upload(tgcrud, sid, project_id, filename, agg_meta, imex_map, threaded, ignore_warnings)

    imex_filename = filename + ".imex"
    write_imex(imex_map, imex_filename)

    return {
        "objects_uploaded" : len(imex_map),
        "imex_location" : imex_filename,
        "tguri" : tguri,
    }

def handle_aggregation_upload(tgcrud, sid, project_id, filename, agg_meta, imex_map, threaded, ignore_warnings):

    # if aggregation is edition then upload related work object
    if is_edition(agg_meta):
        work_path = PurePath(PurePath(filename).parent, agg_meta.edition.is_edition_of)
        tguri = upload_file(tgcrud, sid, project_id, work_path, imex_map, ignore_warnings, referenced_in=filename)
        agg_meta.edition.is_edition_of = tguri  # update isEditionOf

    agg_xml = ET.parse(filename)
    agg_xml_root = agg_xml.getroot()

    if not threaded:
        for ore_aggregates in agg_xml_root.findall(".//ore:aggregates", NAMESPACES):
            _handle_upload_op(tgcrud, sid, project_id, filename, ore_aggregates, imex_map, threaded, ignore_warnings)
    else:
        with ThreadPoolExecutor(max_workers=10) as ex:
            futures = [
                ex.submit(_handle_upload_op, tgcrud, sid, project_id, filename, ore_aggregates, imex_map, threaded, ignore_warnings)
                for ore_aggregates in agg_xml_root.findall(".//ore:aggregates", NAMESPACES)
            ]

            for future in as_completed(futures):
                result = future.result()

    tguri = upload_modified(tgcrud, sid, project_id, agg_xml_root, agg_meta, filename)
    # operations on dict seem to be thread safe in cpython
    # https://docs.python.org/3/glossary.html#term-global-interpreter-lock
    imex_map[filename] = tguri
    return tguri


def _handle_upload_op(tgcrud, sid, project_id, filename, ore_aggregates, imex_map, threaded, ignore_warnings):
    data_path = PurePath(PurePath(filename).parent, ore_aggregates.attrib[RDF_RESOURCE])
    meta = metafile_to_object(data_path, referenced_in=filename)

    if is_aggregation(meta):
        tguri = handle_aggregation_upload(tgcrud, sid, project_id, data_path, meta, imex_map, threaded, ignore_warnings)
    else:
        tguri = upload_file(tgcrud, sid, project_id, data_path, imex_map, ignore_warnings)

    # TODO: is this thread safe?
    ore_aggregates.set(RDF_RESOURCE, base_uri_from(tguri))  # update the xml with the uri


def upload_file(tgcrud, sid, project_id: str, data_path: PurePath, imex_map: dict, ignore_warnings, referenced_in: str = "") -> str:
    """upload an object and its related .meta file to specified project"""

    if data_path in imex_map:
        log.info(f"file already uploaded: {data_path.name} - has uri {imex_map[data_path]}")
        return imex_map[data_path]
    else:
        log.info(f"uploading unmodified file with meta: {data_path.name}")

    try:
        with open(data_path, "r") as the_data:
            mdobj = metafile_to_object(data_path)
            # tgcrud wants a MetadataContainerType, see https://gitlab.gwdg.de/dariah-de/textgridrep/textgrid-python-clients/-/issues/76
            mdcont = MetadataContainerType()
            mdcont.object_value = mdobj

            res = tgcrud.create_resource(
                sid, project_id, the_data.read(), mdcont
            )
            handle_crud_warnings(res, data_path.name, ignore_warnings)

            tguri = res.object_value.generic.generated.textgrid_uri.value
            imex_map[data_path] = tguri
            return tguri
    except FileNotFoundError:
        raise TextgridImportException(f"File '{data_path}' not found, which is referenced in '{referenced_in}'")
    except TextgridCrudException as error:
        handle_crud_exception(error, sid, project_id, data_path)

def handle_crud_warnings(res, filename, ignore_warnings):
    for crudwarn in res.object_value.generic.generated.warning:
        log.warning(f" ⚠️ Warning from tgcrud for {filename}: {crudwarn}")
    if len(res.object_value.generic.generated.warning) > 0 and not ignore_warnings:
        raise TextgridImportException("Stopped import. Please fix your input or try again with --ignore-warnings")

def upload_modified(tgcrud, sid, project_id: str, etree_data, metadata, ignore_warnings, filename="") -> str:
    """upload in memory xml and it textgrid-metadata (possibly modified) as textgridobject"""

    log.info(
        f"uploading modified file '{filename}' with title: {metadata.generic.provided.title[0]}"
    )
    data_str = ET.tostring(etree_data, encoding="utf8", method="xml")

    mdcont = MetadataContainerType()
    mdcont.object_value = metadata
    try:
        res = tgcrud.create_resource(sid, project_id, data_str, mdcont)
        handle_crud_warnings(res, filename, ignore_warnings)
    except TextgridCrudException as error:
        handle_crud_exception(error, sid, project_id, filename)
    return res.object_value.generic.generated.textgrid_uri.value


def metafile_to_object(filename: str, referenced_in:str = "") -> TextgridObject:
    metafile_path = PurePath(f"{filename}.meta")
    try:
        with open(metafile_path, "rb") as meta_file:
            meta: TextgridObject = PARSER.parse(meta_file, TextgridObject)
            #print(SERIALIZER.render(meta))
        return meta
    except FileNotFoundError:
        if filename == referenced_in:
            raise TextgridImportException(f"File '{filename}.meta' not found, which belongs to '{filename}'")
        else:
            raise TextgridImportException(f"File '{filename}.meta' not found, which belongs to '{filename}' and is referenced in '{referenced_in}'")
    except ConverterWarning as warning:
        # TODO ConverterWarning is not thrown, only shown
        raise TextgridImportException(f"xsdata found a problem: {warning}")


def handle_crud_exception(error, sid, project_id, filename):
    # TODO: we can check both here, if sessionid is valid, and if project is existing and accessible, for better feedback
    # tgrud should also communicate the cause
    # error mapping
    # * 404 - project not existing
    # * 401 - sessionid invalid
    # * 500 - something went terribly wrong (invalid metadata)

    msg = f"""
        tgcrud responded with an error uploading '{filename}'
        to project '{project_id}'
        with sessionid starting...ending with '{sid[0:3]}...{sid[-3:]}'

        """
    if "404" in str(error):
        msg += "Are you sure the project ID exists?"
    elif "401" in str(error):
        msg += "Possibly the SESSION_ID is invalid"
    elif "500" in str(error):
        msg += f"""A problem on tgcrud side - is you metadata valid?
        Please check {filename}.meta"""
    else:
        msg += f"new error code found"

    msg += f"""

        ----
        Error message from tgcrud:
        {error}
    """

    raise TextgridImportException(msg)


class TextgridImportException(Exception):
    """Exception thrown by tgimport module"""
