from abc import ABCMeta as ABCMeta0
from builtins import str as str1, bool as bool2, int as int5, Exception as Exception12, RuntimeError as RuntimeError14, len as len_1254, list as list_1271
from types import MappingProxyType as MappingProxyType3
from typing import Callable as Callable4, Sequence as Sequence6, Optional as Optional7, Union as Union8, Any as Any9, MutableSequence as MutableSequence10
from temper_core import cast_by_type as cast_by_type11, Label as Label13, isinstance_int as isinstance_int15, cast_by_test as cast_by_test16, list_join as list_join_1242, generic_eq as generic_eq_1245, list_builder_add as list_builder_add_1246, string_code_points as string_code_points_1249, list_get as list_get_1255, str_cat as str_cat_1265, int_to_string as int_to_string_1266
from temper_core.regex import compiled_regex_compile_formatted as compiled_regex_compile_formatted_1238, compiled_regex_compiled_found as compiled_regex_compiled_found_1239, compiled_regex_compiled_find as compiled_regex_compiled_find_1240, compiled_regex_compiled_replace as compiled_regex_compiled_replace_1241, regex_formatter_push_capture_name as regex_formatter_push_capture_name_1247, regex_formatter_push_code_to as regex_formatter_push_code_to_1248
class Regex(metaclass = ABCMeta0):
  def compiled(this__8) -> 'CompiledRegex':
    return CompiledRegex(this__8)
  def found(this__9, text__121: 'str1') -> 'bool2':
    return this__9.compiled().found(text__121)
  def find(this__10, text__124: 'str1') -> 'MappingProxyType3[str1, Group]':
    return this__10.compiled().find(text__124)
  def replace(this__11, text__127: 'str1', format__128: 'Callable4[[MappingProxyType3[str1, Group]], str1]') -> 'str1':
    return this__11.compiled().replace(text__127, format__128)
class Capture(Regex):
  name__130: 'str1'
  item__131: 'Regex'
  __slots__ = ('name__130', 'item__131')
  def constructor__132(this__50, name__133: 'str1', item__134: 'Regex') -> 'None':
    this__50.name__130 = name__133
    this__50.item__131 = item__134
  def __init__(this__50, name__133: 'str1', item__134: 'Regex') -> None:
    this__50.constructor__132(name__133, item__134)
  @property
  def name(this__330) -> 'str1':
    return this__330.name__130
  @property
  def item(this__334) -> 'Regex':
    return this__334.item__131
class CodePart(Regex, metaclass = ABCMeta0):
  pass
class CodePoints(CodePart):
  value__135: 'str1'
  __slots__ = ('value__135',)
  def constructor__136(this__52, value__137: 'str1') -> 'None':
    this__52.value__135 = value__137
  def __init__(this__52, value__137: 'str1') -> None:
    this__52.constructor__136(value__137)
  @property
  def value(this__310) -> 'str1':
    return this__310.value__135
class Special(Regex, metaclass = ABCMeta0):
  pass
class SpecialSet(CodePart, Special, metaclass = ABCMeta0):
  pass
class CodeRange(CodePart):
  min__145: 'int5'
  max__146: 'int5'
  __slots__ = ('min__145', 'max__146')
  def constructor__147(this__68, min__148: 'int5', max__149: 'int5') -> 'None':
    this__68.min__145 = min__148
    this__68.max__146 = max__149
  def __init__(this__68, min__148: 'int5', max__149: 'int5') -> None:
    this__68.constructor__147(min__148, max__149)
  @property
  def min(this__338) -> 'int5':
    return this__338.min__145
  @property
  def max(this__342) -> 'int5':
    return this__342.max__146
class CodeSet(Regex):
  items__150: 'Sequence6[CodePart]'
  negated__151: 'bool2'
  __slots__ = ('items__150', 'negated__151')
  def constructor__152(this__70, items__153: 'Sequence6[CodePart]', negated: Optional7['bool2'] = None) -> 'None':
    negated__154: Optional7['bool2'] = negated
    if negated__154 is None:
      negated__154 = False
    this__70.items__150 = items__153
    this__70.negated__151 = negated__154
  def __init__(this__70, items__153: 'Sequence6[CodePart]', negated: Optional7['bool2'] = None) -> None:
    negated__154: Optional7['bool2'] = negated
    this__70.constructor__152(items__153, negated__154)
  @property
  def items(this__346) -> 'Sequence6[CodePart]':
    return this__346.items__150
  @property
  def negated(this__350) -> 'bool2':
    return this__350.negated__151
