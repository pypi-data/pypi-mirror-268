from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class OccCls:
	"""Occ commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("occ", core, parent)

	def set(self, length: int, index: int, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:OCC \n
		Snippet: driver.configure.nrSubMeas.cc.allocation.pucch.occ.set(length = 1, index = 1, carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the OCC length and index for PUCCH format F4, for carrier <no>, allocation <a>. \n
			:param length: OCC length
			:param index: OCC index
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('length', length, DataType.Integer), ArgSingle('index', index, DataType.Integer))
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:OCC {param}'.rstrip())

	# noinspection PyTypeChecker
	class OccStruct(StructBase):
		"""Response structure. Fields: \n
			- Length: int: OCC length
			- Index: int: OCC index"""
		__meta_args_list = [
			ArgStruct.scalar_int('Length'),
			ArgStruct.scalar_int('Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length: int = None
			self.Index: int = None

	def get(self, carrierComponentFour=repcap.CarrierComponentFour.Nr1, allocation=repcap.Allocation.Default) -> OccStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUCCh:OCC \n
		Snippet: value: OccStruct = driver.configure.nrSubMeas.cc.allocation.pucch.occ.get(carrierComponentFour = repcap.CarrierComponentFour.Nr1, allocation = repcap.Allocation.Default) \n
		Specifies the OCC length and index for PUCCH format F4, for carrier <no>, allocation <a>. \n
			:param carrierComponentFour: optional repeated capability selector. Default value: Nr1
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for OccStruct structure arguments."""
		carrierComponentFour_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentFour, repcap.CarrierComponentFour)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentFour_cmd_val}:ALLocation{allocation_cmd_val}:PUCCh:OCC?', self.__class__.OccStruct())
