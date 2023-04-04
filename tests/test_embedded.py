from phml.embedded import *
from pytest import raises
import time
from time import time as t_time, sleep
from re import match, sub

def test_embedded_import():
    d_time = EmbeddedImport("time").data
    d_sub_time = EmbeddedImport("time", ["sleep"]).data
    EmbeddedImport("re", "match, sub as substitute").data
    d_re = EmbeddedImport("re", "match, sub as substitute").data

    i_time = Module("time").collect()
    
    i_sleep = Module("time", imports=["sleep"]).collect()
    i_match, i_sub = Module("re", imports=["match", "substitute"]).collect()
    
    assert "match" in d_re
    assert "substitute" in d_re
    assert "time" in d_time
    assert d_time["time"] == time
    assert "sleep" in d_sub_time
    assert d_sub_time["sleep"] == sleep 

    assert "match" in d_re
    assert d_re["match"] == match
    assert "substitute" in d_re
    assert d_re["substitute"] == sub 

    assert i_time == time
    assert i_sleep == sleep
    assert i_match == match
    assert i_sub == sub

def test_embedded_context_slitting():
    code = """\
from time import sleep

message=True

def get_value():
    return message
"""
    
    embedded = Embedded(code)
    assert len(embedded.imports) == 1 and embedded.imports[0].data == {"sleep": sleep}
    assert "message" in embedded and embedded["message"]
    assert "get_value" in embedded and embedded["get_value"]()

def test_embedded_exec():
    early_return = """\
message = True
return message
message = False
"""
    final_assignment = """\
False
message = True
"""

    bracket_in_block = """{{ {'result': True} }}"""

    assert exec_embedded(early_return)
    assert exec_embedded(final_assignment)
    assert exec_embedded_blocks(bracket_in_block) == "{'result': True}"

def test_raise_embedded_exception():
    with raises(EmbeddedPythonException):
        Embedded("raise Exception('Test')")

    try:
        Embedded("raise Exception('Test')")
    except EmbeddedPythonException as epe:
        assert len(str(epe)) > 0

