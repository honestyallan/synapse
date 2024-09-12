#
# This file is licensed under the Affero General Public License (AGPL) version 3.
#
# Copyright 2015 Niklas Riekenbrauck
# Copyright (C) 2023 New Vector, Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# See the GNU Affero General Public License for more details:
# <https://www.gnu.org/licenses/agpl-3.0.html>.
#
# Originally licensed under the Apache License, Version 2.0:
# <http://www.apache.org/licenses/LICENSE-2.0>.
#
# [This file includes modifications made by New Vector Limited]
#
#

from typing import Any

from synapse.types import JsonDict

from ._base import Config


class CUSTOMJWTConfig(Config):
    section = "custom_jwt"

    def read_config(self, config: JsonDict, **kwargs: Any) -> None:
        custom_jwt_config = config.get("custom_jwt", {})
        if custom_jwt_config:
            self.custom_jwt_enabled = custom_jwt_config.get("enabled", False)
            self.custom_jwt_algorithm = custom_jwt_config["algorithm"]
            # The issuer and audiences are optional, if provided, it is asserted
            # that the claims exist on the JWT.
            self.custom_jwt_issuer = custom_jwt_config.get("issuer")
            self.custom_jwt_audiences = custom_jwt_config.get("audiences")
            # check_requirements("jwt")
        else:
            self.custom_jwt_enabled = False
            self.custom_jwt_algorithm = None
            self.custom_jwt_issuer = None
            self.custom_jwt_audiences = None
