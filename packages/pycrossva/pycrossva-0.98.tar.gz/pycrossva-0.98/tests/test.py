import pandas as pd
from pycrossva.transform import transform
from pycrossva.utils import flexible_read, detect_format

# input_data = pd.read_csv("pycrossva/resources/sample_data/2016WHO_mock_data_1.csv")

# input_data = pd.read_csv("/Users/thomas.3912/Research/Sam/VA/Workshops/Dar/final_sample_training_data3.csv")
# final_data = transform(("2016WHOv151", "InterVA5"), input_data, lower=True)
#
# input_data2 = pd.read_csv("/Users/thomas.3912/Research/Sam/VA/Workshops/Dar/jt.csv")
# final_data2 = transform(("2016WHOv151", "InterVA5"), input_data2, lower=True)
#
# final_data.i022a.to_list()
# final_data2.i022a.to_list()

# detect_format("InSilicoVA",
#               flexible_read("pycrossva/resources/sample_data/2016WHO_mock_data_1.csv"))

out = transform(("2016WHOv151", "InterVA4"),
                "pycrossva/resources/sample_data/2016WHO_mock_data_1.csv")
out.columns


my_special_data = pd.read_csv("pycrossva/resources/sample_data/2016WHO_mock_data_1.csv")
my_special_mapping = pd.read_csv("pycrossva/resources/mapping_configuration_files/2016WHOv151_to_InterVA4.csv")
transform(my_special_mapping, my_special_data).loc[range(5),["ACUTE","CHRONIC","TUBER"]]