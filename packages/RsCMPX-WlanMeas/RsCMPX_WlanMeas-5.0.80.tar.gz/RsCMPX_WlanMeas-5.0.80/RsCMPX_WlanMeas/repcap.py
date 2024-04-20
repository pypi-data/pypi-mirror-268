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
	Inst3 = 3
	Inst4 = 4
	Inst5 = 5
	Inst6 = 6
	Inst7 = 7
	Inst8 = 8
	Inst9 = 9
	Inst10 = 10
	Inst11 = 11
	Inst12 = 12
	Inst13 = 13
	Inst14 = 14
	Inst15 = 15
	Inst16 = 16
	Inst17 = 17
	Inst18 = 18
	Inst19 = 19
	Inst20 = 20
	Inst21 = 21
	Inst22 = 22
	Inst23 = 23
	Inst24 = 24
	Inst25 = 25
	Inst26 = 26
	Inst27 = 27
	Inst28 = 28
	Inst29 = 29
	Inst30 = 30
	Inst31 = 31
	Inst32 = 32


# noinspection SpellCheckingInspection
class Antenna(Enum):
	"""Repeated capability Antenna"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8


# noinspection SpellCheckingInspection
class Band(Enum):
	"""Repeated capability Band"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr2 = 2
	Nr5 = 5


# noinspection SpellCheckingInspection
class BandwidthA(Enum):
	"""Repeated capability BandwidthA"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw10 = 10
	Bw20 = 20


# noinspection SpellCheckingInspection
class BandwidthB(Enum):
	"""Repeated capability BandwidthB"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw5 = 5
	Bw10 = 10
	Bw20 = 20


# noinspection SpellCheckingInspection
class BandwidthC(Enum):
	"""Repeated capability BandwidthC"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw5 = 5
	Bw10 = 10
	Bw20 = 20
	Bw40 = 40


# noinspection SpellCheckingInspection
class BandwidthD(Enum):
	"""Repeated capability BandwidthD"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw20 = 20
	Bw40 = 40
	Bw80 = 80
	Bw160 = 160
	Bw8080 = 8080


# noinspection SpellCheckingInspection
class BandwidthE(Enum):
	"""Repeated capability BandwidthE"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw5 = 5
	Bw10 = 10
	Bw20 = 20
	Bw40 = 40
	Bw80 = 80
	Bw160 = 160
	Bw8080 = 8080


# noinspection SpellCheckingInspection
class BandwidthF(Enum):
	"""Repeated capability BandwidthF"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw20 = 20
	Bw40 = 40
	Bw80 = 80
	Bw160 = 160
	Bw320 = 320


# noinspection SpellCheckingInspection
class BandwidthG(Enum):
	"""Repeated capability BandwidthG"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Bw5 = 5
	Bw10 = 10
	Bw20 = 20
	Bw40 = 40
	Bw80 = 80
	Bw160 = 160
	Bw320 = 320


# noinspection SpellCheckingInspection
class Channel(Enum):
	"""Repeated capability Channel"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class Channels(Enum):
	"""Repeated capability Channels"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8


# noinspection SpellCheckingInspection
class Connector(Enum):
	"""Repeated capability Connector"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class Mimo(Enum):
	"""Repeated capability Mimo"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8


# noinspection SpellCheckingInspection
class Reserved(Enum):
	"""Repeated capability Reserved"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3


# noinspection SpellCheckingInspection
class ResourceUnit(Enum):
	"""Repeated capability ResourceUnit"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16
	Nr17 = 17
	Nr18 = 18
	Nr19 = 19
	Nr20 = 20
	Nr21 = 21
	Nr22 = 22
	Nr23 = 23
	Nr24 = 24
	Nr25 = 25
	Nr26 = 26
	Nr27 = 27
	Nr28 = 28
	Nr29 = 29
	Nr30 = 30
	Nr31 = 31
	Nr32 = 32
	Nr33 = 33
	Nr34 = 34
	Nr35 = 35
	Nr36 = 36
	Nr37 = 37
	Nr38 = 38
	Nr39 = 39
	Nr40 = 40
	Nr41 = 41
	Nr42 = 42
	Nr43 = 43
	Nr44 = 44
	Nr45 = 45
	Nr46 = 46
	Nr47 = 47
	Nr48 = 48
	Nr49 = 49
	Nr50 = 50
	Nr51 = 51
	Nr52 = 52
	Nr53 = 53
	Nr54 = 54
	Nr55 = 55
	Nr56 = 56
	Nr57 = 57
	Nr58 = 58
	Nr59 = 59
	Nr60 = 60
	Nr61 = 61
	Nr62 = 62
	Nr63 = 63
	Nr64 = 64
	Nr65 = 65
	Nr66 = 66
	Nr67 = 67
	Nr68 = 68
	Nr69 = 69
	Nr70 = 70
	Nr71 = 71
	Nr72 = 72
	Nr73 = 73
	Nr74 = 74
	Nr75 = 75
	Nr76 = 76
	Nr77 = 77
	Nr78 = 78
	Nr79 = 79
	Nr80 = 80
	Nr81 = 81
	Nr82 = 82
	Nr83 = 83
	Nr84 = 84
	Nr85 = 85
	Nr86 = 86
	Nr87 = 87
	Nr88 = 88
	Nr89 = 89
	Nr90 = 90
	Nr91 = 91
	Nr92 = 92
	Nr93 = 93
	Nr94 = 94
	Nr95 = 95
	Nr96 = 96
	Nr97 = 97
	Nr98 = 98
	Nr99 = 99
	Nr100 = 100
	Nr101 = 101
	Nr102 = 102
	Nr103 = 103
	Nr104 = 104
	Nr105 = 105
	Nr106 = 106
	Nr107 = 107
	Nr108 = 108
	Nr109 = 109
	Nr110 = 110
	Nr111 = 111
	Nr112 = 112
	Nr113 = 113
	Nr114 = 114
	Nr115 = 115
	Nr116 = 116
	Nr117 = 117
	Nr118 = 118
	Nr119 = 119
	Nr120 = 120
	Nr121 = 121
	Nr122 = 122
	Nr123 = 123
	Nr124 = 124
	Nr125 = 125
	Nr126 = 126
	Nr127 = 127
	Nr128 = 128
	Nr129 = 129
	Nr130 = 130
	Nr131 = 131
	Nr132 = 132
	Nr133 = 133
	Nr134 = 134
	Nr135 = 135
	Nr136 = 136
	Nr137 = 137
	Nr138 = 138
	Nr139 = 139
	Nr140 = 140
	Nr141 = 141
	Nr142 = 142
	Nr143 = 143
	Nr144 = 144


# noinspection SpellCheckingInspection
class RxAntenna(Enum):
	"""Repeated capability RxAntenna"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8


