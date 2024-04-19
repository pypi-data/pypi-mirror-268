from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Types import DataType
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from .........Internal.ArgSingleList import ArgSingleList
from .........Internal.ArgSingle import ArgSingle
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AdditionalCls:
	"""Additional commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("additional", core, parent)

	def set(self, dmrs_length: int, cdm_groups: int, dmrs_power: float, antenna_port: int, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.additional.set(dmrs_length = 1, cdm_groups = 1, dmrs_power = 1.0, antenna_port = 1, sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <c>, allocation <a> in segment <no>. \n
			:param dmrs_length: Length of the DM-RS in symbols. The maximum value is limited by the 'maxLength' setting for the bandwidth part.
			:param cdm_groups: Number of DM-RS CDM groups without data.
			:param dmrs_power: Power of DM-RS relative to the PUSCH power.
			:param antenna_port: Antenna port of the DM-RS.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('dmrs_length', dmrs_length, DataType.Integer), ArgSingle('cdm_groups', cdm_groups, DataType.Integer), ArgSingle('dmrs_power', dmrs_power, DataType.Float), ArgSingle('antenna_port', antenna_port, DataType.Integer))
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional {param}'.rstrip())

	# noinspection PyTypeChecker
	class AdditionalStruct(StructBase):
		"""Response structure. Fields: \n
			- Dmrs_Length: int: Length of the DM-RS in symbols. The maximum value is limited by the 'maxLength' setting for the bandwidth part.
			- Cdm_Groups: int: Number of DM-RS CDM groups without data.
			- Dmrs_Power: float: Power of DM-RS relative to the PUSCH power.
			- Antenna_Port: int: Antenna port of the DM-RS."""
		__meta_args_list = [
			ArgStruct.scalar_int('Dmrs_Length'),
			ArgStruct.scalar_int('Cdm_Groups'),
			ArgStruct.scalar_float('Dmrs_Power'),
			ArgStruct.scalar_int('Antenna_Port')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dmrs_Length: int = None
			self.Cdm_Groups: int = None
			self.Dmrs_Power: float = None
			self.Antenna_Port: int = None

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default, allocation=repcap.Allocation.Default) -> AdditionalStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: value: AdditionalStruct = driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.additional.get(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <c>, allocation <a> in segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for AdditionalStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional?', self.__class__.AdditionalStruct())
