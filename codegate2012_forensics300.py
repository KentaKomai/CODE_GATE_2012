#! /usr/bin/python
# -*- coding:utf-8 -*-
import pytz
from datetime import datetime
import re

# using pytz
# URL : http://pytz.sourceforge.net/

unixTime = int(str(1328799447)[0:10])
dt = datetime.fromtimestamp(unixTime, pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%dT%H:%M:%S')
print 'test.wargame.kr|'+str(dt)

