from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RangeCls:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, min_py: int, max_py: int) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency:RANGe \n
		Snippet: driver.configure.uwbMeas.rfSettings.frequency.range.set(min_py = 1, max_py = 1) \n
		No command help available \n
			:param min_py: No help available
			:param max_py: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('min_py', min_py, DataType.Integer), ArgSingle('max_py', max_py, DataType.Integer))
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency:RANGe {param}'.rstrip())

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Response structure. Fields: \n
			- Min_Py: int: No parameter help available
			- Max_Py: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Min_Py'),
			ArgStruct.scalar_int('Max_Py')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Min_Py: int = None
			self.Max_Py: int = None

	def get(self) -> RangeStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency:RANGe \n
		Snippet: value: RangeStruct = driver.configure.uwbMeas.rfSettings.frequency.range.get() \n
		No command help available \n
			:return: structure: for return value, see the help for RangeStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:UWB:MEASurement<Instance>:RFSettings:FREQuency:RANGe?', self.__class__.RangeStruct())
