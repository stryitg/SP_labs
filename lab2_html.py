from spyre import server

import pandas 

class Tables(server.App):
    title = "VHI index"
    
    inputs = [{ "type" : 'dropdown',
                "label" : 'index',
                "options" : [{"label": 'VHI', "value": 'VHI'},
                            {"label" : 'SMN', "value": 'SMN'},
                            {"label" : 'SNT', "value": 'SNT'}],
                "key" : 'index',
                "action_id" : "update_data"},

                { "type" : 'dropdown',
                "label" : 'color',
                "options" : [{"label": 'DarkGreen', "value": 'DarkGreen'},
                            {"label" : 'DarkBlue', "value": 'DarkBlue'},],
                "key" : 'color',
                "action_id" : "update_data"},


              { "type" : 'dropdown',
                "label" : 'region',
                "options" : [{"label": 'Kyiv', "value": '1KYV'},
                            {"label" : 'Lviv', "value": '2LV'},
                            {"label" : 'Odesa', "value": '3ODS'}],
                "key" : 'region',
                "action_id" : "update_data"},

              ###{ "type":'text',
              #  "label": 'year(from 1990-2010)',
              #  "value" : '2000',
              #  "key": 'year',
              #  "action_id" : "update_data"},'''

              { "type":'text',
                "label": 'first weak(from 1-40)',
                "value" : '1',
                "key": 'weak1',
                "action_id" : "update_data"},
                                        
              { "type":'text',
                "label": 'last weak(from 1-40)',
                "value" : '40',
                "key": 'weak2',
                "action_id" : "update_data",},

              { "type": 'slider',
                "label":'year',
                "key":"year" ,
                "min": "1990",
                "max": "2010",
                "action_id": "update_data"}]

    controls = [{   "type" : "hidden",
                    "id" : "update_data"}]

    tabs = ["Plot"]

    outputs = [{"type": "plot",
                "id": "plot",
                "tab": "Plot",
                "control_id": 'update_data'}]        


    def getData(self, params):
        region = params['region']
        print(region[0])
        path = "vhi_id_"+region[0]+"_2017-02-26.csv"
        df = pandas.read_csv(path,index_col=False,header=0)
        return df

    def getPlot(self, params):
        df = self.getData(params)
        df = df[df['year'] == int(params['year'])]
        df = df[(df['weak'] <= int(params['weak2']))&(df['weak'] >= int(params['weak1']))]

        plt_obj = df.plot(x='weak',y=params['index'],color=params['color'])
        plt_obj.set_ylabel(params['index'])
        plt_obj.set_xlabel('weak')
        fig = plt_obj.get_figure()
        return fig


app = Tables()
app.launch()
