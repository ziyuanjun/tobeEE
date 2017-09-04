#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: General I/Q Receiver
# Author: ELEC350
# Description: Lab 1
# Generated: Mon Sep  4 20:19:36 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class output_display(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="General I/Q Receiver")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2500000
        self.rf_gain = rf_gain = 7
        self.if_gain = if_gain = 7
        self.f_c = f_c = 1000
        self.bb_gain = bb_gain = 7
        self.ReceiverGain = ReceiverGain = 30

        ##################################################
        # Blocks
        ##################################################
        _rf_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rf_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	label='RF',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rf_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rf_gain_sizer,
        	value=self.rf_gain,
        	callback=self.set_rf_gain,
        	minimum=0,
        	maximum=90,
        	num_steps=90,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rf_gain_sizer, 9, 2, 1, 1)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Scope Plot")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Magnitude")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Phase")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Real")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Imaginary")
        self.Add(self.notebook_0)
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='IF',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=0,
        	maximum=60,
        	num_steps=60,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_if_gain_sizer, 9, 1, 1, 1)
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='BB',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=0,
        	maximum=90,
        	num_steps=90,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_bb_gain_sizer, 9, 3, 1, 1)
        self.wxgui_scopesink3 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=.05,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink3.win)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(4).GetWin(),
        	title='Imaginary',
        	sample_rate=samp_rate,
        	v_scale=0.05,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(4).Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(3).GetWin(),
        	title='Real',
        	sample_rate=samp_rate,
        	v_scale=.05,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_scopesink2 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(2).GetWin(),
        	title='Phase',
        	sample_rate=samp_rate,
        	v_scale=1,
        	v_offset=0,
        	t_scale=0.002,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2.win)
        self.wxgui_scopesink1 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	title='Magnitude',
        	sample_rate=samp_rate,
        	v_scale=.05,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink1.win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=4,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy' )
        self.osmosdr_source_1.set_sample_rate(samp_rate)
        self.osmosdr_source_1.set_center_freq(200000000, 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(rf_gain, 0)
        self.osmosdr_source_1.set_if_gain(if_gain, 0)
        self.osmosdr_source_1.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_1.set_antenna('', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)

        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        _ReceiverGain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ReceiverGain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ReceiverGain_sizer,
        	value=self.ReceiverGain,
        	callback=self.set_ReceiverGain,
        	label='ReceiverGain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._ReceiverGain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ReceiverGain_sizer,
        	value=self.ReceiverGain,
        	callback=self.set_ReceiverGain,
        	minimum=0,
        	maximum=38,
        	num_steps=38,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_ReceiverGain_sizer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_arg_0, 0), (self.wxgui_scopesink2, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.blocks_complex_to_mag_0, 0), (self.wxgui_scopesink1, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_mag_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.wxgui_scopesink3, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink3.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink1.set_sample_rate(self.samp_rate)
        self.osmosdr_source_1.set_sample_rate(self.samp_rate)

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self._rf_gain_slider.set_value(self.rf_gain)
        self._rf_gain_text_box.set_value(self.rf_gain)
        self.osmosdr_source_1.set_gain(self.rf_gain, 0)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)
        self.osmosdr_source_1.set_if_gain(self.if_gain, 0)

    def get_f_c(self):
        return self.f_c

    def set_f_c(self, f_c):
        self.f_c = f_c

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.osmosdr_source_1.set_bb_gain(self.bb_gain, 0)

    def get_ReceiverGain(self):
        return self.ReceiverGain

    def set_ReceiverGain(self, ReceiverGain):
        self.ReceiverGain = ReceiverGain
        self._ReceiverGain_slider.set_value(self.ReceiverGain)
        self._ReceiverGain_text_box.set_value(self.ReceiverGain)


def main(top_block_cls=output_display, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
