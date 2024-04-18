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
    data=result_sorted, x="menu_item", y="total_revenue", hue="CATEGORY", dodge=False
)
plt.title("Top Grossing Products by Category")
plt.xlabel("Menu Item")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.legend(title="Category")
plt.show()`
    ],
    [
        'make a bar chart using @result_by_category that shows the proportion of orders cancelled my menu item',
        `# Calculate the proportion of cancelled orders for each menu item
result_with_category["cancel_proportion"] = result_with_category[
    "num_orders_cancelled"
] / (
    result_with_category["num_orders_cancelled"]
    + result_with_category["num_orders_completed"]
)

# Plot a bar chart using seaborn
plt.figure(figsize=(10, 8))
sns.barplot(
    data=result_with_category,
    x="cancel_proportion",
    y="menu_item",
    hue="CATEGORY",
    dodge=False,
)
plt.title("Proportion of Cancelled Orders by Menu Item and Category")
plt.xlabel("Cancellation Proportion")
plt.ylabel("Menu Item")
plt.legend(title="Category")
plt.show()`
    ],
    [
        'filter @dataframe for category "Sweets" and show a grouped bar plot showing completed orders by year split by menu item',
        `import pandas as pd
import plotly.express as px

# Filter the dataframe for category 'Sweets'
sweets_df = dataframe[dataframe["CATEGORY"] == "Sweets"]

# Group by ORDER_DATE and MENU_ITEM, and get the count of orders for completed orders
# Assuming 'ORDER_STATUS' column indicates if an order is completed or not
completed_orders = sweets_df[sweets_df["ORDER_STATUS"] == "completed"]
completed_orders["year"] = pd.to_datetime(completed_orders["ORDER_DATE"]).dt.year

grouped_sweets = (
    completed_orders.groupby(["year", "MENU_ITEM"])
    .size()
    .reset_index(name="order_counts")
)

plt.figure(figsize=(10, 6))
sns.barplot(data=grouped_sweets, x="year", y="order_counts", hue="MENU_ITEM")
plt.title("Completed Orders by Year and Menu Item")
plt.xlabel("Year")
plt.ylabel("Completed Orders")
plt.legend(title="Menu Item")
plt.show()`
    ],
    [
        'Make a forecast for monthly completed orders per category. Use @dataframe to first create a dataframe of monthly completed orders and then use the Prophet library to make a 12 month prediction. Put all data in a new dataframe',
        `from prophet import Prophet

# Assuming 'completed_orders' dataframe contains only completed orders
# First, we need to prepare the data for Prophet
completed_orders = dataframe[dataframe["ORDER_STATUS"] == "completed"]

completed_orders["month"] = (
    pd.to_datetime(dataframe["ORDERED_AT"]).dt.to_period("M").dt.to_timestamp()
)

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
//# sourceMappingURL=lib_index_js.5743f57e26d2fd0b793d.js.map