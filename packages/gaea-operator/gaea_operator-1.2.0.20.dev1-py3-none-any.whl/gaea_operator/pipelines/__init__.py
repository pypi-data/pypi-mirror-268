from gaea_operator.pipelines.ocrnet_pipeline import pipeline as ocrnet_pipeline
from gaea_operator.pipelines.ppyoloe_plus_pipeline import pipeline as ppyoloe_plus_pipeline
from gaea_operator.pipelines.resnet_pipeline import pipeline as resnet_pipeline

ppls = [ocrnet_pipeline(), ppyoloe_plus_pipeline(), resnet_pipeline()]