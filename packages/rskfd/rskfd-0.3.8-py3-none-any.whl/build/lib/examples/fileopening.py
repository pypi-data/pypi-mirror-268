# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 2021

(C) 2021, Rohde&Schwarz, ramian
"""

import rskfd

def ConvertIiQq2Wv():
    '''
    Test
    '''
    # there is no sampling rate in an iqw file
    fs = 320e6
    data = rskfd.ReadIqw( r'\\myserver\signal\higher_qams.iiqq', iqiq=False)
    rskfd.WriteWv( data, fs, r'\\myserver\signal\higher_qams.wv')
    rskfd.WriteBin( data, fs, r'\\myserver\signal\higher_qams.bin')
    rskfd.WriteIqTar( data, fs, r'\\myserver\signal\higher_qams.iq.tar')



def ReadFile( filename):
    '''
    Test
    '''
    data,fs = rskfd.ReadWv( filename)
    print( f'RMS power in file: {rskfd.MeanPower( data)} dBm, peak power: {rskfd.MeanPower( data)} dBm.\n')
    rskfd.WriteWv( data, fs, 'myfilename.wv')



def ReadWvTest():
    '''
    Test the wv reading routine (tags!!)
    '''
    iq, fs = rskfd.ReadWv(r'\\myserver\signal\higher_qams.wv')


if __name__ == "__main__":
	pass
    ReadWvTest()
    