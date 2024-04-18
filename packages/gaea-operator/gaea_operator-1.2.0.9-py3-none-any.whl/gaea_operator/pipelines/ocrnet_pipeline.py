#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @File    : ocrnet_pipeline.py
"""
from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from gaea_operator.utils import DEFAULT_TRAIN_CONFIG_FILE_NAME, \
    DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME, \
    ModelTemplate
from gaea_operator.components.transform_eval import transform_eval_step
from gaea_operator.components.package import package_step
from gaea_operator.components.inference import inference_step

@Pipeline(
    name="ocrnet",
    cache_options=CacheOptions(enable=False),
)
def pipeline(accelerator: str = "T4",
             windmill_ak: str = "",
             windmill_sk: str = "",
             windmill_endpoint: str = "",
             experiment_kind: str = "",
             experiment_name: str = "",
             modelstore_name: str = "",
             tracking_uri: str = "",
             project_name: str = "",
             train_dataset_name: str = "",
             val_dataset_name: str = "",
             train_model_name: str = "",
             train_model_display_name: str = "",
             eval_dataset_name: str = "",
             transform_model_name: str = "",
             transform_model_display_name: str = "",
             ensemble_model_name: str = "",
             ensemble_model_display_name: str = ""):
    """
    Pipeline for ocrnet training eval transform.
    """
    base_params = {"flavour": "c8m32gpu1",
                   "queue": "training",
                   "windmill_ak": windmill_ak,
                   "windmill_sk": windmill_sk,
                   "windmill_endpoint": windmill_endpoint,
                   "experiment_name": experiment_name,
                   "experiment_kind": experiment_kind,
                   "tracking_uri": tracking_uri,
                   "project_name": project_name,
                   "model_store_name": modelstore_name}
    base_env = {"PF_JOB_FLAVOUR": "{{flavour}}",
                "PF_JOB_QUEUE_NAME": "{{queue}}",
                "WINDMILL_AK": "{{windmill_ak}}",
                "WINDMILL_SK": "{{windmill_sk}}",
                "WINDMILL_ENDPOINT": "{{windmill_endpoint}}",
                "EXPERIMENT_KIND": "{{experiment_kind}}",
                "EXPERIMENT_NAME": "{{experiment_name}}",
                "TRACKING_URI": "{{tracking_uri}}",
                "PROJECT_NAME": "{{project_name}}"}

    train_params = {"train_dataset_name": train_dataset_name,
                    "val_dataset_name": val_dataset_name,
                    "model_name": train_model_name,
                    "model_display_name": train_model_display_name,
                    "advanced_parameters": '{"iters":"100",'
                                                 '"lr_scheduler.learning_rate":"0.001",'
                                                 '"eval_height":"512",'
                                                 '"eval_width":"512",'
                                                 '"batch_size":"6",'
                                                 '"model_type":"ocrnet"}',
                    "advanced_parameters2": '{"iters":"100",'
                                                 '"lr_scheduler.learning_rate":"0.001",'
                                                 '"eval_height":"512",'
                                                 '"eval_width":"512",'
                                                 '"batch_size":"6",'
                                                 '"model_type":"ocrnet"}'}
    train_env = {"TRAIN_DATASET_NAME": "{{train_dataset_name}}",
                 "VAL_DATASET_NAME": "{{val_dataset_name}}",
                 "MODEL_NAME": "{{model_name}}",
                 "MODEL_DISPLAY_NAME": "{{model_display_name}}",
                 "ADVANCED_PARAMETERS": "{{advanced_parameters2}}"}
    train_env.update(base_env)
    train_params.update(base_params)
    train = ContainerStep(name="train",
                          docker_env="iregistry.baidu-int.com/windmill-public/train:v1.2.28",
                          parameters=train_params,
                          env=train_env,
                          outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                          command=f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                  f'python3 -m gaea_operator.components.train.ocrnet '
                                  f'--output-model-uri={{{{output_model_uri}}}} '
                                  f'--output-uri={{{{output_uri}}}} '
                                  f'$package_path/paddleseg/tools/train.py '
                                  f'--config {{{{output_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                  f'--do_eval '
                                  f'--save_dir={{{{output_model_uri}}}}')

    eval_params = {"dataset_name": eval_dataset_name}
    eval_env = {"DATASET_NAME": "{{dataset_name}}"}
    eval_env.update(base_env)
    eval_params.update(base_params)
    eval = ContainerStep(name="eval",
                         docker_env="iregistry.baidu-int.com/windmill-public/train:v1.2.28",
                         parameters=eval_params,
                         env=eval_env,
                         inputs={"input_model_uri": train.outputs["output_model_uri"]},
                         outputs={"output_uri": Artifact(), "output_dataset_uri": Artifact()},
                         command=f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                 f'python3 -m gaea_operator.components.eval.ocrnet '
                                 f'--input-model-uri={{{{input_model_uri}}}} '
                                 f'--output-uri={{{{output_uri}}}} '
                                 f'--output-dataset-uri={{{{output_dataset_uri}}}} '
                                 f'$package_path/paddleseg/tools/val.py '
                                 f'--config {{{{input_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                 f'--model_path={{{{input_model_uri}}}}/{DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME} '
                                 f'--save_dir={{{{output_uri}}}}')

    transform_params = {"transform_model_name": transform_model_name,
                        "transform_model_display_name": transform_model_display_name,
                        "accelerator": "T4",
                        "advanced_parameters": '{"max_batch_size":"1",'
                                                '"precision":"fp16",'
                                                '"eval_height":"512",'
                                                '"eval_width":"512",'
                                                '"source_framework":"paddle",'
                                                '"model_type":"ocrnet"}',
                        "advanced_parameters1": '{"max_batch_size":"1",'
                                                '"precision":"fp16",'
                                                '"eval_height":"512",'
                                                '"eval_width":"512",'
                                                '"source_framework":"paddle",'
                                                '"model_type":"ocrnet"}'}
    transform_env = {"TRANSFORM_MODEL_NAME": "{{transform_model_name}}",
                     "TRANSFORM_MODEL_DISPLAY_NAME": "{{transform_model_display_name}}",
                     "ACCELERATOR": "{{accelerator}}",
                     "ADVANCED_PARAMETERS": "{{advanced_parameters1}}"}
    transform_env.update(base_env)
    transform_params.update(base_params)
    transform = ContainerStep(name="transform",
                              docker_env="iregistry.baidu-int.com/windmill-public/transform:v1.2.5",
                              env=transform_env,
                              parameters=transform_params,
                              inputs={"input_model_uri": train.outputs["output_model_uri"]},
                              outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                              command=f'python3 -m gaea_operator.components.transform.ocrnet '
                                      f'--input-model-uri={{{{input_model_uri}}}} '
                                      f'--output-uri={{{{output_uri}}}} '
                                      f'--output-model-uri={{{{output_model_uri}}}}').after(eval)

    transform_eval = transform_eval_step(algorithm=ModelTemplate.OCRNET_NAME,
                                         windmill_ak=windmill_ak,
                                         windmill_sk=windmill_sk,
                                         windmill_endpoint=windmill_endpoint,
                                         experiment_kind=experiment_kind,
                                         experiment_name=experiment_name,
                                         tracking_uri=tracking_uri,
                                         project_name=project_name,
                                         accelerator=accelerator,
                                         eval_step=eval,
                                         transform_step=transform)

    package = package_step(algorithm=ModelTemplate.OCRNET_NAME,
                           windmill_ak=windmill_ak,
                           windmill_sk=windmill_sk,
                           windmill_endpoint=windmill_endpoint,
                           experiment_kind=experiment_kind,
                           experiment_name=experiment_name,
                           tracking_uri=tracking_uri,
                           project_name=project_name,
                           accelerator=accelerator,
                           transform_step=transform,
                           transform_eval_step=transform_eval,
                           ensemble_model_name=ensemble_model_name,
                           ensemble_model_display_name=ensemble_model_display_name)

    inference = inference_step(windmill_ak=windmill_ak,
                               windmill_sk=windmill_sk,
                               windmill_endpoint=windmill_endpoint,
                               experiment_kind=experiment_kind,
                               experiment_name=experiment_name,
                               tracking_uri=tracking_uri,
                               project_name=project_name,
                               accelerator=accelerator,
                               eval_step=eval,
                               package_step=package)

    return inference.outputs["output_uri"]


if __name__ == "__main__":
    pipeline_client = pipeline(
        accelerator="v100",
        windmill_ak="1cb1860b8bc848298050edffa2ef9e16",
        windmill_sk="51a7a74c9ef14063a6892d08dd19ffbf",
        windmill_endpoint="http://10.27.240.45:8340",
        experiment_kind="Aim",
        experiment_name="ocrnet",
        tracking_uri="aim://10.27.240.45:8329",
        project_name="workspaces/default/projects/universal-ocrnet",
        train_dataset_name="workspaces/default/projects/universal-ocrnet/datasets/train/versions/1",
        val_dataset_name="workspaces/default/projects/universal-ocrnet/datasets/train/versions/1",
        eval_dataset_name="workspaces/default/projects/universal-ocrnet/datasets/train/versions/1",
        train_model_name="workspaces/default/modelstores/universal-ocrnet/models/ocrnet-model",
        train_model_display_name="ocrnet",
        transform_model_name="workspaces/default/modelstores/universal-ocrnet/models/ocrnet-t4",
        transform_model_display_name="ocrnet-t4",
        ensemble_model_name="workspaces/default/modelstores/universal-ocrnet/models/ocrnet-ensemble",
        ensemble_model_display_name="ocrnet-ensemble"
        )
    pipeline_client.compile(save_path="./ocrnet_pipeline.yaml")
    _, run_id = pipeline_client.run(fs_name="defaultdev")
    print('run-id: {}'.format(run_id))
