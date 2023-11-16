# START ENUM

# gender
MALE = 'M'
FEMALE = 'F'
GENDER_CHOICE = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
)

# Markazda nechinchi marotaba
ONE = 1
TWO = 2
THREE = 3
MORE_THREE = 4

# COUNT_BACK_CENTER_CHOICE = (
#     (ONE, '1'),
#     (TWO, "2"),
#     (THREE, "3"),
#     (MORE_THREE, "3+"),
# )

# Olib kelinishiga asos
IIB_QARORI = 1
SUD_AJRIMI = 2
MARKAZ_BUYRUGI = 3

ARRIVED_REASON_CHOICE = (
    (IIB_QARORI, 'IIB qarori'),
    (SUD_AJRIMI, "Sud ajrimi"),
    (MARKAZ_BUYRUGI, "Markaz buyrug'i"),
)

# Holat aniqlangan joyi
BOZOR = 1
YER_TOLA_VA_CHORDOQ = 2
KOCHA = 3
BOSHQA_JOYLAR = 4
BOSHQA_DAVLATLARDAN = 5

DETERMINED_LOCATION_CHOICE = (
    (BOZOR, 'Bozor'),
    (YER_TOLA_VA_CHORDOQ, "Yer-to‘la va chor-doq"),
    (KOCHA, "Ko'cha"),
    (BOSHQA_JOYLAR, "Boshqa joylar"),
    (BOSHQA_DAVLATLARDAN, "Boshqa davlatlardan"),
)

# Muassasa turi
MAKTABGACHA_TALIM = 1
MAKTAB = 2
KASB_HUNAR_MAKTABI = 3
KASB_HUNAR_KOLLEJI = 4
LITSEY = 5
TEXNIKUM = 6
MAXSUS_TALIM = 7
OTM = 8
OQIMAYDI_ISHLAMAYDI = 9
ISHLAYDI = 10

SCHOOL_TYPE_CHOICE = (
    (MAKTABGACHA_TALIM, "Maktabgacha ta'lim"),
    (MAKTAB, 'Maktab'),
    (KASB_HUNAR_MAKTABI, "Kasb-hunar maktabi"),
    (KASB_HUNAR_KOLLEJI, "Kasb-hunar kolleji"),
    (LITSEY, "Litsey"),
    (TEXNIKUM, "Texnikum"),
    (MAXSUS_TALIM, "Maxsus ta’lim"),
    (OTM, "OTM"),
    (OQIMAYDI_ISHLAMAYDI, "O‘qimaydi/Ishlamaydi"),
    (ISHLAYDI, "Ishlaydi"),
)

# Markazga olib kelgan xodim
INSPECTOR = 1
PSYCHOLOGIST = 2
MARKAZ_XODIMI = 3
OTHER_INSPECTOR = 4

INSPECTOR_TYPE_CHOICE = (
    (INSPECTOR, 'Inspektor'),
    (PSYCHOLOGIST, "Psixolog"),
    (MARKAZ_XODIMI, "Markaz xodimi"),
    (OTHER_INSPECTOR, "Boshqalar"),
)

# Bolaning holati
HAS_PARENTS = 1
HAS_FATHER_OR_MOTHER = 2
IN_GUARDIAN_CARE = 3
NOT_IN_ANYONES_CARE = 4

MARITAL_STATUS_TYPE_CHOICE = (
    (HAS_PARENTS, 'Ota-onasi bor'),
    (HAS_FATHER_OR_MOTHER, "Otasi yoki onasi yo'q"),
    (IN_GUARDIAN_CARE, "Vasiy qaramog'ida"),
    (NOT_IN_ANYONES_CARE, "Hech kimi yo'q"),
)

# Boquvchining turi
FATHER = 1
MOTHER = 2
GUARDIAN = 3

PARENT_TYPE_CHOICE = (
    (FATHER, 'Ota'),
    (MOTHER, "Ona"),
    (GUARDIAN, "Muqobil (Alternativ) boquvchi"),
)

# Hujjat turi
PASSPORT = 1
ID_CARD = 2
BIRTH_PASSPORT = 3
KINDER_PASSPORT = 4
HORIJIY_DAVLAT_HUJJATLARI = 5
OTHER_PASSPORT = 6

