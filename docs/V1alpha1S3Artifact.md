# V1alpha1S3Artifact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) | AccessKeySecret is the secret selector to the bucket&#39;s access key | 
**bucket** | **str** | Bucket is the name of the bucket | 
**endpoint** | **str** | Endpoint is the hostname of the bucket endpoint | 
**insecure** | **bool** | Insecure will connect to the service with TLS | [optional] 
**key** | **str** | Key is the key in the bucket where the artifact resides | 
**region** | **str** | Region contains the optional bucket region | [optional] 
**role_arn** | **str** | RoleARN is the Amazon Resource Name (ARN) of the role to assume. | [optional] 
**secret_key_secret** | [**V1SecretKeySelector**](V1SecretKeySelector.md) | SecretKeySecret is the secret selector to the bucket&#39;s secret key | 
**use_sdk_creds** | **bool** | UseSDKCreds tells the driver to figure out credentials based on sdk defaults. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


