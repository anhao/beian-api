## 备案查询接口API
免费备案查询接口,支持通过域名查询备案信息及通过单位名称查询备案信息

## 域名备案查询

- 请求接口：https://icp.dwz.today/free/icp
- 请求方法：GET/POST
- 请求参数

|参数名称|参数类型|说明|示例|
|---|---|---|---|
|domain|string|要查询的域名|baidu.com|

- 请求示例：https://icp.dwz.today/free/icp?domain=juejin.cn

- 返回参数

```json
{
  "code": 200,
  "message": "success",
  "data": {
    "domain": "juejin.cn",
    "is_icp": true,
    "type": "企业",
    "company_name": "北京北比信息技术有限公司",
    "site_name": null,
    "icp": "京ICP备18012699号-3",
    "home_url": "juejin.cn",
    "date": "2021-10-15 11:21:09"
  },
  "time": 1657261303
}
```

- 返回参数说明

|参数名称|说明|
|---|---|
|code|状态码，返回200则请求成功|
|message|说明|
|data.domain|查询的备案域名|
|data.is_icp|是否备案|
|data.type|备案类型，如企业，个人，事业|
|data.company_name|备案单位名称|
|data.site_name|备案网站名称，不一定有值|
|data.icp|备案ICP号|
|data.home_url|备案域名主页地址|
|data.date|备案信息更新时间|
|time|接口请求时间|

### 代码示例

- PHP

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://icp.dwz.today/free/icp?domain=juejin.cn',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

- GO

```go
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://icp.dwz.today/free/icp?domain=juejin.cn"
	method := "GET"

	client := &http.Client{
	}
	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		fmt.Println(err)
		return
	}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
```

## 主办单位备案信息查询

- 请求接口：https://icp.dwz.today/free/icp/name
- 请求方法：GET/POST
- 请求参数

|参数名称|参数类型|说明|示例|
|---|---|---|---|
|name|string|主办单位名称|北京北比信息技术有限公司|

- 请求示例：https://icp.dwz.today/free/icp/name?name=北京北比信息技术有限公司

- 返回参数：

```json
{
    "code": 200,
    "message": "success",
    "data": [
        {
            "domain": "juejinxiaoce.com",
            "is_icp": true,
            "type": "企业",
            "company_name": "北京北比信息技术有限公司",
            "site_name": null,
            "icp": "京ICP备18012699号-1",
            "home_url": "juejinxiaoce.com",
            "date": "2021-10-15 11:21:09"
        },
        ...
        {
            "domain": "juejinrank.cn",
            "is_icp": true,
            "type": "企业",
            "company_name": "北京北比信息技术有限公司",
            "site_name": null,
            "icp": "京ICP备18012699号-6",
            "home_url": "juejinrank.cn",
            "date": "2021-12-21 09:44:42"
        }
    ],
    "time": 1657262146
}

```

- 返回参数说明

|参数名称|说明|
|---|---|
|code|状态码，返回200则请求成功|
|message|说明|
|data[].domain|备案域名|
|data[].is_icp|是否备案|
|data[].type|备案类型，如企业，个人，事业|
|data[].company_name|备案单位名称|
|data[].site_name|备案网站名称，不一定有值|
|data[].icp|备案ICP号|
|data[].home_url|备案域名主页地址|
|data[].date|备案信息更新时间|
|time|接口请求时间|


### 代码示例

- PHP

```php
<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://icp.dwz.today/free/icp/name?name=E5%8C%97%E4%BA%AC%E5%8C%97%E6%AF%94%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

- GO

```go
package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func main() {

	url := "https://icp.dwz.today/free/icp/name?name=E5%8C%97%E4%BA%AC%E5%8C%97%E6%AF%94%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"
	method := "GET"

	client := &http.Client{
	}
	req, err := http.NewRequest(method, url, nil)

	if err != nil {
		fmt.Println(err)
		return
	}
	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(string(body))
}
```

- Python

```python
import requests

url = "https://icp.dwz.today/free/icp/name?name=E5%8C%97%E4%BA%AC%E5%8C%97%E6%AF%94%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


```