PASSPORT_TYPE_CHOICE = (
    (PASSPORT, 'Biometrik pasport'),
    (ID_CARD, 'ID-karta'),
    (BIRTH_PASSPORT, "Tug'ilganlik haqida guvohnoma"),
    (KINDER_PASSPORT, "Kinder pasport"),
    (HORIJIY_DAVLAT_HUJJATLARI, "Horijiy davlat hujjatlari"),
    (OTHER_PASSPORT, "Boshqalar"),
)

QAROR_BILAN_CHIQARILGAN_ROTM = 1
QOCHGAN_ROTM = 2

HAVE_BEEN_IN_ROTM_REASON_CHOICE = (
    (QAROR_BILAN_CHIQARILGAN_ROTM, 'Qaror bilan chiqarilgan'),
    (QOCHGAN_ROTM, 'Qochgan'),
)

QAROR_BILAN_CHIQARILGAN_ITM = 1
QOCHGAN_ITM = 2

HAVE_BEEN_IN_ITM_REASON_CHOICE = (
    (QAROR_BILAN_CHIQARILGAN_ITM, 'Qaror bilan chiqarilgan'),
    (QOCHGAN_ITM, 'Qochgan'),
)

# Taqsimot turi
FAMILY = 1
BY_GUARDIAN_BODY = 2
ITM = 3
ROTM = 4
SOGLIQNI_SAQLASH_MUASSASASI = 5
BOSHQA_MARKAZGA_YUBORISH = 6
BOSHQA_DAVLATGA_YUBORISH = 7
BOSHQALAR = 8

DISTRIBUTION_TYPE_CHOICE = (
    (FAMILY, 'Oila'),
    (BY_GUARDIAN_BODY, 'Vasiylik organi orqali'),
    (ITM, "ITM"),
    (ROTM, "RO'TM"),
    (SOGLIQNI_SAQLASH_MUASSASASI, "Sog'liqni saqlash muassasasi"),
    (BOSHQA_MARKAZGA_YUBORISH, "Boshqa markazga yuborish"),
    (BOSHQA_DAVLATGA_YUBORISH, "Boshqa davlatga yuborish"),
    (BOSHQALAR, "Boshqalar"),
)

# Qarindoshlik darajasi
KINKDSHIP_FATHER = 1
KINKDSHIP_MOTHER = 2
KINKDSHIP_BROTHER = 3
KINKDSHIP_SISTER = 4
KINKDSHIP_UNCLE = 5
KINKDSHIP_AUNT = 6
KINKDSHIP_UNCLE_MOTHER = 7
KINKDSHIP_AUNT_MOTHER = 8
KINKDSHIP_GRANDFATHER = 9
KINKDSHIP_GRANDMOTHER = 10
VAQTINCHALIK_VAKIL = 11

LEVEL_KINKDSHIP_CHOICE = (
    (KINKDSHIP_FATHER, 'Ota'),
    (KINKDSHIP_MOTHER, 'Ona'),
    (KINKDSHIP_BROTHER, 'Aka'),
    (KINKDSHIP_SISTER, 'Opa'),
    (KINKDSHIP_UNCLE, 'Amaki'),
    (KINKDSHIP_AUNT, 'Amma'),
    (KINKDSHIP_UNCLE_MOTHER, "Tog'a"),
    (KINKDSHIP_AUNT_MOTHER, "Xola"),
    (KINKDSHIP_GRANDFATHER, 'Bobo'),
    (KINKDSHIP_GRANDMOTHER, 'Buvi'),
    (VAQTINCHALIK_VAKIL, 'Vaqinchalik vakil'),
)

# Taqsimot asosi
CENTER_SUMMARY = 1
GOVERNOR_DECISION = 2
MINISTRY_ORGANIZATION_REFERRAL = 3
JUDGMENT = 4
SVV_XULOSASI = 5
NOTARIAL_ISHONCHNOMA = 6

BASIS_DISTRIBUTION_CHOICE = (
    (CENTER_SUMMARY, 'Markaz xulosasi'),
    (GOVERNOR_DECISION, 'Hokim qarori'),
    (MINISTRY_ORGANIZATION_REFERRAL, "Tegishli vazirlik/tashkilot yo'llanmasi"),
    (JUDGMENT, "Sud ajrimi"),
    (SVV_XULOSASI, "SSV xulosasi"),
    (NOTARIAL_ISHONCHNOMA, "Notarial ishonchnoma"),
)

