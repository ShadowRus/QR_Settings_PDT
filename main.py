import streamlit as st
import qrcode
from PIL import Image
#------------------------------------------------------------
dict_ex = {
  "ver": 1,
  "kv": [
    {
      "k": 4,
      "v": {
        "ssid": "MyBestNetwork",
        "pass": "lalalalalalalalalal"
      }
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    }
  ],
  "sb": [
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    },
    {
      "k": 404,
      "v": 404
    }
  ]
}

#--------------------------------------------------------------------

st.title('Настройка ТСД при помощи QR-кода')
st.subheader('Общие настройки ТСД')
#_____________________________________________
lightness= st.slider('Яркость дисплея, %',0,100)
dict_ex['kv'][1]['k'] = 0
dict_ex['kv'][1]['v'] = lightness
#____________________________________________
screen_rotation = st.radio('Поворот экрана', ['Выключено','Включено'])
dict_ex['kv'][2]['k'] = 1
if screen_rotation == "Выключено":
    dict_ex['kv'][2]['v'] = 1
else:
    dict_ex['kv'][2]['v'] = 1
#________________________________________
mobile_net = st.radio('Мобильный интернет', ['Выключено','Включено'])
dict_ex['kv'][3]['k'] = 2
if mobile_net== "Выключено":
    dict_ex['kv'][3]['v'] = 0
else:
    dict_ex['kv'][3]['v'] = 1
#______________________________________________
wifi = st.radio('WiFi', ['Выключено','Включено'])
dict_ex['kv'][4]['k'] = 12
if mobile_net== "Выключено":
    dict_ex['kv'][4]['v'] = 0
else:
    dict_ex['kv'][4]['v'] = 1
#______________________________________________
st.caption("Добавление Wifi сети")
wifi_ssid = st.text_input('SSID/Название сети')
wifi_pass = st.text_input('Password')
dict_ex['kv'][0]['k'] = 4
dict_ex['kv'][0]['v']['ssid'] =wifi_ssid
dict_ex['kv'][0]['v']['pass'] =wifi_pass
#_________________________________________________
nfc = st.radio('NFC', ['Выключено','Включено'])
dict_ex['kv'][5]['k'] = 9
if mobile_net== "Выключено":
    dict_ex['kv'][5]['v'] = 0
else:
    dict_ex['kv'][5]['v'] = 1
#______________________________________________
bt = st.radio('Bluetooth', ['Выключено','Включено'])
dict_ex['kv'][6]['k'] = 13
if mobile_net== "Выключено":
    dict_ex['kv'][6]['v'] = 0
else:
    dict_ex['kv'][6]['v'] = 1
#______________________________________________#________________________________________________________
airplane = st.radio('Авиарежим', ['Выключено','Включено'])
dict_ex['kv'][7]['k'] = 14
if mobile_net== "Выключено":
    dict_ex['kv'][7]['v'] = 0
else:
    dict_ex['kv'][7]['v'] = 1
#______________________________________________
gps = st.radio('Геолокация', ['Выключено','Включено'])
dict_ex['kv'][8]['k'] = 6
if mobile_net== "Выключено":
    dict_ex['kv'][8]['v'] = 0
else:
    dict_ex['kv'][8]['v'] = 1
#______________________________________________
night_mode = st.radio('Ночной режим', ['Выключено','Включено'])
dict_ex['kv'][9]['k'] = 8
if mobile_net== "Выключено":
    dict_ex['kv'][9]['v'] = 0
else:
    dict_ex['kv'][9]['v'] = 1
#______________________________________________
sleep_mode = st.selectbox('Спящий режим',['Never', '1 min','2 min','5 min','10 min','30 min'])
dict_sleep = {'Never': 0, '1 min': 1,'2 min': 2,'5 min': 3,'10 min': 4,'30 min': 5}
dict_ex['kv'][10]['k'] = 3
dict_ex['kv'][10]['v'] = dict_sleep[sleep_mode]
#___________________________________________________________________________
sound_level= st.number_input('Громкость уведомлений',0,10)
dict_ex['kv'][11]['k'] = 15
dict_ex['kv'][11]['v'] = sound_level
#___________________________________________________________________________
notification_sound = st.selectbox('Уведомления',['Звук', 'Звук + вибро','Вибро','Без звука'])
dict_sound = {'Звук': 0, 'Звук + вибро': 1 ,'Вибро': 2,'Без звука': 3}
dict_ex['kv'][12]['k'] = 16
dict_ex['kv'][12]['v'] = dict_sound[notification_sound]
#___________________________________________________________________________
date_time = st.selectbox('Дата и время',['Использовать время по сети', 'Использовать время по GPS','Использовать сервер времени'])
dict_time = {'Использовать время по сети': 0, 'Использовать время по GPS': 1,'Использовать сервер времени': 2}
dict_ex['kv'][13]['k'] = 17
dict_ex['kv'][13]['v'] = dict_time [date_time ]


