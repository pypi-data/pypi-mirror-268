const EDITABLE_FILE_TYPES = [
    ".py",
    ".pyscript",
    ".txt",
    ".json",
    ".geojson",
    ".csv"
];

const PROJ_CONFIRM_MSG = [
    "Opening this project will cause your current project to be deleted from your browser.",
    "Be sure to export your current project before continuing.",
    "Do you want to continue?"
].join(" ");

const UPGRADE_MESSAGE = [
    "Project from the old editor found.",
    "Do you want to save it?",
    "Otherwise it will be deleted."
].join(" ");

const FAIL_START_MSG = [
    "The editor could not start.",
    "Maybe your browser is incompatible.",
    "Try updating!"
].join(" ");

const localRequestChannel = new BroadcastChannel("localRequests");
const localResponseChannel = new BroadcastChannel("localResponses");


function getIsEditable(name) {
    const editableExtension = EDITABLE_FILE_TYPES.filter((x) => name.endsWith(x));
    return editableExtension.length != 0;
}


class OpfsFileManager {

    constructor() {
        const self = this;
        self._fileLocks = {}
    }
    
    clearProject() {
        const self = this;
        
        const directoryFuture = navigator.storage.getDirectory();
        return directoryFuture.then((directory) => {
            return directory.remove({recursive: true});
        });
    }
    
    loadProject(contents) {
        const self = this;
        
        const names = Object.keys(contents);
        const futures = names.map((name) => {
            const content = contents[name];
            return self.updateItem(name, content);
        });
        return Promise.all(futures);
    }

    serializeProject() {
        const self = this;

        return self.getItemNames()
            .then((itemNames) => {
                return itemNames.map((name) => {
                    return self.getItem(name).then((content) => {
                        return {"name": name, "content": content};
                    });
                });
            })
            .then((contentFutures) => {
                return Promise.all(contentFutures);
            })
            .then((contents) => {
                const outputObj = {};
                contents.forEach((item) => {
                    outputObj[item["name"]] = item["content"];
                });
                return outputObj;
            })
            .then((outputObj) => {
                return JSON.stringify(outputObj);
            });
    }
    
    getItemNames() {
        const self = this;
        
        const directoryFuture = navigator.storage.getDirectory();
        return directoryFuture.then((directory) => {
            return Array.fromAsync(directory.keys());
            return names;
        });
    }
    
    getItem(filename) {
        const self = this;
        
        return self._aquireLock(filename)
            .then(() => navigator.storage.getDirectory())
            .then((directory) => directory.getFileHandle(filename))
            .then((fileHandle) => fileHandle.getFile())
            .then((file) => file.text())
            .then((text) => {
                return self._releaseLock(filename).then(() => text);
            });
    }
    
    updateItem(filename, contents) {
        const self = this;
        
        return self._aquireLock(filename)
            .then(() => navigator.storage.getDirectory())
            .then((directory) => directory.getFileHandle(filename, {create: true}))
            .then((fileHandle) => fileHandle.createWritable())
            .then((writable) => {
                return writable.write(contents).then(() => writable);
            })
            .then((stream) => stream.close())
            .then(() => self._releaseLock(filename));
    }
    
    getMbUsed() {
        const self = this;
        
        return self.getItemNames()
            .then((itemNames) => {
                const itemContentFutures = itemNames.map((itemName) => self.getItem(itemName));
                return Promise.all(itemContentFutures);
            })
            .then((contents) => {
                const totalSize = contents.map((x) => x.length).reduce((a, b) => a + b, 0);
                const totalKb = totalSize / 1024;
                const totalMb = totalKb / 1024;
                return totalMb;
            });
    }
    
    createItem(filename) {
        const self = this;
        
        return self._aquireLock(filename)
            .then(() => navigator.storage.getDirectory())
            .then((directory) => directory.getFileHandle(filename, {create: true}))
            .then(() => self._releaseLock(filename));
    }

    removeItem(filename) {
        const self = this;

        return self._aquireLock(filename)
            .then(() => navigator.storage.getDirectory())
            .then((directory) => {
                return directory.removeEntry(filename);
            })
            .then(() => self._releaseLock(filename));
    }

