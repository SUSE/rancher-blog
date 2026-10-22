---
title: "Building Machine Learning Pipelines with Kubeflow Part 3"
date: 2021-04-21T18:29:47
slug: "building-machine-learning-pipelines-with-kubeflow-part-3"
author: "SUSE"
products: ["Kubernetes (generic)"]
tags: ["ai"]
content_type: "tutorial"
draft: true
migration:
  wp_id: 98152
  original_url: "https://www.suse.com/c/rancher_blog/building-machine-learning-pipelines-with-kubeflow-part-3/"
  disposition: archive_redirect
  commercial: false
  outdated_reason: "Kubeflow and TensorFlow 2021 steps"
  redirect_target: "rancher.com/blog (hub)"
---

This post will show you how to serve a Tensorflow model with KFServing on Kubeflow.

In the [previous installment](/blog/building-machine-learning-pipelines-with-kubeflow/) in this series, we learned how to prepare a machine learning project for Kubeflow, construct a pipeline and execute the pipeline via the Kubeflow interface.

This was where we left off:

Here is what the pipeline does:

1. Git clone the repository
2. Download and preprocess the training and test data
3. Perform model training followed by model evaluation. Once that is done, export the model into a `SavedModel`.

## What’s a SavedModel?

In TensorFlow terms, this means that we need to export the model into a *SavedModel*. This serialization operation stores the model’s trained weights and the exact TensorFlow operations.

This is not the end of the story. Now that we have a `SavedModel`, what’s next?

Well, we need to make it do something useful. That’s where *Model Serving* comes in.

## What’s Model Serving, Anyway?

Model serving is taking your trained machine learning model and making it do useful stuff. In our case, it’s being able to take an image of a piece of clothing and classify it correctly. But how do you expose the model behind a service so that others can use it? Enter the *Model Server*.

## What’s a Model Server and Why You Might Need One

Now, you might think: I can always write my own model server! Sure you can. It is relatively easy to use something like Flask, take an image as an input, pass it to the model, and translate the model's prediction into JSON and use that as the response. However, the devil is in the details. For example, take a look at some of the listed features of the [TensorFlow Serving](https://github.com/tensorflow/serving):

- Can serve multiple models or multiple versions of the same model simultaneously
- Exposes both gRPC as well as HTTP inference endpoints
- Allows deployment of new model versions without changing any client code
- Supports canarying new versions and A/B testing experimental models
- Adds minimal latency to inference time due to efficient, low-overhead implementation
- Features a scheduler that groups individual inference requests into batches for joint execution on GPU, with configurable latency controls

This is, of course, not limited to TensorFlow Serving. There are many capable model servers out there too. It is not trivial to write a performant model server that can handle production needs. Now let’s see how we can serve a model with Tensorflow Serving.

## Getting the Code

In case you are following along, you can download the code from GitHub:

```
% git clone https://github.com/benjamintanweihao/kubeflow-mnist.git
```

### Step 4: Serving the Model

