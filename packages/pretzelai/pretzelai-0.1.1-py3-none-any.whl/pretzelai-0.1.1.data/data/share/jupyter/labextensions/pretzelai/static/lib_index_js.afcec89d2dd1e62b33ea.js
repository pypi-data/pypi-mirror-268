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



let index = 0;
const keywordMap = new Map([
    [
        'in @dataframe, for each menu item, I want to get the cancelled and completed order count and total price',
        `# Group the dataframe by 'MENU_ITEM' and 'ORDER_STATUS', then count and sum 'ORDER_ID' and 'PRICE'
result = dataframe.groupby(["MENU_ITEM", "ORDER_STATUS"]).agg(
    ORDER_ID_count=("ORDER_ID", "count"), PRICE_sum=("PRICE", "sum")
)

# Reset index to turn the grouped columns back into regular columns
result = result.reset_index()

# Pivot the table to have 'MENU_ITEM' as index and the counts and sums as columns
result = result.pivot_table(
    index="MENU_ITEM",
    columns="ORDER_STATUS",
    values=["ORDER_ID_count", "PRICE_sum"],
    fill_value=0,
)

# Flatten the MultiIndex in columns
result.columns = [f"{col[1]}_{col[0]}" for col in result.columns]

# Reset index to turn 'MENU_ITEM' back into a column
result = result.reset_index()`
    ],
    [
        'Rename columns in @result to have clearer column names - for eg, num_orders_cancelled',
        `result.columns = [
    "menu_item",
    "num_orders_cancelled",
    "num_orders_completed",
    "cancelled_price_sum",
    "completed_price_sum",
]`
    ],
    [
        'plot the top grossing menu items from @result',
        `import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the total revenue for each menu item
result["total_revenue"] = (
    result["cancelled_price_sum"]
    + result["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
    how="left",
).drop(columns=["MENU_ITEM"])

# Calculate the total revenue for each menu item
result_with_category["total_revenue"] = (
    result_with_category["cancelled_price_sum"]
    + result_with_category["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result_with_category.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
).drop(columns=["MENU_ITEM"])

# Calculate the total revenue for each menu item
result_with_category["total_revenue"] = (
    result_with_category["cancelled_price_sum"]
    + result_with_category["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result_with_category.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
).drop(columns=["MENU_ITEM"])

# Calculate the total revenue for each menu item
result_with_category["total_revenue"] = (
    result_with_category["cancelled_price_sum"]
    + result_with_category["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result_with_category.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
).drop(columns=["MENU_ITEM"])

# Calculate the total revenue for each menu item
result_with_category["total_revenue"] = (
    result_with_category["cancelled_price_sum"]
    + result_with_category["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result_with_category.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
).drop(columns=["MENU_ITEM"])

# Calculate the total revenue for each menu item
result_with_category["total_revenue"] = (
    result_with_category["cancelled_price_sum"]
    + result_with_category["completed_price_sum"]
)

# Sort the result_with_category dataframe by total revenue in descending order
result_sorted = result_with_category.sort_values(by="total_revenue", ascending=False)

# Plot the top grossing products using a bar chart with colors based on category
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_sorted, x="menu_item", y="total_revenue", dodge=False
)
plt.title("Top Grossing Products")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()`
    ],
    [
        'Join @result with @dataframe to get the category for each menu item. Then, color the bars using teh category information',
        `result_with_category = result.merge(
    dataframe[["MENU_ITEM", "CATEGORY"]].drop_duplicates(),
    left_on="menu_item",
    right_on="MENU_ITEM",
).drop(columns=["MENU_ITEM"])

# Group by month and category, then count the completed orders
monthly_completed_orders = (
    completed_orders.groupby(["month", "CATEGORY"])
    .size()
    .reset_index(name="order_count")
)

# Initialize an empty dataframe to store all forecasts
all_forecasts = pd.DataFrame()

# Forecasting with Prophet for each category
for category in monthly_completed_orders["CATEGORY"].unique():
    # Prepare the dataframe for Prophet
    df = monthly_completed_orders[monthly_completed_orders["CATEGORY"] == category][
        ["month", "order_count"]
    ]
    df.columns = ["ds", "y"]  # Prophet requires the columns to be named 'ds' and 'y'

    # Create and fit the model
    model = Prophet()
    model.fit(df)

    # Create future dataframe for 12 months
    future = model.make_future_dataframe(periods=12, freq="M")

    # Predict
    forecast = model.predict(future)

    # Add the category to the forecast
    forecast["category"] = category

    # Select only the necessary columns
    forecast = forecast[["ds", "yhat", "yhat_lower", "yhat_upper", "category"]]

    # Rename 'ds' to 'month'
    forecast.rename(columns={"ds": "month"}, inplace=True)

    # Append to the all_forecasts dataframe
    all_forecasts = pd.concat([all_forecasts, forecast], ignore_index=True)

# all_forecasts dataframe now contains all the forecasts for each category with the specified columns`
    ],
    [
        'Use @all_forecasts to create a stacked bar plot of completed orders by month split by category. use plotly',
        `fig = px.bar(
  all_forecasts,
  x="month",
  y="yhat",
  color="category",
  title="Forecasts by Category",
  labels={"yhat": "Forecast"},
)
fig.update_layout(barmode="stack")
fig.show()`
    ],
    [
        'This chart looks very ugly. Use a cleaner theme like plotly_white, use Arial font and make the plot taller',
        `import plotly.express as px

# Assuming 'all_forecasts' is your DataFrame
fig = px.bar(
    all_forecasts,
    x="month",
    y="yhat",
    color="category",
    title="Forecasts by Category",
    labels={"yhat": "Forecast"},
    height=600,  # Making the chart taller
    template='plotly_white',  # Using a cleaner theme
    color_discrete_sequence=px.colors.qualitative.Plotly  # Using a vibrant color palette
)

# Update layout to enhance font and other aesthetics
fig.update_layout(
    barmode="stack",
    font=dict(
        family="Arial, sans-serif",  # Setting a commonly used, appealing font
        size=12,
        color="black"
    ),
    title=dict(
        font=dict(
            family="Arial, sans-serif",  # Consistent font for the title
            size=18,
            color="black"
        )
    )
)

# Show the figure
fig.show()`
    ]
]);
const PLUGIN_ID = 'cell-code-replacer:plugin';
const extension = {
    id: PLUGIN_ID,
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ICommandPalette, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker],
    activate: (app, palette, notebookTracker) => {
        const { commands } = app;
        const command = 'cell-code-replacer:replace-code';
        const command2 = 'cell-code-replacer:paste-text';
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
                            };
                            let isMapMatch = false;
                            for (const keyword of keywordMap.keys()) {
                                if (userInput.includes(keyword)) {
                                    renderEditor(keywordMap.get(keyword));
                                    isMapMatch = true;
                                    break;
                                }
                            }
                            if (!isMapMatch) {
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
        commands.addCommand(command2, {
            label: 'Paste Text',
            execute: () => {
                navigator.clipboard.writeText(Array.from(keywordMap.keys())[index]);
                index++;
            }
        });
        const category = 'Cell Operations';
        palette.addItem({ command, category });
        palette.addItem({ command: command2, category });
        app.commands.addKeyBinding({
            command,
            keys: ['Accel K'],
            selector: '.jp-Notebook'
        });
        app.commands.addKeyBinding({
            command: command2,
            keys: ['Accel X'],
            selector: '.jp-Notebook'
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (extension);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.afcec89d2dd1e62b33ea.js.map