#date_time_server = st.text_input('Введите адрес сервера времени')


st.subheader('Настройки BarCodeService для сканирующего модуля')

bars_default = st.checkbox('Сбросить настройки',value = False, help = 'Сброс настроек на ТСД на default')
dict_ex['sb'][0]['k'] = 200
if bars_default == False:
    dict_ex['sb'][0]['v'] = 0
else:
    dict_ex['sb'][0]['v'] = 1
#______________________________________________
st.write(' **Основные настройки**')
bars_output = st.radio('Отправка сканирования через ',['BroadCast','KeyBoard','Clipboard'])
dict_out={'BroadCast': 0, 'KeyBoard': 1, 'Clipboard': 2}
dict_ex['sb'][1]['k'] = 201
dict_ex['sb'][1]['v'] = dict_out[bars_output]
#______________________________________________
bars_sleep = st.slider('Задержка нажатия клавиш',0,250)
dict_ex['sb'][2]['k'] = 202
dict_ex['sb'][2]['v'] = bars_sleep
#______________________________________________
bars_invers = st.checkbox('Инверсные коды', value = True, help = 'Включать распознование инверсных кодов')
dict_ex['sb'][3]['k'] = 203
if bars_invers == False:
    dict_ex['sb'][3]['v'] = 0
else:
    dict_ex['sb'][3]['v'] = 1
#______________________________________________
bars_time_scan = st.slider('Максимальное время сканирования',0,10)
dict_ex['sb'][4]['k'] = 204
dict_ex['sb'][4]['v'] = bars_time_scan
#______________________________________________
bars_light = st.checkbox('Подсветка', value = True, help = 'Включать подсветку при сканировании')
dict_ex['sb'][5]['k'] = 205
if bars_light  == False:
    dict_ex['sb'][5]['v'] = 0
else:
    dict_ex['sb'][5]['v'] = 1
#______________________________________________
bars_aim = st.checkbox('Прицел', value = True, help ='Включать прицел при сканировании')
dict_ex['sb'][6]['k'] = 206
if bars_aim  == False:
    dict_ex['sb'][6]['v'] = 0
else:
    dict_ex['sb'][6]['v'] = 1
#______________________________________________
bars_multiscan = st.selectbox('Режим сканирования ',['Однократное','Серийное без повторов','Серийнове всех подряд'])
dict_multi={'Однократное':0,'Серийное без повторов':1,'Серийнове всех подряд':2}
dict_ex['sb'][7]['k'] = 207
dict_ex['sb'][7]['v'] = dict_multi[bars_multiscan ]
#______________________________________________
bars_frame = st.selectbox('Размер поля сканирования ',['4/4','3/4','2/4','1/4','1/8','1/16','1/32','1/64'])
dict_frame={'4/4':0,'3/4':1,'2/4':2,'1/4':3,'1/8':4,'1/16':5,'1/32':6,'1/64':7}
dict_ex['sb'][8]['k'] = 208
dict_ex['sb'][8]['v'] = dict_frame[bars_frame]
#______________________________________________
bars_notification = st.selectbox('Уведомление об успешном сканировании',['Нет','Звук','Вибро','Звук + Вибро'], index=3)
dict_not={'Нет':0,'Звук':1,'Вибро':2,'Звук + Вибро':3}
dict_ex['sb'][9]['k'] = 209
dict_ex['sb'][9]['v'] = dict_not[bars_notification]
#______________________________________________
st.write('**Управляющие кнопки**')
scan_buttons = st.multiselect('Выберите кноки для сканирования',['Левая кнопка','Центральная кнопка','Правая кнопка'],default= ['Левая кнопка','Центральная кнопка','Правая кнопка'])
dict_ex['sb'][10]['k'] = 210
if 'Левая кнопка' in scan_buttons:
    dict_ex['sb'][10]['v'] = 1
