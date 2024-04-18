#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/10
# @Author  : yanxiaodong
# @File    : ppyoloe_plus_m_pipeline.py
"""
from paddleflow.pipeline import Pipeline
from paddleflow.pipeline import CacheOptions
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact
from paddleflow.pipeline import ExtraFS

from gaea_operator.utils import DEFAULT_TRAIN_CONFIG_FILE_NAME, \
    DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME, \
    ModelTemplate
from gaea_operator.components.transform_eval import transform_eval_step
from gaea_operator.components.package import package_step
from gaea_operator.components.inference import inference_step


@Pipeline(
    name="ppyoloe_plus_m",
    cache_options=CacheOptions(enable=False),
)
def pipeline(accelerator: str = "T4",
             extra_fs_name: str = "vistudio",
             extra_fs_mount_path: str = "/home/paddleflow/storage/mnt/fs-root-vistudio",
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
             base_train_dataset_name: str = "",
             base_val_dataset_name: str = "",
             train_model_name: str = "",
             train_model_display_name: str = "",
             eval_dataset_name: str = "",
             transform_model_name: str = "",
             transform_model_display_name: str = "",
             ensemble_model_name: str = "",
             ensemble_model_display_name: str = ""):
    """
    Pipeline for ppyoloe_plus_m training eval transform transform-eval package inference.
    """
    base_params = {"flavour": "c4m16gpu1",
                   "queue": "qtrain",
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
                    "base_train_dataset_name": base_train_dataset_name,
                    "base_val_dataset_name": base_val_dataset_name,
                    "model_name": train_model_name,
                    "model_display_name": train_model_display_name,
                    "advanced_parameters": '{"epoch":"1",'
                                           '"LearningRate.base_lr":"0.00001",'
                                           '"worker_num":"1",'
                                           '"eval_size":"640*640",'
                                           '"TrainReader.batch_size":"8",'
                                           '"model_type":"ppyoloe_m"}'}
    train_env = {"TRAIN_DATASET_NAME": "{{train_dataset_name}}",
                 "VAL_DATASET_NAME": "{{val_dataset_name}}",
                 "BASE_TRAIN_DATASET_NAME": "{{base_train_dataset_name}}",
                 "BASE_VAL_DATASET_NAME": "{{base_val_dataset_name}}",
                 "MODEL_NAME": "{{model_name}}",
                 "MODEL_DISPLAY_NAME": "{{model_display_name}}",
                 "ADVANCED_PARAMETERS": "{{advanced_parameters}}",
                 "PF_EXTRA_WORK_DIR": extra_fs_mount_path}
    train_env.update(base_env)
    train_params.update(base_params)
    train = ContainerStep(name="train",
                          docker_env="iregistry.baidu-int.com/windmill-public/train/paddlepaddle:v1.2.0.1",
                          parameters=train_params,
                          env=train_env,
                          extra_fs=[ExtraFS(name=extra_fs_name, mount_path=extra_fs_mount_path)],
                          outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                          command=f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                  f'python3 -m gaea_operator.components.train.ppyoloe_plus '
                                  f'--output-model-uri={{{{output_model_uri}}}} '
                                  f'--output-uri={{{{output_uri}}}} '
                                  f'--log_dir={{{{output_uri}}}} '
                                  f'$package_path/paddledet/tools/train.py '
                                  f'-c {{{{output_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                  f'-o save_dir={{{{output_model_uri}}}}')

    eval_params = {"dataset_name": eval_dataset_name,
                   "advanced_parameters": '{"conf_threshold":"0.1",'
                                          '"iou_threshold":"0.50"}'}
    eval_env = {"DATASET_NAME": "{{dataset_name}}",
                "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    eval_env.update(base_env)
    eval_params.update(base_params)
    eval = ContainerStep(name="eval",
                         docker_env="iregistry.baidu-int.com/windmill-public/train/paddlepaddle:v1.2.0.1",
                         parameters=eval_params,
                         env=eval_env,
                         inputs={"input_model_uri": train.outputs["output_model_uri"]},
                         outputs={"output_uri": Artifact(), "output_dataset_uri": Artifact()},
                         command=f'package_path=$(python3 -c "import site; print(site.getsitepackages()[0])") && '
                                 f'python3 -m gaea_operator.components.eval.ppyoloe_plus '
                                 f'--input-model-uri={{{{input_model_uri}}}} '
                                 f'--output-uri={{{{output_uri}}}} '
                                 f'--output-dataset-uri={{{{output_dataset_uri}}}} '
                                 f'--log_dir={{{{output_uri}}}} '
                                 f'$package_path/paddledet/tools/eval.py '
                                 f'-c {{{{input_model_uri}}}}/{DEFAULT_TRAIN_CONFIG_FILE_NAME} '
                                 f'-o weights={{{{input_model_uri}}}}/{DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME}')

    transform_params = {"transform_model_name": transform_model_name,
                        "transform_model_display_name": transform_model_display_name,
                        "accelerator": "T4",
                        "advanced_parameters": '{"iou_threshold":"0.45",'
                                               '"conf_threshold":"0.1",'
                                               '"max_box_num":"30",'
                                               '"max_batch_size":"1",'
                                               '"precision":"fp16",'
                                               '"eval_size":"640*640",'
                                               '"source_framework":"paddle",'
                                               '"model_type":"ppyoloe_m"}'}
    transform_env = {"TRANSFORM_MODEL_NAME": "{{transform_model_name}}",
                     "TRANSFORM_MODEL_DISPLAY_NAME": "{{transform_model_display_name}}",
                     "ACCELERATOR": "{{accelerator}}",
                     "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
    transform_env.update(base_env)
    transform_params.update(base_params)
    transform = ContainerStep(name="transform",
                              docker_env="iregistry.baidu-int.com/windmill-public/transform:v1.2.0.1",
                              env=transform_env,
                              parameters=transform_params,
                              inputs={"input_model_uri": train.outputs["output_model_uri"]},
                              outputs={"output_model_uri": Artifact(), "output_uri": Artifact()},
                              command=f'python3 -m gaea_operator.components.transform.ppyoloe_plus '
                                      f'--input-model-uri={{{{input_model_uri}}}} '
                                      f'--output-uri={{{{output_uri}}}} '
                                      f'--output-model-uri={{{{output_model_uri}}}}').after(eval)

    transform_eval = transform_eval_step(algorithm=ModelTemplate.PPYOLOE_PLUS_NAME,
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

    package = package_step(algorithm=ModelTemplate.PPYOLOE_PLUS_NAME,
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
        accelerator="T4",
        windmill_ak="a1a9069e2b154b2aa1a83ed12316d163",
        windmill_sk="eefac23d2660404e93855197ce60efb3",
        windmill_endpoint="http://10.27.240.5:8340",
        experiment_kind="Aim",
        experiment_name="ppyoloe_plus_m",
        tracking_uri="aim://10.27.240.5:8329",
        project_name="workspaces/internal/projects/proj-o97H2oAE",
        train_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        val_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        eval_dataset_name="workspaces/internal/projects/proj-o97H2oAE/datasets/ds-UCKo4LyJ/versions/1",
        train_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus",
        train_model_display_name="ppyoloe-plus",
        transform_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus-t4",
        transform_model_display_name="ppyoloe-plus-t4",
        ensemble_model_name="workspaces/internal/modelstores/ms-6TDGY7Hv/models/ppyoloe-plus-ensemble",
        ensemble_model_display_name="ppyoloe-plus-ensemble")
    pipeline_client.compile(save_path="../ppyoloe_plus_m_pipeline.yaml")
    _, run_id = pipeline_client.run(fs_name="vistudio")
