# cutlet-docker

Docker version of [cutlet](https://github.com/polm/cutlet)

## Config

### Container port

Default: 23333

To modify the port, you need to change both ports in [main.py](/main.py), [run.bat](/run.bat) and [Dockerfile](/Dockerfile):

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

### Local machine port

Default: 23333

To modify the port, you need to change the port in [run.bat](/run.bat):

```batch
docker run -d -p <local_machine_port>:23333 --name my-cutlet-full cutlet-api-full
```

## Build

Run [build.bat](/build.bat)

## Run

Run [run.bat](/run.bat)

## Test

1. Navigate to `http://localhost:<local_machine_port>/docs#/default/convert_to_romaji_convert_post`
2. `Try it out`
3. Input `{"text": "こんにちは"}` and execute