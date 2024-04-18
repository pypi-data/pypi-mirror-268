#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
GNSS time/date management
Beilin Jacques
ENSG/IGN

"""

from gpsdatetime import gpsdatetime

class gpstime(gpsdatetime):
    """GPS time management
    Jacques Beilin - ENSG/DPTS

    """

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)

        
if __name__ == "__main__":

#    test()
    time_1 = gpstime(wk=1931, wd=1, sec=8)
    print(time_1.st_iso_epoch())