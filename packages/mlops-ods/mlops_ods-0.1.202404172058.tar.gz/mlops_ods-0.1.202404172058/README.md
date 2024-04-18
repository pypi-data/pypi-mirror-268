# MLOps ODS
This project for ml model with MLOps instruments

the methodology of repo (github flow - one main branch, and developing in other brunches):
- main branch: 'master'
- other branches: 'fix-', 'feature-', 'model-', 'experiment-'

Docker image (build / run):
```commandline
docker build . -t mlops_ods_image
docker run -it mlops_ods_image /bin/bash
```
build for linux:
```commandline
docker build . -t mlops_ods_image --platform linux/amd64
```
run with port and volumes if necessary:
```commandline
docker run -p 8888:8888 -v {path-to-local-folder-(pwd)}:/app/volumes -it mlops_ods_image /bin/bash
```
