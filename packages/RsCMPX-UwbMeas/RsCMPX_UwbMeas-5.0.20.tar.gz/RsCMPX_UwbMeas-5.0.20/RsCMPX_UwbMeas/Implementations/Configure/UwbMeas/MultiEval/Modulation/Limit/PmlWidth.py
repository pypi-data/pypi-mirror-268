from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmlWidthCls:
	"""PmlWidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmlWidth", core, parent)

	def set(self, enable: bool, limit: float) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth \n
		Snippet: driver.configure.uwbMeas.multiEval.modulation.limit.pmlWidth.set(enable = False, limit = 1.0) \n
		Activates and defines a lower limit for the pulse mainlobe width. \n
			:param enable: No help available
			:param limit: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('enable', enable, DataType.Boolean), ArgSingle('limit', limit, DataType.Float))
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth {param}'.rstrip())

	# noinspection PyTypeChecker
	class PmlWidthStruct(StructBase):
		"""Response structure. Fields: \n
			- Enable: bool: No parameter help available
			- Limit: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Limit')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Limit: float = None

	def get(self) -> PmlWidthStruct:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth \n
		Snippet: value: PmlWidthStruct = driver.configure.uwbMeas.multiEval.modulation.limit.pmlWidth.get() \n
		Activates and defines a lower limit for the pulse mainlobe width. \n
			:return: structure: for return value, see the help for PmlWidthStruct structure arguments."""
		return self._core.io.query_struct(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:MODulation:LIMit:PMLWidth?', self.__class__.PmlWidthStruct())
