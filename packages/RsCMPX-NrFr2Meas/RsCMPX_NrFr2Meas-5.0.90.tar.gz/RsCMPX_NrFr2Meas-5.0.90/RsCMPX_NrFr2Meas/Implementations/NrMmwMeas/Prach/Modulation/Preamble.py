from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PreambleCls:
	"""Preamble commands group definition. 2 total commands, 0 Subgroups, 2 group commands
	Repeated Capability: Preamble, default value after init: Preamble.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_preamble_get', 'repcap_preamble_set', repcap.Preamble.Nr1)

	def repcap_preamble_set(self, preamble: repcap.Preamble) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Preamble.Default
		Default value after init: Preamble.Nr1"""
		self._cmd_group.set_repcap_enum_value(preamble)

	def repcap_preamble_get(self) -> repcap.Preamble:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Preamble_Rel: int: Reliability indicator for the preamble
			- Evm_Rms_Low: float: EVM RMS value, low EVM window position
			- Evm_Rms_High: float: EVM RMS value, high EVM window position
			- Evm_Peak_Low: float: EVM peak value, low EVM window position
			- Evm_Peak_High: float: EVM peak value, high EVM window position
			- Mag_Error_Rms_Low: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Rms_High: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Peak_Low: float: Magnitude error peak value, low EVM window position
			- Mag_Err_Peak_High: float: Magnitude error peak value, high EVM window position
			- Ph_Error_Rms_Low: float: Phase error RMS value, low EVM window position
			- Ph_Error_Rms_High: float: Phase error RMS value, high EVM window position
			- Ph_Error_Peak_Low: float: Phase error peak value, low EVM window position
			- Ph_Error_Peak_High: float: Phase error peak value, high EVM window position
			- Frequency_Error: float: Carrier frequency error
			- Timing_Error: float: Time error
			- Tx_Power: float: User equipment power
			- Peak_Power: float: User equipment peak power
			- Antenna_1_Pow: float: Power at RX antenna 1
			- Antenna_2_Pow: float: Power at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Preamble_Rel'),
			ArgStruct.scalar_float('Evm_Rms_Low'),
			ArgStruct.scalar_float('Evm_Rms_High'),
			ArgStruct.scalar_float('Evm_Peak_Low'),
			ArgStruct.scalar_float('Evm_Peak_High'),
			ArgStruct.scalar_float('Mag_Error_Rms_Low'),
			ArgStruct.scalar_float('Mag_Error_Rms_High'),
			ArgStruct.scalar_float('Mag_Error_Peak_Low'),
			ArgStruct.scalar_float('Mag_Err_Peak_High'),
			ArgStruct.scalar_float('Ph_Error_Rms_Low'),
			ArgStruct.scalar_float('Ph_Error_Rms_High'),
			ArgStruct.scalar_float('Ph_Error_Peak_Low'),
			ArgStruct.scalar_float('Ph_Error_Peak_High'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Antenna_1_Pow'),
			ArgStruct.scalar_float('Antenna_2_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Preamble_Rel: int = None
			self.Evm_Rms_Low: float = None
			self.Evm_Rms_High: float = None
			self.Evm_Peak_Low: float = None
			self.Evm_Peak_High: float = None
			self.Mag_Error_Rms_Low: float = None
			self.Mag_Error_Rms_High: float = None
			self.Mag_Error_Peak_Low: float = None
			self.Mag_Err_Peak_High: float = None
			self.Ph_Error_Rms_Low: float = None
			self.Ph_Error_Rms_High: float = None
			self.Ph_Error_Peak_Low: float = None
			self.Ph_Error_Peak_High: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Tx_Power: float = None
			self.Peak_Power: float = None
			self.Antenna_1_Pow: float = None
			self.Antenna_2_Pow: float = None

	def read(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble<Number> \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.preamble.read(preamble = repcap.Preamble.Default) \n
		Return the single value results of the EVM vs Preamble and Power vs Preamble squares, for a selected preamble. See also
		'Squares EVM vs Preamble, Power vs Preamble'. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble{preamble_cmd_val}?', self.__class__.ResultData())

	def fetch(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble<Number> \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.preamble.fetch(preamble = repcap.Preamble.Default) \n
		Return the single value results of the EVM vs Preamble and Power vs Preamble squares, for a selected preamble. See also
		'Squares EVM vs Preamble, Power vs Preamble'. \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._cmd_group.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble{preamble_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'PreambleCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PreambleCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
