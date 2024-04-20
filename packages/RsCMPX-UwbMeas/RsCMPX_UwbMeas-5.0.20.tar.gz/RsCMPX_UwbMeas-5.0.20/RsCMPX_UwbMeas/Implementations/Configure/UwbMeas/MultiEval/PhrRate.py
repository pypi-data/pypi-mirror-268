from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PhrRateCls:
	"""PhrRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phrRate", core, parent)

	def set(self, phr_data_rate: enums.PhrDataRate, record=repcap.Record.Nr1) -> None:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate<Record> \n
		Snippet: driver.configure.uwbMeas.multiEval.phrRate.set(phr_data_rate = enums.PhrDataRate.DRHP, record = repcap.Record.Nr1) \n
		Specifies the data rate of the PHY header (PHR) or selects the type of signal if there is no PHR. \n
			:param phr_data_rate: DRMD: 110 kb/s or 850 kb/s (DRMDR) DRLP: 850 kb/s (DRBM_LP) DRHP: 6.8 Mb/s (DRBM_HP) RHML: 3.9 Mb/s or 7.8 Mb/s (DRHM_LR) RHMH: 15.6 Mb/s or 31.2 Mb/s (DRHM_HR) SYNC: PPDU with SYNC field only (SYNC_ONLY) RSF: ranging sequence fragment IGN: ignore selected PPDU SYFD: PPDU with SYNC and SFD fields only (SYNC_SFD) NBANd: narrowband signal
			:param record: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.enum_scalar_to_str(phr_data_rate, enums.PhrDataRate)
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		self._core.io.write(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate{record_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, record=repcap.Record.Nr1) -> enums.PhrDataRate:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate<Record> \n
		Snippet: value: enums.PhrDataRate = driver.configure.uwbMeas.multiEval.phrRate.get(record = repcap.Record.Nr1) \n
		Specifies the data rate of the PHY header (PHR) or selects the type of signal if there is no PHR. \n
			:param record: optional repeated capability selector. Default value: Nr1
			:return: phr_data_rate: DRMD: 110 kb/s or 850 kb/s (DRMDR) DRLP: 850 kb/s (DRBM_LP) DRHP: 6.8 Mb/s (DRBM_HP) RHML: 3.9 Mb/s or 7.8 Mb/s (DRHM_LR) RHMH: 15.6 Mb/s or 31.2 Mb/s (DRHM_HR) SYNC: PPDU with SYNC field only (SYNC_ONLY) RSF: ranging sequence fragment IGN: ignore selected PPDU SYFD: PPDU with SYNC and SFD fields only (SYNC_SFD) NBANd: narrowband signal"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PHRRate{record_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.PhrDataRate)
