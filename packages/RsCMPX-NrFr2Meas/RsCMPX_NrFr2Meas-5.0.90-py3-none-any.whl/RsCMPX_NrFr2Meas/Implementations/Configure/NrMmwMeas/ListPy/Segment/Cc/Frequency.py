from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrequencyCls:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:FREQuency \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.cc.frequency.set(frequency = 1.0, sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Selects the center frequency of carrier <c>, used in segment <no>. Using the unit CH, the frequency can be set via the
		channel number. The allowed channel number range depends on the operating band, see 'Frequency bands'. For the supported
		frequency range, see 'Frequency ranges'. \n
			:param frequency: No help available
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:FREQuency {param}')

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponentExt=repcap.CarrierComponentExt.Default) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<carrier>]:FREQuency \n
		Snippet: value: float = driver.configure.nrMmwMeas.listPy.segment.cc.frequency.get(sEGMent = repcap.SEGMent.Default, carrierComponentExt = repcap.CarrierComponentExt.Default) \n
		Selects the center frequency of carrier <c>, used in segment <no>. Using the unit CH, the frequency can be set via the
		channel number. The allowed channel number range depends on the operating band, see 'Frequency bands'. For the supported
		frequency range, see 'Frequency ranges'. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponentExt: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency: No help available"""
		sEGMent_cmd_val = self._cmd_group.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponentExt_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentExt, repcap.CarrierComponentExt)
		response = self._core.io.query_str(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponentExt_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
