import { expect } from "chai";
import * as path from "path";

import { buildRegexSchema, getAllFilePaths, loadRegexYAMLs } from "../../src/js/functions";

const REFERENCE_PATH_TO_PWX_STDIN_YML = path.join(
    __dirname,
    "..",
    "assets",
    "file/applications/espresso/5.2.1/pw.x/stdin.yml",
);

const REFERENCE_ASSETS_PATHS = [
    "file/applications/espresso/5.2.1/pw.x/stdin.yml",
    "file/applications/espresso/7.1/pw.x/stdin.yml",
    "file/fortran_namelist.yml",
];

const REFERENCE_YAML_CONTENT = {
    _fingerprints: [
        { regex: "^&control", flags: ["g", "i"], isRequired: true },
        { regex: "^&electrons", flags: ["g", "i"], isRequired: true },
    ],
    control: {
        _format: {
            namelist: {
                regex: "(\\$|&){{BLOCK_NAME}}\\n(?:\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+)(?:\\n\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+))*)?\\s*\\/",
                flags: ["g", "m"],
                params: {
                    BLOCK_NAME: ["CONTROL", "ELECTRONS", "IONS", "CELL", "SYSTEM"],
                },
            },
        },
        calculation: { regex: "calculation\\s*=\\s*'([^']+)'", flags: ["g", "m", "i"] },
        title: { regex: "title\\s*=\\s*'([^']+)'", flags: ["g", "m", "i"] },
        restart_mode: { regex: "restart_mode\\s*=\\s*'([^']+)'", flags: ["g", "m", "i"] },
    },
};

const REFERENCE_SCHEMA_CONTENT_INTERMEDIATE = {
    _fingerprints: [
        { regex: "^&control", flags: ["g", "i"], isRequired: true },
        { regex: "^&electrons", flags: ["g", "i"], isRequired: true },
    ],
    control: {
        _format: {
            namelist: {
                regex: "($|&){{BLOCK_NAME}}\\n(?:\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+)(?:\\n\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+))*)?\\s*\\/",
                flags: ["g", "m", "i"],
                params: {
                    BLOCK_NAME: ["CONTROL", "SYSTEM", "ELECTRONS", "IONS", "CELL"],
                },
            },
        },
        calculation: { regex: "calculation\\s*=\\s*'([^']+)'", flags: ["g", "m", "i"] },
    },
};

const REFERENCE_SCHEMA_CONTENT_FINAL = {
    applications: {
        espresso: {
            "5.2.1": {
                "pw.x": {
                    _fingerprints: [
                        {
                            flags: ["g", "i"],
                            isRequired: true,
                            regex: "^&control",
                        },
                        {
                            flags: ["g", "i"],
                            isRequired: true,
                            regex: "^&electrons",
                        },
                    ],
                    control: {
                        _format: {
                            namelist: {
                                flags: ["g", "m", "i"],
                                regex: "($|&){{BLOCK_NAME}}\\n(?:\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+)(?:\\n\\s+[A-Za-z_]+\\s*=\\s*(?:['\"].*?['\"]|[^\\/\\n]+))*)?\\s*\\/",
                                params: {
                                    BLOCK_NAME: ["CONTROL", "SYSTEM", "ELECTRONS", "IONS", "CELL"],
                                },
                            },
                        },
                        calculation: {
                            flags: ["g", "m", "i"],
                            regex: "calculation\\s*=\\s*'([^']+)'",
                        },
                    },
                },
            },
        },
    },
};
describe("build schema from assets tests", () => {
    it("should get all file paths", () => {
        const filePaths: string[] | undefined = [];
        const allPaths = getAllFilePaths(path.join(__dirname, "..", "assets"), filePaths);
        expect(allPaths.length).to.be.eql(3);

        allPaths.forEach((assetPath, index) =>
            expect(assetPath).to.contain(REFERENCE_ASSETS_PATHS[index]),
        );
    });

    it("should load Regex YAML", () => {
        const regexObject = loadRegexYAMLs(REFERENCE_PATH_TO_PWX_STDIN_YML);
        expect(regexObject.filePath).to.be.eql(REFERENCE_PATH_TO_PWX_STDIN_YML);
        expect(regexObject.parsedContent).to.be.eql(REFERENCE_YAML_CONTENT);
    });

    it("should build Regex Schema", () => {
        const _regexApplicationSchemas = {};
        const updatedSchemas = buildRegexSchema({
            filePath: REFERENCE_PATH_TO_PWX_STDIN_YML,
            parsedContent: REFERENCE_SCHEMA_CONTENT_INTERMEDIATE,
            _regexApplicationSchemas,
        });
        expect(updatedSchemas).to.be.eql(REFERENCE_SCHEMA_CONTENT_FINAL);
    });
});
