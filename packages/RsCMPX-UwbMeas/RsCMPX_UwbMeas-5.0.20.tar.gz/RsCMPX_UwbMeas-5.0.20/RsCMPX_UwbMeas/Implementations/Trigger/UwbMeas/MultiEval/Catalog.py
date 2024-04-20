from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CatalogCls:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def get_source(self) -> List[str]:
		"""SCPI: TRIGger:UWB:MEASurement<Instance>:MEValuation:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.uwbMeas.multiEval.catalog.get_source() \n
		Lists all trigger source values that can be set using method RsCMPX_UwbMeas.Trigger.UwbMeas.MultiEval.source. \n
			:return: trigger_sources: Comma-separated list of all supported values, one string per value.
		"""
		response = self._core.io.query_str('TRIGger:UWB:MEASurement<Instance>:MEValuation:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
