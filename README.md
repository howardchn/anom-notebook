# My Anomaly Detection Notebook and Examples

## Build your own image
```
# build image
docker build -t anom-notebook .

# run the container
docker run --rm -itd -p 8000:8888 -e GRANT_SUDO="yes" --user root anom-notebook
```

Once the container is running, brows the address: `localhost:8000` and login, the note is under `anom` folder.

## Use existing note server
Copy following files into your node and refresh.