# noinspection SpellCheckingInspection
class Segment(Enum):
	"""Repeated capability Segment"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2


# noinspection SpellCheckingInspection
class SegmentB(Enum):
	"""Repeated capability SegmentB"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16
	Nr17 = 17
	Nr18 = 18
	Nr19 = 19
	Nr20 = 20
	Nr21 = 21
	Nr22 = 22
	Nr23 = 23
	Nr24 = 24
	Nr25 = 25
	Nr26 = 26
	Nr27 = 27
	Nr28 = 28
	Nr29 = 29
	Nr30 = 30
	Nr31 = 31
	Nr32 = 32


# noinspection SpellCheckingInspection
class Smi(Enum):
	"""Repeated capability Smi"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr4 = 4


# noinspection SpellCheckingInspection
class SMimoPath(Enum):
	"""Repeated capability SMimoPath"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Count2 = 2
	Count4 = 4
	Count8 = 8


# noinspection SpellCheckingInspection
class Spatial(Enum):
	"""Repeated capability Spatial"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4


# noinspection SpellCheckingInspection
class Stream(Enum):
	"""Repeated capability Stream"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8


# noinspection SpellCheckingInspection
class TrueMimoPath(Enum):
	"""Repeated capability TrueMimoPath"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Count1 = 1
	Count2 = 2
	Count3 = 3
	Count4 = 4


# noinspection SpellCheckingInspection
class User(Enum):
	"""Repeated capability User"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16
	Nr17 = 17
	Nr18 = 18
	Nr19 = 19
	Nr20 = 20
	Nr21 = 21
	Nr22 = 22
	Nr23 = 23
	Nr24 = 24
	Nr25 = 25
	Nr26 = 26
	Nr27 = 27
	Nr28 = 28
	Nr29 = 29
	Nr30 = 30
	Nr31 = 31
	Nr32 = 32
	Nr33 = 33
	Nr34 = 34
	Nr35 = 35
	Nr36 = 36
	Nr37 = 37
	Nr38 = 38
	Nr39 = 39
	Nr40 = 40
	Nr41 = 41
	Nr42 = 42
	Nr43 = 43
	Nr44 = 44
	Nr45 = 45
	Nr46 = 46
	Nr47 = 47
	Nr48 = 48
	Nr49 = 49
	Nr50 = 50
	Nr51 = 51
	Nr52 = 52
	Nr53 = 53
	Nr54 = 54
	Nr55 = 55
	Nr56 = 56
	Nr57 = 57
	Nr58 = 58
	Nr59 = 59
	Nr60 = 60
	Nr61 = 61
	Nr62 = 62
	Nr63 = 63
	Nr64 = 64
	Nr65 = 65
	Nr66 = 66
	Nr67 = 67
	Nr68 = 68
	Nr69 = 69
	Nr70 = 70
	Nr71 = 71
	Nr72 = 72
	Nr73 = 73
	Nr74 = 74
	Nr75 = 75
	Nr76 = 76
	Nr77 = 77
	Nr78 = 78
	Nr79 = 79
	Nr80 = 80
	Nr81 = 81
	Nr82 = 82
	Nr83 = 83
	Nr84 = 84
	Nr85 = 85
	Nr86 = 86
	Nr87 = 87
	Nr88 = 88
	Nr89 = 89
	Nr90 = 90
	Nr91 = 91
	Nr92 = 92
	Nr93 = 93
	Nr94 = 94
	Nr95 = 95
	Nr96 = 96
	Nr97 = 97
	Nr98 = 98
	Nr99 = 99
	Nr100 = 100
	Nr101 = 101
	Nr102 = 102
	Nr103 = 103
	Nr104 = 104
	Nr105 = 105
	Nr106 = 106
	Nr107 = 107
	Nr108 = 108
	Nr109 = 109
	Nr110 = 110
	Nr111 = 111
	Nr112 = 112
	Nr113 = 113
	Nr114 = 114
	Nr115 = 115
	Nr116 = 116
	Nr117 = 117
	Nr118 = 118
	Nr119 = 119
	Nr120 = 120
	Nr121 = 121
	Nr122 = 122
	Nr123 = 123
	Nr124 = 124
	Nr125 = 125
	Nr126 = 126
	Nr127 = 127
	Nr128 = 128
	Nr129 = 129
	Nr130 = 130
	Nr131 = 131
	Nr132 = 132
	Nr133 = 133
	Nr134 = 134
	Nr135 = 135
	Nr136 = 136
	Nr137 = 137
	Nr138 = 138
	Nr139 = 139
	Nr140 = 140
	Nr141 = 141
	Nr142 = 142
	Nr143 = 143
	Nr144 = 144


