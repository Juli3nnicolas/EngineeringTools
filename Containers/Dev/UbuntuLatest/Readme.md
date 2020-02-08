# Container purpose

Provide a ready-to-use ubuntu-image for development purpose. Man is properly configured (man pages are not downloaded by default to reduce the size of the final image), vim and git are installed.
For git, ssh keys have to be manually copied if needed for github/gitlab or any other repository holder.

## Run a dev container

Copy the content of example_env.list into env.list

```
cp example_env.list env.list
```

Then set the environment variables with your own data.
Finally run the two following commands to build the image and run the container.

```
docker image build -t dev_ubuntu:latest .
docker run --name dev_<project_name> --env-file env.list -v <path_to_project_root>:/app -it dev_ubuntu_latest /bin/bash
```
