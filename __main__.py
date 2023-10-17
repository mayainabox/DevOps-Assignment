import pulumi
from pulumi_azure_native import storage, resources
import pulumi_kubernetes as k8s

# Define an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

# Define an Azure resource (Storage Account)
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2,
)

# Define a Kubernetes Deployment for Nginx
nginx_deployment = k8s.apps.v1.Deployment(
    "nginx-deployment",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name="nginx-deployment",
    ),
    spec=k8s.apps.v1.DeploymentSpecArgs(
        replicas=4,  # 4 pods for the deployment
        selector=k8s.meta.v1.LabelSelectorArgs(
            match_labels={"app": "nginx"},
        ),
        template=k8s.core.v1.PodTemplateSpecArgs(
            metadata=k8s.meta.v1.ObjectMetaArgs(
                labels={"app": "nginx"},
            ),
            spec=k8s.core.v1.PodSpecArgs(
                containers=[
                    k8s.core.v1.ContainerArgs(
                        name="nginx",
                        image="nginx",
                        ports=[k8s.core.v1.ContainerPortArgs(container_port=80)],
                    )
                ],
            ),
        ),
    ),
)

# Define a Kubernetes Service for Nginx
nginx_service = k8s.core.v1.Service(
    "nginx-service",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name="nginx-service",
    ),
    spec=k8s.core.v1.ServiceSpecArgs(
        selector={"app": "nginx"},
        ports=[k8s.core.v1.ServicePortArgs(port=80, target_port=80)],
    ),
)

# Export the primary key of the Storage Account and other relevant information if needed
primary_key = (
    pulumi.Output.all(resource_group.name, account.name)
    .apply(
        lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0], account_name=args[1]
        )
    )
    .apply(lambda accountKeys: accountKeys.keys[0].value)
)

pulumi.export("primary_storage_key", primary_key)
