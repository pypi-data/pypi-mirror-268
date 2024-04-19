<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-yinying-chat
</div>

# 介绍
- 本插件适配银影API，可以在nonebot中调用的银影API，调用模型默认为：（yinyingllm-v2）进行回复。
# 安装

* 手动安装
  ```
  将该文件夹拖入/plugins文件夹内
  ```

  后在bot项目的pyproject.toml文件手动添加插件：

  ```
  plugin_dirs = ["xxxxxx","xxxxxx",......,"下载完成的插件路径/nonebot-plugin-yinying-chat"]
  ```

# 使用方法

- chat 使用该命令进行聊天
- @机器人 chat 使用该指令进行聊天也可以
- clear 清除当前用户的聊天记录
