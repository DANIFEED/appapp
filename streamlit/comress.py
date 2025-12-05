# compress_model.py
import joblib
import gzip
import pickle

# Сожмите модель
with open('house_price_model.pkl', 'rb') as f_in:
    with gzip.open('house_price_model.pkl.gz', 'wb') as f_out:
        f_out.write(f_in.read())
print("Модель сжата!")