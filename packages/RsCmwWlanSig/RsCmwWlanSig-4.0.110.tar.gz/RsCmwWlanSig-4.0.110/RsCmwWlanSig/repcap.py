from enum import Enum
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_DEFAULT as DefaultRepCap
# noinspection PyPep8Naming
from .Internal.RepeatedCapability import VALUE_EMPTY as EmptyRepCap


# noinspection SpellCheckingInspection
class Instance(Enum):
	"""Global Repeated capability Instance"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Inst1 = 1
	Inst2 = 2


# noinspection SpellCheckingInspection
class Antenna(Enum):
	"""Repeated capability Antenna"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class DomainName(Enum):
	"""Repeated capability DomainName"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class Dummy(Enum):
	"""Repeated capability Dummy"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3


# noinspection SpellCheckingInspection
class IpRouteAddress(Enum):
	"""Repeated capability IpRouteAddress"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class IpVersion(Enum):
	"""Repeated capability IpVersion"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	V4 = 4
	V6 = 6


# noinspection SpellCheckingInspection
class PacketGenerator(Enum):
	"""Repeated capability PacketGenerator"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3


# noinspection SpellCheckingInspection
class Plnm(Enum):
	"""Repeated capability Plnm"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class Realm(Enum):
	"""Repeated capability Realm"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5


# noinspection SpellCheckingInspection
class Station(Enum):
	"""Repeated capability Station"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class User(Enum):
	"""Repeated capability User"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
