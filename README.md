# cutlet-docker

Docker version of [cutlet](https://github.com/polm/cutlet)

[cutlet](https://github.com/polm/cutlet) 的 Docker 版本

## Build | 构建

Download all the files in this repo first, Then run [build.bat](/build.bat).

首先下载本仓库的所有文件，之后执行 [build.bat](/build.bat)。

This operation will takes a lot of time, please wait.

该操作非常耗时，请耐心等待完成。

## Run | 运行

Run [run.bat](/run.bat)

执行 [run.bat](/run.bat)

If you see error output like the following text:

如果你遇到了类似下述报错：

```batch
docker: Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:8000 -> 127.0.0.1:0: listen tcp 0.0.0.0:8000: bind: An attempt was made to access a socket in a way forbidden by its access permissions.
```

Please try to change the port (see [Config (optional)](#config-optional--配置可选) for more info)

请尝试更改端口（参见 [配置（可选）](#config-optional--配置可选)）

## Test | 测试

1. Navigate to `http://localhost:<local_machine_port>/docs#/default/convert_to_romaji_convert_post` via your browser
2. Click `Try it out`
3. Input `{"text": "こんにちは"}` and click `Execute`

1. 浏览器访问 `http://localhost:<local_machine_port>/docs#/default/convert_to_romaji_convert_post`
2. 点按 `Try it out`
3. 键入 `{"text": "こんにちは"}` 后点按 `Execute`

## Config in BetterLyrics | 在 BetterLyrics 中配置

If everything works as expected, you can now config it in BetterLyrics.

如果没有任何问题现在可以进入 BetterLyrics 进行配置了。

Go to `Settings` -> `Playback sources` -> `Japanese annotation`, input the server address into the text filed.

前往 `设置` -> `播放源` -> `日语注音`, 文本框内键入服务器地址。

> Server address format: `http://localhost:<local_machine_port>`
> 服务器地址格式：`http://localhost:<local_machine_port>`

> Default server address: `http://localhost:23333`
> 服务器默认地址：`http://localhost:23333`


## Config (optional) | 配置（可选）

### Container port | 容器端口

Default: 23333

默认：23333

To modify the port, you need to change all the `<container_port>` in the following files:

要更改端口，请在下述文件中依次更改 `<container_port>`：

- [main.py](/main.py)

```batch
uvicorn.run(app, host="0.0.0.0", port=<container_port>)
```

- [run.bat](/run.bat)

```batch
docker run -d -p 23333:<container_port> --name my-cutlet-full cutlet-api-full
```

- [Dockerfile](/Dockerfile)

```dockerfile
EXPOSE <container_port>
```

### Local machine port | 本机端口

Default: 23333

默认：23333

To modify the port, you need to change `<local_machine_port>` in the following file:

要更改端口，请修改下述文件中的 `<local_machine_port>`：

```batch
docker run -d -p <local_machine_port>:23333 --name my-cutlet-full cutlet-api-full
```