class Or(Regex):
  items__155: 'Sequence6[Regex]'
  __slots__ = ('items__155',)
  def constructor__156(this__73, items__157: 'Sequence6[Regex]') -> 'None':
    this__73.items__155 = items__157
  def __init__(this__73, items__157: 'Sequence6[Regex]') -> None:
    this__73.constructor__156(items__157)
  @property
  def items(this__314) -> 'Sequence6[Regex]':
    return this__314.items__155
class Repeat(Regex):
  item__158: 'Regex'
  min__159: 'int5'
  max__160: 'Union8[int5, None]'
  reluctant__161: 'bool2'
  __slots__ = ('item__158', 'min__159', 'max__160', 'reluctant__161')
  def constructor__162(this__76, item__163: 'Regex', min__164: 'int5', max__165: 'Union8[int5, None]', reluctant: Optional7['bool2'] = None) -> 'None':
    reluctant__166: Optional7['bool2'] = reluctant
    if reluctant__166 is None:
      reluctant__166 = False
    this__76.item__158 = item__163
    this__76.min__159 = min__164
    this__76.max__160 = max__165
    this__76.reluctant__161 = reluctant__166
  def __init__(this__76, item__163: 'Regex', min__164: 'int5', max__165: 'Union8[int5, None]', reluctant: Optional7['bool2'] = None) -> None:
    reluctant__166: Optional7['bool2'] = reluctant
    this__76.constructor__162(item__163, min__164, max__165, reluctant__166)
  @property
  def item(this__354) -> 'Regex':
    return this__354.item__158
  @property
  def min(this__358) -> 'int5':
    return this__358.min__159
  @property
  def max(this__362) -> 'Union8[int5, None]':
    return this__362.max__160
  @property
  def reluctant(this__366) -> 'bool2':
    return this__366.reluctant__161
class Sequence(Regex):
  items__175: 'Sequence6[Regex]'
  __slots__ = ('items__175',)
  def constructor__176(this__82, items__177: 'Sequence6[Regex]') -> 'None':
    this__82.items__175 = items__177
  def __init__(this__82, items__177: 'Sequence6[Regex]') -> None:
    this__82.constructor__176(items__177)
  @property
  def items(this__370) -> 'Sequence6[Regex]':
    return this__370.items__175
class Group:
  name__178: 'str1'
  value__179: 'str1'
  codePointsBegin__180: 'int5'
  __slots__ = ('name__178', 'value__179', 'codePointsBegin__180')
  def constructor__181(this__85, name__182: 'str1', value__183: 'str1', codePointsBegin__184: 'int5') -> 'None':
    this__85.name__178 = name__182
    this__85.value__179 = value__183
    this__85.codePointsBegin__180 = codePointsBegin__184
  def __init__(this__85, name__182: 'str1', value__183: 'str1', codePointsBegin__184: 'int5') -> None:
    this__85.constructor__181(name__182, value__183, codePointsBegin__184)
  @property
  def name(this__298) -> 'str1':
    return this__298.name__178
  @property
  def value(this__302) -> 'str1':
    return this__302.value__179
  @property
  def code_points_begin(this__306) -> 'int5':
    return this__306.codePointsBegin__180
