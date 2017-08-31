#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Zoom Fft
# Generated: Tue Aug 29 09:03:08 2017
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
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class zoom_fft(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Zoom Fft")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.ratio_chooser = ratio_chooser = 20
        self.zoom_ratio = zoom_ratio = ratio_chooser
        self.samp_rate = samp_rate = 2500000
        self.freq = freq = 94500000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate/zoom_ratio,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Plot',
        	peak_hold=False,
        	win=window.blackmanharris,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self._ratio_chooser_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.ratio_chooser,
        	callback=self.set_ratio_chooser,
        	label='ratio_chooser',
        	choices=[2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        	labels=[],
        )
        self.Add(self._ratio_chooser_chooser)
        self.osmosdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy' )
        self.osmosdr_source_1.set_sample_rate(samp_rate)
        self.osmosdr_source_1.set_center_freq(freq, 0)
        self.osmosdr_source_1.set_freq_corr(0, 0)
        self.osmosdr_source_1.set_dc_offset_mode(0, 0)
        self.osmosdr_source_1.set_iq_balance_mode(0, 0)
        self.osmosdr_source_1.set_gain_mode(False, 0)
        self.osmosdr_source_1.set_gain(10, 0)
        self.osmosdr_source_1.set_if_gain(20, 0)
        self.osmosdr_source_1.set_bb_gain(20, 0)
        self.osmosdr_source_1.set_antenna('', 0)
        self.osmosdr_source_1.set_bandwidth(0, 0)

        self.low_pass_filter_0 = filter.fir_filter_ccf(zoom_ratio, firdes.low_pass(
        	1, samp_rate, samp_rate/zoom_ratio/2, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate/zoom_ratio,True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.osmosdr_source_1, 0), (self.low_pass_filter_0, 0))

    def get_ratio_chooser(self):
        return self.ratio_chooser

    def set_ratio_chooser(self, ratio_chooser):
        self.ratio_chooser = ratio_chooser
        self.set_zoom_ratio(self.ratio_chooser)
        self._ratio_chooser_chooser.set_value(self.ratio_chooser)

    def get_zoom_ratio(self):
        return self.zoom_ratio

    def set_zoom_ratio(self, zoom_ratio):
        self.zoom_ratio = zoom_ratio
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.zoom_ratio)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.zoom_ratio/2, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/self.zoom_ratio)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/self.zoom_ratio)
        self.osmosdr_source_1.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/self.zoom_ratio/2, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate/self.zoom_ratio)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.wxgui_fftsink2_0.set_baseband_freq(self.freq)
        self.osmosdr_source_1.set_center_freq(self.freq, 0)


def main(top_block_cls=zoom_fft, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
