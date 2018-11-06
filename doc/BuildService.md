# Building the Service

## Flask

To run the service from the command line using **Flask**, simply copy the **config.json** file in **service/build/prd** into **service/src** and then  execute the client from the command line thusly: **python3 foodtruck_service.py**. The usage statement will appear to give you more instructions regarding the additional command line parameters.

## Docker

To run the docker image, simply execute the following shell scripts in order:

    1. ./prddockerize.sh _version number}
    2. ./runprd.sh {version number}

After that, the docker image should start up.