    _aquireLock(filename) {
        const self = this;
        if (self._fileLocks[filename] !== undefined) {
            const promise = self._fileLocks[filename]["promise"];
            if (promise === null) {
                return new Promise((resolve) => {
                    setTimeout(() => {
                        self._aquireLock(filename).then(resolve);
                    }, 100);
                });
            } else {
                return promise.then(() => {
                    return self._aquireLock(filename);
                });
            }
        }

        self._fileLocks[filename] = {
            "promise": null,
            "release": null
        };
        const promise = new Promise((resolve) => {
            self._fileLocks[filename]["release"] = resolve;
        });
        self._fileLocks[filename]["promise"] = promise;
        return new Promise((resolve) => resolve());
    }

    _releaseLock(filename) {
        const self = this;
        if (self._fileLocks[filename] === undefined) {
            return;
        }

        const lock = self._fileLocks[filename];
        self._fileLocks[filename] = undefined;
        
        const release = lock["release"];
        if (release === null) {
            return new Promise((resolve) => {
                setTimeout(() => {
                    self._releaseLock(filename).then(resolve);
                }, 100);
            });
        } else {
            return new Promise((resolve) => {
                release();
                resolve();
            });
        }
    }
    
}


class LocalStorageFileManager {
    
    clearProject() {
        const self = this;
        
        return new Promise((resolve) => {
            for (const [filename, content] of Object.entries(localStorage)) {
                localStorage.removeItem(filename);
            } 
        });
    }
    
    loadProject(contents) {
        const self = this;
        
        return new Promise((resolve) => {
            for (const [filename, content] of Object.entries(contents)) {
                self.updateFile(filename, content);
            }
            resolve(); 
        });
    }

    serializeProject() {
        const self = this;

        return new Promise((resolve) => {
            resolve(JSON.stringify(localStorage));
        });
    }
    
    getItemNames() {
        const self = this;
        
        return new Promise((resolve) => {
            resolve(Object.keys(localStorage));
        });
    }
    
    getItem(name) {
        const self = this;
        
        return new Promise((resolve) => {
            resolve(localStorage[name]);
        });
    }
    
    updateItem(name, contents) {
        const self = this;
        
        return new Promise((resolve) => {
            localStorage.setItem(filename, contents);
            resolve();
        })
    }
    
    getMbUsed() {
        const self = this;
        
        return self.getItemNames()
            .then((itemNames) => {
                const itemContentFutures = itemNames.map((itemName) => self.getItem(itemName));
                return Promise.all(itemContentFutures);
            })
            .then((contents) => {
                const totalSize = contents.map((x) => x.length).reduce((a, b) => a + b, 0);
                const totalKb = totalSize / 1024;
                const totalMb = totalKb / 1024;
                return totalMb;
            });
    }
    
    createItem(filename) {
        const self = this;
        
        return new Promise((resolve) => {
            if (localStorage.getItem(filename) === null) {
                localStorage.setItem(filename, "");
            }
            resolve();
        });
    }

    removeItem(filename) {
        const self = this;

        if (self._removePause) {
            self._removesWaiting.push(filename);
        } else {
            return new Promise((resolve) => {
                localStorage.removeItem(filename);
                resolve();
            });
        }
    }
    
}


class FilesListPresenter {

    constructor(rootDiv, sketchbookPresenter) {
        const self = this;

        self._rootDiv = rootDiv;
        self._sketchbookPresenter = sketchbookPresenter;
        self._selected = null;
    }

    setItems(newItems) {
        const self = this;

        newItems.sort();

        const sourceList = self._rootDiv.querySelector(".selection-list");
        sourceList.innerHTML = "";

        const newDivs = newItems.map((name) => {
            const newDiv = document.createElement("div");
            newDiv.classList.add("item");

            const newLink = document.createElement("a");
            newLink.href = "#" + name;
            newLink.classList.add("file-link");
            const newContent = document.createTextNode(name);
            newLink.appendChild(newContent);

            const delLink = document.createElement("a");
            delLink.href = "#" + name + "-delete";
            delLink.innerHTML = "delete";
            delLink.classList.add("del-link");

            newDiv.appendChild(newLink);
            newDiv.appendChild(delLink);

            const openFile = (event) => {
                event.preventDefault();
                event.stopPropagation();
                self._sketchbookPresenter.setFileOpen(name);
            };
            newLink.addEventListener("click", openFile);
            newDiv.addEventListener("click", openFile);

            delLink.addEventListener("click", (event) => {
                event.preventDefault();
                event.stopPropagation();
                self._sketchbookPresenter.deleteFile(name);
            });

            return newDiv;
        });

        newDivs.forEach((newDiv) => sourceList.appendChild(newDiv));

        self.setSelected(self.getSelected());
    }

