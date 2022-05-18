#new push mothed
git remote set-url origin https://{token}@github.com/qiangmanl/azure_deploy_googleads_example.git 
git branch -M main
git push -u origin main

#azure app update
cd to webapp project path

$az webapp up --name {webappname} --html


#azure deploy

export RESOURCE_GROUP=learn-acf7735b-8fcb-4ae5-91d3-4383f0dcb68e

export AZURE_REGION=centralus

export AZURE_APP_PLAN=popupappplan-acf7735b

export AZURE_WEB_APP=popupwebapp-acf7735b

az appservice plan create --name $AZURE_APP_PLAN --resource-group $RESOURCE_GROUP --location $AZURE_REGION --sku FREE  --is-linux 

az webapp create --name $AZURE_WEB_APP --resource-group $RESOURCE_GROUP --plan $AZURE_APP_PLAN --runtime "PYTHON:3.9"

git clone https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart
  
cd msdocs-python-flask-webapp-quickstart

az webapp up -n $AZURE_WEB_APP --runtime 'PYTHON:3.9' --sku FREE --logs

#debug

https://popupwebapp-acf7735b.scm.azurewebsites.net/DebugConsole
