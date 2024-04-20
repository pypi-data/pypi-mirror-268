from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitrateCls:
	"""Bitrate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Record, default value after init: Record.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitrate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_record_get', 'repcap_record_set', repcap.Record.Nr1)

	def repcap_record_set(self, record: repcap.Record) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Record.Default
		Default value after init: Record.Nr1"""
		self._cmd_group.set_repcap_enum_value(record)

	def repcap_record_get(self) -> repcap.Record:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def get(self, record=repcap.Record.Default) -> str:
		"""SCPI: CONFigure:UWB:MEASurement<Instance>:MEValuation:PHR:BITRate<Record> \n
		Snippet: value: str = driver.configure.uwbMeas.multiEval.phr.bitrate.get(record = repcap.Record.Default) \n
		Queries the data rate of the PHR. \n
			:param record: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Bitrate')
			:return: phr_bitrate: No help available"""
		record_cmd_val = self._cmd_group.get_repcap_cmd_value(record, repcap.Record)
		response = self._core.io.query_str(f'CONFigure:UWB:MEASurement<Instance>:MEValuation:PHR:BITRate{record_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'BitrateCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BitrateCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