# Vasiylik turi
GUARDIAN = 1
PARTNER = 2
PATRONAGE = 3
CHILDHOOD = 4
HOUSE_OF_MERCY = 5
FAMILY_ORPHANAGE = 6
SOS_BOLALAR_SHAHARCHASI = 7

TYPE_GUARDIANSHIP_CHOICE = (
    (GUARDIAN, 'Vasiy'),
    (PARTNER, 'Homiy'),
    (PATRONAGE, "Patronat"),
    (CHILDHOOD, "Farzandlik"),
    (HOUSE_OF_MERCY, "Mehribonlik uyi"),
    (FAMILY_ORPHANAGE, "Oilaviy bolalar uyi"),
    (SOS_BOLALAR_SHAHARCHASI, "SOS bolalar shaharchasi"),
)

# ITM yo’nalishi
HARBIY = 1
MADANIYAT_VA_SANAT = 2
SPORT = 3
FAN_YONALISHI = 4
ITM_BOSHQALAR = 5

ITM_DIRECTION_CHOICE = (
    (HARBIY, 'Harbiy'),
    (MADANIYAT_VA_SANAT, "Ma'daniyat va sa'nat"),
    (SPORT, "Sport"),
    (FAN_YONALISHI, "Fan yo'nalishi"),
    (ITM_BOSHQALAR, "Boshqalar"),
)

# RO’TM turi
GIRL_ROTM = 1
BOY_ROTM = 2

ROTM_TYPE_CHOICE = (
    (GIRL_ROTM, "Qiz bolalar uchun RO'TM"),
    (BOY_ROTM, "O'g'il bolalar uchun RO'TM"),
)

# Sudlanganlik ro'yxati
OME = 1
SINOV = 2
SHARTLI = 3
UY_QAMOGI = 4
JARIMA = 5
BOSHQALAR = 6


# Taqsimlangan bolaning ta'lim muassasa turi
OLIY_TALIM = 1
ORTA_MAXSUS_TALIM = 2

EMPLOYMENT_EDUCATION_TYPE_CHOICE = (
    (OLIY_TALIM, "Oliy ta'lim"),
    (ORTA_MAXSUS_TALIM, "O'rta maxsus ta'lim"),
)

# Juvenile status
ANIQLANGAN = 1
MARKAZGA_QABUL_QILINGAN = 2
TAQSIMLANGAN = 3
MONITORING_JARAYONIDA = 4
BANKDLIK_TAMINLANISH_JARAYONIDA = 5
BANDLIK_TAMINLANGAN = 6
BOSHQA_DAVLATGA_YUBORILGAN = 7
BOSHQA_MARKAZGA_YUBORILGAN = 8
ARXIVDA = 9
BOSHQA_MARKAZGA_YUBORISH_JARAYONIDA = 10
OTA_ONASIDAN_QAYTARILGAN  = 11
ITMDAN_QOCHGAN  = 12
VASIYLIK_TURIDAN_QAYTARILGAN  = 13

JUVENILE_STATUS_CHOICES = (
    (ANIQLANGAN, "Aniqlangan"),
    (MARKAZGA_QABUL_QILINGAN, "Markazga qabul qilingan"),
    (TAQSIMLANGAN, "Taqsimlangan"),
    (MONITORING_JARAYONIDA, "Monitoring jarayonida"),
    (BANKDLIK_TAMINLANISH_JARAYONIDA, "Bandlik ta’minlanish jarayonida"),
    (BANDLIK_TAMINLANGAN, "Bandligi taminlangan"),
    (BOSHQA_DAVLATGA_YUBORILGAN, "Boshqa davlatga yuborilgan"),
    (BOSHQA_MARKAZGA_YUBORILGAN, "Boshqa markazga yuborilgan"),
    (ARXIVDA, "Arxixda"),
    (BOSHQA_MARKAZGA_YUBORISH_JARAYONIDA, "Boshqa markazga yuborish jarayonida"),
    (OTA_ONASIDAN_QAYTARILGAN, "Ota-onasidan qaytarilgan"),
    (ITMDAN_QOCHGAN, "ITMdan qochgan"),
    (VASIYLIK_TURIDAN_QAYTARILGAN, "Vasiylik turidan qaytarilgan"),
)


