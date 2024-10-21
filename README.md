# started-notify

GitHub repository started notify 💕

当有人标星（Star）时，发送邮件提醒。

## 使用方法

1. 将 [.github/workflows/started_notify.yml](https://github.com/foyoux/started-notify/blob/main/.github/workflows/started_notify.yml)
文件复制到需要提醒标星的项目 `.github/workflows/` 目录（没有就创建）下
2. 设置接收通知的邮箱, 以下方式二选一
    - 添加 `NOTIFY_EMAIL` secret: 接收邮件的邮箱,
      参考 [Actions secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
    - 修改 `started_notify.yml`: 将 **${{secrets.NOTIFY_EMAIL}}** 替换成接收提醒邮件的邮箱地址。eg: `xxx@qq.com`

## 效果预览

<p align="center">
  <img src="images/started-notify-preview.png" width="400" alt="获取邮箱授权码"/>
</p>
