# Read from shell the environment variables
# Example:
# [default]
# aws_access_key_id=<access_key>
# aws_secret_access_key=<secret_key>
# aws_session_token=<session_token>
echo "Enter the content of ~/.aws/credentials file"
read input_string_1
read input_string_2
read input_string_3
read input_string_4

# Write the content to ~/.aws/credentials file
rm -f ~/.aws/credentials
echo "$input_string_1
$input_string_2
$input_string_3
$input_string_4" > ~/.aws/credentials

# Extract variables from the text
AWS_ACCESS_KEY_ID=$(echo "$input_string_2" | grep -oP '(?<=aws_access_key_id=).*')
AWS_SECRET_ACCESS_KEY=$(echo "$input_string_3" | grep -oP '(?<=aws_secret_access_key=).*')
AWS_SESSION_TOKEN=$(echo "$input_string_4" | grep -oP '(?<=aws_session_token=).*')


# Set default region
AWS_DEFAULT_REGION="us-east-1"

# Check if the environment variables are set
if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ] || [ -z "$AWS_SESSION_TOKEN" ] || [ -z "$AWS_DEFAULT_REGION" ]; then
    echo "Please set all the environment variables"
    exit 1
fi


# Write .env file with environment variables
rm -f .env
echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION" > .env

# Set eks-secrets.yml with base64 encoded environment variables
AWS_ACCESS_KEY_ID=$(echo -n $AWS_ACCESS_KEY_ID | base64 -w 0)
AWS_SECRET_ACCESS_KEY=$(echo -n $AWS_SECRET_ACCESS_KEY | base64 -w 0)
AWS_SESSION_TOKEN=$(echo -n $AWS_SESSION_TOKEN | base64 -w 0)
AWS_DEFAULT_REGION=$(echo -n $AWS_DEFAULT_REGION | base64 -w 0)
echo "apiVersion: v1
kind: Secret
metadata:
  name: eks-editor-secrets
type: Opaque
data:
  AWS_ACCESS_KEY_ID: $AWS_ACCESS_KEY_ID
  AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY
  AWS_SESSION_TOKEN: $AWS_SESSION_TOKEN
  AWS_DEFAULT_REGION: $AWS_DEFAULT_REGION" > eks-secrets.yml


# Enter name of the cluster
# echo "Enter the name of the cluster"
# read CLUSTER_NAME
# aws eks update-kubeconfig --region $AWS_DEFAULT_REGION --name $CLUSTER_NAME