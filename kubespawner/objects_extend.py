from kubernetes_asyncio.client.models import (
    V1Job,
    V1JobSpec,
    V1ObjectMeta,
    V1PodTemplateSpec,
    V1PodSpec,
    V1Container,
)


def create_job(image,
               container_name,
               job_name,
               pull_policy):
    container = V1Container(
        image=image,
        name=container_name,
        image_pull_policy=pull_policy,
    )

    pod_template = V1PodTemplateSpec(
        spec=V1PodSpec(restart_policy="Never", containers=[container]),
        metadata=V1ObjectMeta(name=job_name, labels={"pod_name": job_name})
    )

    metadata = V1ObjectMeta(name=job_name, labels={"job_name": job_neme})
    job = V1Job(
        api_version="batch/v1",
        kind="Job",
        metadata=metadata,
        spec=V1JobSpec(backoff_limit=0, template=pod_template),
    )

    return job
