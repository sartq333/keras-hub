"""Mixtral model preset configurations."""

# Metadata for loading pretrained model weights.
backbone_presets = {
    "gpt2_base_en": {
        "metadata": {
            "description": (
                "mixtral model"
            ),
            "params": 56000000000 ,
            "path": "mixtral",
        },
        "kaggle_handle": "kaggle://keras/mistral/keras/mixtral_8x7b-instruct-v0.1-hf/1",
    }
}