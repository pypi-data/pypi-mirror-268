import re

from mat3ra.fixtures import get_content_by_reference_path
from mat3ra.regex.data.schemas import SCHEMAS
from mat3ra.utils import object as object_utils
from mat3ra.utils import regex as regex_utils


def test_schemas_espresso_pwx_stdin():
    espresso_namelist_regex_obj = object_utils.get(
        SCHEMAS, "/applications/espresso/5.2.1/pw.x/control/_format/namelist"
    )

    # Assuming file content is in a variable named 'file'
    file_content = get_content_by_reference_path("applications/espresso/v5.4.0/stdin")

    espresso_namelist_regex = espresso_namelist_regex_obj["regex"].replace("{{BLOCK_NAME}}", "CONTROL")

    control_block_regex = re.compile(
        espresso_namelist_regex.encode().decode("unicode_escape"),
        regex_utils.convert_js_flags_to_python(espresso_namelist_regex_obj["flags"]),
    )

    control_blocks_match = control_block_regex.match(file_content)
    control_block = control_blocks_match[0] if control_blocks_match else None

    regex_object = object_utils.get(SCHEMAS, "/applications/espresso/5.2.1/pw.x/control/calculation")
    regex_calculation = re.compile(
        regex_object["regex"],
        # Adjust flags as needed; the join operation is omitted since Python doesn't use an array for flags
        regex_utils.convert_js_flags_to_python(regex_object["flags"]),
    )

    # getting calculation param value
    calculation = list(regex_calculation.finditer(control_block))
    calculation_line, calculation_value = calculation[0].group(0), calculation[0].group(1) if calculation else (
        None,
        None,
    )
    assert calculation_value == "scf"
    assert calculation_line == "calculation = 'scf'"
