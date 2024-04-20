// eslint-disable-next-line import/no-extraneous-dependencies
import { JsYamlAllSchemas } from "@mat3ra/code/dist/js/utils";
import * as fs from "fs";
import * as yaml from "js-yaml";
import * as pointer from "json-pointer";
import * as path from "path";

declare const __dirname: string;

export function getAllFilePaths(
    directoryPath: string = path.join(__dirname, "..", "assets"),
    filePaths: string[] = [],
) {
    const filesPaths = fs.readdirSync(directoryPath);

    // eslint-disable-next-line no-restricted-syntax
    for (const filePath of filesPaths) {
        const fullPath = path.join(directoryPath, filePath);
        const stats = fs.statSync(fullPath);

        if (stats.isFile()) {
            filePaths.push(fullPath);
        } else if (stats.isDirectory()) {
            getAllFilePaths(fullPath, filePaths);
        }
    }

    return filePaths;
}

export function loadRegexYAMLs(filePath: string) {
    const fileContent = fs.readFileSync(filePath, "utf8");
    const parsedContent = yaml.load(fileContent, { schema: JsYamlAllSchemas });
    return { filePath, parsedContent };
}

export function buildRegexSchema({
    filePath,
    parsedContent,
    _regexApplicationSchemas = {},
}: {
    filePath: string;
    parsedContent: unknown;
    _regexApplicationSchemas: object;
}) {
    const yamlFileRegexp = /\/file\/[a-zA-Z]*\/.*\.yml/g;

    if (filePath.match(yamlFileRegexp)) {
        const categoryRegex = /\/file\/([^/]+)/;
        const categoryMatch = filePath.match(categoryRegex);

        if (categoryMatch === null || !categoryMatch.length) return _regexApplicationSchemas;
        console.log(`filePath ${filePath} matched ${categoryMatch[1]} FileRegexp`);

        const directoryPath = path.dirname(filePath);
        const [, applicationSubPath] = directoryPath.split("/file");

        pointer.set(_regexApplicationSchemas, applicationSubPath, parsedContent);
    }

    return _regexApplicationSchemas;
}

export function writeSchemasToTarget({ filePath, schema }: { filePath: string; schema: object }) {
    fs.writeFileSync(path.resolve(filePath), JSON.stringify(schema) + "\n", "utf8");
}
