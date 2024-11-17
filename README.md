```python


import time
from ame_6 import Auto, Template, close_airtest_log
from DrissionPage import Chromium

close_airtest_log()

# 连接浏览器
browser = Chromium()
# 获取标签页对象
tab = browser.latest_tab
# 访问网页
tab.get('https://www.baidu.com')

time.sleep(5)

auto = Auto(tab)

auto.touch(Template(r"tpl1731819512530.png", record_pos=(-0.17, -0.009), resolution=(3440, 1440)))

time.sleep(300)

```