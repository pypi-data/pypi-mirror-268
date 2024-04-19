from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExtremeCls:
	"""Extreme commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured subframes with failed limit check
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
			- Tx_Power_Minimum: float: Minimum user equipment power
			- Tx_Power_Maximum: float: Maximum user equipment power
			- Peak_Power_Min: float: Minimum user equipment peak power
			- Peak_Power_Max: float: Maximum user equipment peak power
			- Psd_Minimum: float: No parameter help available
			- Psd_Maximum: float: No parameter help available
			- Evm_Dmrs_Low: float: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: float: Carrier frequency error in ppm
			- Iq_Imbalance: float: I/Q gain imbalance
			- Iq_Quadrature_Err: float: No parameter help available
			- Ant_1_Pow_Min: float: Minimum power at RX antenna 1
			- Ant_1_Pow_Max: float: Maximum power at RX antenna 1
			- Ant_2_Pow_Min: float: Minimum power at RX antenna 2
			- Ant_2_Pow_Max: float: Maximum power at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
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
			ArgStruct.scalar_float('Tx_Power_Minimum'),
			ArgStruct.scalar_float('Tx_Power_Maximum'),
			ArgStruct.scalar_float('Peak_Power_Min'),
			ArgStruct.scalar_float('Peak_Power_Max'),
			ArgStruct.scalar_float('Psd_Minimum'),
			ArgStruct.scalar_float('Psd_Maximum'),
			ArgStruct.scalar_float('Evm_Dmrs_Low'),
			ArgStruct.scalar_float('Evm_Dmrs_High'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_float('Freq_Err_Ppm'),
			ArgStruct.scalar_float('Iq_Imbalance'),
			ArgStruct.scalar_float('Iq_Quadrature_Err'),
			ArgStruct.scalar_float('Ant_1_Pow_Min'),
			ArgStruct.scalar_float('Ant_1_Pow_Max'),
			ArgStruct.scalar_float('Ant_2_Pow_Min'),
			ArgStruct.scalar_float('Ant_2_Pow_Max')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
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
			self.Tx_Power_Minimum: float = None
			self.Tx_Power_Maximum: float = None
			self.Peak_Power_Min: float = None
			self.Peak_Power_Max: float = None
			self.Psd_Minimum: float = None
			self.Psd_Maximum: float = None
			self.Evm_Dmrs_Low: float = None
			self.Evm_Dmrs_High: float = None
			self.Mag_Err_Dmrs_Low: float = None
			self.Mag_Err_Dmrs_High: float = None
			self.Ph_Error_Dmrs_Low: float = None
			self.Ph_Error_Dmrs_High: float = None
			self.Freq_Err_Ppm: float = None
			self.Iq_Imbalance: float = None
			self.Iq_Quadrature_Err: float = None
			self.Ant_1_Pow_Min: float = None
			self.Ant_1_Pow_Max: float = None
			self.Ant_2_Pow_Min: float = None
			self.Ant_2_Pow_Max: float = None

	def fetch(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> FetchStruct:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:MODulation:EXTReme \n
		Snippet: value: FetchStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.modulation.extreme.fetch(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return modulation single value results for segment <no> in list mode. The values described below are returned by FETCh
		commands. The first four values (reliability to out of tolerance result) are also returned by CALCulate commands.
		The remaining values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:MODulation:EXTReme?', self.__class__.FetchStruct())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Seg_Reliability: int: Reliability indicator for the segment
			- Statist_Expired: int: Reached statistical length in slots
			- Out_Of_Tolerance: int: Percentage of measured subframes with failed limit check
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
			- Sample_Clock_Err: enums.ResultStatus2: No parameter help available
			- Timing_Error: float or bool: Time error
			- Tx_Power_Minimum: float or bool: Minimum user equipment power
			- Tx_Power_Maximum: float or bool: Maximum user equipment power
			- Peak_Power_Min: float or bool: Minimum user equipment peak power
			- Peak_Power_Max: float or bool: Maximum user equipment peak power
			- Psd_Minimum: float or bool: No parameter help available
			- Psd_Maximum: float or bool: No parameter help available
			- Evm_Dmrs_Low: float or bool: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float or bool: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float or bool: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float or bool: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float or bool: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float or bool: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: enums.ResultStatus2: Carrier frequency error in ppm
			- Iq_Imbalance: enums.ResultStatus2: I/Q gain imbalance
			- Iq_Quadrature_Err: enums.ResultStatus2: No parameter help available
			- Ant_1_Pow_Min: enums.ResultStatus2: Minimum power at RX antenna 1
			- Ant_1_Pow_Max: enums.ResultStatus2: Maximum power at RX antenna 1
			- Ant_2_Pow_Min: enums.ResultStatus2: Minimum power at RX antenna 2
			- Ant_2_Pow_Max: enums.ResultStatus2: Maximum power at RX antenna 2"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Seg_Reliability'),
			ArgStruct.scalar_int('Statist_Expired'),
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
			ArgStruct.scalar_enum('Sample_Clock_Err', enums.ResultStatus2),
			ArgStruct.scalar_float_ext('Timing_Error'),
			ArgStruct.scalar_float_ext('Tx_Power_Minimum'),
			ArgStruct.scalar_float_ext('Tx_Power_Maximum'),
			ArgStruct.scalar_float_ext('Peak_Power_Min'),
			ArgStruct.scalar_float_ext('Peak_Power_Max'),
			ArgStruct.scalar_float_ext('Psd_Minimum'),
			ArgStruct.scalar_float_ext('Psd_Maximum'),
			ArgStruct.scalar_float_ext('Evm_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Evm_Dmrs_High'),
			ArgStruct.scalar_float_ext('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float_ext('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float_ext('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_enum('Freq_Err_Ppm', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Imbalance', enums.ResultStatus2),
			ArgStruct.scalar_enum('Iq_Quadrature_Err', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ant_1_Pow_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ant_1_Pow_Max', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ant_2_Pow_Min', enums.ResultStatus2),
			ArgStruct.scalar_enum('Ant_2_Pow_Max', enums.ResultStatus2)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Seg_Reliability: int = None
			self.Statist_Expired: int = None
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
			self.Sample_Clock_Err: enums.ResultStatus2 = None
			self.Timing_Error: float or bool = None
			self.Tx_Power_Minimum: float or bool = None
			self.Tx_Power_Maximum: float or bool = None
			self.Peak_Power_Min: float or bool = None
			self.Peak_Power_Max: float or bool = None
			self.Psd_Minimum: float or bool = None
			self.Psd_Maximum: float or bool = None
			self.Evm_Dmrs_Low: float or bool = None
			self.Evm_Dmrs_High: float or bool = None
			self.Mag_Err_Dmrs_Low: float or bool = None
			self.Mag_Err_Dmrs_High: float or bool = None
			self.Ph_Error_Dmrs_Low: float or bool = None
			self.Ph_Error_Dmrs_High: float or bool = None
			self.Freq_Err_Ppm: enums.ResultStatus2 = None
			self.Iq_Imbalance: enums.ResultStatus2 = None
			self.Iq_Quadrature_Err: enums.ResultStatus2 = None
			self.Ant_1_Pow_Min: enums.ResultStatus2 = None
			self.Ant_1_Pow_Max: enums.ResultStatus2 = None
			self.Ant_2_Pow_Min: enums.ResultStatus2 = None
			self.Ant_2_Pow_Max: enums.ResultStatus2 = None

	def calculate(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent<nr>[:CC<carrier>]:MODulation:EXTReme \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.listPy.segment.cc.modulation.extreme.calculate(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Return modulation single value results for segment <no> in list mode. The values described below are returned by FETCh
		commands. The first four values (reliability to out of tolerance result) are also returned by CALCulate commands.
		The remaining values returned by CALCulate commands are limit check results, one value for each result listed below. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:MODulation:EXTReme?', self.__class__.CalculateStruct())
