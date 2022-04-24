#new push mothed
git remote set-url origin https://{token}@github.com/qiangmanl/azure_deploy_googleads_example.git 
git branch -M main
git push -u origin main

#azure app update
cd to webapp project path

$az webapp up --name {webappname} --html