else:
    dict_ex['sb'][10]['v'] = 0
dict_ex['sb'][11]['k'] = 211
if 'Центральная кнопка' in scan_buttons:
    dict_ex['sb'][11]['v'] = 1
else:
    dict_ex['sb'][11]['v'] = 0

dict_ex['sb'][12]['k'] = 212
if 'Правая кнопка' in scan_buttons:
    dict_ex['sb'][12]['v'] = 1
else:
    dict_ex['sb'][12]['v'] = 0
#_____________________________________________
st.write('**Нажатие клавиш**')
dict_space1=['Нет','Tab','Enter','Shift','Ctrl','Alt','CapsLock','Esc','Space','F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']
key1_before = st.selectbox('Клавиша 1 до сканирования',dict_space1)
key2_before = st.selectbox('Клавиша 2 до сканирования',dict_space1)
key1_after = st.selectbox('Клавиша 1 после сканирования',dict_space1)
key2_after = st.selectbox('Клавиша 2 после сканирования',dict_space1)

dict_ex['sb'][13]['k'] = 213
dict_ex['sb'][13]['v'] = dict_space1.index(key1_before)

dict_ex['sb'][14]['k'] = 214
dict_ex['sb'][14]['v'] = dict_space1.index(key2_before)

dict_ex['sb'][15]['k'] = 215
dict_ex['sb'][15]['v'] = dict_space1.index(key1_after)

dict_ex['sb'][16]['k'] = 216
dict_ex['sb'][16]['v'] = dict_space1.index(key2_after)

#_________________________________________________________________________
st.write('**Префиксы и суффиксы**')
dict_space2=['Пусто','Tab','Enter','Space','Символ']
dict_spaces2={'Пусто':500,'Tab':501,'Enter': 502,'Space':503,'Символ':504}
bars_prefix1= st.selectbox('Префикс 1',dict_space2)

dict_ex['sb'][17]['k'] = 217
if bars_prefix1 == "Символ":
    pr1_char = st.text_input('Символ префикса 1')
    dict_ex['sb'][17]['v'] = ord(pr1_char)
else:
    dict_ex['sb'][17]['v'] = dict_spaces2[bars_prefix1]

bars_prefix2= st.selectbox('Префикс 2',dict_space2)

dict_ex['sb'][18]['k'] = 218
if bars_prefix2 == "Символ":
    pr2_char = st.text_input('Символ префикса 2')
    dict_ex['sb'][18]['v'] = ord(pr2_char)
else:
    dict_ex['sb'][18]['v'] = dict_spaces2[bars_prefix2]

bars_sufix1 = st.selectbox('Суффикс 1',dict_space2)

dict_ex['sb'][19]['k'] = 219
if bars_sufix1 == "Символ":
    sf1_char = st.text_input('Символ суффикса 1')
    dict_ex['sb'][19]['v'] = ord(sf1_char)
else:
    dict_ex['sb'][19]['v'] = dict_spaces2[bars_sufix1]

bars_sufix2 = st.selectbox('Суффикс 2',dict_space2)

dict_ex['sb'][20]['k'] = 220
if bars_sufix2 == "Символ":
    sf2_char = st.text_input('Символ суффикса 2')
    dict_ex['sb'][20]['v'] = ord(sf2_char)
else:
    dict_ex['sb'][20]['v'] = dict_spaces2[bars_sufix2]
#________________________________________________________
st.write('**Преобразование**')
bars_registr = st.selectbox('Преобразование регистра',['Нет','В ВЕРХНИЙ','в нижний'])
list_reg=['Нет','В ВЕРХНИЙ','в нижний']
dict_ex['sb'][21]['k'] = 221
dict_ex['sb'][21]['v'] = list_reg.index(bars_registr)

bars_GS = st.selectbox('Заменять GS(0x1D)',dict_space2)

dict_ex['sb'][22]['k'] = 222
if bars_GS == "Символ":
    gs_char = st.text_input('Символ для замены GS')
    dict_ex['sb'][22]['v'] = ord(gs_char )
else:
    dict_ex['sb'][22]['v'] = dict_spaces2[bars_GS]

