import json
import logging
import re

from microcore import ui


def remove_json_wrapper(input_string: str, allow_in_text: bool = True) -> str:
    input_string = str(input_string).strip()
    if input_string.startswith("```json") and input_string.endswith("```"):
        input_string = input_string[7:-3].strip()
        return input_string
    if allow_in_text and not (
            (input_string.startswith("{") and input_string.endswith("}"))
            or (input_string.startswith("[") and input_string.endswith("]"))
            or (input_string.startswith('"') and input_string.endswith('"'))
            or input_string.isdigit()
            or input_string in ["true", "false", "null"]
    ):
        try:
            start_curly = input_string.index("{")
            start_square = input_string.index("[")
            if start_curly < start_square:
                input_string = input_string[start_curly: input_string.rindex("}") + 1]
            else:
                input_string = input_string[start_square: input_string.rindex("]") + 1]
        except ValueError as e:
            logging.exception(e)
            return input_string
    return input_string


def fix_json(s: str) -> str:
    """
    Fix internal JSON content
    """
    def between_lines(pattern):
        return fr'({json_obj_before}{pattern}{json_obj_after})|({json_list_before}{pattern}{json_list_after})'

    json_obj_before = r'((?<=\{)|(?<=[\"\d]\,)|(?<=null\,)|(?<=true\,)|(?<=false\,)|(?<=[\"\d])|(?<=null)|(?<=true)|(?<=false))\s*'
    json_obj_after = r'\s*((?=\})|(?=\"[^"\n]+\"\s*\:\s*))'
    json_list_before = r'((?<=\[)|(?<=[\"\d]\,)|(?<=null\,)|(?<=true\,)|(?<=false\,)|(?<=[\"\d])|(?<=null)|(?<=true)|(?<=false))\s*'
    json_list_after = r'\s*((?=[\]\"\d])|(?=true)|(?=false)|(?=null))'
    json_before = rf'({json_obj_before}|{json_list_before})'
    json_after = rf'({json_obj_after}|{json_list_after})'

    try:
        comment = r'(//|\#)[^\n]*\n'
        comments = fr"({comment})+"
        s = re.sub(between_lines(comments), '\n', s)
        return json.dumps(json.loads(s), indent=4)
    except:
        ...

    try:
        # ... typically added by LLMs to identify that sequence may be continued
        s = re.sub(between_lines(r'\.\.\.\n'), '\n', s)
        return json.dumps(json.loads(s), indent=4)
    except:
        ...

    try:
        # missing comma between strings on separate lines
        s = re.sub(r'\"\s*\n\s*\"', '",\n"', s)
        return json.dumps(json.loads(s), indent=4)
    except json.JSONDecodeError:
        ...
    try:
        # Redundant trailing comma
        s = re.sub(r"((?<=[\"\d])|(?<=null)|(?<=true)|(?<=false))\s*\,(?=\s*[\}\]])", '', s)
        return json.dumps(json.loads(s), indent=4)
    except json.JSONDecodeError:
        ...
    try:
        # Fix incorrect quotes
        s = re.sub(fr"({json_before}\')|(\'{json_after})", '"', s)
        s = re.sub(fr"\'\s*\,\s*{json_after}", '", ', s)
        s = re.sub(fr"\'\s*\:\s*(?=[\'\"])", '": ', s)
        s = re.sub(fr"(?<=[\'\"])\s*\:\s*\'", ': "', s)
        return json.dumps(json.loads(s), indent=4)
    except json.JSONDecodeError:
        ...

    return s
