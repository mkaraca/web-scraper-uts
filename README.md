# ÜTS Sisteminde Kayıtlı Firmaların Bilgileri
Bu Python projesinde https://utsuygulama.saglik.gov.tr/UTS/ sisteminde kayıtlı firmaların verileri, gerçek bir kullanıcı gibi davranılarak kaydedilmektedir.

## Amaç:
ÜTS sisteminde kayıtlı firmalara bir bilgilendirme e-postası gönderilmek istenmektedir. Fakat bu firmaların e-posta adreslerine toplu bir şekilde erişim imkanı bulunmamaktadır.

## Kodu Çalıştırmadan Önce:
- Yüklü olması gereken program: https://chromedriver.chromium.org/downloads
- Kütüphanler: `pip install -r requirements.txt`

## Kodu Çalıştırmak İçin:
`src` klasöründe iken `py uts.py`

## Not:
- Tüm HTML elemanlarının görünür olmasını sağlamak ve hata almamak için selenium browser'ı açıldıktan sonra `Ctrl + -` tuşlarını kullanarak %80 zoom out yapmak gerekiyor.
- Webdrive'da güvenlik uyarısı almamak için Chrome'a `ca.crt` sertifikasının eklenmesi gerekebilir. `Chrome > Settings > Manage certificates > Import`