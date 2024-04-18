from typing import Final
from xmltodict3 import XmlTextToDict

from .file_pomes import file_get_data

XML_FILE_HEADER: Final[str] = '<?xml version="1.0" encoding="UTF-8" ?>'


def xml_normalize_keys(source: dict) -> dict:
    """
    Clone *source*, removing *namespaces* and the prefixes *'@'* e *'#'* from its key names.

    The key order is kept unchanged.

    :param source: the reference dict
    :return: the new, normalized, dict
    """
    # initialize the return variable
    result: dict = {}

    # traverse the dictionary
    for curr_key, curr_value in source.items():

        # is 'curr_value' a dictionary ?
        if isinstance(curr_value, dict):
            # yes, proceed recursively
            result[curr_key] = xml_normalize_keys(curr_value)
        # is 'curr_value' a list ?
        elif isinstance(curr_value, list):
            # yes, traverse it
            result[curr_key] = []
            for item in curr_value:
                # is 'item' a dictionary ?
                if isinstance(item, dict):
                    # yes, proceed recursively
                    result[curr_key].append(xml_normalize_keys(item))
                else:
                    result[curr_key].append(item)
        # does the current key have a prefix to be removed ?
        elif curr_key[0:1] in ["@", "#"]:
            # yes, remove it
            result[curr_key[1:]] = curr_value
        else:
            pos: int = curr_key.find(":")
            if pos == 0:
                result[curr_key] = curr_value
            else:
                result[curr_key[pos+1:]] = curr_value

    return result


def xml_to_dict(file_data: bytes | str) -> dict:
    """
    Convert the XML into a *dict*, by removing namespaces, and keys prefixed with "@" e "#".

    O XML de entrada deve estar em *file_data* (tipo *bytes*),
    ou em arquivo do sistema com o caminho especificado por *file_data* (tipo *str*).

    :param file_data: XML a ser convertido
    :return: dict normalizado
    """
    # obtain the file data
    file_bytes: bytes = file_get_data(file_data)

    # converte o XML em dict
    xml_data = XmlTextToDict(xml_text=file_bytes.decode(),
                             ignore_namespace=True)
    result: dict = xml_data.get_dict()

    # normalize the dict, removing namespaces, and prefixos '@' e '#' from the key names
    return xml_normalize_keys(result)
