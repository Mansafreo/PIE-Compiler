; ModuleID = "main"
target triple = "x86_64-unknown-linux-gnu"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

define i32 @"main"()
{
entry:
  %"n_0" = alloca i32
  store i32 0, i32* %"n_0"
  %"total_0" = alloca i32
  store i32 0, i32* %"total_0"
  %"i_0" = alloca i32
  store i32 0, i32* %"i_0"
  %"avg_0" = alloca float
  store float              0x0, float* %"avg_0"
  %"prompt_0" = alloca [256 x i8]
  %".6" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 0
  store i8 0, i8* %".6"
  %".8" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 1
  store i8 0, i8* %".8"
  %".10" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 2
  store i8 0, i8* %".10"
  %".12" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 3
  store i8 0, i8* %".12"
  %".14" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 4
  store i8 0, i8* %".14"
  %".16" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 5
  store i8 0, i8* %".16"
  %".18" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 6
  store i8 0, i8* %".18"
  %".20" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 7
  store i8 0, i8* %".20"
  %".22" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 8
  store i8 0, i8* %".22"
  %".24" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 9
  store i8 0, i8* %".24"
  %".26" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 10
  store i8 0, i8* %".26"
  %".28" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 11
  store i8 0, i8* %".28"
  %".30" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 12
  store i8 0, i8* %".30"
  %".32" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 13
  store i8 0, i8* %".32"
  %".34" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 14
  store i8 0, i8* %".34"
  %".36" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 15
  store i8 0, i8* %".36"
  %".38" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 16
  store i8 0, i8* %".38"
  %".40" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 17
  store i8 0, i8* %".40"
  %".42" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 18
  store i8 0, i8* %".42"
  %".44" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 19
  store i8 0, i8* %".44"
  %".46" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 20
  store i8 0, i8* %".46"
  %".48" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 21
  store i8 0, i8* %".48"
  %".50" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 22
  store i8 0, i8* %".50"
  %".52" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 23
  store i8 0, i8* %".52"
  %".54" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 24
  store i8 0, i8* %".54"
  %".56" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 25
  store i8 0, i8* %".56"
  %".58" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 26
  store i8 0, i8* %".58"
  %".60" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 27
  store i8 0, i8* %".60"
  %".62" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 28
  store i8 0, i8* %".62"
  %".64" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 29
  store i8 0, i8* %".64"
  %".66" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 30
  store i8 0, i8* %".66"
  %".68" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 31
  store i8 0, i8* %".68"
  %".70" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 32
  store i8 0, i8* %".70"
  %".72" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 33
  store i8 0, i8* %".72"
  %".74" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 34
  store i8 0, i8* %".74"
  %".76" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 35
  store i8 0, i8* %".76"
  %".78" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 36
  store i8 0, i8* %".78"
  %".80" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 37
  store i8 0, i8* %".80"
  %".82" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 38
  store i8 0, i8* %".82"
  %".84" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 39
  store i8 0, i8* %".84"
  %".86" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 40
  store i8 0, i8* %".86"
  %".88" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 41
  store i8 0, i8* %".88"
  %".90" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 42
  store i8 0, i8* %".90"
  %".92" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 43
  store i8 0, i8* %".92"
  %".94" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 44
  store i8 0, i8* %".94"
  %".96" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 45
  store i8 0, i8* %".96"
  %".98" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 46
  store i8 0, i8* %".98"
  %".100" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 47
  store i8 0, i8* %".100"
  %".102" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 48
  store i8 0, i8* %".102"
  %".104" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 49
  store i8 0, i8* %".104"
  %".106" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 50
  store i8 0, i8* %".106"
  %".108" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 51
  store i8 0, i8* %".108"
  %".110" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 52
  store i8 0, i8* %".110"
  %".112" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 53
  store i8 0, i8* %".112"
  %".114" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 54
  store i8 0, i8* %".114"
  %".116" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 55
  store i8 0, i8* %".116"
  %".118" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 56
  store i8 0, i8* %".118"
  %".120" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 57
  store i8 0, i8* %".120"
  %".122" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 58
  store i8 0, i8* %".122"
  %".124" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 59
  store i8 0, i8* %".124"
  %".126" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 60
  store i8 0, i8* %".126"
  %".128" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 61
  store i8 0, i8* %".128"
  %".130" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 62
  store i8 0, i8* %".130"
  %".132" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 63
  store i8 0, i8* %".132"
  %".134" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 64
  store i8 0, i8* %".134"
  %".136" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 65
  store i8 0, i8* %".136"
  %".138" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 66
  store i8 0, i8* %".138"
  %".140" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 67
  store i8 0, i8* %".140"
  %".142" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 68
  store i8 0, i8* %".142"
  %".144" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 69
  store i8 0, i8* %".144"
  %".146" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 70
  store i8 0, i8* %".146"
  %".148" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 71
  store i8 0, i8* %".148"
  %".150" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 72
  store i8 0, i8* %".150"
  %".152" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 73
  store i8 0, i8* %".152"
  %".154" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 74
  store i8 0, i8* %".154"
  %".156" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 75
  store i8 0, i8* %".156"
  %".158" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 76
  store i8 0, i8* %".158"
  %".160" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 77
  store i8 0, i8* %".160"
  %".162" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 78
  store i8 0, i8* %".162"
  %".164" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 79
  store i8 0, i8* %".164"
  %".166" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 80
  store i8 0, i8* %".166"
  %".168" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 81
  store i8 0, i8* %".168"
  %".170" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 82
  store i8 0, i8* %".170"
  %".172" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 83
  store i8 0, i8* %".172"
  %".174" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 84
  store i8 0, i8* %".174"
  %".176" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 85
  store i8 0, i8* %".176"
  %".178" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 86
  store i8 0, i8* %".178"
  %".180" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 87
  store i8 0, i8* %".180"
  %".182" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 88
  store i8 0, i8* %".182"
  %".184" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 89
  store i8 0, i8* %".184"
  %".186" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 90
  store i8 0, i8* %".186"
  %".188" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 91
  store i8 0, i8* %".188"
  %".190" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 92
  store i8 0, i8* %".190"
  %".192" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 93
  store i8 0, i8* %".192"
  %".194" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 94
  store i8 0, i8* %".194"
  %".196" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 95
  store i8 0, i8* %".196"
  %".198" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 96
  store i8 0, i8* %".198"
  %".200" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 97
  store i8 0, i8* %".200"
  %".202" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 98
  store i8 0, i8* %".202"
  %".204" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 99
  store i8 0, i8* %".204"
  %".206" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 100
  store i8 0, i8* %".206"
  %".208" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 101
  store i8 0, i8* %".208"
  %".210" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 102
  store i8 0, i8* %".210"
  %".212" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 103
  store i8 0, i8* %".212"
  %".214" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 104
  store i8 0, i8* %".214"
  %".216" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 105
  store i8 0, i8* %".216"
  %".218" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 106
  store i8 0, i8* %".218"
  %".220" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 107
  store i8 0, i8* %".220"
  %".222" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 108
  store i8 0, i8* %".222"
  %".224" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 109
  store i8 0, i8* %".224"
  %".226" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 110
  store i8 0, i8* %".226"
  %".228" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 111
  store i8 0, i8* %".228"
  %".230" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 112
  store i8 0, i8* %".230"
  %".232" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 113
  store i8 0, i8* %".232"
  %".234" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 114
  store i8 0, i8* %".234"
  %".236" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 115
  store i8 0, i8* %".236"
  %".238" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 116
  store i8 0, i8* %".238"
  %".240" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 117
  store i8 0, i8* %".240"
  %".242" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 118
  store i8 0, i8* %".242"
  %".244" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 119
  store i8 0, i8* %".244"
  %".246" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 120
  store i8 0, i8* %".246"
  %".248" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 121
  store i8 0, i8* %".248"
  %".250" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 122
  store i8 0, i8* %".250"
  %".252" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 123
  store i8 0, i8* %".252"
  %".254" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 124
  store i8 0, i8* %".254"
  %".256" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 125
  store i8 0, i8* %".256"
  %".258" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 126
  store i8 0, i8* %".258"
  %".260" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 127
  store i8 0, i8* %".260"
  %".262" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 128
  store i8 0, i8* %".262"
  %".264" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 129
  store i8 0, i8* %".264"
  %".266" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 130
  store i8 0, i8* %".266"
  %".268" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 131
  store i8 0, i8* %".268"
  %".270" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 132
  store i8 0, i8* %".270"
  %".272" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 133
  store i8 0, i8* %".272"
  %".274" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 134
  store i8 0, i8* %".274"
  %".276" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 135
  store i8 0, i8* %".276"
  %".278" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 136
  store i8 0, i8* %".278"
  %".280" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 137
  store i8 0, i8* %".280"
  %".282" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 138
  store i8 0, i8* %".282"
  %".284" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 139
  store i8 0, i8* %".284"
  %".286" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 140
  store i8 0, i8* %".286"
  %".288" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 141
  store i8 0, i8* %".288"
  %".290" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 142
  store i8 0, i8* %".290"
  %".292" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 143
  store i8 0, i8* %".292"
  %".294" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 144
  store i8 0, i8* %".294"
  %".296" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 145
  store i8 0, i8* %".296"
  %".298" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 146
  store i8 0, i8* %".298"
  %".300" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 147
  store i8 0, i8* %".300"
  %".302" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 148
  store i8 0, i8* %".302"
  %".304" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 149
  store i8 0, i8* %".304"
  %".306" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 150
  store i8 0, i8* %".306"
  %".308" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 151
  store i8 0, i8* %".308"
  %".310" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 152
  store i8 0, i8* %".310"
  %".312" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 153
  store i8 0, i8* %".312"
  %".314" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 154
  store i8 0, i8* %".314"
  %".316" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 155
  store i8 0, i8* %".316"
  %".318" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 156
  store i8 0, i8* %".318"
  %".320" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 157
  store i8 0, i8* %".320"
  %".322" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 158
  store i8 0, i8* %".322"
  %".324" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 159
  store i8 0, i8* %".324"
  %".326" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 160
  store i8 0, i8* %".326"
  %".328" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 161
  store i8 0, i8* %".328"
  %".330" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 162
  store i8 0, i8* %".330"
  %".332" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 163
  store i8 0, i8* %".332"
  %".334" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 164
  store i8 0, i8* %".334"
  %".336" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 165
  store i8 0, i8* %".336"
  %".338" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 166
  store i8 0, i8* %".338"
  %".340" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 167
  store i8 0, i8* %".340"
  %".342" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 168
  store i8 0, i8* %".342"
  %".344" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 169
  store i8 0, i8* %".344"
  %".346" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 170
  store i8 0, i8* %".346"
  %".348" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 171
  store i8 0, i8* %".348"
  %".350" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 172
  store i8 0, i8* %".350"
  %".352" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 173
  store i8 0, i8* %".352"
  %".354" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 174
  store i8 0, i8* %".354"
  %".356" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 175
  store i8 0, i8* %".356"
  %".358" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 176
  store i8 0, i8* %".358"
  %".360" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 177
  store i8 0, i8* %".360"
  %".362" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 178
  store i8 0, i8* %".362"
  %".364" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 179
  store i8 0, i8* %".364"
  %".366" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 180
  store i8 0, i8* %".366"
  %".368" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 181
  store i8 0, i8* %".368"
  %".370" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 182
  store i8 0, i8* %".370"
  %".372" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 183
  store i8 0, i8* %".372"
  %".374" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 184
  store i8 0, i8* %".374"
  %".376" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 185
  store i8 0, i8* %".376"
  %".378" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 186
  store i8 0, i8* %".378"
  %".380" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 187
  store i8 0, i8* %".380"
  %".382" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 188
  store i8 0, i8* %".382"
  %".384" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 189
  store i8 0, i8* %".384"
  %".386" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 190
  store i8 0, i8* %".386"
  %".388" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 191
  store i8 0, i8* %".388"
  %".390" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 192
  store i8 0, i8* %".390"
  %".392" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 193
  store i8 0, i8* %".392"
  %".394" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 194
  store i8 0, i8* %".394"
  %".396" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 195
  store i8 0, i8* %".396"
  %".398" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 196
  store i8 0, i8* %".398"
  %".400" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 197
  store i8 0, i8* %".400"
  %".402" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 198
  store i8 0, i8* %".402"
  %".404" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 199
  store i8 0, i8* %".404"
  %".406" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 200
  store i8 0, i8* %".406"
  %".408" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 201
  store i8 0, i8* %".408"
  %".410" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 202
  store i8 0, i8* %".410"
  %".412" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 203
  store i8 0, i8* %".412"
  %".414" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 204
  store i8 0, i8* %".414"
  %".416" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 205
  store i8 0, i8* %".416"
  %".418" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 206
  store i8 0, i8* %".418"
  %".420" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 207
  store i8 0, i8* %".420"
  %".422" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 208
  store i8 0, i8* %".422"
  %".424" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 209
  store i8 0, i8* %".424"
  %".426" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 210
  store i8 0, i8* %".426"
  %".428" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 211
  store i8 0, i8* %".428"
  %".430" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 212
  store i8 0, i8* %".430"
  %".432" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 213
  store i8 0, i8* %".432"
  %".434" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 214
  store i8 0, i8* %".434"
  %".436" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 215
  store i8 0, i8* %".436"
  %".438" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 216
  store i8 0, i8* %".438"
  %".440" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 217
  store i8 0, i8* %".440"
  %".442" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 218
  store i8 0, i8* %".442"
  %".444" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 219
  store i8 0, i8* %".444"
  %".446" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 220
  store i8 0, i8* %".446"
  %".448" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 221
  store i8 0, i8* %".448"
  %".450" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 222
  store i8 0, i8* %".450"
  %".452" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 223
  store i8 0, i8* %".452"
  %".454" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 224
  store i8 0, i8* %".454"
  %".456" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 225
  store i8 0, i8* %".456"
  %".458" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 226
  store i8 0, i8* %".458"
  %".460" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 227
  store i8 0, i8* %".460"
  %".462" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 228
  store i8 0, i8* %".462"
  %".464" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 229
  store i8 0, i8* %".464"
  %".466" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 230
  store i8 0, i8* %".466"
  %".468" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 231
  store i8 0, i8* %".468"
  %".470" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 232
  store i8 0, i8* %".470"
  %".472" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 233
  store i8 0, i8* %".472"
  %".474" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 234
  store i8 0, i8* %".474"
  %".476" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 235
  store i8 0, i8* %".476"
  %".478" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 236
  store i8 0, i8* %".478"
  %".480" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 237
  store i8 0, i8* %".480"
  %".482" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 238
  store i8 0, i8* %".482"
  %".484" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 239
  store i8 0, i8* %".484"
  %".486" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 240
  store i8 0, i8* %".486"
  %".488" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 241
  store i8 0, i8* %".488"
  %".490" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 242
  store i8 0, i8* %".490"
  %".492" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 243
  store i8 0, i8* %".492"
  %".494" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 244
  store i8 0, i8* %".494"
  %".496" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 245
  store i8 0, i8* %".496"
  %".498" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 246
  store i8 0, i8* %".498"
  %".500" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 247
  store i8 0, i8* %".500"
  %".502" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 248
  store i8 0, i8* %".502"
  %".504" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 249
  store i8 0, i8* %".504"
  %".506" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 250
  store i8 0, i8* %".506"
  %".508" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 251
  store i8 0, i8* %".508"
  %".510" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 252
  store i8 0, i8* %".510"
  %".512" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 253
  store i8 0, i8* %".512"
  %".514" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 254
  store i8 0, i8* %".514"
  %".516" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 255
  store i8 0, i8* %".516"
  %"grade_0" = alloca i8
  store i8 0, i8* %"grade_0"
  %"valid_0" = alloca i1
  store i1 0, i1* %"valid_0"
  %".520" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 0
  store i8 69, i8* %".520"
  %".522" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 1
  store i8 110, i8* %".522"
  %".524" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 2
  store i8 116, i8* %".524"
  %".526" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 3
  store i8 101, i8* %".526"
  %".528" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 4
  store i8 114, i8* %".528"
  %".530" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 5
  store i8 32, i8* %".530"
  %".532" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 6
  store i8 116, i8* %".532"
  %".534" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 7
  store i8 104, i8* %".534"
  %".536" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 8
  store i8 101, i8* %".536"
  %".538" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 9
  store i8 32, i8* %".538"
  %".540" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 10
  store i8 110, i8* %".540"
  %".542" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 11
  store i8 117, i8* %".542"
  %".544" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 12
  store i8 109, i8* %".544"
  %".546" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 13
  store i8 98, i8* %".546"
  %".548" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 14
  store i8 101, i8* %".548"
  %".550" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 15
  store i8 114, i8* %".550"
  %".552" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 16
  store i8 32, i8* %".552"
  %".554" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 17
  store i8 111, i8* %".554"
  %".556" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 18
  store i8 102, i8* %".556"
  %".558" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 19
  store i8 32, i8* %".558"
  %".560" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 20
  store i8 116, i8* %".560"
  %".562" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 21
  store i8 101, i8* %".562"
  %".564" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 22
  store i8 115, i8* %".564"
  %".566" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 23
  store i8 116, i8* %".566"
  %".568" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 24
  store i8 32, i8* %".568"
  %".570" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 25
  store i8 115, i8* %".570"
  %".572" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 26
  store i8 99, i8* %".572"
  %".574" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 27
  store i8 111, i8* %".574"
  %".576" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 28
  store i8 114, i8* %".576"
  %".578" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 29
  store i8 101, i8* %".578"
  %".580" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 30
  store i8 115, i8* %".580"
  %".582" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 31
  store i8 58, i8* %".582"
  %".584" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 32
  store i8 0, i8* %".584"
  %".586" = bitcast [256 x i8]* %"prompt_0" to i8*
  call void @"output_string"(i8* %".586")
  call void @"input_int"(i32* %"n_0")
  store i32 0, i32* %"total_0"
  store i32 0, i32* %"i_0"
  br label %"L0"
L0:
  %"i_0.1" = load i32, i32* %"i_0"
  %"n_0.1" = load i32, i32* %"n_0"
  %".592" = icmp slt i32 %"i_0.1", %"n_0.1"
  %"t0" = alloca i1
  store i1 %".592", i1* %"t0"
  %"t0.1" = load i1, i1* %"t0"
  br i1 %"t0.1", label %"if_true", label %"L2"
L2:
  %"n_0.2" = load i32, i32* %"n_0"
  %".645" = icmp eq i32 %"n_0.2", 0
  %"t3" = alloca i1
  store i1 %".645", i1* %"t3"
  %"t3.1" = load i1, i1* %"t3"
  br i1 %"t3.1", label %"if_true.1", label %"L3"
if_true:
  %"score_1" = alloca i32
  store i32 0, i32* %"score_1"
  %".596" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 0
  store i8 69, i8* %".596"
  %".598" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 1
  store i8 110, i8* %".598"
  %".600" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 2
  store i8 116, i8* %".600"
  %".602" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 3
  store i8 101, i8* %".602"
  %".604" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 4
  store i8 114, i8* %".604"
  %".606" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 5
  store i8 32, i8* %".606"
  %".608" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 6
  store i8 116, i8* %".608"
  %".610" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 7
  store i8 101, i8* %".610"
  %".612" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 8
  store i8 115, i8* %".612"
  %".614" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 9
  store i8 116, i8* %".614"
  %".616" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 10
  store i8 32, i8* %".616"
  %".618" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 11
  store i8 115, i8* %".618"
  %".620" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 12
  store i8 99, i8* %".620"
  %".622" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 13
  store i8 111, i8* %".622"
  %".624" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 14
  store i8 114, i8* %".624"
  %".626" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 15
  store i8 101, i8* %".626"
  %".628" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 16
  store i8 58, i8* %".628"
  %".630" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 17
  store i8 0, i8* %".630"
  %".632" = bitcast [256 x i8]* %"prompt_0" to i8*
  call void @"output_string"(i8* %".632")
  call void @"input_int"(i32* %"score_1")
  %"total_0.1" = load i32, i32* %"total_0"
  %"score_1.1" = load i32, i32* %"score_1"
  %".635" = add i32 %"total_0.1", %"score_1.1"
  %"t1" = alloca i32
  store i32 %".635", i32* %"t1"
  %".637" = load i32, i32* %"t1"
  store i32 %".637", i32* %"total_0"
  br label %"L1"
L1:
  %"i_0.2" = load i32, i32* %"i_0"
  %".640" = add i32 %"i_0.2", 1
  %"t2" = alloca i32
  store i32 %".640", i32* %"t2"
  %".642" = load i32, i32* %"t2"
  store i32 %".642", i32* %"i_0"
  br label %"L0"
L3:
  store i1 1, i1* %"valid_0"
  br label %"L4"
if_true.1:
  store i1 0, i1* %"valid_0"
  br label %"L4"
L4:
  %"valid_0.1" = load i1, i1* %"valid_0"
  %".652" = icmp eq i1 %"valid_0.1", 1
  %"t4" = alloca i1
  store i1 %".652", i1* %"t4"
  %"t4.1" = load i1, i1* %"t4"
  br i1 %"t4.1", label %"if_true.2", label %"L5"
L5:
  store float              0x0, float* %"avg_0"
  br label %"L6"
if_true.2:
  %"total_0.2" = load i32, i32* %"total_0"
  %"n_0.3" = load i32, i32* %"n_0"
  %".655" = sdiv i32 %"total_0.2", %"n_0.3"
  %"t5" = alloca i32
  store i32 %".655", i32* %"t5"
  %".657" = load i32, i32* %"t5"
  %".658" = sitofp i32 %".657" to float
  store float %".658", float* %"avg_0"
  br label %"L6"
L6:
  %"avg_0.1" = load float, float* %"avg_0"
  %".663" = fcmp oge float %"avg_0.1", 0x4056800000000000
  %"t6" = alloca i1
  store i1 %".663", i1* %"t6"
  %"t6.1" = load i1, i1* %"t6"
  br i1 %"t6.1", label %"if_true.3", label %"L7"
L7:
  %"avg_0.2" = load float, float* %"avg_0"
  %".668" = fcmp oge float %"avg_0.2", 0x4054000000000000
  %"t7" = alloca i1
  store i1 %".668", i1* %"t7"
  %"t7.1" = load i1, i1* %"t7"
  br i1 %"t7.1", label %"if_true.4", label %"L9"
if_true.3:
  store i8 65, i8* %"grade_0"
  br label %"L8"
L8:
  %".688" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 0
  store i8 65, i8* %".688"
  %".690" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 1
  store i8 118, i8* %".690"
  %".692" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 2
  store i8 101, i8* %".692"
  %".694" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 3
  store i8 114, i8* %".694"
  %".696" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 4
  store i8 97, i8* %".696"
  %".698" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 5
  store i8 103, i8* %".698"
  %".700" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 6
  store i8 101, i8* %".700"
  %".702" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 7
  store i8 32, i8* %".702"
  %".704" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 8
  store i8 83, i8* %".704"
  %".706" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 9
  store i8 99, i8* %".706"
  %".708" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 10
  store i8 111, i8* %".708"
  %".710" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 11
  store i8 114, i8* %".710"
  %".712" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 12
  store i8 101, i8* %".712"
  %".714" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 13
  store i8 58, i8* %".714"
  %".716" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 14
  store i8 0, i8* %".716"
  %".718" = bitcast [256 x i8]* %"prompt_0" to i8*
  call void @"output_string"(i8* %".718")
  %"avg_0.5" = load float, float* %"avg_0"
  call void @"output_float"(float %"avg_0.5")
  %".721" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 0
  store i8 71, i8* %".721"
  %".723" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 1
  store i8 114, i8* %".723"
  %".725" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 2
  store i8 97, i8* %".725"
  %".727" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 3
  store i8 100, i8* %".727"
  %".729" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 4
  store i8 101, i8* %".729"
  %".731" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 5
  store i8 58, i8* %".731"
  %".733" = getelementptr [256 x i8], [256 x i8]* %"prompt_0", i32 0, i32 6
  store i8 0, i8* %".733"
  %".735" = bitcast [256 x i8]* %"prompt_0" to i8*
  call void @"output_string"(i8* %".735")
  %"grade_0.1" = load i8, i8* %"grade_0"
  call void @"output_char"(i8 %"grade_0.1")
  %"d_0" = alloca i32
  store i32 0, i32* %"d_0"
  store i32 5, i32* %"d_0"
  %"f_0" = alloca i32
  store i32 0, i32* %"f_0"
  store i32 10, i32* %"f_0"
  %"d_0.1" = load i32, i32* %"d_0"
  %".742" = icmp sgt i32 %"d_0.1", 3
  %"t10" = alloca i1
  store i1 %".742", i1* %"t10"
  %"f_0.1" = load i32, i32* %"f_0"
  %".744" = icmp sgt i32 %"f_0.1", 3
  %"t11" = alloca i1
  store i1 %".744", i1* %"t11"
  %"t10.1" = load i1, i1* %"t10"
  %"t11.1" = load i1, i1* %"t11"
  br i1 %"t10.1", label %"and_true", label %"and_end"
L9:
  %"avg_0.3" = load float, float* %"avg_0"
  %".673" = fcmp oge float %"avg_0.3", 0x4051800000000000
  %"t8" = alloca i1
  store i1 %".673", i1* %"t8"
  %"t8.1" = load i1, i1* %"t8"
  br i1 %"t8.1", label %"if_true.5", label %"L11"
if_true.4:
  store i8 66, i8* %"grade_0"
  br label %"L10"
L10:
  br label %"L8"
L11:
  %"avg_0.4" = load float, float* %"avg_0"
  %".678" = fcmp oge float %"avg_0.4", 0x404e000000000000
  %"t9" = alloca i1
  store i1 %".678", i1* %"t9"
  %"t9.1" = load i1, i1* %"t9"
  br i1 %"t9.1", label %"if_true.6", label %"L13"
if_true.5:
  store i8 67, i8* %"grade_0"
  br label %"L12"
L12:
  br label %"L10"
L13:
  store i8 70, i8* %"grade_0"
  br label %"L14"
if_true.6:
  store i8 68, i8* %"grade_0"
  br label %"L14"
L14:
  br label %"L12"
and_true:
  %"t11.2" = load i1, i1* %"t11"
  br label %"and_end"
and_end:
  %".748" = phi  i1 [0, %"L8"], [%"t11.2", %"and_true"]
  %"t12" = alloca i1
  store i1 %".748", i1* %"t12"
  %"t12.1" = load i1, i1* %"t12"
  br i1 %"t12.1", label %"if_true.7", label %"L16"
L16:
  call void @"exit_program"()
  ret i32 0
if_true.7:
  store i32 10, i32* %"d_0"
  br label %"L16"
}

declare void @"input_float"(float* %".1")

declare void @"input_int"(i32* %".1")

declare void @"input_string"(i8* %".1")

declare void @"input_char"(i8* %".1")

declare void @"output_float"(float %".1")

declare void @"output_int"(i32 %".1")

declare void @"output_string"(i8* %".1")

declare void @"output_char"(i8 %".1")

declare void @"exit_program"()
