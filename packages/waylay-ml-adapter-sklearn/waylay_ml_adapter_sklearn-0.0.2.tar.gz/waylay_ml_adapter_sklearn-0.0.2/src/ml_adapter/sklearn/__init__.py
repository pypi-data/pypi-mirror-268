"""ML Adapter for sklearn."""

from ml_adapter.api.data.common import V1_PROTOCOL
from ml_adapter.base.assets.manifest import (
    default_plug_v1_script,
    default_webscript_script,
)
from ml_adapter.numpy import V1NumpyModelAdapter

SKLEARN_REQUIREMENTS = [
    *V1NumpyModelAdapter.DEFAULT_REQUIREMENTS,
    "scikit-learn",
    "waylay-ml-adapter-sklearn",
]


class V1SklearnPredictAdapter(V1NumpyModelAdapter):
    """ModelAdapter for sklearn models with a 'predict' method."""

    model_method = "predict"
    DEFAULT_SCRIPT = {
        "webscript": default_webscript_script(
            "ml_adapter.sklearn", "V1SklearnPredictAdapter"
        ),
        "plug": default_plug_v1_script("ml_adapter.sklearn", "V1SklearnPredictAdapter"),
    }
    DEFAULT_REQUIREMENTS = SKLEARN_REQUIREMENTS


class V1SklearnPredictProbaAdapter(V1NumpyModelAdapter):
    """ModelAdapter for sklearn models with a 'predict_proba' method."""

    model_method = "predict_proba"
    DEFAULT_SCRIPT = {
        "webscript": default_webscript_script(
            "ml_adapter.sklearn", "V1SklearnPredictProbaAdapter"
        ),
        "plug": default_plug_v1_script(
            "ml_adapter.sklearn", "V1SklearnPredictProbaAdapter"
        ),
    }
    DEFAULT_REQUIREMENTS = SKLEARN_REQUIREMENTS


__all__ = [
    "V1_PROTOCOL",
    "default_webscript_script",
    "default_plug_v1_script",
    "V1NumpyModelAdapter",
    "V1SklearnPredictAdapter",
    "V1SklearnPredictProbaAdapter",
]
