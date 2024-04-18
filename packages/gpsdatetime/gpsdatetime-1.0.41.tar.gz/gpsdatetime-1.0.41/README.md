# gpsdatetime - Python GPS date/time management package

This is a python library for GNSS date/time transformations

## Usage

### Initialize gpsdatetime object

```python
import gpsdatetime as gpst
```

* init from current computer date/time
```python
t = gpst.gpsdatetime()
```

* init from modified julian date 
```python
t=gpst.gpsdatetime(mjd=54605.678)
```

* init from GPS week and second of week
```python
t=gpst.gpsdatetime(wk=1400, wsec=600700)
```

* init from usual time elements
```python
t=gpst.gpsdatetime(yyyy=2016, mon=1, dd=7, h=3, min=5, sec=5)
```

* init from SINEX time string
```python
t=gpst.gpsdatetime('16:004:46888')
```

* init from sinex date elements
```python
t=gpst.gpsdatetime(yyyy=2016, doy=004, dsec=45677)
```

* init from iso time string
```python
t=gpst.gpsdatetime('16:01:04T03:05:05Z')
```

* init from RINEX time string
```python
t=gpst.gpsdatetime('18 10  9 12 20 45.00000')
```
or
```python
t=gpst.gpsdatetime('2018 10  9 12 20 45.00000')
```

### Update date/time

Several functions are provided in order to update date/time.

| Function | Parameters | Purpose |
| :------- |:-----------| --------|
| just_now | | update from current date/time |
|ymdhms_t|year, month, day+[hour/minute/second]| update with date |
|yyyyddds_t|year, day-of-year, second-of-day||
|gpswkd_t|GPS week, day of week||
|gpswks_t|GPS week, second of week||
|mjd_t|modified julian day||
|jd_t|Julian day||
|snx_t|'20:123:43200'| update with Sinex time string|
|rinex_t|'2018 10  9 12 20 45.00000'|update with Rinex time string|
|iso_t|'16:01:04T03:05:05Z'|update with iso time string|
|timestamp_t|'10/Aug/2023:09:33:43 +0000'|update with timestamp time string|

### Time calculations

* add 5 seconds (or substract 2s) to gpsdatetime object t
```python
t += 5
t -= 2
```

* add x days, hour, seconds to current object
```python
t.add_day(x)
t.add_h(y)
t.add_s(z)
```

* test wether t is before t1 or not 
```python
if t < t1:
    print('t before t1')
```

* duration between two time objects
```python
t1 = gpst.gpsdatetime()
t2 = gpst.gpsdatetime()
Delta_t  = t2 - t1 # result in seconds
```

* set t object to current date at 0h00
```python
t.day00()
```

* set t object to current week on sunday morning 0h00
```python
t.wk00()
```

* set t object to beginning of current hour
```python
t.h00()
```

* set t object to beginning of current minute
```python
t.m00()
```

### Get attributes


| Attribute  | Description     | Unit |
| :--------------- |:---------------| -----|
|s1970  | seconds from 01-01-1970 à 0h00Z | second |
|mjd  | Modified Julian Date (MJD = JD – 2400000.5) | decimal days |
|jd  | Julian Date | decimal days |
|jd50  | Julian Date from J1950 | decimal days |
|wk  | GPS week | week I4 |
|wsec  | seconds in GPS week | float [0..604800]  |
|yyyy  | year (4 digits) | year I4 [1902..2079] |
|yy  | year (2 digits) | year (I2) |
|mon  | month number | I2  [1..12]  |
|dd  | day of month | I2 [1..31] |
|hh  | hour | I2 [0..24] |
|min  | minute | I2 [0..60] |
|sec  | second | I2 [0..60] |
|doy  | day of year (DOY) | I3 [1..366] |
|wd  | day of week (DOW) | I1 [0..6] |
|dsec  | second of day | float [0..86400] |
|dy  | decimal year | float [0..366]  |
|GMST  | Greenwich Mean Sidereal Time | decimal hours |
|EQEQ  | Equation of equinoxes | decimal hours |
|GAST  | Greenwich Aparent Sidereal Time | decimal hours |


```python
y = t.yyyy
# y = 2020
```

### Print time strings 

* Return iso time string : 
```python
iso_t = t.st_iso_epoch()
# 2020-10-01T12:00:26Z 
```

or

```python
iso_t = t.st_iso_epoch(2)
# 2020-10-01T12:00:26.00Z 
```

* Return Ephem (https://pypi.org/project/ephem/) time string : 2020/10/01 12:00:26.0 
```python
s = t.st_pyephem_epoch()
```

* Return Rinex time string : 2020 10 01 12 00 26.0000000 
```python
s = t.st_rinex_epoch()
```

* Return Sinex time string : 20:010:43226
```python
s = t.st_snx_epoch()
```

* Return time stamp
```python
s = t.st_timestamp_epoch()
```

* Print all date/time elements
```python
print(t)
"""
gpsdatetime (version 1.0.38)
-----------------------------------------------------------------
s1970 : 1677283200.000000
YYYY_MM_DD : 2023/02/25  
HH:MM:SS : 00:00:00.000000000
GPS week : 2250
Day of week : 6 (SAT)
Second of week : 518400.000000000
Second of day : 0.000000000      
session : a
Modified Julian Date : 60000.000000  
Julian Date : 2460000.500000
YYYY : 2023  DOY : 056
GMST (dec. hour) : 10.306795
GAST (dec. hour) : 10.306635
Eq. of Equinoxes (dec. hour) : -0.000160
-----------------------------------------------------------------
"""
```



## Installation

Installation is accomplished from the command line.

* From pypi

```
user@desktop$pip3 install gpsdatetime
```

* From package source directory

```
user@desktop:~/gpsdatetime$ python3 setup.py install
```

## licence

Copyright (C) 2014-2023, Jacques Beilin / ENSG-Geomatique

Distributed under terms of the CECILL-C licence.
