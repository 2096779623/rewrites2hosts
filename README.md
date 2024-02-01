# rewrites2hosts
将 AdGuardHome 的 DNS 重写规则转换成 Hosts 格式

# 例子

```bash
D:\rewrites2hosts>python main.py ad.yaml
github.com 20.27.177.113
raw.githubusercontent.com raw.fgit.cf
api.github.com 20.205.243.168
gist.github.com 20.205.243.166
raw.github.com raw.fgit.cf
alive.github.com 140.82.112.25
dash.cloudflare.com 104.17.111.184
static.dash.cloudflare.com 104.18.10.29
static.cloudflareinsights.com 104.16.57.101
github.githubassets.com 185.199.108.154
avatars.githubusercontent.com 185.199.109.133
D:\rewrites2hosts>
```
