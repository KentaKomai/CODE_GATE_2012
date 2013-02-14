#! /usr/bin/python
# -*- coding:utf-8 -*-
import pytz
from datetime import datetime
import re

now = int(str(1329009797205)[0:10])
dt = datetime.fromtimestamp(now, pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%dT%H:%M:%S%z')
index = re.search('\+([0-9]{1}){4}', dt)
st = index.start()
ed = index.end()
dt = dt[0:st+3] + ':' + dt[st+3:ed]
print '1_UNI/**/ON_SELECT|'+str(dt)

