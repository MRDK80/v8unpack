# Каноническое имя хендлера формы внутренней обработки.
# Бинарный формат идентичен Form; подкласс нужен чтобы __name__ совпадал
# с именем модуля — этого требует helper.get_class_metadata_object().
from v8unpack.MetaDataObject.Form import Form


class DataProcessorForm(Form):
    pass
