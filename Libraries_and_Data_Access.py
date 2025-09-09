# Menginstal library viresclient untuk mengambil data SWARM
!pip install viresclient
# library yang digunakan
import joblib
import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns
import xgboost as xgb
import lightgbm as lgb
import plotly.express as px
import matplotlib.pyplot as plt
from viresclient import set_token
from sklearn.utils import resample
from viresclient import SwarmRequest
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix

# Set up request data ke server Swarm
set_token("https://vires.services/ows", set_default=True)
request = SwarmRequest()

# Memanggil data dari ketiga satelit SWARM (Alpha, Bravo, dan Charlie)
request.set_collection(
    "SW_OPER_IBIATMS_2F",
    "SW_OPER_MAGA_LR_1B",
    "SW_OPER_EFIA_LP_1B",
    "SW_OPER_IBIBTMS_2F",
    "SW_OPER_MAGB_LR_1B",
    "SW_OPER_EFIB_LP_1B",
    "SW_OPER_IBICTMS_2F",
    "SW_OPER_MAGC_LR_1B",
    "SW_OPER_EFIC_LP_1B"
    )



# Memanggil produk yang diinginkan
request.set_products(
    measurements=['Ne', 'Bubble_Probability', 'F', 'B_NEC','Bubble_Index'],
    auxiliaries=['F107','Kp','Longitude', 'Latitude', 'MLT' ],
    sampling_step="PT10S" #pengambilan data per 10 detik
    )
request.set_range_filter(parameter="Latitude", minimum=-45, maximum=45)
request.set_range_filter(parameter="MLT",minimum=18, maximum=24) #melakukan filter pada data yang diinginkan

# Pengambilan data dari tahun 2018 hingga 2024
data = request.get_between(
    dt.datetime(2018, 1, 1),
    dt.datetime(2024, 12, 30)
    )

# Mengubah data dalam bentuk CSV
df = data.as_dataframe() # Konversi data menjadi DataFrame Pandas
df.to_csv('Data SWARM 2018-2024.csv')
