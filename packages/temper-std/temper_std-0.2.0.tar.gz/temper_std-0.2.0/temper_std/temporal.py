from typing import Sequence as Sequence6, Any as Any9
from builtins import int as int5, bool as bool2, str as str1
from temper_core import int_to_string as int_to_string_1266, string_code_points as string_code_points_1249, str_cat as str_cat_1265
# Type nym`std//temporal.temper.md`.Date connected to datetime.date
daysInMonth__21: 'Sequence6[int5]' = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
def isLeapYear__19(year__22: 'int5') -> 'bool2':
  return__13: 'bool2'
  t_132: 'int5'
  if year__22 % 4 == 0:
    if year__22 % 100 != 0:
      return__13 = True
    else:
      t_132 = year__22 % 400
      return__13 = t_132 == 0
  else:
    return__13 = False
  return return__13
def pad__20(padding__24: 'str1', num__25: 'int5') -> 'str1':
  'If the decimal representation of \\|num\\| is longer than [padding],\nthen that representation.\nOtherwise any sign for [num] followed by the prefix of [padding]\nthat would bring the integer portion up to the length of [padding].\n\n```temper\npad("0000", 123) == "0123") &&\npad("000", 123) == "123") &&\npad("00", 123) == "123") &&\npad("0000", -123) == "-0123") &&\npad("000", -123) == "-123") &&\npad("00", -123) == "-123")\n```'
  return__14: 'str1'
  t_185: 'Any9'
  decimal__27: 'str1' = int_to_string_1266(num__25, 10)
  t_181: 'Any9' = string_code_points_1249(decimal__27)
  decimalCodePoints__28: 'Any9' = t_181
  sign__29: 'str1'
  if decimalCodePoints__28.read() == 45:
    sign__29 = '-'
    t_185 = decimalCodePoints__28.advance(1)
    decimalCodePoints__28 = t_185
  else:
    sign__29 = ''
  paddingCp__30: 'Any9' = string_code_points_1249(padding__24)
  nNeeded__31: 'int5' = paddingCp__30.length - decimalCodePoints__28.length
  if nNeeded__31 <= 0:
    return__14 = decimal__27
  else:
    pad__32: 'str1' = paddingCp__30.limit(nNeeded__31).to_string()
    decimalOnly__33: 'str1' = decimalCodePoints__28.to_string()
    return__14 = str_cat_1265(sign__29, pad__32, decimalOnly__33)
  return return__14
