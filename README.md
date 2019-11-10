# aiohttp-logger

A HTTP Web service for logging

## Daily Logger

Writes log and rotates daily

| Information |      Value      |
| ----------- | --------------- |
| Path        | `/daily-logger` |
| Method      | POST            |

| Parameters | Required |                           Description                           |
| ---------- | -------- | --------------------------------------------------------------- |
| log_path   | Yes      | Path of log file (name included), for e.g: `/var/log/daily.log` |
| msg        | Yes      | Message to write log                                            |
| day        | Yes      | The day that log is written                                     |

Sample cURL

```bash
curl -X POST \
  http://127.0.0.1/daily-logger \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 396' \
  -H 'Content-Type: multipart/form-data; boundary=--------------------------706269951415340071129519' \
  -H 'Host: 127.0.0.1' \
  -H 'Postman-Token: f17115a1-ceda-4852-8777-6c116e37899b,859651ea-3322-4738-96f7-60c0c1781f18' \
  -H 'User-Agent: PostmanRuntime/7.19.0' \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F 'msg=My Message' \
  -F log_path=daily.log \
  -F day=2019-11-10
```