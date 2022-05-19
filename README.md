#new push mothed
git remote set-url origin https://{token}@github.com/qiangmanl/azure_deploy_googleads_example.git 
git branch -M main
git push -u origin main

#azure app update
cd to webapp project path

$az webapp up --name {webappname} --html


#azure deploy


export AZURE_REGION=centralus

export AZURE_APP_PLAN=popupappplan-acf7735b

export AZURE_WEB_APP=popupwebapp-acf7735b

az appservice plan create --name $AZURE_APP_PLAN --resource-group $RESOURCE_GROUP --location $AZURE_REGION --sku FREE  --is-linux 

az webapp create --name $AZURE_WEB_APP --resource-group $RESOURCE_GROUP --plan $AZURE_APP_PLAN --runtime "PYTHON:3.9"

#git remote resp
az webapp deployment source config-local-git --name $AZURE_WEB_APP --resource-group $RESOURCE_GROUP

#
az webapp config set -g  $RESOURCE_GROUP -n $AZURE_WEB_APP


git clone https://github.com/qiangmanl/azure_deploy_googleads_example
  
cd azure_deploy_googleads_example

az webapp up -n $AZURE_WEB_APP --runtime 'PYTHON:3.7' --sku FREE --logs

https://popupwebapp-acf7735b.scm.azurewebsites.net/DebugConsole

#list all server platform
az webapp list-runtimes

az group delete --name $AZURE_WEB_APP --no-wait

