from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PpduCls:
	"""Ppdu commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppdu", core, parent)

	def get_records(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:RECords \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.ppdu.get_records() \n
		Defines the number of PPDUs for configuration. \n
			:return: number_pp_du: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:RECords?')
		return Conversions.str_to_int(response)

	def set_records(self, number_pp_du: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:RECords \n
		Snippet: driver.configure.uwbMeas.multiEval.ppdu.set_records(number_pp_du = 1) \n
		Defines the number of PPDUs for configuration. \n
			:param number_pp_du: No help available
		"""
		param = Conversions.decimal_value_to_str(number_pp_du)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:RECords {param}')

	def get_srecord(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:SRECord \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.ppdu.get_srecord() \n
		Selects one PPDU for display and configuration via the GUI. \n
			:return: selected_record: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:SRECord?')
		return Conversions.str_to_int(response)

	def set_srecord(self, selected_record: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:SRECord \n
		Snippet: driver.configure.uwbMeas.multiEval.ppdu.set_srecord(selected_record = 1) \n
		Selects one PPDU for display and configuration via the GUI. \n
			:param selected_record: No help available
		"""
		param = Conversions.decimal_value_to_str(selected_record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:SRECord {param}')

	def get_number(self) -> int:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer \n
		Snippet: value: int = driver.configure.uwbMeas.multiEval.ppdu.get_number() \n
		No command help available \n
			:return: ppdu_number: No help available
		"""
		response = self._core.io.query_str('CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer?')
		return Conversions.str_to_int(response)

	def set_number(self, ppdu_number: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer \n
		Snippet: driver.configure.uwbMeas.multiEval.ppdu.set_number(ppdu_number = 1) \n
		No command help available \n
			:param ppdu_number: No help available
		"""
		param = Conversions.decimal_value_to_str(ppdu_number)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PPDU:NUMBer {param}')
