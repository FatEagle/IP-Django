# 用被反向代理后的Django获取IP地址和地理信息

## 获取IP
反向代理后, 用户IP不会存储在`REMOTE_ADDR`中, 而会存储在`HTTP_X_FORWARDED_FOR`.

`REMOTE_ADDR` 存储了NGINX发出的请求时的IP.
`HTTP_X_FORWARDED_FOR` 存储了访问NGINX的请求的IP

## 获取地理位置信息
使用百度地图开放地址平台, 官方网址如下:
http://lbsyun.baidu.com/index.php?title=%E9%A6%96%E9%A1%B5

其可以通过IP地址获取地理位置, 调用百度的API即可.