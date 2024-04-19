from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AverageCls:
	"""Average commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
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
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Sample_Clock_Err: float: No parameter help available
			- Timing_Error: float: Time error
			- Tx_Power: float: User equipment power
			- Peak_Power: float: User equipment peak power
			- Psd: float: No parameter help available
			- Evm_Dmrs_Low: float: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: float: Carrier frequency error in ppm
			- Iq_Imbalance: float: I/Q gain imbalance
			- Iq_Quadrature_Err: float: No parameter help available
			- Antenna_1_Pow: float: Power at RX antenna 1
			- Antenna_2_Pow: float: Power at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Out_Of_Tolerance'),
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
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Sample_Clock_Err'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power'),
			ArgStruct.scalar_float('Peak_Power'),
			ArgStruct.scalar_float('Psd'),
			ArgStruct.scalar_float('Evm_Dmrs_Low'),
			ArgStruct.scalar_float('Evm_Dmrs_High'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_float('Freq_Err_Ppm'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Iq_Quadrature_Err'),
			ArgStruct.scalar_float('Antenna_1_Pow'),
			ArgStruct.scalar_float('Antenna_2_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Out_Of_Tolerance: int = None
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
			self.Iq_Offset: float = None
			self.Frequency_Error: float = None
			self.Sample_Clock_Err: float = None
			self.Timing_Error: float = None
			self.Tx_Power: float = None
			self.Peak_Power: float = None
			self.Psd: float = None
			self.Evm_Dmrs_Low: float = None
			self.Evm_Dmrs_High: float = None
			self.Mag_Err_Dmrs_Low: float = None
			self.Mag_Err_Dmrs_High: float = None
			self.Ph_Error_Dmrs_Low: float = None
			self.Ph_Error_Dmrs_High: float = None
			self.Freq_Err_Ppm: float = None
			self.Iq_Imbalance: float = None
			self.Iq_Quadrature_Err: float = None
			self.Antenna_1_Pow: float = None
			self.Antenna_2_Pow: float = None

	def read(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:MODulation:AVERage \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.cc.layer.modulation.average.read(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Return the current, average and standard deviation single value results for carrier <no>, layer <l>. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:MODulation:AVERage?', self.__class__.ResultData())

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:MODulation:AVERage \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.cc.layer.modulation.average.fetch(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Return the current, average and standard deviation single value results for carrier <no>, layer <l>. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:MODulation:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. the percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms_Low: float or bool: EVM RMS value, low EVM window position
			- Evm_Rms_High: float or bool: EVM RMS value, high EVM window position
			- Evm_Peak_Low: float or bool: EVM peak value, low EVM window position
			- Evm_Peak_High: float or bool: EVM peak value, high EVM window position
			- Mag_Error_Rms_Low: float or bool: Magnitude error RMS value, low EVM window position
			- Mag_Error_Rms_High: float or bool: Magnitude error RMS value, low EVM window position
			- Mag_Error_Peak_Low: float or bool: Magnitude error peak value, low EVM window position
			- Mag_Err_Peak_High: float or bool: Magnitude error peak value, high EVM window position
			- Ph_Error_Rms_Low: float or bool: Phase error RMS value, low EVM window position
			- Ph_Error_Rms_High: float or bool: Phase error RMS value, high EVM window position
			- Ph_Error_Peak_Low: float or bool: Phase error peak value, low EVM window position
			- Ph_Error_Peak_High: float or bool: Phase error peak value, high EVM window position
			- Iq_Offset: float or bool: I/Q origin offset
			- Frequency_Error: float or bool: Carrier frequency error
			- Sample_Clock_Err: float or bool: No parameter help available
			- Timing_Error: float or bool: Time error
			- Tx_Power: float or bool: User equipment power
			- Peak_Power: float or bool: User equipment peak power
			- Psd: float or bool: No parameter help available
			- Evm_Dmrs_Low: float or bool: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float or bool: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float or bool: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float or bool: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float or bool: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float or bool: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: float or bool: Carrier frequency error in ppm
			- Iq_Imbalance: float or bool: I/Q gain imbalance
			- Iq_Quadrature_Err: float or bool: No parameter help available
			- Antenna_1_Pow: float or bool: Power at RX antenna 1
			- Antenna_2_Pow: float or bool: Power at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float_ext('Evm_Rms_Low'),
			ArgStruct.scalar_float_ext('Evm_Rms_High'),
			ArgStruct.scalar_float_ext('Evm_Peak_Low'),
			ArgStruct.scalar_float_ext('Evm_Peak_High'),
			ArgStruct.scalar_float_ext('Mag_Error_Rms_Low'),
			ArgStruct.scalar_float_ext('Mag_Error_Rms_High'),
			ArgStruct.scalar_float_ext('Mag_Error_Peak_Low'),
			ArgStruct.scalar_float_ext('Mag_Err_Peak_High'),
			ArgStruct.scalar_float_ext('Ph_Error_Rms_Low'),
			ArgStruct.scalar_float_ext('Ph_Error_Rms_High'),
			ArgStruct.scalar_float_ext('Ph_Error_Peak_Low'),
			ArgStruct.scalar_float_ext('Ph_Error_Peak_High'),
			ArgStruct.scalar_float_ext('Iq_Offset'),
			ArgStruct.scalar_float_ext('Frequency_Error'),
			ArgStruct.scalar_float_ext('Sample_Clock_Err'),
			ArgStruct.scalar_float_ext('Timing_Error'),
			ArgStruct.scalar_float_ext('Tx_Power'),
			ArgStruct.scalar_float_ext('Peak_Power'),
			ArgStruct.scalar_float_ext('Psd'),
			ArgStruct.scalar_float_ext('Evm_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Evm_Dmrs_High'),
			ArgStruct.scalar_float_ext('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float_ext('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_float_ext('Freq_Err_Ppm'),
			ArgStruct.scalar_float_ext('Iq_Imbalance'),
			ArgStruct.scalar_float_ext('Iq_Quadrature_Err'),
			ArgStruct.scalar_float_ext('Antenna_1_Pow'),
			ArgStruct.scalar_float_ext('Antenna_2_Pow')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms_Low: float or bool = None
			self.Evm_Rms_High: float or bool = None
			self.Evm_Peak_Low: float or bool = None
			self.Evm_Peak_High: float or bool = None
			self.Mag_Error_Rms_Low: float or bool = None
			self.Mag_Error_Rms_High: float or bool = None
			self.Mag_Error_Peak_Low: float or bool = None
			self.Mag_Err_Peak_High: float or bool = None
			self.Ph_Error_Rms_Low: float or bool = None
			self.Ph_Error_Rms_High: float or bool = None
			self.Ph_Error_Peak_Low: float or bool = None
			self.Ph_Error_Peak_High: float or bool = None
			self.Iq_Offset: float or bool = None
			self.Frequency_Error: float or bool = None
			self.Sample_Clock_Err: float or bool = None
			self.Timing_Error: float or bool = None
			self.Tx_Power: float or bool = None
			self.Peak_Power: float or bool = None
			self.Psd: float or bool = None
			self.Evm_Dmrs_Low: float or bool = None
			self.Evm_Dmrs_High: float or bool = None
			self.Mag_Err_Dmrs_Low: float or bool = None
			self.Mag_Err_Dmrs_High: float or bool = None
			self.Ph_Error_Dmrs_Low: float or bool = None
			self.Ph_Error_Dmrs_High: float or bool = None
			self.Freq_Err_Ppm: float or bool = None
			self.Iq_Imbalance: float or bool = None
			self.Iq_Quadrature_Err: float or bool = None
			self.Antenna_1_Pow: float or bool = None
			self.Antenna_2_Pow: float or bool = None

	def calculate(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:MODulation:AVERage \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.cc.layer.modulation.average.calculate(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Return the current, average and standard deviation single value results for carrier <no>, layer <l>. The values described
		below are returned by FETCh and READ commands. CALCulate commands return limit check results instead, one value for each
		result listed below. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:MODulation:AVERage?', self.__class__.CalculateStruct())
