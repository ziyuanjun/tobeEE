#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mono FM Radio
# Author: OZ9AEC
# Description: WFM receiver (mono only)
# Generated: Mon Sep  4 20:17:27 2017
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

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class analog_wfm_rx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Mono FM Radio")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.xlate_tune = xlate_tune = 0
        self.usrp_freq = usrp_freq = 101.8e6
        self.samp_rate = samp_rate = 2500e3
        self.rx_freq = rx_freq = usrp_freq+xlate_tune
        self.rf_gain = rf_gain = 7
        self.if_gain = if_gain = 7
        self.filter_taps = filter_taps = firdes.low_pass(1, samp_rate, 250000, 20000, firdes.WIN_HAMMING, 6.76)
        self.bb_gain = bb_gain = 7
        self.af_gain = af_gain = 0.3

        ##################################################
        # Blocks
        ##################################################
        _xlate_tune_sizer = wx.BoxSizer(wx.VERTICAL)
        self._xlate_tune_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_xlate_tune_sizer,
        	value=self.xlate_tune,
        	callback=self.set_xlate_tune,
        	label='Fine frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._xlate_tune_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_xlate_tune_sizer,
        	value=self.xlate_tune,
        	callback=self.set_xlate_tune,
        	minimum=-250e3,
        	maximum=250e3,
        	num_steps=500,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_xlate_tune_sizer, 7, 0, 1, 5)
        _usrp_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._usrp_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_usrp_freq_sizer,
        	value=self.usrp_freq,
        	callback=self.set_usrp_freq,
        	label='USRP frequency',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._usrp_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_usrp_freq_sizer,
        	value=self.usrp_freq,
        	callback=self.set_usrp_freq,
        	minimum=88e6,
        	maximum=108e6,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_usrp_freq_sizer, 6, 0, 1, 5)
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
        self.nbook = self.nbook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "Receiver")
        self.nbook.AddPage(grc_wxgui.Panel(self.nbook), "Audio")
        self.GridAdd(self.nbook, 0, 0, 5, 5)
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
        _af_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._af_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	label='AF',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._af_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_af_gain_sizer,
        	value=self.af_gain,
        	callback=self.set_af_gain,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_af_gain_sizer, 9, 0, 1, 1)
        self.xlating_fir_filter = filter.freq_xlating_fir_filter_ccc(1, (filter_taps), -xlate_tune, samp_rate)
        self._rx_freq_static_text = forms.static_text(
        	parent=self.GetWin(),
        	value=self.rx_freq,
        	callback=self.set_rx_freq,
        	label='Receive',
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._rx_freq_static_text, 5, 3, 1, 1)
        self.rr_stereo_right = filter.rational_resampler_fff(
                interpolation=48,
                decimation=2500,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy' )
        self.osmosdr_source_1.set_sample_rate(samp_rate)
        self.osmosdr_source_1.set_center_freq(usrp_freq, 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(rf_gain, 0)
        self.osmosdr_source_1.set_if_gain(if_gain, 0)
        self.osmosdr_source_1.set_bb_gain(bb_gain, 0)
        self.osmosdr_source_1.set_antenna('', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)

        self.fftsink_rf = fftsink2.fft_sink_c(
        	self.nbook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=-30,
        	ref_scale=1.0,
        	sample_rate=samp_rate/2,
        	fft_size=512,
        	fft_rate=10,
        	average=True,
        	avg_alpha=0.5,
        	title='Baseband',
        	peak_hold=False,
        )
        self.nbook.GetPage(0).Add(self.fftsink_rf.win)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.audio_sink = audio.sink(48000, '', True)
        self.af_gain_stereo_left = blocks.multiply_const_vff((af_gain, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.af_gain_stereo_left, 0), (self.audio_sink, 0))
        self.connect((self.af_gain_stereo_left, 0), (self.audio_sink, 1))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.rr_stereo_right, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.xlating_fir_filter, 0))
        self.connect((self.rr_stereo_right, 0), (self.af_gain_stereo_left, 0))
        self.connect((self.xlating_fir_filter, 0), (self.blocks_delay_0, 0))
        self.connect((self.xlating_fir_filter, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.xlating_fir_filter, 0), (self.fftsink_rf, 0))

    def get_xlate_tune(self):
        return self.xlate_tune

    def set_xlate_tune(self, xlate_tune):
        self.xlate_tune = xlate_tune
        self._xlate_tune_slider.set_value(self.xlate_tune)
        self._xlate_tune_text_box.set_value(self.xlate_tune)
        self.xlating_fir_filter.set_center_freq(-self.xlate_tune)
        self.set_rx_freq(self.usrp_freq+self.xlate_tune)

    def get_usrp_freq(self):
        return self.usrp_freq

    def set_usrp_freq(self, usrp_freq):
        self.usrp_freq = usrp_freq
        self._usrp_freq_slider.set_value(self.usrp_freq)
        self._usrp_freq_text_box.set_value(self.usrp_freq)
        self.set_rx_freq(self.usrp_freq+self.xlate_tune)
        self.osmosdr_source_1.set_center_freq(self.usrp_freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_filter_taps(firdes.low_pass(1, self.samp_rate, 250000, 20000, firdes.WIN_HAMMING, 6.76))
        self.osmosdr_source_1.set_sample_rate(self.samp_rate)
        self.fftsink_rf.set_sample_rate(self.samp_rate/2)

    def get_rx_freq(self):
        return self.rx_freq

    def set_rx_freq(self, rx_freq):
        self.rx_freq = rx_freq
        self._rx_freq_static_text.set_value(self.rx_freq)

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

    def get_filter_taps(self):
        return self.filter_taps

    def set_filter_taps(self, filter_taps):
        self.filter_taps = filter_taps
        self.xlating_fir_filter.set_taps((self.filter_taps))

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.osmosdr_source_1.set_bb_gain(self.bb_gain, 0)

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        self._af_gain_slider.set_value(self.af_gain)
        self._af_gain_text_box.set_value(self.af_gain)
        self.af_gain_stereo_left.set_k((self.af_gain, ))


def main(top_block_cls=analog_wfm_rx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
