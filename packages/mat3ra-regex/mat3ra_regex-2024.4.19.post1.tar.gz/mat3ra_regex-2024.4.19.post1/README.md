# regex

## Usage

1. Install package adding to package.json:
    ```json

    "dependencies": {
        "@exabyte-io/regex": "2023.9.1"
    }
    ```
Or using npm:
    ```bash
    npm i @exabyte-io/regex@2023.9.1
    ```

2. Import package:
    ```javascript
    import regexSchemas from "@exabyte-io/regex/lib/schemas";
    ```

3. Use regex schemas:
    ```javascript
   const calculationPattern = regexSchemas.espresso["5.8.1"].["pw.x"].calculation;
   const regex = new RegExp(calculationPattern.regex, calculationPattern.flags.join("));
   ```

## Development
To run tests:
```bash
npm test
```
To run lint:
```bash
npm run lint
```
To build regex schemas for development:
```bash
npm run build:schemas:dev
```

## Add new regex schemas
1. Add new yamls for `stdin` and `stdout` to `assets/file/applications/<application_name>/<application_version>/<unit_name>/`
2. Run `npm run build:schemas:dev` to generate new regex schemas for dev
3. Add tests for newly added regex schemas

## Usage

1. Install dependency (list in `package.json` ar with `npm install`):

```bash
npm install @exabyte-io/regex
```

2. Import `schema.json` with compiled regexes in your code:

```js
import regexesSchema from "@exabyte-io/regex/data/schemas.json"
```

3. Use `regexesSchema` object to found needed regex based on application and version for example (you can use `json-pointer` to get needed path):

```js
import pointer from "json-pointer";

const espressoNamelistRegex = pointer.get(
    schemas,
    "/applications/espresso/5.2.1/pw.x/control/_format/namelist",
);

// _format/namelist contains regex with template string
// available templates for regex should be enumerated in params section
// name of param define template string to replace
// possible values will be enumerated as value of param
// "params":{"BLOCK_NAME":["CONTROL","ELECTRONS","IONS","CELL","SYSTEM"]}

const controlBlockRegex = new RegExp(
    espressoNamelistRegex.regex.replace('{{BLOCK_NAME}}', 'CONTROL'),
    espressoNamelistRegex.flags.join(""),
);

// getting namelist blocks
const controlBlocksMatch = file.match(controlBlockRegex);
const controlBlock = controlBlocksMatch[0];


const regexObject = pointer.get(
    schemas,
    "/applications/espresso/5.2.1/pw.x/control/calculation",
);
const regexCalculation = new RegExp(
    regexObject.regex,
    regexObject.flags.join(""),
);

// getting calculation param value
const calculation = controlBlock.matchAll(regexCalculation);
const [calcluationLine, calculationValue] = Array.from(calculation)[0];


console.log({ calcluationLine, calculationValue })
```