class RegexRefs__19:
  codePoints__185: 'CodePoints'
  group__186: 'Group'
  orObject__187: 'Or'
  __slots__ = ('codePoints__185', 'group__186', 'orObject__187')
  def constructor__188(this__87, code_points: Optional7['CodePoints'] = None, group: Optional7['Group'] = None, or_object: Optional7['Or'] = None) -> 'None':
    codePoints__189: Optional7['CodePoints'] = code_points
    group__190: Optional7['Group'] = group
    orObject__191: Optional7['Or'] = or_object
    t_1206: 'CodePoints'
    t_1208: 'Group'
    t_1210: 'Or'
    if codePoints__189 is None:
      t_1206 = CodePoints('')
      codePoints__189 = t_1206
    if group__190 is None:
      t_1208 = Group('', '', 0)
      group__190 = t_1208
    if orObject__191 is None:
      t_1210 = Or(())
      orObject__191 = t_1210
    this__87.codePoints__185 = codePoints__189
    this__87.group__186 = group__190
    this__87.orObject__187 = orObject__191
  def __init__(this__87, code_points: Optional7['CodePoints'] = None, group: Optional7['Group'] = None, or_object: Optional7['Or'] = None) -> None:
    codePoints__189: Optional7['CodePoints'] = code_points
    group__190: Optional7['Group'] = group
    orObject__191: Optional7['Or'] = or_object
    this__87.constructor__188(codePoints__189, group__190, orObject__191)
  @property
  def code_points(this__318) -> 'CodePoints':
    return this__318.codePoints__185
  @property
  def group(this__322) -> 'Group':
    return this__322.group__186
  @property
  def or_object(this__326) -> 'Or':
    return this__326.orObject__187
class CompiledRegex:
  data__192: 'Regex'
  compiled__206: 'Any9'
  __slots__ = ('data__192', 'compiled__206')
  def constructor__193(this__20, data__194: 'Regex') -> 'None':
    this__20.data__192 = data__194
    t_1080: 'str1' = this__20.format__225()
    t_1081: 'Any9' = compiled_regex_compile_formatted_1238(this__20, t_1080)
    this__20.compiled__206 = t_1081
  def __init__(this__20, data__194: 'Regex') -> None:
    this__20.constructor__193(data__194)
  def found(this__21, text__197: 'str1') -> 'bool2':
    return compiled_regex_compiled_found_1239(this__21, this__21.compiled__206, text__197)
  def find(this__22, text__200: 'str1') -> 'MappingProxyType3[str1, Group]':
    return compiled_regex_compiled_find_1240(this__22, this__22.compiled__206, text__200, regexRefs__117)
  def replace(this__23, text__203: 'str1', format__204: 'Callable4[[MappingProxyType3[str1, Group]], str1]') -> 'str1':
    return compiled_regex_compiled_replace_1241(this__23, this__23.compiled__206, text__203, format__204, regexRefs__117)
  def format__225(this__28) -> 'str1':
    return RegexFormatter__29().format(this__28.data__192)
  @property
  def data(this__408) -> 'Regex':
    return this__408.data__192