# HORIJLIK BOLANI KIMGA BERIB YUBORILISHI
OTA_ONA_YOKI_ORNINI_BOSUVCHI_SHAXSGA = 1
CHET_EL_ELCHIXONASIGA = 2
CHET_EL_MARKAZI_XODIMIGA = 3

FOREIGN_TO_WHOM_GIVEN_CHOICES = (
    (OTA_ONA_YOKI_ORNINI_BOSUVCHI_SHAXSGA, 'Ota-onasi yoki uni o‘rnini bosuvchi shaxsga'),
    (CHET_EL_ELCHIXONASIGA, "Chet-el Elchixonasiga"),
    (CHET_EL_MARKAZI_XODIMIGA, "Chet-el Markazi xodimiga"),
)


# (TAQSIMLASH) Sog‘liqni saqlash muasassasi turi
RUHIY_ASAB_KASALLIKLARI_DISPANSERI = 1
NARKALOGIYA_DISPANSERI = 2
TERI_TANOSIL_DISPANSERI = 3
SIL_KASALLIKLARI_DISPANSERI = 4
SOGLIGIDA_NUQSONI_BOR_BOLALAR_MUASSASASI = 5


TYPE_HEALTHCARE_FACILITY = (
    (RUHIY_ASAB_KASALLIKLARI_DISPANSERI, 'Ruhiy-asab kasalliklari dispanseri'),
    (NARKALOGIYA_DISPANSERI, "Narkologiya dispanseri"),
    (TERI_TANOSIL_DISPANSERI, "Teri-tanosil dispanseri"),
    (SIL_KASALLIKLARI_DISPANSERI, "Sil kasaliklari dispanseri"),
    (SOGLIGIDA_NUQSONI_BOR_BOLALAR_MUASSASASI, "Sog‘ligida nuqsoni bor bolalar muassasasi"),
)

# O‘zlashtirishi 
ALO  = 1
YAXSHI = 2
QONIQARLI = 3
QONIQARSIZ = 4


MASTERY_TYPE_CHOICE = (
    (ALO, "A'lo"),
    (YAXSHI, "Yaxshi"),
    (QONIQARLI, "Qoniqarli"),
    (QONIQARSIZ, "Qoniqarsiz"),
)

# Hulqi 
HULQI_YAXSHI = 1
HULQI_QONIQARLI = 2
HULQI_QONIQARSIZ = 3


CHARACTER_TYPE_CHOICE = (
    (HULQI_YAXSHI, "Yaxshi"),
    (HULQI_QONIQARLI, "Qoniqarli"),
    (HULQI_QONIQARSIZ, "Qoniqarsiz"),
)

# Notification Status
KELIB_TUSHGAN = 1
TASDIQLANDI = 2
RAD_ETILDI = 3


NOTIFICATION_STATUS_CHOICE = (
    (KELIB_TUSHGAN, "Kelib tushdi"),
    (TASDIQLANDI, "Tasdiqlandi"),
    (RAD_ETILDI, "Rad etildi"),
)

# Notification Status
KELIB_TUSHGAN = 1
TASDIQLANDI = 2
RAD_ETILDI = 3

MONITORING_JARAYONIDA = 1
ITM_VA_ROTMNI_TUGALLAGAN = 2
OTA_ONASIDAN_QAYTARILGAN = 3
ITMDAN_QOCHGAN = 4
VASIYLIK_TURIDAN_QAYTARILGAN = 5

MONITORING_STATUS_CHOICE = (
    (MONITORING_JARAYONIDA, "Monitoring jarayonida"),
    (ITM_VA_ROTMNI_TUGALLAGAN, "RO‘TM va ITMni tugallagan"),
    (OTA_ONASIDAN_QAYTARILGAN, "Ota-onasidan qaytarilgan"),
    (ITMDAN_QOCHGAN, "ITMdan qochgan"),
    (VASIYLIK_TURIDAN_QAYTARILGAN, "Vasiylik turidan qaytarilgan"),
)
# END ENUM
