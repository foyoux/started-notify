# started-notify
github repository started notify 💕

当有人标星（Star）时，发送邮件提醒。



## 使用方法

1. 将 [.github/workflows/star_notify.yml](https://github.com/foyoux/started-notify/blob/main/.github/workflows/star_notify.yml) 文件复制到需要提醒标星的项目 `.github/workflows/` 目录（没有就创建）下
2. 添加 [Actions secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) 或者直接修改 [.github/workflows/star_notify.yml](https://github.com/foyoux/started-notify/blob/main/.github/workflows/star_notify.yml)
   - 添加 `NOTIFY_EMAIL` secret: 接收邮件的邮箱
   - 修改 `star_notify.yml`: 将 **${{secrets.NOTIFY_EMAIL}}** 替换成接收提醒邮件的邮箱地址。eg: `xxx@qq.com`

## 效果预览

<p align="center">
  <img src="http://110.42.175.98:5512/down/LKPvT9xK2lFx?fname=/started-notify/started-notify-preview.png" alt="获取邮箱授权码"/>
</p>
