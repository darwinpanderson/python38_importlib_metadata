Purpose
===
The purpose of this repository is to demonstrate some functionality of the `importlib.metadata` library, specifically the `metadata` and `version` functions.


Quickstart Guide
===
**Docker Compose Commands**
```
docker-compose build
docker-compose up
```

**Demonstration Endpoints**

| Endpoint                 |                     Description                      |
| :----------------------- |:-----------------------------------------------------|
| /api/                    | API index                                            |
| /api/packages/           | Lists all valid packages                             |
| /api/packages/\<package> | Lists details of supplied package (version/metadata) |
