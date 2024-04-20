from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MaximumCls:
	"""Maximum commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability indicator'
			- Low: List[float]: EVM value for low EVM window position.
			- High: List[float]: EVM value for high EVM window position."""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Low', DataType.FloatList, None, False, True, 1),
			ArgStruct('High', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Low: List[float] = None
			self.High: List[float] = None

	def read(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> ResultData:
		"""SCPI: READ:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:EVMagnitude:MAXimum \n
		Snippet: value: ResultData = driver.nrSubMeas.multiEval.cc.layer.evMagnitude.maximum.read(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Returns the values of the EVM RMS diagrams for the OFDM symbols in the measured slot, for carrier <no>, layer/antenna <l>.
		The results of the current, average and maximum diagrams can be retrieved. There is one pair of EVM values per OFDM
		symbol, returned in the following order: <Reliability>, {<Low>, <High>}symbol 0, {<Low>, <High>}symbol 1, ... See also
		'Square EVM'. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'READ:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:EVMagnitude:MAXimum?', self.__class__.ResultData())

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> ResultData:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:EVMagnitude:MAXimum \n
		Snippet: value: ResultData = driver.nrSubMeas.multiEval.cc.layer.evMagnitude.maximum.fetch(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		Returns the values of the EVM RMS diagrams for the OFDM symbols in the measured slot, for carrier <no>, layer/antenna <l>.
		The results of the current, average and maximum diagrams can be retrieved. There is one pair of EVM values per OFDM
		symbol, returned in the following order: <Reliability>, {<Low>, <High>}symbol 0, {<Low>, <High>}symbol 1, ... See also
		'Square EVM'. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:EVMagnitude:MAXimum?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Low: List[enums.ResultStatus2]: No parameter help available
			- High: List[enums.ResultStatus2]: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Low', DataType.EnumList, enums.ResultStatus2, False, True, 1),
			ArgStruct('High', DataType.EnumList, enums.ResultStatus2, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Low: List[enums.ResultStatus2] = None
			self.High: List[enums.ResultStatus2] = None

	def calculate(self, carrierComponent=repcap.CarrierComponent.Default, layer=repcap.Layer.Default) -> CalculateStruct:
		"""SCPI: CALCulate:NRSub:MEASurement<Instance>:MEValuation[:CC<no>][:LAYer<layer>]:EVMagnitude:MAXimum \n
		Snippet: value: CalculateStruct = driver.nrSubMeas.multiEval.cc.layer.evMagnitude.maximum.calculate(carrierComponent = repcap.CarrierComponent.Default, layer = repcap.Layer.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param layer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Layer')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		layer_cmd_val = self._cmd_group.get_repcap_cmd_value(layer, repcap.Layer)
		return self._core.io.query_struct(f'CALCulate:NRSub:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:LAYer{layer_cmd_val}:EVMagnitude:MAXimum?', self.__class__.CalculateStruct())
