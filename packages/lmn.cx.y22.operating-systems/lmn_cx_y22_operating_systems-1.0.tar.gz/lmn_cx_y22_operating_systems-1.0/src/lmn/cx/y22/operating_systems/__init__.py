# SPDX-FileCopyrightText: 2024 Alex Lemna
# SPDX-License-Identifier: 0BSD OR MIT OR Apache-2.0
from ._operating_systems import OS, OperatingSystem, __version__, determine_os

__all__ = ["determine_os", "OperatingSystem", "OS"]
__version_info__ = tuple(int(n) for n in __version__.split(".") if n.isdigit())
