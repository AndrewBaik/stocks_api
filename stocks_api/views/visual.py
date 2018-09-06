from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
import numpy as np
import pandas as pd
import requests
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool, ZoomInTool, ZoomOutTool, ResetTool


class VisualAPIView(APIViewSet):
    def create(self, request, symbol=None):
        """
        """
        if not symbol:
            return Response(json='Company not found', status=404)

        url = f'https://api.iextrading.com/1.0/stock/{symbol}/chart/5y'
        data = requests.get(url)

        if not data:
            return Response(json='Invalid Company', status=404)

        import pdb; pdb.set_trace()
        df = pd.DataFrame(data)
        seqs = np.arange(df.shape[0])

        df['seqs'] = pd.Series(seqs)
        df['changePercent'] = df['changePercent'].apply(lambda x: str(x)+'%')
        df['mid'] = df.apply(lambda x: (x['open'] + x['close']) / 2, axis=1)
        df['height'] = df.apply(lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001, axis=1)

        inc = df.close > df.open
        dec = df.close < df.open
        w = .3

        sourceInc = bk.ColumnDataSource(df.loc[inc])
        sourceDec = bk.ColumnDataSource(df.loc[dec])

        hover = HoverTool(tooltips=[('date', '@date'), ('low', '@low'), ('high', '@high'), ('open', '@open'), ('close', '@close'), ('percent', '@changePercent')])
        TOOLS = [hover, BoxZoomTool(), PanTool(), ZoomInTool(), ZoomOutTool(), ResetTool()]
        p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{symbol}', toolbar_location='above')

        p.xaxis.major_label_orientation = np.pi/4
        p.grid.grid_line_alpha = w
        descriptor = Label(x=70, y=70, text='Past 5 years')
        p.add_layout(descriptor)

        p.segment(df.seqs[inc], df.high[inc], df.seqs[inc], df.low[inc], color='green')
        p.segment(df.seqs[dec], df.high[dec], df.seqs[dec], df.low[dec], color='red')

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)
        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)

        bk.save(p, f'./static/{symbol}candle_stick.html', filename=f'5yr_candlestock')

        return Response(json='Data Created', status=200)