    setSelected(newItem) {
        const self = this;

        const options = Array.of(...self._rootDiv.querySelectorAll(".item"));

        options.forEach((option) => {
            option.classList.remove("selected");
            option.ariaSelected = false;
        });

        if (newItem === null) {
            self._selected = null;
            return;
        }

        
        const isEditable = getIsEditable(newItem);
        if (!isEditable) {
            window.open("/" + newItem, '_blank');
            self._selected = null;
            return;
        }

        const matching = options.filter(
            (x) => x.querySelector(".file-link").innerHTML === newItem
        );
        if (matching.length == 0) {
            return;
        }

        matching[0].classList.add("selected");
        matching[0].ariaSelected = true;

        self._selected = newItem;
    }

    getSelected(newItem) {
        const self = this;
        return self._selected;
    }

}


class EditorPresenter {

    constructor(rootDiv, sketchbookPresenter) {
        const self = this;
        self._rootDiv = rootDiv;
        self._sketchbookPresenter = sketchbookPresenter;
        self._editor = ace.edit(rootDiv.id);
        self._editor.setOption("enableKeyboardAccessibility", true);
        self._editor.getSession().setMode("ace/mode/python");
        self._selected = null;

        setInterval(() => {
            self.save();
        }, 5000);
    }

    setContents(filename, content) {
        const self = this;
        self._editor.setValue(content);
        self._editor.clearSelection();
        self._selected = filename;
        document.getElementById("editor-holder").style.display = "block";
    }

    hide() {
        const self = this;
        document.getElementById("editor-holder").style.display = "none";
        self._selected = null;
    }

    save() {
        const self = this;
        
        if (self._selected === null) {
            return;
        }
        
        self._sketchbookPresenter.updateFile(self._selected, self._editor.getValue());
    }

}


class SketchbookPresenter {

    constructor() {
        const self = this;

        self._sourcesList = new FilesListPresenter(document.getElementById("sources"), self);
        self._assetsList = new FilesListPresenter(document.getElementById("assets"), self);
        self._editor = new EditorPresenter(document.getElementById("editor"), self);
        self._fileManager = new OpfsFileManager();

        const runButton = document.getElementById("run-button");
        runButton.addEventListener("click", (event) => {
            event.preventDefault();
            self._editor.save();
            setTimeout(() => {
                window.open(runButton.href, '_blank').focus();
            }, 100);
        });

        document.getElementById("new-button").addEventListener("click", (event) => {
            event.preventDefault();
            const newName = prompt("New filename:");
            const newNameProper = newName.endsWith(".py") ? newName : newName + ".py";
            self.addNewFile(newNameProper);
        });

        const hiddenFileInput = document.getElementById("hidden-file-chooser");

        document.getElementById("upload-button").addEventListener("click", (event) => {
            event.preventDefault();
            hiddenFileInput.click();
        });

        document.getElementById("import-button").addEventListener("click", (event) => {
            event.preventDefault();
            hiddenFileInput.click();
        });

        hiddenFileInput.addEventListener("change", (event) => {
            event.preventDefault();
            const file = hiddenFileInput.files[0];
            const filename = file.name;

            const isEditable = getIsEditable(filename);

            if (filename.endsWith(".skprj")) {
                if (!confirm(PROJ_CONFIRM_MSG)) {
                    return;
                }

                file.text().then((contentsStr) => {
                    const contents = JSON.parse(contentsStr);

                    self._fileManager.clearProject()
                        .then(() => self._fileManager.loadProject(contents))
                        .then(() => self.refreshFilesList());
                });

                return;
            } else if (isEditable) {
                file.text().then((contents) => {
                    self.updateFileAndRefresh(filename, contents);
                });
            } else {
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.addEventListener("load", () => {
                    const contents = reader.result;
                    self.updateFileAndRefresh(filename, contents);
                });
            }
        });

        document.getElementById("export-button").addEventListener("click", (event) => {
            self.exportProject();
        });

        self.refreshFilesList();
        self.setFileOpen(null);
    }

    refreshFilesList() {
        const self = this;

        const updateListsFuture = self._fileManager.getItemNames().then((itemNames) => {
            const sources = itemNames.filter((x) => x.endsWith(".py"));
            self._sourcesList.setItems(sources);

            const assets = itemNames.filter((x) => !x.endsWith(".py"));
            self._assetsList.setItems(assets);
        });
        
        const updateStorageUsed = self._fileManager.getMbUsed().then((totalMb) => {
            document.getElementById("current-usage").innerHTML = Math.round(totalMb * 10) / 10;
            document.getElementById("storage-bar").value = totalMb;
        });

        return Promise.all([updateListsFuture, updateStorageUsed]);
    }

