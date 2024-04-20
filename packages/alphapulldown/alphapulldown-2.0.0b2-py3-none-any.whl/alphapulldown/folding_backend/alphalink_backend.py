""" Implements structure prediction backend using AlphaLink2.

    Copyright (c) 2024 European Molecular Biology Laboratory

    Author: Valentin Maurer <valentin.maurer@embl-hamburg.de>
            Dingquan Yu <dingquan.yu@embl-hamburg.de>
"""
from typing import Dict
from os.path import join, exists

from alphapulldown.objects import MultimericObject

from .folding_backend import FoldingBackend


class AlphaLinkBackend(FoldingBackend):
    """
    A backend class for running protein structure predictions using the AlphaLink model.
    """
    @staticmethod
    def setup(
        model_dir: str,
        crosslinks: str,
        model_name: str = "multimer_af2_crop",
        **kwargs,
    ) -> Dict:
        """
        Initializes and configures an AlphaLink model runner including crosslinking data.

        Parameters
        ----------
        model_name : str
            The name of the model to use for prediction. Set to be multimer_af2_crop as used in AlphaLink2
        model_dir : str
            Path to the pytorch checkpoint that corresponds to the neural network weights from AlphaLink2.
        crosslinks : str
            The path to the file containing crosslinking data.
        **kwargs : dict
            Additional keyword arguments for model configuration.

        Returns
        -------
        Dict
            A dictionary records the path to the AlphaLink2 neural network weights
            i.e. a pytorch checkpoint file, crosslink information,
            and Pytorch model configs
        """
        from unifold.config import model_config

        if not exists(model_dir):
            raise FileNotFoundError(
                f"AlphaLink2 network weight does not exist at: {model_dir}"
            )
        if not model_dir.endswith(".pt"):
            f"{model_dir} does not seem to be a pytorch checkpoint."

        configs = model_config(model_name)

        return {
            "crosslinks": crosslinks,
            "param_path": model_dir,
            "configs": configs,
        }

    @staticmethod
    def predict(
        configs: Dict,
        param_path: str,
        crosslinks: str,
        multimeric_object: MultimericObject,
        output_dir: str,
        **kwargs,
    ):
        """
        Predicts the structure of proteins using configured AlphaLink models.

        Parameters
        ----------
        model_config : Dict
            Configuration dictionary for the AlphaLink model obtained from
            py:meth:`AlphaLinkBackend.setup`.
        multimeric_object : MultimericObject
            An object containing the features of the multimeric protein to predict.
        output_dir : str
            The directory where the prediction outputs will be saved.
        **kwargs : dict
            Additional keyword arguments for prediction.
        """

        from unifold.alphalink_inference import alphalink_prediction

        alphalink_prediction(
            multimeric_object.feature_dict,
            join(output_dir, multimeric_object.description),
            input_seqs=multimeric_object.input_seqs,
            chain_id_map=multimeric_object.chain_id_map,
            configs=configs,
            param_path=param_path,
            crosslinks=crosslinks,
        )

    def postprocess(**kwargs) -> None:
        return None
