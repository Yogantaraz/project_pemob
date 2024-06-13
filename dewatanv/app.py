from flask import Flask
from modules.akun_endpoints import akun_endpoints
from modules.data_wisata_endpoints import data_wisata_endpoints
from modules.kategori_endpoints import kategori_endpoints
from modules.profile_endpoints import profile_endpoints
from modules.ulasan_endpoints import ulasan_endpoints
from modules.wisata_favorit_endpoints import wisata_favorit_endpoints

app = Flask(__name__)

app.register_blueprint(akun_endpoints, url_prefix='/akun')
app.register_blueprint(data_wisata_endpoints, url_prefix='/data_wisata')
app.register_blueprint(kategori_endpoints, url_prefix='/kategori')
app.register_blueprint(profile_endpoints, url_prefix='/profile')
app.register_blueprint(ulasan_endpoints, url_prefix='/ulasan')
app.register_blueprint(wisata_favorit_endpoints, url_prefix='/wisata_favorit')

if __name__ == '__main__':
    app.run()
