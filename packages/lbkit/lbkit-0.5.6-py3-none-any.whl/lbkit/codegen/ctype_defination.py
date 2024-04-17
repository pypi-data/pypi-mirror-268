"""语言相关类型定义"""
import sys


class IdfValidator():
    def odf_schema(self, allow_ref, idf_validator):
        return None


class BoolValidator(IdfValidator):
    def odf_schema(self, allow_ref, idf_validator):
        if allow_ref:
            return {
                "anyOf": [
                    {
                        "type": "boolean"
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            return {
                "type": "boolean"
            }


class BoolArrayValidator(BoolValidator):
    def odf_schema(self, allow_ref, idf_validator):
        parent_schema = super().odf_schema(False, idf_validator)
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "type": "array",
                        "item": parent_schema
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "type": "array",
                "item": parent_schema
            }

        return schema


class IntegerValidator(IdfValidator):
    maximum = sys.maxsize * 2
    minimum = -(sys.maxsize + 1) * 2

    def __init__(self, max, min):
        self.maximum = max
        self.minimum = min
        super().__init__()

    def odf_schema(self, allow_ref, idf_validator):
        """
            返回整数类型成员的ODF schema
            idf_validator为IDF模型中加载的数据验证器的对象
        """
        max = idf_validator.get("max", self.maximum)
        if max > self.maximum:
            max = self.maximum
        min = idf_validator.get("min", self.minimum)
        if min < self.minimum:
            min = self.minimum
        if allow_ref:
            return {
                "anyOf": [
                    {
                        "type": "integer",
                        "maximum": max,
                        "minimum": min
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            return {
                "type": "integer",
                "maximum": max,
                "minimum": min
            }


class IntegerArrayValidator(IntegerValidator):
    def odf_schema(self, allow_ref, idf_validator):
        parent_schema = super().odf_schema(False, idf_validator)
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "type": "array",
                        "item": parent_schema
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "type": "array",
                "item": parent_schema
            }

        return schema


class FloatValidator(IdfValidator):
    maximum = sys.float_info.max
    minimum = -sys.float_info.max

    def __init__(self):
        super().__init__()

    def odf_schema(self, allow_ref, idf_validator):
        """
            返回整数类型成员的ODF schema
            idf_validator为IDF模型中加载的数据验证器的对象
        """
        max = idf_validator.get("max", self.maximum)
        min = idf_validator.get("min", self.minimum)
        exclusive_max = idf_validator.get("exclusive_max", None)
        exclusive_min = idf_validator.get("exclusive_min", None)
        max_key = "maximum"
        max_val = max
        min_key = "minimum"
        min_val = min
        if exclusive_max is not None:
            max_key = "exclusiveMaximum"
            max_val = exclusive_max
        if exclusive_min is not None:
            max_key = "exclusiveMinimum"
            min_val = exclusive_min
        if allow_ref:
            return {
                "anyOf": [
                    {
                        "type": "number",
                        max_key: max_val,
                        min_key: min_val
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            return {
                "type": "number",
                max_key: max_val,
                min_key: min_val
            }


class FloatArrayValidator(FloatValidator):
    def odf_schema(self, allow_ref, idf_validator):
        parent_schema = super().odf_schema(False, idf_validator)
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "type": "array",
                        "item": parent_schema
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "type": "array",
                "item": parent_schema
            }
        return schema


class StringValidator(IdfValidator):
    pattern = None
    def __init__(self, pattern):
        self.pattern = pattern
        super().__init__()

    def odf_schema(self, allow_ref, idf_validator):
        pattern = idf_validator.get("pattern", self.pattern)
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "type": "string"
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
            if pattern is not None:
                schema["anyOf"][0]["pattern"] = pattern
        else:
            schema = {
                "type": "string",
                "pattern": pattern
            }
        return schema


class StringArrayValidator(StringValidator):
    def odf_schema(self, allow_ref, idf_validator):
        parent_schema = super().odf_schema(False, idf_validator)
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "type": "array",
                        "item": parent_schema
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "type": "array",
                "item": parent_schema
            }
        return schema

class RefObjValidator(IdfValidator):
    def __init__(self):
        super().__init__()

    def odf_schema(self, allow_ref, idf_validator):
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "$ref": "#/$defs/ref_obj"
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "$ref": "#/$defs/ref_obj"
            }
        return schema


class RefObjArrayValidator(RefObjValidator):
    def odf_schema(self, allow_ref, idf_validator):
        if allow_ref:
            schema = {
                "anyOf": [
                    {
                        "$ref": "#/$defs/ref_obj_array"
                    },
                    {
                        "$ref": "#/$defs/ref_value"
                    }
                ]
            }
        else:
            schema = {
                "$ref": "#/$defs/ref_obj_array"
            }
        return schema


class CTypeBase(object):
    """C语言相关的操作函数＆类型定义"""
    def __init__(self, declare, free_func, encode_func, decode_func, validator: IdfValidator = None):
        self.declare = declare
        self.free_func = free_func
        self.encode_func = encode_func
        self.decode_func = decode_func
        self.validator = validator


"""定义支持的C语言类型"""
CTYPE_OBJS = {
    "boolean": CTypeBase(
        ["gboolean <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_boolean(<arg_name>)"],
        ["<arg_in> = g_variant_get_boolean(<arg_name>)"],
        BoolValidator()
    ),
    "byte": CTypeBase(
        ["guint8 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_byte(<arg_name>)"],
        ["<arg_in> = g_variant_get_byte(<arg_name>)"],
        IntegerValidator(0xff, 0)
    ),
    "int16": CTypeBase(
        ["gint16 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_int16(<arg_name>)"],
        ["<arg_in> = g_variant_get_int16(<arg_name>)"],
        IntegerValidator(0x7fff, -(0x8000))
    ),
    "uint16": CTypeBase(
        ["guint16 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_uint16(<arg_name>)"],
        ["<arg_in> = g_variant_get_uint16(<arg_name>)"],
        IntegerValidator(0xffff, 0)
    ),
    "int32": CTypeBase(
        ["gint32 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_int32(<arg_name>)"],
        ["<arg_in> = g_variant_get_int32(<arg_name>)"],
        IntegerValidator(0x7fff_ffff, -(0x8000_0000))
    ),
    "uint32": CTypeBase(
        ["guint32 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_uint32(<arg_name>)"],
        ["<arg_in> = g_variant_get_uint32(<arg_name>)"],
        IntegerValidator(0xffff_ffff, 0)
    ),
    "int64": CTypeBase(
        ["gint64 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_int64(<arg_name>)"],
        ["<arg_in> = g_variant_get_int64(<arg_name>)"],
        IntegerValidator(0x7fff_ffff_ffff_ffff, -(0x8000_0000_0000_0000))
    ),
    "uint64": CTypeBase(
        ["guint64 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_uint64(<arg_name>)"],
        ["<arg_in> = g_variant_get_uint64(<arg_name>)"],
        IntegerValidator(0xffff_ffff_ffff_ffff, 0)
    ),
    "size": CTypeBase(
        ["gsize <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_uint64(<arg_name>)"],
        ["<arg_in> = g_variant_get_uint64(<arg_name>)"],
        IntegerValidator(0xffff_ffff_ffff_ffff, 0)
    ),
    "ssize": CTypeBase(
        ["gssize <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_int64(<arg_name>)"],
        ["<arg_in> = g_variant_get_int64(<arg_name>)"],
        IntegerValidator(0x7fff_ffff_ffff_ffff, -(0x8000_0000_0000_0000))
    ),
    "double": CTypeBase(
        ["gdouble <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_double(<arg_name>)"],
        ["<arg_in> = g_variant_get_double(<arg_name>)"],
        FloatValidator()
    ),
    "unixfd": CTypeBase(
        ["gint32 <arg_name>"],
        [],
        ["<arg_out> = g_variant_new_handle(<arg_name>)"],
        ["<arg_in> = g_variant_get_handle(<arg_name>)"],
        IntegerValidator(0x7fff_ffff_ffff_ffff, 0)
    ),
    "string": CTypeBase(
        ["<const>gchar *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_string_encode(<arg_name>)"],
        ["<arg_in> = g_strdup(g_variant_get_string(<arg_name>, NULL))"],
        StringValidator("^.*$")
    ),
    "object_path": CTypeBase(
        ["<const>gchar *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_object_path_encode(<arg_name>)"],
        ["<arg_in> = g_strdup(g_variant_get_string(<arg_name>, NULL))"],
        StringValidator("^(/[A-Z0-9a-z_]+)*$")
    ),
    "signature": CTypeBase(
        ["<const>gchar *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_signature_encode(<arg_name>)"],
        ["<arg_in> = g_strdup(g_variant_get_string(<arg_name>, NULL))"],
        StringValidator("^([abynqiuxtdsogv\\{\\}\\(\\)])+$")
    ),
    "variant": CTypeBase(
        ["GVariant *<arg_name>"],
        ["gcl_unref_p((GVariant **)&<arg_name>)"],
        ["g_variant_take_ref(<arg_name>)", "<arg_out> = g_variant_new_variant(<arg_name>)"],
        ["<arg_in> = g_variant_get_variant(<arg_name>)"],
        IdfValidator()
    ),
    "array[boolean]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gboolean *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_boolean_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_boolean_decode(<arg_name>, &n_<arg_in>)"],
        BoolArrayValidator()
    ),
    "array[byte]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>guint8 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_byte_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_byte_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0xff, 0)
    ),
    "array[int16]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gint16 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_int16_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_int16_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0x7fff, -(0x8000))
    ),
    "array[uint16]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>guint16 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_uint16_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_uint16_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0xffff, 0)
    ),
    "array[int32]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gint32 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_int32_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_int32_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0x7fff_ffff, -(0x80000000))
    ),
    "array[uint32]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>guint32 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_uint32_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_uint32_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0xffff_ffff, 0)
    ),
    "array[int64]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gint64 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_int64_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_int64_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0x7fff_ffff_ffff_ffff, -(0x8000_0000_0000_0000))
    ),
    "array[uint64]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>guint64 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_uint64_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_uint64_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0xffff_ffff_ffff_ffff, 0)
    ),
    "array[ssize]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gssize *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_int64_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_int64_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0xffff_ffff_ffff_ffff, 0)
    ),
    "array[size]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gsize *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_uint64_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_uint64_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0x7fff_ffff_ffff_ffff, -(0x8000_0000_0000_0000))
    ),
    "array[double]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gdouble *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_double_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_double_decode(<arg_name>, &n_<arg_in>)"],
        FloatArrayValidator()
    ),
    "array[unixfd]": CTypeBase(
        ["gsize n_<arg_name>" ,"<const>gint32 *<arg_name>"],
        ["gcl_free_p((void **)&<arg_name>)"],
        ["<arg_out> = gcl_array_handle_encode(<arg_name>, n_<arg_name>)"],
        ["<arg_in> = gcl_array_handle_decode(<arg_name>, &n_<arg_in>)"],
        IntegerArrayValidator(0x7fff_ffff_ffff_ffff, 0)
    ),
    "array[string]": CTypeBase(
        ["gchar * <const>*<arg_name>"],
        ["gcl_strfreev_p(&<arg_name>)"],
        ["<arg_out> = gcl_array_string_encode(<arg_name>)"],
        ["<arg_in> = gcl_array_string_decode(<arg_name>)"],
        StringArrayValidator("^.*$")
    ),
    "array[object_path]": CTypeBase(
        ["gchar * <const>*<arg_name>"],
        ["gcl_strfreev_p(&<arg_name>)"],
        ["<arg_out> = gcl_array_object_path_encode(<arg_name>)"],
        ["<arg_in> = gcl_array_object_path_decode(<arg_name>)"],
        StringArrayValidator("^(/[A-Z0-9a-z_]+)*$")
    ),
    "array[signature]": CTypeBase(
        ["gchar * <const>*<arg_name>"],
        ["gcl_strfreev_p(&<arg_name>)"],
        ["<arg_out> = gcl_array_signature_encode(<arg_name>)"],
        ["<arg_in> = gcl_array_signature_decode(<arg_name>)"],
        StringArrayValidator("^([abynqiuxtdsogv\\{\\}\\(\\)])+$")
    )
}