If you have been following along from the previous article, the output from the Training and Evaluation step would be the `SavedModel`. If case you don’t have it, you can use this [one](https://github.com/benjamintanweihao/kubeflow-mnist/blob/43420b9168c32bd1caac116f30d205e9dd737967/fmnist.zip).

Before we figure out how to deploy the model on Kubeflow, we can take the `SavedModel` and test it on a TensorFlow Serving container image. From there, we can test that model prediction works. If so, we can move on to writing the pipeline component for model serving.

In the project root directory, run the following command to launch TensorFlow Serving and point it to the directory of the exported model:

This post will show you how to serve a Tensorflow model with KFServing on Kubeflow.

In the [previous installment](/blog/building-machine-learning-pipelines-with-kubeflow/) in this series, we learned how to prepare a machine learning project for Kubeflow, construct a pipeline and execute the pipeline via the Kubeflow interface.

This was where we left off:

Here is what the pipeline does:

1. Git clone the repository
2. Download and preprocess the training and test data
3. Perform model training followed by model evaluation. Once that is done, export the model into a `SavedModel`.

## What’s a SavedModel?

In TensorFlow terms, this means that we need to export the model into a *SavedModel*. This serialization operation stores the model’s trained weights and the exact TensorFlow operations.

This is not the end of the story. Now that we have a `SavedModel`, what’s next?

Well, we need to make it do something useful. That’s where *Model Serving* comes in.

## What’s Model Serving, Anyway?

Model serving is taking your trained machine learning model and making it do useful stuff. In our case, it’s being able to take an image of a piece of clothing and classify it correctly. But how do you expose the model behind a service so that others can use it? Enter the *Model Server*.

## What’s a Model Server and Why You Might Need One

Now, you might think: I can always write my own model server! Sure you can. It is relatively easy to use something like Flask, take an image as an input, pass it to the model, and translate the model's prediction into JSON and use that as the response. However, the devil is in the details. For example, take a look at some of the listed features of the [TensorFlow Serving](https://github.com/tensorflow/serving):

- Can serve multiple models or multiple versions of the same model simultaneously
- Exposes both gRPC as well as HTTP inference endpoints
- Allows deployment of new model versions without changing any client code
- Supports canarying new versions and A/B testing experimental models
- Adds minimal latency to inference time due to efficient, low-overhead implementation
- Features a scheduler that groups individual inference requests into batches for joint execution on GPU, with configurable latency controls

This is, of course, not limited to TensorFlow Serving. There are many capable model servers out there too. Writing a performant model server that can handle production needs is not trivial. Now let’s see how we can serve a model with Tensorflow Serving.

## Getting the Code

In case you are following along, you can download the code from GitHub:

```
% git clone https://github.com/benjamintanweihao/kubeflow-mnist.git
```

### Step 4: Serving the Model

If you have been following along from the previous article, the output from the Training and Evaluation step would be the `SavedModel`. If case you don’t have it, you can use this [one](https://github.com/benjamintanweihao/kubeflow-mnist/blob/43420b9168c32bd1caac116f30d205e9dd737967/fmnist.zip).

Before we figure out how to deploy the model on Kubeflow, we can take the `SavedModel` and test it on a TensorFlow Serving container image. From there, we can test that model prediction works. If so, we can move on to writing the pipeline component for model serving.

In the project root directory, run the following command to launch TensorFlow Serving and point it to the directory of the exported model:

```
docker run -t --rm -p 8501:8501 -v "$PWD/export:/models/" -e MODEL_NAME=mnist \ tensorflow/serving:1.14.0
```

If everything went well, you should see the following output near the end:

```
2021-01-31 09:00:39.941486: I tensorflow_serving/core/loader_harness.cc:86] Successfully loaded servable version {name: mnist version: 1611590079} 2021-01-31 09:00:39.949655: I tensorflow_serving/model_servers/server.cc:324] Running gRPC ModelServer at 0.0.0.0:8500 ... [warn] getaddrinfo: address family for nodename not supported 2021-01-31 09:00:39.956144: I tensorflow_serving/model_servers/server.cc:344] Exporting HTTP/REST API at:localhost:8501 ... [evhttp_server.cc : 239] RAW: Entering the event loop ...
```

Now, execute the script `serving_demo.py` and you should see the following result displayed:

![img](https://media1-production-mightynetworks.imgix.net/asset/22868651/1619020947078.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

This script randomly picks an image from the test dataset (since it is already formatted nicely in the way the model expects), creates a request that the TensorFlow Serving API expects, performs the prediction, and returns the result as shown.

Now that we have established that we can successfully make requests, it’s time to work on the servable component!

### Step 5: Create the Servable Component

Before we get into writing the component, there are a few things that we need to take care of to get serving the work done properly. This is a good time as any to talk about KFServing.

### KFServing

KFServing provides a Custom Resource Definition to serve ML models on most of the popular frameworks and has excellent support for the popular ones such as TensorFlow, PyTorch and ScikitLearn. The following diagram is a good illustration:

![](https://media1-production-mightynetworks.imgix.net/asset/22868660/1619020947611.jpeg?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)In our case, model assets (represented by the grey cylinder on the right) are stored on MinIO.

A couple of things need to happen before this would work.

1. First, in the Rancher UI, click on **Projects/Namespace**. Search for the `Kubeflow` namespace, then select **Edit** and move it to **Default** as shown in the diagram below. This will allow Rancher to manage Kubeflow’s `ConfigMaps` and `Secrets` among other things.

![0](https://media1-production-mightynetworks.imgix.net/asset/22868680/1619020964129.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Next, click on **Add Namespace**.  Create a namepace with `kfserving-inference-service` and label the namespace with the `serving.kubeflow.org/inferenceservice=enabled` label. Note that the namespace shouldn’t have a `control-plane` level. This could happen if you might be reusing an existing namespace. (If you are using `kfserving-inference-service` chances are you don’t have to worry about this.)  The Rancher UI makes this super simple without having to type any commands:

![](https://media1-production-mightynetworks.imgix.net/asset/22868658/1619020947654.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Just as you did with the `kubeflow`namespace, add the `kfserving-inference-service` to the `Default` project:

![](https://media1-production-mightynetworks.imgix.net/asset/22868656/1619020947685.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

2. Within this namespace, you would need to create two things:

a) A Secret that would contain the MinIO credentials:

Under **Resources**, select **Secrets**, followed by **Add Secret**. Fill in the following:

![](https://media1-production-mightynetworks.imgix.net/asset/22868659/1619020948416.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

For the `awsSecretAccessKey` fill in the following value `minio123`, and for the `awsAccessKeyID`  fill in `minio`. These are the default values used by MinIO.

b) A ServiceAccount that points to this Secret.

Since Rancher doesn’t have a menu option for Service Accounts, we will need to create it ourselves. No worries though, since the Rancher UI has `kubectl` baked in. In the top-level menu bar, select the **first** option. Under `clusters`, select `local`. Your page should look like this:

![](https://media1-production-mightynetworks.imgix.net/asset/22868661/1619020949105.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Now, select **Launch kubectl**:

From the terminal, create a file named `sa.yaml` and fill it in with the following:

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: sa
  namespace: kfserving-inference-service
secrets:
  - name: minio-s3-secret
```

![](https://media1-production-mightynetworks.imgix.net/asset/22868665/1619020954517.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Save the file, and run the following command:

```
kubectl create -f sa.yaml
```

You should see `serviceaccount/sa created` as the output. You need to create a Service Account because the Serving Op will then reference this `ServiceAccount` to access the MinIO credentials.

3. Make sure there is support for TensorFlow 1.14 and 1.14-gpu by checking the `ConfigMap`.

Go to the top-level menu, select the first option, and ensure that `Default` is selected. Then, select **Resources** followed by **Config**. Use the *Search* menu near the top right and search for `inferenceservice-config`:

![](https://media1-production-mightynetworks.imgix.net/asset/22868667/1619020955263.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Click on the `inferenceservice-config` link followed by `Edit`. Scroll down to the `predictors` section and make sure that it includes `1.14.0` and `1.14.0-gpu`. If there are other versions of TensorFlow that you want to use, this is the place to add it:

![](https://media1-production-mightynetworks.imgix.net/asset/22868671/1619020955309.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

4. Next, we need to create a bucket in MinIO. This means that we need to access it first. Under **Resources**, select

**Workloads**. Under the search, type in *minio* and click on the single result:

![](https://media1-production-mightynetworks.imgix.net/asset/22868674/1619020955926.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

From here, we know that the port is `9000`. What about the IP address? Click on the link to the running MinIO pod:

![](https://media1-production-mightynetworks.imgix.net/asset/22868676/1619020960295.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Here, we can see the Pod IP. Go to your browser and enter `http://<pod_ip>:9000`:

![](https://media1-production-mightynetworks.imgix.net/asset/22868681/1619020963265.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Let’s create a bucket called `servedmodels`. Select the red `+` button and the bottom right followed by `Create Bucket` and type in `servedmodels`. This should be the result:

![](https://media1-production-mightynetworks.imgix.net/asset/22868679/1619020963635.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

Now, before we write the pipeline, let’s ensure the inference service and our setup have worked. What we can do is upload the model that we have trained previously onto the bucket:

Unfortunately, the MinIO interface doesn’t allow you to upload an entire folder. But we can do it relatively easily using the MinIO client Docker image:

```
docker pull minio/mc docker run -it --entrypoint=/bin/bash -v $PWD:/kubeflow-mnist/ minio/mc // Here, adapt the IP address to the one you found just now.
# mc alias set minio http://10.43.47.20:9000 minio minio123
# cd kubeflow-mnist/fmnist/saved_models
# mc cp --recursive 1611590079/ minio/servedmodels/fmnist/1611590079/saved_model
```

If you refresh, you should see the copied files:

![](https://media1-production-mightynetworks.imgix.net/asset/22868678/1619020963665.png?ixlib=rails-0.3.0&fm=jpg&q=75&auto=format&w=1400&h=1400&fit=max)

### Serving Component

Finally, after all that set up work, here’s the serving component in all its glory:

```
def serving_op(image: str,               pvolume: PipelineVolume,               bucket_name: str,               model_name: str,               model_version: str):    namespace = 'kfserving-inference-service'    runtime_version = '1.14.0'    service_account_name = 'sa'
    storage_uri = f"s3://{bucket_name}/{model_name}/saved_model/{model_version}"
    op = dsl.ContainerOp(        name='serve model',        image=image,        command=[CONDA_PYTHON_CMD, f"{PROJECT_ROOT}/serving/kfs_deployer.py"],        arguments=[            '--namespace', namespace,            '--name', f'{model_name}-{model_version}-1',            '--storage_uri', storage_uri,            '--runtime_version', runtime_version,            '--service_account_name', service_account_name        ],        container_kwargs={'image_pull_policy': 'IfNotPresent'},        pvolumes={"/workspace": pvolume}    )     return op
```

Most of the hard work is delegated to `kfs_deployer.py`:

```
def create_inference_service(namespace: str,                             name: str,                             storage_uri: str,                             runtime_version: str,                             service_account_name: str):    api_version = constants.KFSERVING_GROUP + '/' + constants.KFSERVING_VERSION    default_endpoint_spec = V1alpha2EndpointSpec(        predictor=V1alpha2PredictorSpec(            min_replicas=1,            service_account_name=service_account_name,            tensorflow=V1alpha2TensorflowSpec(                runtime_version=runtime_version,                storage_uri=storage_uri,                resources=V1ResourceRequirements(                    requests={'cpu': '100m', 'memory': '1Gi'},                    limits={'cpu': '100m', 'memory': '1Gi'}))))     isvc = V1alpha2InferenceService(api_version=api_version,                                    kind=constants.KFSERVING_KIND,                                    metadata=client.V1ObjectMeta(                                        name=name, namespace=namespace),                                    spec=V1alpha2InferenceServiceSpec(default=default_endpoint_spec))    KFServing = KFServingClient()    KFServing.create(isvc)    KFServing.get(name, namespace=namespace, watch=True, timeout_seconds=300)
```

The whole point of `kfs_deployer.py` is to construct an *Inference\_Service* that serves the version of the model that we point to.  The full source of `kfs_deployer.py` can be found [here](https://github.com/benjamintanweihao/kubeflow-mnist/blob/master/serving/kfs_deployer.py).

## A Minimal Serving Pipeline

Instead of showing you the entire pipeline from data ingestion to model serving, here’s a minimal serving pipeline that contains two components: Git clone and the serving component. However, this should be enough information for you to build out the full pipeline!

```
@dsl.pipeline(    name='Serving Pipeline',    description='This is a single component Pipeline for Serving'
)
def serving_pipeline(        image: str = 'benjamintanweihao/kubeflow-mnist',        repo_url: str = 'https://github.com/benjamintanweihao/kubeflow-mnist.git', ):    model_name = 'fmnist'    export_bucket = 'servedmodels'    model_version = '1611590079'
    git_clone = git_clone_op(repo_url=repo_url)     serving_op(image=image,               pvolume=git_clone.pvolume,               bucket_name=export_bucket,               model_name=model_name,               model_version=model_version) 
if __name__ == '__main__':    kfp.compiler.Compiler().compile(serving_pipeline, 'serving-pipeline.zip')
```

Executing the script invokes the compiler, resulting in `serving-pipeline.zip`. Then upload the file via the Kubeflow UI and create a run. If everything went well, an Inference Service would be deployed with the Fashion MNIST model being served.

## Conclusion

In this article, we finally tackled the end of the pipeline. Making the model servable is very important since it’s the step that makes the machine learning model useful, yet it is a step that is often ignored.

Kubeflow comes built-in with a CRD for model serving, KFServing, that can handle a wide variety of machine learning frameworks, not just TensorFlow. KFServing brings all the benefits that model servers have to your Kubernetes cluster.

I hope you found this series of articles useful! Putting Machine Learning models to production is certainly not a trivial task, but tools like Kubeflow provide a good framework for structuring your machine learning projects and pipelines into something composable and coherent.
