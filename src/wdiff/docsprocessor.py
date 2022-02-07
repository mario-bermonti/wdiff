from docrep import DocstringProcessor

class CustomDoctringProcessor(DocstringProcessor):
    param_like_sections = ["Rules"] + DocstringProcessor.param_like_sections

docstrings = CustomDoctringProcessor()
_COMMON_SECTIONS = ["Rules"]    # sections to be extracted from most docstrings 
