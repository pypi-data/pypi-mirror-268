#!/bin/bash
# shellcheck disable=SC2046

BUILD_ONLY=false
SERVICE_NAME=${PWD##*/}
DOCKERFILE=Dockerfile


SERVICE_STAGE="prod"
GIT_BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# if [[ "$GIT_BRANCH_NAME" == "master" ]]; then
#     SERVICE_STAGE=prod
# fi


while getopts ":t:f:-:" optchar; do
    case "${optchar}" in
        t) SERVICE_NAME=$OPTARG ;;
        f) DOCKERFILE=$OPTARG ;;
        -)
            case "${OPTARG}" in
                "build-only")
                    BUILD_ONLY=true
                    ;;
                *)
                    echo "Unknown option --${OPTARG}" >&2
                    ;;
            esac;;
        *)
            echo "Non-option argument: '-${OPTARG}'" >&2
            ;;
    esac
done


echo "**********************************************"
echo " Deployment Parameters"
echo "**********************************************"

if [[ -z "$SERVICE_NAME" ]]; then
    echo "Error: SERVICE_NAME is empty";
    exit 1;
fi

REGISTRY_NAME="$SERVICE_NAME-$SERVICE_STAGE"
DOCKER_PATH="867112626405.dkr.ecr.ap-northeast-2.amazonaws.com/$REGISTRY_NAME"

echo "- Service name: $SERVICE_NAME"
echo "- Regisry name: $REGISTRY_NAME"
echo "- Registry path: $DOCKER_PATH"

aws ecr describe-repositories --repository-names "$REGISTRY_NAME" &> /dev/null
if [ $? -ne 0 ]; then
    echo "Creating a new repository..."
    aws ecr create-repository --repository-name "$REGISTRY_NAME"
fi


if [[ -f "VERSION" ]]
then
    # bump up package version
    perl -i -pe 's/\b(\d+)(?=\D*$)/$1+1/e' VERSION

    version=$(cat VERSION) || ""
else
    version=""
fi

echo "- Build version: $version"
echo "- Build Only: $BUILD_ONLY"
echo "- Dockerfile: $DOCKERFILE"

if [ ! -f "$DOCKERFILE" ]; then
    echo "* Error: $DOCKERFILE does not exist."
    exit
fi

echo "- Logging in to Docker..."

AWS_ECR_LOGIN=$(aws ecr get-login-password)

docker login -u AWS -p "$AWS_ECR_LOGIN" "$DOCKER_PATH"


echo ""
echo "**********************************************"
echo " Building Docker image "
echo "**********************************************"

options=("-t" "$REGISTRY_NAME" "-f" "$DOCKERFILE" ".")
options+=("--build-arg" "service_stage=$SERVICE_STAGE")
options+=("--platform" "linux/amd64")

if [[ -z $version ]]
then
    docker build "${options[@]}"

    echo "- Pushing to Amazon ECR..."

    docker tag "$REGISTRY_NAME" "$DOCKER_PATH"
    docker push "$DOCKER_PATH"
    docker rmi "$DOCKER_PATH"
else
    docker build "${options[@]}" --build-arg version="$version"

    echo "- Pushing to Amazon ECR..."

    docker tag "$REGISTRY_NAME" "$DOCKER_PATH:latest"
    docker tag "$REGISTRY_NAME" "$DOCKER_PATH:$version"

    docker push "$DOCKER_PATH:latest"
    docker push "$DOCKER_PATH:$version"

    echo "- Deleting temporary tags..."

    docker rmi "$DOCKER_PATH:latest"
    docker rmi "$DOCKER_PATH:$version"
fi

# docker rm -f $(docker ps -a -q)
docker rmi $(docker images -f "dangling=true" -q) &> /dev/null

echo ""

docker images


echo ""
echo "**********************************************"
echo " Restarting Kubernetes Pods"
echo "**********************************************"

kubectl rollout restart deployment "$SERVICE_NAME"

echo ""

kubectl get pod