# noinspection SpellCheckingInspection
class UserIx(Enum):
	"""Repeated capability UserIx"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
	Nr9 = 9
	Nr10 = 10
	Nr11 = 11
	Nr12 = 12
	Nr13 = 13
	Nr14 = 14
	Nr15 = 15
	Nr16 = 16
	Nr17 = 17
	Nr18 = 18
	Nr19 = 19
	Nr20 = 20
	Nr21 = 21
	Nr22 = 22
	Nr23 = 23
	Nr24 = 24
	Nr25 = 25
	Nr26 = 26
	Nr27 = 27
	Nr28 = 28
	Nr29 = 29
	Nr30 = 30
	Nr31 = 31
	Nr32 = 32
	Nr33 = 33
	Nr34 = 34
	Nr35 = 35
	Nr36 = 36
	Nr37 = 37
	Nr38 = 38
	Nr39 = 39
	Nr40 = 40
	Nr41 = 41
	Nr42 = 42
	Nr43 = 43
	Nr44 = 44
	Nr45 = 45
	Nr46 = 46
	Nr47 = 47
	Nr48 = 48
	Nr49 = 49
	Nr50 = 50
	Nr51 = 51
	Nr52 = 52
	Nr53 = 53
	Nr54 = 54
	Nr55 = 55
	Nr56 = 56
	Nr57 = 57
	Nr58 = 58
	Nr59 = 59
	Nr60 = 60
	Nr61 = 61
	Nr62 = 62
	Nr63 = 63
	Nr64 = 64
	Nr65 = 65
	Nr66 = 66
	Nr67 = 67
	Nr68 = 68
	Nr69 = 69
	Nr70 = 70
	Nr71 = 71
	Nr72 = 72
	Nr73 = 73
	Nr74 = 74
	Nr75 = 75
	Nr76 = 76
	Nr77 = 77
	Nr78 = 78
	Nr79 = 79
	Nr80 = 80
	Nr81 = 81
	Nr82 = 82
	Nr83 = 83
	Nr84 = 84
	Nr85 = 85
	Nr86 = 86
	Nr87 = 87
	Nr88 = 88
	Nr89 = 89
	Nr90 = 90
	Nr91 = 91
	Nr92 = 92
	Nr93 = 93
	Nr94 = 94
	Nr95 = 95
	Nr96 = 96
	Nr97 = 97
	Nr98 = 98
	Nr99 = 99
	Nr100 = 100
	Nr101 = 101
	Nr102 = 102
	Nr103 = 103
	Nr104 = 104
	Nr105 = 105
	Nr106 = 106
	Nr107 = 107
	Nr108 = 108
	Nr109 = 109
	Nr110 = 110
	Nr111 = 111
	Nr112 = 112
	Nr113 = 113
	Nr114 = 114
	Nr115 = 115
	Nr116 = 116
	Nr117 = 117
	Nr118 = 118
	Nr119 = 119
	Nr120 = 120
	Nr121 = 121
	Nr122 = 122
	Nr123 = 123
	Nr124 = 124
	Nr125 = 125
	Nr126 = 126
	Nr127 = 127
	Nr128 = 128
	Nr129 = 129
	Nr130 = 130
	Nr131 = 131
	Nr132 = 132
	Nr133 = 133
	Nr134 = 134
	Nr135 = 135
	Nr136 = 136
	Nr137 = 137
	Nr138 = 138
	Nr139 = 139
	Nr140 = 140
	Nr141 = 141
	Nr142 = 142
	Nr143 = 143
	Nr144 = 144


# noinspection SpellCheckingInspection
class UtError(Enum):
	"""Repeated capability UtError"""
	Empty = EmptyRepCap
	Default = DefaultRepCap
	Nr1 = 1
	Nr2 = 2
	Nr3 = 3
	Nr4 = 4
	Nr5 = 5
	Nr6 = 6
	Nr7 = 7
	Nr8 = 8
