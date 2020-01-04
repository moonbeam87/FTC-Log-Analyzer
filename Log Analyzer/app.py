# -*- coding: utf-8 -*-
#By Dev Patel from FTC Team Robot Uprising 14607

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    #Code for Sample Pages are required, would need a ".py" file similar to "overview.py"
##    if pathname == "/ftc-log-analyzer/sample-page-1":
##        return sample-page-1.create_layout(app)
##    elif pathname == "/ftc-log-analyzer/sample-page-2":
##        return sample-page-2.create_layout(app)
##    else:
    return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
