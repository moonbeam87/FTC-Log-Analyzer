import dash_html_components as html
import dash_core_components as dcc
#By Dev Patel from FTC Team Robot Uprising 14607


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
                                 
            html.Div(
                [
                    html.A(
                        html.Button("GitHub", id="learn-more-button"),
                        href="https://github.com/moonbeam87/FTC-Log-Analyzer",
                    ),
                ],
                className="row",
            ),
            html.Hr(),
            html.Div(
                [
                    html.Div(
                        [html.H5("FTC Log Analyzer")],
                        className="2 columns main-title",
                    ),
                    dcc.Upload(html.Button('Upload File')),
                    
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
            
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/ftc-log-analyzer/overview",
                className="tab first",
            ),
            #Sample code to add another page is below :)
##            dcc.Link(
##                "Sample Page 1",
##                href="/ftc-log-analyzer/sample-page-1",
##                className="tab",
##            ),
##            dcc.Link(
##                "Sample Page 2",
##                href="/ftc-log-analyzer/sample-page-2",
##                className="tab",
##            ),
            
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df): #This is a helpful method for two column .csv files provided by plot.ly
    #They really do a good job on documentation
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
