import * as fs from "fs";
import * as path from "path";

import {
    buildRegexSchema,
    getAllFilePaths,
    loadRegexYAMLs,
    writeSchemasToTarget,
} from "./functions";

declare const __dirname: string;
const regexApplicationSchemas = {};

const paths = getAllFilePaths();

paths
    .map(loadRegexYAMLs)
    // @ts-ignore
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    .forEach((parsed: any) =>
        buildRegexSchema({ ...parsed, _regexApplicationSchemas: regexApplicationSchemas }),
    );

writeSchemasToTarget({
    schema: regexApplicationSchemas,
    filePath: path.resolve(__dirname, "..", "..", "data", "schemas.json"),
});

fs.writeFileSync(
    "./src/py/mat3ra/regex/data/schemas.py",
    [
        "import json",
        `SCHEMAS = json.loads(r'''${JSON.stringify(regexApplicationSchemas)}''')`,
        "",
    ].join("\n"),
    "utf8",
);