    addNewFile(filename) {
        const self = this;

        return self._fileManager.createItem(filename).then(() => {
            self.refreshFilesList();
            self.setFileOpen(filename);
        });
    }

    setFileOpen(filename) {
        const self = this;

        self._editor.save();

        const updateEditor = () => {
            return new Promise((resolve) => {
                if (filename === null || !getIsEditable(filename)) {
                    self._editor.hide();
                    resolve();
                } else {
                    self._fileManager.getItem(filename).then((contents) => {
                        const runButton = document.getElementById("run-button");
                        runButton.href = "/sketch.html?filename=" + filename;
                        self._editor.setContents(filename, contents);
                        resolve();
                    });
                }
            })
        };

        const updateLists = () => {
            new Promise((resolve) => {
                self._sourcesList.setSelected(filename);
                self._assetsList.setSelected(filename);
                resolve();
            });
        };

        return updateEditor().then(updateLists);
    }

    updateFile(filename, contents) {
        const self = this;
        return self._fileManager.updateItem(filename, contents);
    }

    updateFileAndRefresh(filename, contents) {
        const self = this;
        self.updateFile(filename, contents).then(() => self.refreshFilesList());
    }

    deleteFile(filename) {
        const self = this;

        const updateFileSelected = () => {
            return new Promise((resolve) => {
                if (filename === self._sourcesList.getSelected()) {
                    self._sourcesList.setSelected(null);
                    self.setFileOpen(null).then(() => resolve());
                } else {
                    resolve();
                }
            });
        };
        
        const removeFile = () => {
            return new Promise((resolve) => {
                if (!confirm("Are you sure you want to remove this file?")) {
                    resolve();
                } else {
                    self._fileManager.removeItem(filename)
                        .then(() => {
                            return self.refreshFilesList();
                        })
                        .then(() => resolve());
                }
            })
            
        };

        return updateFileSelected().then(removeFile);
    }

    exportProject() {
        const self = this;

        const makeDownload = (newString) => {
            const newUrl = URL.createObjectURL(new Blob([newString]));

            const downloadLink = document.createElement("a");
            downloadLink.href = newUrl;
            downloadLink.download = "project.skprj";
            downloadLink.click();
        };

        return self._fileManager.serializeProject().then(makeDownload);
    }

}


function checkMigration() {
    const sourceFilesystem = new LocalStorageFileManager();
    sourceFilesystem.getItemNames().then((itemNames) => {
        console.log(itemNames);
        if (itemNames.length == 0) {
            return;
        }
        
        if (confirm(UPGRADE_MESSAGE)) {
            const makeDownload = (newString) => {
                const newUrl = URL.createObjectURL(new Blob([newString]));

                const downloadLink = document.createElement("a");
                downloadLink.href = newUrl;
                downloadLink.download = "oldProject.skprj";
                downloadLink.click();
            };

            return sourceFilesystem.serializeProject().then(makeDownload);
        }

        sourceFilesystem.clearProject();
    })
}


function main() {
    const sketchbook = new SketchbookPresenter();

    // Thanks MDN (CC0)
    // https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides
    try {
        navigator.serviceWorker.register("/service_worker.js", {
            scope: "/",
        }).then((registration) => {
            if (registration.installing) {
                console.log("Service worker installing");
            } else if (registration.waiting) {
                console.log("Service worker installed");
            } else if (registration.active) {
                console.log("Service worker active");
            }
        });
    } catch (error) {
        alert(FAIL_START_MSG)
        console.log(error);
    }

    checkMigration();
}



localRequestChannel.addEventListener("message", (event) => {
    const name = event.data.name;

    const makeResponse = () => {
        const filename = name.substring(1, name.length);
        
        const fileManager = new OpfsFileManager();
        return fileManager.getItem(filename).then((content) => {
            if (content === null) {
                return new Promise((resolve) => resolve(null));
            } else if (getIsEditable(name)) {
                return new Promise((resolve) => resolve(new Blob([content])));
            } else {
                return fetch(content).then(x => x.blob());
            }
        });
    };
    
    makeResponse().then((content) => {
        localResponseChannel.postMessage({
            "name": name,
            "content": content
        });
    });
});


main();
