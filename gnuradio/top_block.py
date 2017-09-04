#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Sep  1 11:19:04 2017
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

from gnuradio import analog
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
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.fc = fc = 25000
        self.f_cut_off = f_cut_off = 25000

        ##################################################
        # Blocks
        ##################################################
        self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab1")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab2")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab3")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab4")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "tab5")
        self.Add(self.notebook)
        _fc_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fc_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fc_sizer,
        	value=self.fc,
        	callback=self.set_fc,
        	label='fc',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fc_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fc_sizer,
        	value=self.fc,
        	callback=self.set_fc,
        	minimum=0,
        	maximum=samp_rate/2,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fc_sizer)
        _f_cut_off_sizer = wx.BoxSizer(wx.VERTICAL)
        self._f_cut_off_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_f_cut_off_sizer,
        	value=self.f_cut_off,
        	callback=self.set_f_cut_off,
        	label='f_cut_off',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._f_cut_off_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_f_cut_off_sizer,
        	value=self.f_cut_off,
        	callback=self.set_f_cut_off,
        	minimum=0,
        	maximum=50000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_f_cut_off_sizer)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	title='FM Demodulated Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.notebook.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_2 = fftsink2.fft_sink_c(
        	self.notebook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='After LP Filter',
        	peak_hold=False,
        )
        self.notebook.GetPage(0).Add(self.wxgui_fftsink2_2.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FM Demodulated FFT Plot',
        	peak_hold=False,
        )
        self.notebook.GetPage(2).Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_1 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, f_cut_off, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, f_cut_off, 100, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/ziyuan/Program/tobeEE/gnuradio/FM_TX.dat', True)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 1)
        self.blocks_complex_to_arg_0 = blocks.complex_to_arg(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, fc, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blocks_complex_to_arg_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.wxgui_fftsink2_2, 0))
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_arg_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.low_pass_filter_1, 0), (self.blocks_float_to_complex_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self._fc_slider.set_value(self.fc)
        self._fc_text_box.set_value(self.fc)
        self.analog_sig_source_x_1.set_frequency(self.fc)
        self.analog_sig_source_x_0.set_frequency(self.fc)

    def get_f_cut_off(self):
        return self.f_cut_off

    def set_f_cut_off(self, f_cut_off):
        self.f_cut_off = f_cut_off
        self._f_cut_off_slider.set_value(self.f_cut_off)
        self._f_cut_off_text_box.set_value(self.f_cut_off)
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.f_cut_off, 100, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
