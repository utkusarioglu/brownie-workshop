Param (
  [Parameter(Mandatory=$True)] [string] $DbName,
  [Parameter(Mandatory=$True)] [string] $EvalArg
)

function Get-ContainerName {
  $ContainerName =  yq `
    '.services[] | select(.container_name == "*mongo*") | .container_name' `
    .docker/docker-compose.dev.yml
  return $ContainerName
}

function Main {
  Param (
    [Parameter(Mandatory=$True)] [string] $DbName,
    [Parameter(Mandatory=$True)] [string] $EvalArg
  )

  $ContainerName = Get-ContainerName

  docker -c u-Boulanger exec -it `
    brownie-workshop-mongodb-community-server `
    mongosh `
      "mongodb://${ContainerName}/${DbName}" `
      --quiet `
      --eval "${EvalArg}"
}

Main $DbName $EvalArg
