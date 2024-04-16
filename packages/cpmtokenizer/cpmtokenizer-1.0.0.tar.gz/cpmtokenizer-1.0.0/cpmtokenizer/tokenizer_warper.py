# -*- coding: utf-8 -*-
import ctypes
from ctypes import *
import faulthandler
faulthandler.enable()

class CPMCTokenizer:
    def __init__(self, catepillar_vocab_file_path, lib_token_so_file_path):
        #初始化依赖库和函数参数
        lib = ctypes.cdll.LoadLibrary(lib_token_so_file_path)
        lib.setCatePillarVocabFile.argtypes = [ctypes.c_char_p]
        lib.getTokenizer.restype = ctypes.c_void_p
        lib.encode.argtypes = [ctypes.c_void_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)]
        lib.decode.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int),ctypes.c_char_p]
        lib.get_arr_value.argtypes = [ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_int)]
        self.lib = lib

        #初始化tokenizer文件路径并获取tokenizer
        self.lib.setCatePillarVocabFile(catepillar_vocab_file_path.encode('utf-8'))
        self.tokenizer = self.lib.getTokenizer()

    def __del__(self):
        # 释放资源
        pass
    #返回值python list[int]
    def encode(self, text):
       try:
           length = ctypes.c_int()
           text_lenth = len(text)
           init_arr = [0]*text_lenth*4
           res_ptr = (ctypes.c_int * text_lenth )(*init_arr)
           del init_arr
           self.lib.encode(self.tokenizer, text.encode('utf-8'), ctypes.byref(length),res_ptr)
       
           res = [res_ptr[i] for i in range(length.value)]
           return res
       except Exception as e:
           print(e)
           return []
    
    #返回值string
    def decode(self, token_ids):
       try:
           length = ctypes.c_int()
           length.value = len(token_ids)
       
           c_int_array = (ctypes.c_int * length.value )(*token_ids)

           data =  ctypes.create_string_buffer(length.value*32)
           
           self.lib.decode(self.tokenizer, c_int_array, ctypes.byref(length), data)
           return ctypes.string_at(data).decode('utf-8')
       
       except Exception as e:
           print(e)
    
##test
def test():
    tokenizer = CPMCTokenizer("/home/workspace/mb/mb_data/engine/cpmc/20240309.txt",'/home/workspace/mb/.mindbuild-out/dbg/engine/cpmc/base/libtext_tokenizer_wraper_shared.so')
    res = tokenizer.encode("afdf afa fafafafaf dfasdf efaf")
    print(res)
    decoded = tokenizer.decode(res)
    print(decoded.__class__)
    print(decoded)

#test()