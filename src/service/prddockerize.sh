# args:
# -----
# $1 - build version

sudo docker build --network=host -t willx2cr.azurecr.io/foodtruck/foodtruck-img-prd:$1 -f build/prd/Dockerfile .
