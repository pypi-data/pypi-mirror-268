from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UwbMeasCls:
	"""UwbMeas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uwbMeas", core, parent)

	def get_spath(self) -> List[str]:
		"""SCPI: CATalog:UWB:MEAS<instance>:SPATh \n
		Snippet: value: List[str] = driver.catalog.uwbMeas.get_spath() \n
		Returns the names of the available RF connections. \n
			:return: name_signal_path: Comma-separated list of strings, one string per RF connection.
		"""
		response = self._core.io.query_str('CATalog:UWB:MEAS<Instance>:SPATh?')
		return Conversions.str_to_str_list(response)
