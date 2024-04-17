# ---------------------------------------------------------------------
# Copyright (c) 2024 Qualcomm Innovation Center, Inc. All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# ---------------------------------------------------------------------
# THIS FILE WAS AUTO-GENERATED. DO NOT EDIT MANUALLY.

import inspect
from unittest.mock import patch

import pytest

from qai_hub_models.models.squeezenet1_1 import Model


@pytest.fixture(autouse=True)
def mock_from_pretrained():
    """
    Model.from_pretrained() can be slow. Invoke it once and cache it so all invocations
    across all tests return the cached instance of the model.
    """
    sig = inspect.signature(Model.from_pretrained)
    mock = patch(
        "qai_hub_models.models.squeezenet1_1.Model.from_pretrained",
        return_value=Model.from_pretrained(),
    )
    mock_obj = mock.start()
    mock_obj.__signature__ = sig
