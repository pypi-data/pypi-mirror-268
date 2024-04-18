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
                    const buttonsContainer = document.createElement('div');
                    buttonsContainer.style.marginTop = '10px';
                    buttonsContainer.style.marginLeft = '70px';
                    buttonsContainer.style.display = 'flex';
                    buttonsContainer.style.flexDirection = 'row';
                    inputContainer.style.marginTop = '10px';
                    inputContainer.style.marginLeft = '70px';
                    inputContainer.style.display = 'flex';
                    inputContainer.style.flexDirection = 'column';
                    activeCell.node.appendChild(inputContainer);
                    activeCell.node.appendChild(buttonsContainer);
                    const inputField = document.createElement('textarea');
                    inputField.placeholder = 'Enter your text';
                    inputField.style.width = '100%';
                    inputField.style.height = '100px';
                    inputContainer.appendChild(inputField);
                    const submitButton = document.createElement('button');
                    submitButton.textContent = 'Submit';
                    submitButton.style.backgroundColor = 'lightblue';
                    submitButton.style.borderRadius = '5px';
                    submitButton.style.border = '1px solid darkblue';
                    submitButton.style.maxWidth = '100px';
                    submitButton.style.minHeight = '25px';
                    submitButton.style.marginTop = '10px';
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
                                try {
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
                                    acceptButton.style.backgroundColor = 'lightblue';
                                    acceptButton.style.borderRadius = '5px';
                                    acceptButton.style.border = '1px solid darkblue';
                                    acceptButton.style.maxWidth = '100px';
                                    acceptButton.style.minHeight = '25px';
                                    acceptButton.style.marginTop = '10px';
                                    acceptButton.style.marginRight = '10px';
                                    acceptButton.addEventListener('click', () => {
                                        activeCell.model.sharedModel.source = gen;
                                        commands.execute('notebook:run-cell');
                                        activeCell.node.removeChild(diffContainer);
                                        activeCell.node.removeChild(buttonsContainer);
                                    });
                                    buttonsContainer.appendChild(acceptButton);
                                    const rejectButton = document.createElement('button');
                                    rejectButton.textContent = 'Reject';
                                    rejectButton.style.backgroundColor = 'lightblue';
                                    rejectButton.style.borderRadius = '5px';
                                    rejectButton.style.border = '1px solid darkblue';
                                    rejectButton.style.maxWidth = '100px';
                                    rejectButton.style.minHeight = '25px';
                                    rejectButton.style.marginTop = '10px';
                                    rejectButton.style.marginRight = '10px';
                                    rejectButton.addEventListener('click', () => {
                                        activeCell.node.removeChild(diffContainer);
                                        activeCell.node.removeChild(buttonsContainer);
                                        activeCell.model.sharedModel.source = oldCode;
                                    });
                                    buttonsContainer.appendChild(rejectButton);
                                    const editPromptButton = document.createElement('button');
                                    editPromptButton.textContent = 'Edit Prompt';
                                    editPromptButton.style.backgroundColor = 'lightblue';
                                    editPromptButton.style.borderRadius = '5px';
                                    editPromptButton.style.border = '1px solid darkblue';
                                    editPromptButton.style.maxWidth = '100px';
                                    editPromptButton.style.minHeight = '25px';
                                    editPromptButton.style.marginTop = '10px';
                                    editPromptButton.style.marginRight = '10px';
                                    editPromptButton.addEventListener('click', () => {
                                        activeCell.node.removeChild(diffContainer);
                                        activeCell.node.removeChild(buttonsContainer);
                                        activeCell.node.appendChild(inputContainer);
                                        inputContainer.appendChild(inputField);
                                        inputContainer.appendChild(submitButton);
                                    });
                                    buttonsContainer.appendChild(editPromptButton);
                                    // Handle Enter key press to trigger accept on accept/reject buttons
                                    buttonsContainer.addEventListener('keydown', event => {
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
                                    buttonsContainer.addEventListener('keydown', event => {
                                        if (event.key === 'Escape') {
                                            event.preventDefault();
                                            rejectButton.click();
                                        }
                                    });
                                }
                                catch (error) {
                                    console.log('Error rendering editor:', error);
                                }
                            };
                            const isLocalhost = window.location.hostname === 'localhost';
                            const options = {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: isLocalhost
                                    ? JSON.stringify({
                                        model: 'gpt-4-turbo-preview',
                                        messages: [
                                            {
                                                role: 'user',
                                                content: `Write python code to do \n"""\n${userInput}\n"""\nThe previous code is\n"""\n${oldCode}\n"""\nReturn ONLY executable python code, no backticks`
                                            }
                                        ]
                                    })
                                    : JSON.stringify({
                                        oldCode,
                                        userInput
                                    })
                            };
                            if (isLocalhost) {
                                options.headers.Authorization =
                                    'Bearer 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';
                            }
                            fetch(isLocalhost
                                ? 'https://api.openai.com/v1/chat/completions'
                                : 'https://q8qeei2tn4.execute-api.us-west-1.amazonaws.com/default/pretzel_notebook', options)
                                .then(response => response.json())
                                .then(data => {
                                const gen = isLocalhost
                                    ? data.choices[0].message.content
                                    : data.message;
                                renderEditor(gen);
                            })
                                .catch(error => {
                                activeCell.model.sharedModel.source = `# Error: ${error}\n${oldCode}`;
                                activeCell.node.removeChild(diffContainer);
                                activeCell.node.removeChild(inputContainer);
                            });
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
//# sourceMappingURL=lib_index_js.e79e5a4470bffae4b2de.js.map