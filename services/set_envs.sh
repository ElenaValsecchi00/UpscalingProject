# Read from shell the environment variables
# Example:
# [default]
# aws_access_key_id=<access_key>
# aws_secret_access_key=<secret_key>
# aws_session_token=<session_token>
echo "Enter the content of ~/.aws/credentials file"
read input_string

# Write the content to ~/.aws/credentials file
rm -f ~/.aws/credentials
echo "$input_string" > ~/.aws/credentials

# Extract variables from the text
aws_access_key_id=$(echo "$input_string" | grep -oP '(?<=aws_access_key_id=).*')
aws_secret_access_key=$(echo "$input_string" | grep -oP '(?<=aws_secret_access_key=).*')
aws_session_token=$(echo "$input_string" | grep -oP '(?<=aws_session_token=).*')


# Check if the environment variables are set
if [ -z "$AWS_ACCESS_KEY_ID" ] || [ -z "$AWS_SECRET_ACCESS_KEY" ] || [ -z "$AWS_SESSION_TOKEN" ] || [ -z "$AWS_DEFAULT_REGION" ]; then
    echo "Please set all the environment variables"
    exit 1
fi

# Set default region
AWS_DEFAULT_REGION="us-east-1"

# Write .env file with environment variables
rm -f .env
echo "AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
AWS_SESSION_TOKEN=$AWS_SESSION_TOKEN
AWS_DEFAULT_REGION=$AWS_DEFAULT_REGION" > .env

# Set eks-secrets.yml with base64 encoded environment variables
AWS_ACCESS_KEY_ID=$(echo -n $AWS_ACCESS_KEY_ID | base64)
AWS_SECRET_ACCESS_KEY=$(echo -n $AWS_SECRET_ACCESS_KEY | base64)
AWS_SESSION_TOKEN=$(echo -n $AWS_SESSION_TOKEN | base64)
AWS_DEFAULT_REGION=$(echo -n $AWS_DEFAULT_REGION | base64)
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