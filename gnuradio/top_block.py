#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Sep  6 12:53:25 2017
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
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import blks2 as grc_blks2
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
        self.Ind_s = Ind_s = 0
        self.Am_s = Am_s = 1.25893
        self.samp_rate = samp_rate = 512000
        self.Ind = Ind = Ind_s
        self.Am_sig = Am_sig = Am_s

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
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
        self.Add(self.wxgui_scopesink2_0.win)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((Am_sig, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_float*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=Ind,
        	output_index=0,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 30000, 1, 0)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, 1, 0)
        self._Ind_s_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.Ind_s,
        	callback=self.set_Ind_s,
        	label='Ind_s',
        	choices=[0, 1],
        	labels=[],
        )
        self.Add(self._Ind_s_chooser)
        _Am_s_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Am_s_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Am_s_sizer,
        	value=self.Am_s,
        	callback=self.set_Am_s,
        	label='Am_s',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Am_s_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Am_s_sizer,
        	value=self.Am_s,
        	callback=self.set_Am_s,
        	minimum=0,
        	maximum=50,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Am_s_sizer)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blks2_selector_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_Ind_s(self):
        return self.Ind_s

    def set_Ind_s(self, Ind_s):
        self.Ind_s = Ind_s
        self.set_Ind(self.Ind_s)
        self._Ind_s_chooser.set_value(self.Ind_s)

    def get_Am_s(self):
        return self.Am_s

    def set_Am_s(self, Am_s):
        self.Am_s = Am_s
        self.set_Am_sig(self.Am_s)
        self._Am_s_slider.set_value(self.Am_s)
        self._Am_s_text_box.set_value(self.Am_s)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_Ind(self):
        return self.Ind

    def set_Ind(self, Ind):
        self.Ind = Ind
        self.blks2_selector_0.set_input_index(int(self.Ind))

    def get_Am_sig(self):
        return self.Am_sig

    def set_Am_sig(self, Am_sig):
        self.Am_sig = Am_sig
        self.blocks_multiply_const_vxx_0.set_k((self.Am_sig, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
