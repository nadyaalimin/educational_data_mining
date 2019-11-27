# The Web App

The web applicaion is built using [dash](https://dash.plot.ly). 

## Codebase structure

The heart of the web application is on `main.py`. Other components live insite the `app` directory, containing three main python files:

| File            | Description                                |
| --------------- | ------------------------------------------ |
| `components.py` | UI components                              |
| `layout.py`     | Contains the main layout for the whole app |
| `callbacks.py`  | Dash callbacks                             |

### `main.py`

### `components.py`

### `layout.py`

Here is the snippet of the UI. The `Root()` function returns main layout of the web app.

```python
def Root():
    element = dbc.Container([
        Header.render(),
        InputContainer.render(),
        html.Hr(),
        RecommendationContainer.render(),
    ], className="pb-5 mb-5")
    return element
```


### `callbacks.py`

Below is an illustration of the full callback graph:

![callback](
