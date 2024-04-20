from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AreaCls:
	"""Area commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("area", core, parent)

	def set(self, enable_lower: bool, enable_upper: bool) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:AREA \n
		Snippet: driver.configure.uwbMeas.multiEval.pmask.limit.area.set(enable_lower = False, enable_upper = False) \n
		Enables limit checks for the pulse mask. \n
			:param enable_lower: Enables the check of lower limits
			:param enable_upper: Enables the check of upper limits
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable_lower', enable_lower, DataType.Boolean), ArgSingle('enable_upper', enable_upper, DataType.Boolean))
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:AREA {param}'.rstrip())

	# noinspection PyTypeChecker
	class AreaStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable_Lower: bool: Enables the check of lower limits
			- Enable_Upper: bool: Enables the check of upper limits"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable_Lower'),
			ArgStruct.scalar_bool('Enable_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable_Lower: bool = None
			self.Enable_Upper: bool = None

	def get(self) -> AreaStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:AREA \n
		Snippet: value: AreaStruct = driver.configure.uwbMeas.multiEval.pmask.limit.area.get() \n
		Enables limit checks for the pulse mask. \n
			:return: structure: for return value, see the help for AreaStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PMASk:LIMit:AREA?', self.__class__.AreaStruct())
