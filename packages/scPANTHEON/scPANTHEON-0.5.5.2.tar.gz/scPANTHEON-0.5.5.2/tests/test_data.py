import json
from bokeh.models import ColumnDataSource, CDSView, IndexFilter, CustomJS, Circle, Div, Panel, Tabs, CheckboxGroup, FileInput,FixedTicker, ColorBar, LogColorMapper, Widget, Quad
from bokeh.models.widgets import Select, Button, ColorPicker,TextInput, DataTable, MultiSelect, AutocompleteInput
from bokeh.events import ButtonClick
from bokeh.transform import log_cmap
from bokeh.palettes import d3
from bokeh.layouts import row, column, layout
from bokeh.io import curdoc# current document
from bokeh.plotting import figure, show, save
from bokeh.resources import CDN
import pandas 
import numpy as np
import scipy.sparse as ss
import colorcet as cc
import scanpy as sc
# from new_func import new_layout
# from main3 import change_class_color
# import mysql.connector
import os, sys, io
import importlib
from PyQt5.QtWidgets import *
from appdirs import AppDirs
import requests, zipfile, tarfile, shutil, subprocess

data_path = '../data/result.h5ad'
adata = sc.read_h5ad(data_path)
print(adata)


TOOLTIPS = [
        ("(x,y)", "($x, $y)"),
        ("color", "@color"),
]
color_list = d3['Category20c'][20]

class FlowPlot:
    def __init__(self, data=None, color_map=None, x_init_idx = 3, y_init_idx = 1, allow_select = True, select_color_change = True, main_plot = None,title=None):
        self.adata = data
        self.adata_a = self.adata
        '''ind = [0, 1]
        self.adata = self.adata[:, ind]'''
        self.data_df = self.adata.to_df()
        self.data_log = np.log1p(self.data_df)

        self.label_existed, view_existed = False, False # group_label_existed
        # personalized
        try:
            group_list = list(self.adata.uns['category_dict'].keys()) 
            #  uns can get any kinds of data type like dict or list
            if main_plot == None and group_list != []:
                self.label_existed = True
        except:
            self.adata.uns['category_dict'] = dict()   
            group_list = list(self.adata.obs.columns) 
            # print("group list:", group_list)
            if group_list != [] and main_plot == None:
                self.label_existed = True
                for group in group_list: 
                    self.adata.uns['category_dict'][group] = pandas.DataFrame(columns=['class_name','color','cell_num']) 
                    class_list = self.adata.obs[group] 
                    # ??? why transform now?
                    self.adata.obs[group] = pandas.Series(self.adata.obs[group], dtype=object)
                    class_dict = {}
                    for value in class_list: # ??? every single cell value?
                        class_dict[value] = class_dict.get(value,0) + 1 
                    ind = 0 
                    for key in class_dict.keys():
                        self.adata.uns['category_dict'][group].loc[ind,:] = {'class_name': key, 'cell_num': class_dict[key], 'color':color_list[int(ind*4%20)]}
                        ind = ind + 1
                    
        self.adata.obs['ind'] = pandas.Series(np.array(range(self.data_df.shape[0])).astype(int).tolist(), index=self.data_df.index)  
        self.data_columns = self.data_df.columns.values.tolist()
        print(self.data_columns)
        self.data_df['color'] = pandas.Series(d3['Category20c'][20][0], index=self.data_df.index)
        # self.data_log['color'] = pandas.Series(d3['Category20c'][20][0], index=self.data_df.index)
        self.data_df['hl_gene'] = pandas.Series(np.full(self.data_df.shape[0], 3), index=self.data_df.index)    
        self.source = ColumnDataSource(data=self.data_df[self.data_columns[0:2]+['color']+['hl_gene']])                             
        self.opts = dict(plot_width=500, plot_height=500, min_border=0, tools="pan,lasso_select,box_select,wheel_zoom,save")
        views = list(self.adata.obsm.keys())
        if views != []:
            for view_name in views:
                for i in range(self.adata.obsm[view_name].shape[1]):
                    self.data_df[view_name+str(i)] = pandas.Series(self.adata.obsm[view_name][:,i],index=self.data_df.index)
                    # self.data_log[view_name+str(i)] = self.data_df[view_name+str(i)]
            view_existed = True
        else:
            view_existed = False
        #self.source = ColumnDataSource(data=self.adata[:,0:2])
        self.view = CDSView(source=self.source, filters=[IndexFilter([i for i in range(self.data_df.shape[0])])])
        self.cur_color = color_list[0]
        self.p = figure(width=500, height=500, tools="pan,lasso_select,box_select,tap,wheel_zoom,save,hover",title=title, tooltips=TOOLTIPS, output_backend="webgl")
        #self.p.output_backend = "svg"
        #print("backend is ", self.p.output_backend)     
        # Choose Map   
        if view_existed:
            view_list = list(self.adata.obsm.keys())+['generic_columns']
            self.choose_panel = Select(title='Choose map:', value=view_list[0], options=view_list)
            self.data_columns = list([self.choose_panel.value +str(i) for i in range(self.adata.obsm[self.choose_panel.value].shape[1])])
            self.source.data = self.data_df[self.data_columns[0:2]+['color']+['hl_gene']]
        else:
            self.choose_panel = Select(title='Choose map:',value='generic_columns',options=['generic_columns'])
        self.choose_panel.on_change('value',lambda attr, old, new :self.change_view_list())
        self.p.xaxis.axis_label = self.data_columns[x_init_idx]
        self.p.yaxis.axis_label = self.data_columns[y_init_idx]
        print(self.data_columns[x_init_idx], self.data_columns[y_init_idx])
        self.x = x_init_idx
        self.y = y_init_idx
        # plot cell get
        self.r = self.p.circle(self.data_columns[x_init_idx], self.data_columns[y_init_idx],  source=self.source, view=self.view, fill_alpha=1,fill_color=color_map,line_color=None )
        # glygh list
        self.glylist = [self.r,]
        self.s_x = AutocompleteInput(title="x axis:", value=self.data_columns[x_init_idx], completions=self.data_columns, min_characters=1)
        self.s_y = AutocompleteInput(title="y axis:", value=self.data_columns[y_init_idx], completions=self.data_columns, min_characters=1)
        # Attach reaction
        self.s_x.on_change("value", lambda attr, old, new: self.tag_func(self.s_x, self.r.glyph, 'x', self.p) )
        self.s_y.on_change("value", lambda attr, old, new: self.tag_func(self.s_y, self.r.glyph, 'y', self.p) )
        # Set default fill color
        if select_color_change:
            self.r.selection_glyph = Circle(fill_alpha=1,fill_color=self.cur_color, line_color='black')
        self.allow_select = allow_select
        print('label and view existed',self.label_existed, view_existed)
        save(self.p)
        show(self.p)

Figure = FlowPlot(data=adata, color_map='color')