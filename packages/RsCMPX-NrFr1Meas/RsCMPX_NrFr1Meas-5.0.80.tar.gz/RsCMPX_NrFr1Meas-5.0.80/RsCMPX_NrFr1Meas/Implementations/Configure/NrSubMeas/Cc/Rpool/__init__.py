from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RpoolCls:
	"""Rpool commands group definition. 10 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rpool", core, parent)

	@property
	def pssch(self):
		"""pssch commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_pssch'):
			from .Pssch import PsschCls
			self._pssch = PsschCls(self._core, self._cmd_group)
		return self._pssch

	@property
	def pscch(self):
		"""pscch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pscch'):
			from .Pscch import PscchCls
			self._pscch = PscchCls(self._core, self._cmd_group)
		return self._pscch

	def set(self, no_rbs: int, start_rb: int, sub_chan_size: enums.SubChanSize, no_sub_chans: int, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol \n
		Snippet: driver.configure.nrSubMeas.cc.rpool.set(no_rbs = 1, start_rb = 1, sub_chan_size = enums.SubChanSize.RB10, no_sub_chans = 1, carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param no_rbs: No help available
			:param start_rb: No help available
			:param sub_chan_size: No help available
			:param no_sub_chans: No help available
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('no_rbs', no_rbs, DataType.Integer), ArgSingle('start_rb', start_rb, DataType.Integer), ArgSingle('sub_chan_size', sub_chan_size, DataType.Enum, enums.SubChanSize), ArgSingle('no_sub_chans', no_sub_chans, DataType.Integer))
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol {param}'.rstrip())

	# noinspection PyTypeChecker
	class RpoolStruct(StructBase):
		"""Response structure. Fields: \n
			- No_Rbs: int: No parameter help available
			- Start_Rb: int: No parameter help available
			- Sub_Chan_Size: enums.SubChanSize: No parameter help available
			- No_Sub_Chans: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('No_Rbs'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Sub_Chan_Size', enums.SubChanSize),
			ArgStruct.scalar_int('No_Sub_Chans')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.No_Rbs: int = None
			self.Start_Rb: int = None
			self.Sub_Chan_Size: enums.SubChanSize = None
			self.No_Sub_Chans: int = None

	def get(self, carrierComponentOne=repcap.CarrierComponentOne.Nr1) -> RpoolStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>[:CC<no>]:RPOol \n
		Snippet: value: RpoolStruct = driver.configure.nrSubMeas.cc.rpool.get(carrierComponentOne = repcap.CarrierComponentOne.Nr1) \n
		No command help available \n
			:param carrierComponentOne: optional repeated capability selector. Default value: Nr1
			:return: structure: for return value, see the help for RpoolStruct structure arguments."""
		carrierComponentOne_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponentOne, repcap.CarrierComponentOne)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:CC{carrierComponentOne_cmd_val}:RPOol?', self.__class__.RpoolStruct())

	def clone(self) -> 'RpoolCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RpoolCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