class RegexFormatter__29:
  out__227: 'MutableSequence10[str1]'
  __slots__ = ('out__227',)
  def format(this__30, regex__229: 'Regex') -> 'str1':
    this__30.pushRegex__232(regex__229)
    t_1175: 'MutableSequence10[str1]' = this__30.out__227
    def fn__1172(x__231: 'str1') -> 'str1':
      return x__231
    return list_join_1242(t_1175, '', fn__1172)
  def pushRegex__232(this__31, regex__233: 'Regex') -> 'None':
    t_764: 'bool2'
    t_765: 'Capture'
    t_768: 'bool2'
    t_769: 'CodePoints'
    t_772: 'bool2'
    t_773: 'CodeRange'
    t_776: 'bool2'
    t_777: 'CodeSet'
    t_780: 'bool2'
    t_781: 'Or'
    t_784: 'bool2'
    t_785: 'Repeat'
    t_788: 'bool2'
    t_789: 'Sequence'
    try:
      cast_by_type11(regex__233, Capture)
      t_764 = True
    except Exception12:
      t_764 = False
    with Label13() as s__1243_1244:
      if t_764:
        try:
          t_765 = cast_by_type11(regex__233, Capture)
        except Exception12:
          s__1243_1244.break_()
        this__31.pushCapture__235(t_765)
      else:
        try:
          cast_by_type11(regex__233, CodePoints)
          t_768 = True
        except Exception12:
          t_768 = False
        if t_768:
          try:
            t_769 = cast_by_type11(regex__233, CodePoints)
          except Exception12:
            s__1243_1244.break_()
          this__31.pushCodePoints__251(t_769, False)
        else:
          try:
            cast_by_type11(regex__233, CodeRange)
            t_772 = True
          except Exception12:
            t_772 = False
          if t_772:
            try:
              t_773 = cast_by_type11(regex__233, CodeRange)
            except Exception12:
              s__1243_1244.break_()
            this__31.pushCodeRange__256(t_773)
          else:
            try:
              cast_by_type11(regex__233, CodeSet)
              t_776 = True
            except Exception12:
              t_776 = False
            if t_776:
              try:
                t_777 = cast_by_type11(regex__233, CodeSet)
              except Exception12:
                s__1243_1244.break_()
              this__31.pushCodeSet__262(t_777)
            else:
              try:
                cast_by_type11(regex__233, Or)
                t_780 = True
              except Exception12:
                t_780 = False
              if t_780:
                try:
                  t_781 = cast_by_type11(regex__233, Or)
                except Exception12:
                  s__1243_1244.break_()
                this__31.pushOr__274(t_781)
              else:
                try:
                  cast_by_type11(regex__233, Repeat)
                  t_784 = True
                except Exception12:
                  t_784 = False
                if t_784:
                  try:
                    t_785 = cast_by_type11(regex__233, Repeat)
                  except Exception12:
                    s__1243_1244.break_()
                  this__31.pushRepeat__278(t_785)
                else:
                  try:
                    cast_by_type11(regex__233, Sequence)
                    t_788 = True
                  except Exception12:
                    t_788 = False
                  if t_788:
                    try:
                      t_789 = cast_by_type11(regex__233, Sequence)
                    except Exception12:
                      s__1243_1244.break_()
                    this__31.pushSequence__283(t_789)
                  elif generic_eq_1245(regex__233, begin):
                    try:
                      list_builder_add_1246(this__31.out__227, '^')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, dot):
                    try:
                      list_builder_add_1246(this__31.out__227, '.')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, end):
                    try:
                      list_builder_add_1246(this__31.out__227, '$')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, word_boundary):
                    try:
                      list_builder_add_1246(this__31.out__227, '\\b')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, digit):
                    try:
                      list_builder_add_1246(this__31.out__227, '\\d')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, space):
                    try:
                      list_builder_add_1246(this__31.out__227, '\\s')
                    except Exception12:
                      s__1243_1244.break_()
                  elif generic_eq_1245(regex__233, word):
                    try:
                      list_builder_add_1246(this__31.out__227, '\\w')
                    except Exception12:
                      s__1243_1244.break_()
                  else:
                    None
      return
    raise RuntimeError14()
  def pushCapture__235(this__32, capture__236: 'Capture') -> 'None':
    list_builder_add_1246(this__32.out__227, '(')
    t_759: 'MutableSequence10[str1]' = this__32.out__227
    t_1159: 'str1' = capture__236.name
    regex_formatter_push_capture_name_1247(this__32, t_759, t_1159)
    t_1160: 'Regex' = capture__236.item
    this__32.pushRegex__232(t_1160)
    list_builder_add_1246(this__32.out__227, ')')
  def pushCode__242(this__34, code__243: 'int5', insideCodeSet__244: 'bool2') -> 'None':
    regex_formatter_push_code_to_1248(this__34, this__34.out__227, code__243, insideCodeSet__244)
  def pushCodePoints__251(this__36, codePoints__252: 'CodePoints', insideCodeSet__253: 'bool2') -> 'None':
    t_1148: 'int5'
    t_1149: 'Any9'
    t_1153: 'Any9' = string_code_points_1249(codePoints__252.value)
    slice__255: 'Any9' = t_1153
    while True:
      if not slice__255.is_empty:
        t_1148 = slice__255.read()
        this__36.pushCode__242(t_1148, insideCodeSet__253)
        t_1149 = slice__255.advance(1)
        slice__255 = t_1149
      else:
        break
  def pushCodeRange__256(this__37, codeRange__257: 'CodeRange') -> 'None':
    list_builder_add_1246(this__37.out__227, '[')
    this__37.pushCodeRangeUnwrapped__259(codeRange__257)
    list_builder_add_1246(this__37.out__227, ']')
  def pushCodeRangeUnwrapped__259(this__38, codeRange__260: 'CodeRange') -> 'None':
    t_1141: 'int5' = codeRange__260.min
    this__38.pushCode__242(t_1141, True)
    list_builder_add_1246(this__38.out__227, '-')
    t_1143: 'int5' = codeRange__260.max
    this__38.pushCode__242(t_1143, True)
  def pushCodeSet__262(this__39, codeSet__263: 'CodeSet') -> 'None':
    t_1137: 'int5'
    t_737: 'bool2'
    t_738: 'CodeSet'
    t_743: 'CodePart'
    adjusted__265: 'Regex' = this__39.adjustCodeSet__267(codeSet__263, regexRefs__117)
    try:
      cast_by_type11(adjusted__265, CodeSet)
      t_737 = True
    except Exception12:
      t_737 = False
    with Label13() as s__1250_1252:
      if t_737:
        with Label13() as s__1251_1253:
          try:
            t_738 = cast_by_type11(adjusted__265, CodeSet)
            list_builder_add_1246(this__39.out__227, '[')
          except Exception12:
            s__1251_1253.break_()
          if t_738.negated:
            try:
              list_builder_add_1246(this__39.out__227, '^')
            except Exception12:
              s__1251_1253.break_()
          else:
            None
          i__266: 'int5' = 0
          while True:
            t_1137 = len_1254(t_738.items)
            if i__266 < t_1137:
              try:
                t_743 = list_get_1255(t_738.items, i__266)
              except Exception12:
                s__1251_1253.break_()
              this__39.pushCodeSetItem__271(t_743)
              i__266 = i__266 + 1
            else:
              break
          try:
            list_builder_add_1246(this__39.out__227, ']')
            s__1250_1252.break_()
          except Exception12:
            pass
        raise RuntimeError14()
      this__39.pushRegex__232(adjusted__265)
  def adjustCodeSet__267(this__40, codeSet__268: 'CodeSet', regexRefs__269: 'RegexRefs__19') -> 'Regex':
    return codeSet__268
  def pushCodeSetItem__271(this__41, codePart__272: 'CodePart') -> 'None':
    t_724: 'bool2'
    t_725: 'CodePoints'
    t_728: 'bool2'
    t_729: 'CodeRange'
    t_732: 'bool2'
    t_733: 'SpecialSet'
    try:
      cast_by_type11(codePart__272, CodePoints)
      t_724 = True
    except Exception12:
      t_724 = False
    with Label13() as s__1256_1257:
      if t_724:
        try:
          t_725 = cast_by_type11(codePart__272, CodePoints)
        except Exception12:
          s__1256_1257.break_()
        this__41.pushCodePoints__251(t_725, True)
      else:
        try:
          cast_by_type11(codePart__272, CodeRange)
          t_728 = True
        except Exception12:
          t_728 = False
        if t_728:
          try:
            t_729 = cast_by_type11(codePart__272, CodeRange)
          except Exception12:
            s__1256_1257.break_()
          this__41.pushCodeRangeUnwrapped__259(t_729)
        else:
          try:
            cast_by_type11(codePart__272, SpecialSet)
            t_732 = True
          except Exception12:
            t_732 = False
          if t_732:
            try:
              t_733 = cast_by_type11(codePart__272, SpecialSet)
            except Exception12:
              s__1256_1257.break_()
            this__41.pushRegex__232(t_733)
          else:
            None
      return
    raise RuntimeError14()
  def pushOr__274(this__42, or__275: 'Or') -> 'None':
    t_1121: 'int5'
    t_716: 'Regex'
    t_721: 'Regex'
    with Label13() as s__1258_1260:
      if not (not or__275.items):
        with Label13() as s__1259_1262:
          try:
            list_builder_add_1246(this__42.out__227, '(?:')
            t_716 = list_get_1255(or__275.items, 0)
          except Exception12:
            s__1259_1262.break_()
          this__42.pushRegex__232(t_716)
          i__277: 'int5' = 1
          while True:
            t_1121 = len_1254(or__275.items)
            if i__277 < t_1121:
              try:
                list_builder_add_1246(this__42.out__227, '|')
                t_721 = list_get_1255(or__275.items, i__277)
              except Exception12:
                break
              this__42.pushRegex__232(t_721)
              i__277 = i__277 + 1
            else:
              try:
                list_builder_add_1246(this__42.out__227, ')')
              except Exception12:
                s__1259_1262.break_()
              s__1258_1260.break_()
        raise RuntimeError14()
  def pushRepeat__278(this__43, repeat__279: 'Repeat') -> 'None':
    t_1111: 'Regex'
    t_703: 'bool2'
    t_704: 'bool2'
    t_705: 'bool2'
    t_708: 'int5'
    t_710: 'MutableSequence10[str1]'
    with Label13() as s__1263_1264:
      min__281: 'int5'
      max__282: 'Union8[int5, None]'
      try:
        list_builder_add_1246(this__43.out__227, '(?:')
        t_1111 = repeat__279.item
        this__43.pushRegex__232(t_1111)
        list_builder_add_1246(this__43.out__227, ')')
        min__281 = repeat__279.min
        max__282 = repeat__279.max
      except Exception12:
        s__1263_1264.break_()
      if min__281 == 0:
        t_703 = max__282 == 1
      else:
        t_703 = False
      if t_703:
        try:
          list_builder_add_1246(this__43.out__227, '?')
        except Exception12:
          s__1263_1264.break_()
      else:
        if min__281 == 0:
          t_704 = max__282 == None
        else:
          t_704 = False
        if t_704:
          try:
            list_builder_add_1246(this__43.out__227, '*')
          except Exception12:
            s__1263_1264.break_()
        else:
          if min__281 == 1:
            t_705 = max__282 == None
          else:
            t_705 = False
          if t_705:
            try:
              list_builder_add_1246(this__43.out__227, '+')
            except Exception12:
              s__1263_1264.break_()
          else:
            try:
              list_builder_add_1246(this__43.out__227, str_cat_1265('{', int_to_string_1266(min__281)))
            except Exception12:
              s__1263_1264.break_()
            if min__281 != max__282:
              try:
                list_builder_add_1246(this__43.out__227, ',')
              except Exception12:
                s__1263_1264.break_()
              if max__282 != None:
                t_710 = this__43.out__227
                try:
                  t_708 = cast_by_test16(max__282, isinstance_int15)
                  list_builder_add_1246(t_710, int_to_string_1266(t_708))
                except Exception12:
                  s__1263_1264.break_()
              else:
                None
            else:
              None
            try:
              list_builder_add_1246(this__43.out__227, '}')
            except Exception12:
              s__1263_1264.break_()
      if repeat__279.reluctant:
        try:
          list_builder_add_1246(this__43.out__227, '?')
        except Exception12:
          s__1263_1264.break_()
      else:
        None
      return
    raise RuntimeError14()
  def pushSequence__283(this__44, sequence__284: 'Sequence') -> 'None':
    t_1109: 'int5'
    t_697: 'Regex'
    i__286: 'int5' = 0
    with Label13() as s__1267_1268:
      while True:
        t_1109 = len_1254(sequence__284.items)
        if i__286 < t_1109:
          try:
            t_697 = list_get_1255(sequence__284.items, i__286)
          except Exception12:
            break
          this__44.pushRegex__232(t_697)
          i__286 = i__286 + 1
        else:
          s__1267_1268.break_()
      raise RuntimeError14()
  def max_code(this__45, codePart__288: 'CodePart') -> 'Union8[int5, None]':
    return__116: 'Union8[int5, None]'
    t_1087: 'Any9'
    t_1089: 'Any9'
    t_1094: 'Union8[int5, None]'
    t_1097: 'Union8[int5, None]'
    t_1100: 'Union8[int5, None]'
    t_1103: 'Union8[int5, None]'
    t_670: 'bool2'
    t_671: 'CodePoints'
    t_683: 'bool2'
    t_684: 'CodeRange'
    try:
      cast_by_type11(codePart__288, CodePoints)
      t_670 = True
    except Exception12:
      t_670 = False
    with Label13() as s__1269_1270:
      if t_670:
        try:
          t_671 = cast_by_type11(codePart__288, CodePoints)
        except Exception12:
          s__1269_1270.break_()
        value__290: 'str1' = t_671.value
        if not value__290:
          return__116 = None
        else:
          max__291: 'int5' = 0
          t_1087 = string_code_points_1249(value__290)
          slice__292: 'Any9' = t_1087
          while True:
            if not slice__292.is_empty:
              next__293: 'int5' = slice__292.read()
              if next__293 > max__291:
                max__291 = next__293
              else:
                None
              t_1089 = slice__292.advance(1)
              slice__292 = t_1089
            else:
              break
          return__116 = max__291
      else:
        try:
          cast_by_type11(codePart__288, CodeRange)
          t_683 = True
        except Exception12:
          t_683 = False
        if t_683:
          try:
            t_684 = cast_by_type11(codePart__288, CodeRange)
            t_1094 = t_684.max
            return__116 = t_1094
          except Exception12:
            s__1269_1270.break_()
        elif generic_eq_1245(codePart__288, digit):
          t_1097 = string_code_points_1249('9').read()
          try:
            return__116 = t_1097
          except Exception12:
            s__1269_1270.break_()
        elif generic_eq_1245(codePart__288, space):
          t_1100 = string_code_points_1249(' ').read()
          try:
            return__116 = t_1100
          except Exception12:
            s__1269_1270.break_()
        elif generic_eq_1245(codePart__288, word):
          t_1103 = string_code_points_1249('z').read()
          try:
            return__116 = t_1103
          except Exception12:
            s__1269_1270.break_()
        else:
          return__116 = None
      return return__116
    raise RuntimeError14()
  def constructor__294(this__98, out: Optional7['MutableSequence10[str1]'] = None) -> 'None':
    out__295: Optional7['MutableSequence10[str1]'] = out
    t_1083: 'MutableSequence10[str1]'
    if out__295 is None:
      t_1083 = list_1271()
      out__295 = t_1083
    this__98.out__227 = out__295
  def __init__(this__98, out: Optional7['MutableSequence10[str1]'] = None) -> None:
    out__295: Optional7['MutableSequence10[str1]'] = out
    this__98.constructor__294(out__295)
