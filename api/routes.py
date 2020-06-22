from api import app
from boto_scripts import file_download, file_upload
from df_manipulations import df_sum
from flask import jsonify


@app.route('/')
def index():
    df = file_download('df.csv', 'bucket.with.csv')

    res_df = df_sum(df)
    res_df.to_csv('result.csv')

    file_upload('result.csv', 'bucket.with.csv')

    return jsonify('success')
