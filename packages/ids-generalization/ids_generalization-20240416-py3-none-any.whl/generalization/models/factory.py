"""
From the original paper (adapted):
1. Imagenet: Inception V3 (Szegedy et al., 2016)
2. CIFAR10: A smaller version of Inception,
            Alexnet (Krizhevsky et al., 2012),
            MLPs with 1 and 3 hidden layers

Author: Stepp1
"""

from functools import partial

JAX_ERROR = NotImplementedError("JAX models will not be implemented.")


class ModelFactory:
    def __init__(self):
        self.lib: str = None
        self.key = None
        self.model_creators_torch = {
            "resnet18": partial(create_resnet, resnet_size=18, lib="torch"),
            "resnet34": partial(create_resnet, resnet_size=34, lib="torch"),
            "alexnet": partial(create_alexnet, lib="torch"),
            "mlp_1x512": partial(
                create_mlp,
                hidden_sizes=[512],
                out_size=10,
                lib="torch",
            ),
            "mlp_3x512": partial(
                create_mlp,
                hidden_sizes=[512] * 3,
                out_size=10,
                lib="torch",
            ),
            "inception": partial(create_inception, lib="torch"),
        }

        try:
            assert self.lib != "jax"
        except AssertionError:
            raise JAX_ERROR

    def create_model(self, model_type: str, lib: str = None, **kwargs):
        self.lib = lib or self.lib
        if self.lib == "jax":
            raise JAX_ERROR
        elif self.lib == "torch":
            model = self.model_creators_torch[model_type](**kwargs)
        else:
            raise ValueError(f"Unknown library: {self.lib}")

        return model

    def get_cifar_models(self, model_name: str = None, lib: str = "torch", **kwargs):
        self.lib = lib or self.lib
        models = {
            "resnet18": self.create_model("resnet18", cifar=True, **kwargs),
            "alexnet": self.create_model("alexnet", cifar=True, **kwargs),
            "inception": self.create_model("inception", cifar=True, **kwargs),
            "mlp_3x512": self.create_model("mlp_3x512", **kwargs),
        }
        return models if model_name is None else {model_name: models[model_name]}

    def get_imagenet_models(self, model_name: str = None, lib: str = "torch"):
        self.lib = lib or self.lib
        models = {
            "inception": self.create_model("inception"),
            "resnet18": self.create_model("resnet18"),
            "resnet34": self.create_model("resnet34"),
        }

        return models if model_name is None else {model_name: models[model_name]}


def create_mlp(hidden_sizes: int, out_size: int, lib: str = "torch", **kwargs):
    if lib == "jax":
        raise JAX_ERROR
    elif lib == "torch":
        from .pytorch import mlp

        in_size = kwargs.get("in_size", 3 * 32 * 32)
        if "in_size" in kwargs:
            kwargs.pop("in_size")
        model = mlp(
            in_size=in_size, hidden_sizes=hidden_sizes, out_size=out_size, **kwargs
        )
    else:
        raise ValueError(f"Unknown library: {lib}")

    return model


def create_resnet(
    resnet_size: int = 18,
    weights: str = None,
    cifar: bool = False,
    lib: str = "torch",
    **kwargs,
):
    if lib == "jax":
        raise JAX_ERROR
    elif lib == "torch":
        from .pytorch import resnet

        if "in_size" in kwargs:
            kwargs.pop("in_size")
        model = resnet(resnet_size=resnet_size, weights=weights, cifar=cifar, **kwargs)
    else:
        raise ValueError(f"Unknown library: {lib}")

    return model


def create_alexnet(weights=None, cifar=False, lib="torch", **kwargs):
    if lib == "jax":
        raise JAX_ERROR
    elif lib == "torch":
        from .pytorch import alexnet

        if "in_size" in kwargs:
            kwargs.pop("in_size")
        model = alexnet(weights=weights, cifar=cifar, **kwargs)
    else:
        raise ValueError(f"Unknown library: {lib}")

    return model


def create_inception(weights=None, cifar=False, small="False", lib="torch", **kwargs):
    cifar = small or cifar
    if lib == "jax":
        raise NotImplementedError
    elif lib == "torch":
        from .pytorch import inception

        if "in_size" in kwargs:
            kwargs.pop("in_size")
        model = inception(weights=weights, cifar=cifar, **kwargs)
    else:
        raise ValueError(f"Unknown library: {lib}")

    return model
