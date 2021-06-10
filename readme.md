NOTICE: ARCHIVED AND DISCONTINUED
===
This project was originally created for a Python talk over two years ago. I am now archiving it as there are a number of Dependabot warnings and compatibility issues with the initial configuration. I may recreate this at some point in the future to demonstrate the functionality, but this project will no longer be maintained actively.

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
