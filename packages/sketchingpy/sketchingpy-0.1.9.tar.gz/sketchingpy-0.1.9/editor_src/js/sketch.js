const PYSCRIPT_CONFIG = {
    "packages": ["/dist/sketchingpy-0.1.9-py3-none-any.whl"]
};

const CORE_SRC = "/third_party/core.js?v=0.0.2";


function getSketchName() {
    const paramsStr = window.location.search;
    const params = new URLSearchParams(paramsStr);
    return params.get("filename");
}


function buildConfigObj() {
    const filesObj = {};
    const filenames = Object.keys(localStorage);
    filenames.forEach((filename) => {
        filesObj["/" + filename] = filename;
    });
    return {
        "packages": PYSCRIPT_CONFIG["packages"],
        "files": filesObj
    };
}


function main() {
    const millis = Date.now();
    const sketchName = getSketchName();
    const configObj = buildConfigObj();

    const sketchLabelText = document.createTextNode(sketchName);
    document.getElementById("sketch-label").appendChild(sketchLabelText);

    let progress = 0;
    const progressBar = document.getElementById("sketch-load-progress");
    progressBar.value = 0;
    const incrementBar = () => {
        progressBar.value += 1;

        if (progressBar.value < 19) {
            setTimeout(incrementBar, 500);
        }
    };
    incrementBar();

    const pyscriptTag = document.createElement("script");
    pyscriptTag.src = CORE_SRC;
    document.getElementById("sketch-main").appendChild(pyscriptTag);

    const configTag = document.createElement("py-config");
    configTag.innerHTML = JSON.stringify(configObj);
    document.getElementById("sketch-main").appendChild(configTag);

    const sketchTag = document.createElement("script");
    sketchTag.type = "py";
    sketchTag.src = sketchName + "?v=" + millis;
    document.getElementById("sketch-main").appendChild(sketchTag);
}


main();
