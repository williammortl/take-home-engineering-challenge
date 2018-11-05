# args:
# -----
# $1 - build version
# $2 - WillACR password

sudo docker login willx2cr.azurecr.io -u WillX2CR -p $2
sudo docker push willx2cr.azurecr.io/foodtruck/foodtruck-img-prd:$1