"use strict";
(self["webpackChunkpretzelai"] = self["webpackChunkpretzelai"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var monaco_editor__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! monaco-editor */ "webpack/sharing/consume/default/monaco-editor/monaco-editor");
/* harmony import */ var monaco_editor__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(monaco_editor__WEBPACK_IMPORTED_MODULE_2__);



const keywordMap = new Map();
keywordMap.set('hello', 'Hello, how are you?');
keywordMap.set('goodbye', 'Goodbye, have a nice day.');
const PLUGIN_ID = 'cell-code-replacer:plugin';
const extension = {
    id: PLUGIN_ID,
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker],
    activate: (app, palette, notebookTracker) => {
        const { commands } = app;
        const command = 'cell-code-replacer:replace-code';
        commands.addCommand(command, {
            label: 'Replace Cell Code',
            execute: () => {
                const activeCell = notebookTracker.activeCell;
                if (activeCell) {
                    const oldCode = activeCell.model.sharedModel.source;
                    // Create an input field and append it below the cell
                    const inputContainer = document.createElement('div');
                    inputContainer.style.marginTop = '10px';
                    inputContainer.style.marginLeft = '70px';
                    activeCell.node.appendChild(inputContainer);
                    const inputField = document.createElement('input');
                    inputField.type = 'text';
                    inputField.placeholder = 'Enter your text';
                    inputField.style.width = '50%';
                    inputContainer.appendChild(inputField);
                    const submitButton = document.createElement('button');
                    submitButton.textContent = 'Submit';
                    inputContainer.appendChild(submitButton);
                    inputField.focus();
                    const handleAccept = () => {
                        const userInput = inputField.value;
                        if (userInput !== '') {
                            const diffContainer = document.createElement('div');
                            diffContainer.style.marginTop = '10px';
                            diffContainer.style.height = '200px';
                            activeCell.node.appendChild(diffContainer);
                            // Remove input field and submit button
                            inputContainer.removeChild(inputField);
                            inputContainer.removeChild(submitButton);
                            // Show "Thinking ..." message
                            const thinkingMessage = document.createElement('div');
                            thinkingMessage.textContent = 'Thinking ...';
                            inputContainer.appendChild(thinkingMessage);
                            const renderEditor = (gen) => {
                                const diffEditor = monaco_editor__WEBPACK_IMPORTED_MODULE_2__.editor.createDiffEditor(diffContainer, {
                                    readOnly: true,
                                    theme: 'vs-dark'
                                });
                                diffEditor.setModel({
                                    original: monaco_editor__WEBPACK_IMPORTED_MODULE_2__.editor.createModel(oldCode, 'python'),
                                    modified: monaco_editor__WEBPACK_IMPORTED_MODULE_2__.editor.createModel(gen, 'python')
                                });
                                // Remove "Thinking ..." message
                                inputContainer.removeChild(thinkingMessage);
                                // Create "Accept" and "Reject" buttons
                                const acceptButton = document.createElement('button');
                                acceptButton.textContent = 'Accept';
                                acceptButton.addEventListener('click', () => {
                                    activeCell.model.sharedModel.source = gen;
                                    commands.execute('notebook:run-cell');
                                    activeCell.node.removeChild(diffContainer);
                                    activeCell.node.removeChild(inputContainer);
                                });
                                inputContainer.appendChild(acceptButton);
                                const rejectButton = document.createElement('button');
                                rejectButton.textContent = 'Reject';
                                rejectButton.addEventListener('click', () => {
                                    activeCell.node.removeChild(diffContainer);
                                    activeCell.node.removeChild(inputContainer);
                                });
                                inputContainer.appendChild(rejectButton);
                                // Handle Enter key press to trigger accept on accept/reject buttons
                                inputContainer.addEventListener('keydown', event => {
                                    if (event.key === 'Enter') {
                                        event.preventDefault();
                                        const activeElement = document.activeElement;
                                        if (activeElement === acceptButton) {
                                            acceptButton.click();
                                        }
                                        else if (activeElement === rejectButton) {
                                            rejectButton.click();
                                        }
                                    }
                                });
                                // Handle Escape key press to trigger reject on accept/reject buttons
                                inputContainer.addEventListener('keydown', event => {
                                    if (event.key === 'Escape') {
                                        event.preventDefault();
                                        rejectButton.click();
                                    }
                                });
                            };
                            for (const keyword in keywordMap) {
                                if (userInput.includes(keyword)) {
                                    renderEditor(keywordMap.get(keyword));
                                    break;
                                }
                            }
                        }
                    };
                    // Handle Enter key press to trigger submit
                    inputField.addEventListener('keydown', event => {
                        if (event.key === 'Enter') {
                            event.preventDefault();
                            handleAccept();
                        }
                    });
                    // Handle submit button click to trigger accept
                    submitButton.addEventListener('click', handleAccept);
                }
            }
        });
        const category = 'Cell Operations';
        palette.addItem({ command, category });
        app.commands.addKeyBinding({
            command,
            keys: ['Accel K'],
            selector: '.jp-Notebook'
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.44593dcd89ccf7ce13d2.js.map