#_________________________________________________________________
st.write('**Типы штрихкодов**')
bars_code = st.radio('Типы штрихкодов',['Включить все','Отключить все'], index=0)

dict_ex['sb'][23]['k'] = 100
if bars_code == 'Включить все':
    dict_ex['sb'][23]['v'] = 1
else:
    dict_ex['sb'][23]['v'] = 0

#__________________________________________________________
#st.write('**DataMatrix**')
bars_DM = st.radio('DataMatrix', ['Выключено','Включено'], index=1)

dict_ex['sb'][24]['k'] = 101
if bars_DM== "Выключено":
    dict_ex['sb'][24]['v'] = 0
else:
    dict_ex['sb'][24]['v'] = 1
#________________________________________________________
#bars_DM_max = st.slider('Max len',1,3116, value = 3116)
#bars_DM_min = st.slider('Min len',1,3116, value = 1)
#bars_DM_inv = st.checkbox('Инверсный DataMatrix', value = True, help = 'Включить распознование инверсного DataMatrix')
#bars_DM_mir = st.checkbox('Зеркальный DataMatrix', value = True, help = 'Включить распознование зеркального DataMatrix')
#st.write('**EAN-13**')
bars_EAN13 = st.radio('EAN-13', ['Выключено','Включено'], index=1)

dict_ex['sb'][25]['k'] = 106
if bars_EAN13 == "Выключено":
    dict_ex['sb'][25]['v'] = 0
else:
    dict_ex['sb'][25]['v'] = 1
#________________________________________________________
bars_EAN8 = st.radio('EAN-8', ['Выключено','Включено'], index=1)

dict_ex['sb'][26]['k'] = 116
if bars_EAN8 == "Выключено":
    dict_ex['sb'][26]['v'] = 0
else:
    dict_ex['sb'][26]['v'] = 1
#________________________________________________________

bars_PDF417 = st.radio('PDF-417', ['Выключено','Включено'], index=1)

dict_ex['sb'][27]['k'] = 121
if bars_PDF417 == "Выключено":
    dict_ex['sb'][27]['v'] = 0
else:
    dict_ex['sb'][27]['v'] = 1
#________________________________________________________
bars_MicroPDF417 = st.radio('Micro PDF-417', ['Выключено','Включено'], index=1)

dict_ex['sb'][28]['k'] = 125
if bars_MicroPDF417 == "Выключено":
    dict_ex['sb'][28]['v'] = 0
else:
    dict_ex['sb'][28]['v'] = 1
#________________________________________________________
bars_GS1_DataBar = st.radio('GS1 DataBar', ['Выключено','Включено'], index=1)
dict_ex['sb'][29]['k'] = 130
if bars_GS1_DataBar == "Выключено":
    dict_ex['sb'][29]['v'] = 0
else:
    dict_ex['sb'][29]['v'] = 1
#________________________________________________________
bars_GS1_128 = st.radio('GS1-128', ['Выключено','Включено'], index=1)
dict_ex['sb'][30]['k'] = 136
if bars_GS1_DataBar == "Выключено":
    dict_ex['sb'][30]['v'] = 0
else:
    dict_ex['sb'][30]['v'] = 1
#________________________________________________________
bars_Code128 = st.radio('Code-128', ['Выключено','Включено'], index=1)
dict_ex['sb'][31]['k'] = 140
if bars_Code128  == "Выключено":
    dict_ex['sb'][31]['v'] = 0
else:
    dict_ex['sb'][31]['v'] = 1
#________________________________________________________
bars_Code39 = st.radio('Code39', ['Выключено','Включено'], index=1)
dict_ex['sb'][32]['k'] = 145
if bars_Code39 == "Выключено":
    dict_ex['sb'][32]['v'] = 0
else:
    dict_ex['sb'][32]['v'] = 1
#________________________________________________________
bars_QRCode = st.radio('QR-code', ['Выключено','Включено'], index=1)
dict_ex['sb'][33]['k'] = 150
if bars_QRCode  == "Выключено":
    dict_ex['sb'][33]['v'] = 0
else:
    dict_ex['sb'][33]['v'] = 1
#________________________________________________________
if st.button('Generate QR'):
    im1=qrcode.make(dict_ex)
    im1.save('qr.jpg')
    image = Image.open('qr.jpg')
    st.image(image)