regexRefs__117: 'RegexRefs__19' = RegexRefs__19()
class Begin__12(Special):
  __slots__ = ()
  def constructor__138(this__54) -> 'None':
    None
  def __init__(this__54) -> None:
    this__54.constructor__138()
begin: 'Special' = Begin__12()
class Dot__13(Special):
  __slots__ = ()
  def constructor__139(this__56) -> 'None':
    None
  def __init__(this__56) -> None:
    this__56.constructor__139()
dot: 'Special' = Dot__13()
class End__14(Special):
  __slots__ = ()
  def constructor__140(this__58) -> 'None':
    None
  def __init__(this__58) -> None:
    this__58.constructor__140()
end: 'Special' = End__14()
class WordBoundary__15(Special):
  __slots__ = ()
  def constructor__141(this__60) -> 'None':
    None
  def __init__(this__60) -> None:
    this__60.constructor__141()
word_boundary: 'Special' = WordBoundary__15()
class Digit__16(SpecialSet):
  __slots__ = ()
  def constructor__142(this__62) -> 'None':
    None
  def __init__(this__62) -> None:
    this__62.constructor__142()
digit: 'SpecialSet' = Digit__16()
class Space__17(SpecialSet):
  __slots__ = ()
  def constructor__143(this__64) -> 'None':
    None
  def __init__(this__64) -> None:
    this__64.constructor__143()
space: 'SpecialSet' = Space__17()
class Word__18(SpecialSet):
  __slots__ = ()
  def constructor__144(this__66) -> 'None':
    None
  def __init__(this__66) -> None:
    this__66.constructor__144()
word: 'SpecialSet' = Word__18()
def entire(item__167: 'Regex') -> 'Regex':
  global begin, end
  return Sequence((begin, item__167, end))
def one_or_more(item__169: 'Regex', reluctant: Optional7['bool2'] = None) -> 'Repeat':
  reluctant__170: Optional7['bool2'] = reluctant
  if reluctant__170 is None:
    reluctant__170 = False
  return Repeat(item__169, 1, None, reluctant__170)
def optional(item__172: 'Regex', reluctant: Optional7['bool2'] = None) -> 'Repeat':
  reluctant__173: Optional7['bool2'] = reluctant
  if reluctant__173 is None:
    reluctant__173 = False
  return Repeat(item__172, 0, 1, reluctant__173)
