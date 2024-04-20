import { expect } from "chai";
import * as fs from "fs";
import pointer from "json-pointer";
import * as path from "path";

import schemas from "../../data/schemas.json";

describe("use espresso regexes", () => {
    const espressoNamelistRegex = pointer.get(
        schemas,
        "/applications/espresso/5.2.1/pw.x/control/_format/namelist",
    );

    const file = fs.readFileSync(
        path.resolve("tests/fixtures/applications/espresso/5.2.1/pw.x"),
        "utf8",
    );

    it("should get control block", () => {
        const controlBlockRegex = new RegExp(
            espressoNamelistRegex.regex.replace(
                "{{BLOCK_NAME}}",
                espressoNamelistRegex.params.BLOCK_NAME[0],
            ),
            espressoNamelistRegex.flags.join(""),
        );
        const controlBlockMatch = file.match(controlBlockRegex);

        if (!controlBlockMatch) return;
        expect(controlBlockMatch.length).to.be.eql(1);
        expect(controlBlockMatch[0]).to.be.eql(`&CONTROL
    calculation = 'scf'
    title = ''
    verbosity = 'low'
    restart_mode = 'from_scratch'
    wf_collect = .true.
    tstress = .true.
    tprnfor = .true.
    outdir = '{{ JOB_WORK_DIR }}/outdir'
    wfcdir = '{{ JOB_WORK_DIR }}/outdir'
    prefix = '__prefix__'
    pseudo_dir = '{{ JOB_WORK_DIR }}/pseudo'
/`);
    });

    it("should get electrons block", () => {
        const electornsBlockRegex = new RegExp(
            espressoNamelistRegex.regex.replace(
                "{{BLOCK_NAME}}",
                espressoNamelistRegex.params.BLOCK_NAME[1],
            ),
            espressoNamelistRegex.flags.join(""),
        );
        const electronsBlockMatch = file.match(electornsBlockRegex);

        if (!electronsBlockMatch) return;
        expect(electronsBlockMatch.length).to.be.eql(1);
        expect(electronsBlockMatch[0]).to.be.eql(`&ELECTRONS
    diagonalization = 'david'
    diago_david_ndim = 4
    diago_full_acc = .true.
    mixing_beta = 0.3
    startingwfc = 'atomic+random'
/`);
    });

    it("should parse values from CONTROL block", () => {
        const controlBlockRegex = new RegExp(
            espressoNamelistRegex.regex.replace(
                "{{BLOCK_NAME}}",
                espressoNamelistRegex.params.BLOCK_NAME[0],
            ),
            espressoNamelistRegex.flags.join(""),
        );
        const controlBlockMatch = file.match(controlBlockRegex);

        if (!controlBlockMatch) return;
        const controlBlock = controlBlockMatch[0];
        const regexObject = pointer.get(
            schemas,
            "/applications/espresso/5.2.1/pw.x/control/calculation",
        );
        const regexCalculation = new RegExp(
            "calculation\\s*=\\s*'([^']+)'",
            regexObject.flags.join(""),
        );

        const calculation = controlBlock.matchAll(regexCalculation);
        const [calcluationLine, calculationValue] = Array.from(calculation)[0];

        expect(calcluationLine).to.be.eql("calculation = 'scf'");
        expect(calculationValue).to.be.eql("scf");
    });
});
