# -*- coding: utf-8 -*-


__author__ = 'aeiwz'

import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px
import dash


class plot_NMR_spec:
    def __init__(self, spectra, ppm, label):
        
        self.spectra = spectra
        self.ppm = ppm
        self.label = label


    def median_spectra_group(self, color_map=None, 
                    title='<b>Medien Spectra of <sup>1</sup>H NMR data</b>', title_font_size=28, 
                    legend_name='<b>Group</b>', legend_font_size=20, 
                    axis_font_size=20, 
                    fig_height = 800, fig_width = 2000,
                    line_width = 1.5, legend_order=None
                    ):

        from plotly import graph_objs as go
        from plotly import express as px

        spectra = self.spectra
        ppm = self.ppm
        label = self.label
        

        df_mean = spectra.groupby(label).median()

        #check if color_map is provided
        if color_map is None:
            color_map = dict(zip(df_mean.index, px.colors.qualitative.Plotly))
        else:
            if len(color_map) != len(df_mean.index):
                raise ValueError('Color map must have the same length as group labels')
            else:
                color_map = color_map

        

        #plot spectra
        fig = go.Figure()
        for i in df_mean.index:
            fig.add_trace(go.Scatter(x=ppm, y=df_mean.loc[i,:], mode='lines', name=i, line=dict(color=color_map[i], width=line_width)))

        fig.update_layout(
            autosize=False,
            width=fig_width,
            height=fig_height,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=4
            )
        )

        fig.update_xaxes(showline=True, showgrid=False, linewidth=1, linecolor='rgb(82, 82, 82)', mirror=True)
        fig.update_yaxes(showline=True, showgrid=False, linewidth=1, linecolor='rgb(82, 82, 82)', mirror=True)

        #Set font size of label
        fig.update_layout(font=go.layout.Font(size=axis_font_size))
        #Add title
        fig.update_layout(title={'text': title, 'xanchor': 'center', 'yanchor': 'top'}, 
                        title_x=0.5, 
                        xaxis_title="<b>δ<sup>1</sup>H</b>", yaxis_title="<b>Intensity</b>",
                        title_font_size=title_font_size,
                        title_yanchor="top",
                        title_xanchor="center")

        #Add legend

        fig.update_layout(legend=dict( title=legend_name, font=dict(size=legend_font_size)))
        #Invert x-axis
        fig.update_xaxes(autorange="reversed")
        #Alpha background
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        #fig.update_layout(title='Medien Spectra', xaxis_title='δ <sup>1</sup>H', yaxis_title='Intensity')

        #set y-axis tick format to scientific notation with 4 decimal places
        fig.update_layout(yaxis=dict(tickformat=".2e"))

        return fig

