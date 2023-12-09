# ÜTS Sisteminde Kayıtlı Firmaların Bilgileri
Bu projede https://utsuygulama.saglik.gov.tr/UTS/ sisteminde kayıtlı firmaların verileri, gerçek bir kullanıcı gibi davranılarak kaydedilmektedir.


# Kodu Çalıştırmadan Önce:
- https://chromedriver.chromium.org/downloads
- `pip install -r requirements.txt`

# Kodu Çalıştırmak İçin:
`src` klasöründe iken `py uts.py`

# Not:
- Tüm HTML elemanlarının görünür olmasını sağlamak ve hata almamak için selenium browser'ı açıldıktan sonra `Ctrl + -` tuşlarını kullanarak %80 zoom out yapmak gerekiyor.
- Webdrive'da güvenlik uyarısı almamak için Chrome'a `ca.crt` sertifikasının eklenmesi gerekebilir. `Chrome > Settings > Manage certificates > Import`