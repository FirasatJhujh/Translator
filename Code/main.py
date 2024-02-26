import tkinter as tk
from googletrans import Translator
import customtkinter as ctk
from threading import Thread
from PIL import Image , ImageTk
from functools import lru_cache
import time
# import os
import numpy as np
import requests

language_codes = np.array([['Auto', 'Auto'], ['Afrikaans', 'af'], ['Albanian', 'sq'], ['Amharic', 'am'], ['Arabic', 'ar'], ['Armenian', 'hy'], ['Azerbaijani', 'az'], ['Basque', 'eu'], ['Belarusian', 'be'], ['Bengali', 'bn'], ['Bosnian', 'bs'], ['Bulgarian', 'bg'], ['Catalan', 'ca'], ['Cebuano', 'ceb'], ['Chinese (Simplified)', 'zh-CN'], ['Chinese (Traditional)', 'zh-TW'], ['Corsican', 'co'], ['Croatian', 'hr'], ['Czech', 'cs'], ['Danish', 'da'], ['Dutch', 'nl'], ['English', 'en'], ['Esperanto', 'eo'], ['Estonian', 'et'], ['Finnish', 'fi'], ['French', 'fr'], ['Frisian', 'fy'], ['Galician', 'gl'], ['Georgian', 'ka'], ['German', 'de'], ['Greek', 'el'], ['Gujarati', 'gu'], ['Haitian Creole', 'ht'], ['Hausa', 'ha'], ['Hawaiian', 'haw'], ['Hebrew', 'he'], ['Hindi', 
'hi'], ['Hmong', 'hmn'], ['Hungarian', 'hu'], ['Icelandic', 'is'], ['Igbo', 'ig'], ['Indonesian', 'id'], ['Irish', 'ga'], ['Italian', 'it'], ['Japanese', 'ja'], ['Javanese', 'jv'], ['Kannada', 'kn'], ['Kazakh', 'kk'], ['Khmer', 'km'], ['Kinyarwanda', 'rw'], ['Korean', 'ko'], ['Kurdish', 'ku'], ['Kyrgyz', 'ky'], ['Lao', 'lo'], ['Latin', 'la'], ['Latvian', 'lv'], ['Lithuanian', 'lt'], ['Luxembourgish', 'lb'], ['Macedonian', 'mk'], ['Malagasy', 'mg'], ['Malay', 'ms'], ['Malayalam', 'ml'], ['Maltese', 'mt'], ['Maori', 'mi'], ['Marathi', 'mr'], ['Mongolian', 'mn'], ['Myanmar (Burmese)', 'my'], ['Nepali', 'ne'], ['Norwegian', 'no'], ['Nyanja (Chichewa)', 'ny'], ['Odia (Oriya)', 'or'], ['Pashto', 'ps'], ['Persian', 'fa'], ['Polish', 'pl'], ['Portuguese', 'pt'], ['Punjabi', 'pa'], ['Romanian', 'ro'], ['Russian', 'ru'], ['Samoan', 'sm'], ['Scots Gaelic', 'gd'], ['Serbian', 'sr'], ['Sesotho', 'st'], ['Shona', 'sn'], ['Sindhi', 'sd'], ['Sinhala', 'si'], ['Slovak', 'sk'], ['Slovenian', 'sl'], ['Somali', 'so'], ['Spanish', 'es'], ['Sundanese', 'su'], ['Swahili', 'sw'], ['Swedish', 'sv'], ['Tagalog (Filipino)', 'tl'], ['Tajik', 'tg'], ['Tamil', 'ta'], ['Tatar', 'tt'], ['Telugu', 'te'], ['Thai', 'th'], ['Turkish', 'tr'], ['Turkmen', 'tk'], ['Urdu', 'ur'], ['Uzbek', 'uz'], ['Vietnamese', 'vi'], ['Welsh', 'cy'], ['Xhosa', 'xh'], ['Yiddish', 'yi'], ['Yoruba', 'yo'], ['Zulu', 'zu'], ['Abkhazian', 'ab'], ['Afar', 'aa'], ['Akan', 'ak'], ['Albanian', 'sq'], ['Amharic', 'am'], ['Arabic', 'ar'], ['Aragonese', 'an'], ['Armenian', 'hy'], ['Assamese', 'as'], ['Avaric', 'av'], ['Avestan', 'ae'], ['Aymara', 'ay'], ['Azerbaijani', 'az'], ['Bambara', 'bm'], ['Bashkir', 'ba'], 
['Basque', 'eu'], ['Belarusian', 'be'], ['Bengali', 'bn'], ['Bihari', 'bh'], ['Bislama', 'bi'], ['Bosnian', 'bs'], ['Breton', 'br'], ['Bulgarian', 'bg'], ['Burmese', 'my'], ['Catalan', 'ca'], ['Chamorro', 'ch'], ['Chechen', 'ce'], ['Chichewa', 'ny'], ['Chinese', 'zh'], ['Chuvash', 'cv'], ['Cornish', 'kw'], ['Corsican', 'co'], ['Cree', 'cr'], ['Croatian', 'hr'], ['Czech', 'cs'], ['Danish', 'da'], ['Divehi', 'dv'], ['Dutch', 'nl'], ['Dzongkha', 'dz'], ['Esperanto', 'eo'], ['Estonian', 'et'], ['Ewe', 'ee'], ['Faroese', 'fo'], ['Fijian', 'fj'], ['Finnish', 'fi'], ['French', 'fr'], ['Frisian', 'fy'], ['Galician', 'gl'], ['Georgian', 'ka'], ['German', 'de'], ['Greek', 'el'], ['Greenlandic', 'kl'], ['Guarani', 'gn'], ['Gujarati', 'gu'], ['Haitian Creole', 'ht'], ['Hausa', 'ha'], ['Hebrew', 'he'], ['Herero', 'hz'], ['Hindi', 'hi'], ['Hiri Motu', 'ho'], ['Hungarian', 'hu'], ['Icelandic', 'is'], ['Ido', 'io'], ['Igbo', 'ig'], 
['Indonesian', 'id'], ['Interlingua', 'ia'], ['Interlingue', 'ie'], ['Inuktitut', 'iu'], ['Inupiaq', 'ik'], ['Irish', 'ga'], ['Italian', 'it'], ['Japanese', 'ja'], ['Javanese', 'jv'], ['Kalaallisut', 'kl'], ['Kannada', 'kn'], ['Kashmiri', 'ks'], ['Kazakh', 'kk'], ['Khmer', 'km'], ['Kikuyu', 'ki'], ['Kinyarwanda', 'rw'], ['Kirghiz', 'ky'], ['Komi', 'kv'], ['Kongo', 'kg'], ['Korean', 'ko'], ['Kurdish', 'ku'], ['Lao', 'lo'], ['Latin', 'la'], ['Latvian', 'lv'], ['Limburgish', 'li'], ['Lingala', 'ln'], ['Lithuanian', 'lt'], ['Luba-Katanga', 'lu'], ['Luxembourgish', 'lb'], ['Macedonian', 'mk'], ['Malagasy', 'mg'], ['Malay', 'ms'], ['Malayalam', 'ml'], ['Maltese', 'mt'], ['Manx', 'gv'], ['Maori', 'mi'], ['Marathi', 'mr'], ['Marshallese', 'mh'], ['Mongolian', 'mn'], ['Nauru', 'na'], ['Navajo', 'nv'], ['Ndonga', 'ng'], ['Nepali', 'ne'], ['Northern Sami', 'se'], ['Norwegian', 'no'], ['Occitan', 'oc'], ['Ojibwa', 'oj'], ['Oriya', 'or'], ['Oromo', 'om'], ['Ossetian', 'os'], ['Pali', 'pi'], ['Panjabi', 'pa'], ['Pashto', 
'ps'], ['Persian', 'fa'], ['Polish', 'pl'], ['Portuguese', 'pt'], ['Quechua', 'qu'], ['Romanian', 'ro'], ['Romansh', 'rm'], ['Rundi', 'rn'], ['Russian', 'ru'], ['Samoan', 'sm'], ['Sango', 'sg'], ['Sanskrit', 'sa'], ['Sardinian', 'sc'], ['Scottish Gaelic', 'gd'], ['Serbian', 'sr'], ['Shona', 'sn'], ['Sindhi', 'sd'], ['Sinhala', 'si'], ['Slovak', 'sk'], ['Slovenian', 'sl'], ['Somali', 'so'], ['Southern Sotho', 'st'], ['Spanish', 'es'], ['Sundanese', 'su'], ['Swahili', 'sw'], ['Swati', 'ss'], ['Swedish', 'sv'], ['Tajik', 'tg'], ['Tamil', 'ta'], ['Tatar', 
'tt'], ['Telugu', 'te'], ['Thai', 'th'], ['Tibetan', 'bo'], ['Tigrinya', 'ti'], ['Tonga', 'to'], ['Tsonga', 'ts'], ['Tswana', 'tn'], ['Turkish', 'tr'], ['Turkmen', 'tk'], ['Twi', 'tw'], 
['Uighur', 'ug'], ['Ukrainian', 'uk'], ['Urdu', 'ur'], ['Uzbek', 'uz'], ['Venda', 've'], ['Vietnamese', 'vi'], ['Volapük', 'vo'], ['Walloon', 'wa'], ['Welsh', 'cy'], ['Wolof', 'wo'], ['Western Frisian', 'fy'], ['Xhosa', 'xh'], ['Yiddish', 'yi'], ['Yoruba', 'yo'], ['Zhuang', 'za'], ['Zulu', 'zu'], ['Afar', 'aa'], ['Abkhazian', 'ab'], ['Avestan', 'ae'], ['Afrikaans', 'af'], ['Akan', 'ak'], ['Amharic', 'am'], ['Aragonese', 'an'], ['Arabic', 'ar'], ['Assamese', 'as'], ['Avaric', 'av'], ['Aymara', 'ay'], ['Azerbaijani', 'az'], ['Bashkir', 'ba'], ['Belarusian', 'be'], ['Bulgarian', 'bg'], ['Bihari', 'bh'], ['Bislama', 'bi'], ['Bambara', 'bm'], ['Bengali', 'bn'], ['Tibetan', 'bo'], ['Breton', 'br'], ['Bosnian', 'bs'], ['Catalan', 'ca'], ['Chechen', 'ce'], ['Chamorro', 'ch'], ['Corsican', 'co'], ['Cree', 'cr'], ['Czech', 'cs'], ['Church Slavic', 'cu'], ['Chuvash', 'cv'], ['Welsh', 'cy'], ['Danish', 'da'], ['German', 'de'], ['Divehi', 'dv'], ['Dzongkha', 'dz'], ['Ewe', 'ee'], ['Greek', 'el'], ['English', 'en'], ['Esperanto', 'eo'], ['Spanish', 'es'], ['Estonian', 'et'], ['Basque', 'eu'], ['Persian', 'fa'], ['Fulah', 'ff'], ['Finnish', 'fi'], ['Fijian', 'fj'], ['Faroese', 'fo'], ['French', 'fr'], ['Western Frisian', 'fy'], ['Irish', 'ga'], ['Scottish Gaelic', 'gd'], ['Galician', 'gl'], ['Guarani', 'gn'], ['Gujarati', 'gu'], ['Manx', 'gv'], ['Hausa', 'ha'], ['Hebrew', 'he'], ['Hindi', 'hi'], ['Hiri Motu', 'ho'], ['Croatian', 'hr'], ['Haitian Creole', 'ht'], ['Hungarian', 'hu'], ['Armenian', 'hy'], ['Herero', 'hz'], ['Interlingua', 'ia'], ['Indonesian', 'id'], ['Interlingue', 'ie'], ['Igbo', 'ig'], ['Sichuan Yi', 'ii'], ['Inupiaq', 'ik'], ['Ido', 'io'], ['Icelandic', 'is'], ['Italian', 'it'], ['Inuktitut', 'iu'], ['Japanese', 'ja'], ['Javanese', 'jv'], ['Georgian', 'ka'], ['Kongo', 'kg'], ['Kikuyu', 'ki'], ['Kuanyama', 'kj'], ['Kazakh', 'kk'], ['Greenlandic', 'kl'], ['Central Khmer', 'km'], ['Kannada', 'kn'], ['Korean', 'ko'], ['Kanuri', 'kr'], ['Kashmiri', 'ks'], ['Kurdish', 'ku'], ['Komi', 'kv'], ['Cornish', 'kw'], ['Kirghiz', 'ky'], ['Latin', 'la'], ['Luxembourgish', 'lb'], ['Ganda', 'lg'], ['Limburgan', 'li'], ['Lingala', 'ln'], ['Lao', 'lo'], ['Lithuanian', 'lt'], ['Luba-Katanga', 'lu'], ['Latvian', 
'lv'], ['Malagasy', 'mg'], ['Marshallese', 'mh'], ['Maori', 'mi'], ['Macedonian', 'mk'], ['Malayalam', 'ml'], ['Mongolian', 'mn'], ['Marathi', 'mr'], ['Malay', 'ms'], ['Maltese', 'mt'], 
['Burmese', 'my'], ['Nauru', 'na'], ['Norwegian Bokmål', 'nb'], ['North Ndebele', 'nd'], ['Nepali', 'ne'], ['Ndonga', 'ng'], ['Dutch', 'nl'], ['Norwegian Nynorsk', 'nn'], ['Norwegian', 'no'], ['Southern Ndebele', 'nr'], ['Navajo', 'nv'], ['Chichewa', 'ny'], ['Occitan', 'oc'], ['Ojibwa', 'oj'], ['Oromo', 'om'], ['Oriya', 'or'], ['Ossetian', 'os'], ['Panjabi', 'pa'], ['Pali', 'pi'], ['Polish', 'pl'], ['Pashto', 'ps'], ['Portuguese', 'pt'], ['Quechua', 'qu'], ['Romansh', 'rm'], ['Rundi', 'rn'], ['Romanian', 'ro'], ['Russian', 'ru'], ['Kinyarwanda', 'rw'], ['Sanskrit', 'sa'], ['Sardinian', 'sc'], ['Sindhi', 'sd'], ['Northern Sami', 'se'], ['Sango', 'sg'], ['Sinhala', 'si'], ['Slovak', 'sk'], ['Slovenian', 'sl'], ['Samoan', 'sm'], ['Shona', 'sn'], ['Somali', 'so'], ['Albanian', 'sq'], ['Serbian', 'sr'], ['Swati', 'ss'], ['Sotho, Southern', 'st'], ['Sundanese', 'su'], ['Swedish', 'sv'], ['Swahili', 'sw'], ['Tamil', 'ta'], 
['Telugu', 'te'], ['Tajik', 'tg'], ['Thai', 'th'], ['Tigrinya', 'ti'], ['Turkmen', 'tk'], ['Tagalog', 'tl'], ['Tswana', 'tn'], ['Tonga', 'to'], ['Turkish', 'tr'], ['Tsonga', 'ts'], ['Tatar', 'tt'], ['Twi', 'tw'], ['Tahitian', 'ty'], ['Uighur', 'ug'], ['Ukrainian', 'uk'], ['Urdu', 'ur'], ['Uzbek', 'uz'], ['Venda', 've'], ['Vietnamese', 'vi'], ['Volapük', 'vo'], ['Walloon', 'wa'], ['Wolof', 'wo'], ['Xhosa', 'xh'], ['Yiddish', 'yi'], ['Yoruba', 'yo'], ['Zhuang', 'za'], ['Zulu', 'zu']])

def findCode(lang):
    return "".join([code for code in language_codes if lang in code][0][1])
    
def findLang(code):
    return "".join([lang for lang in language_codes if code in lang][0][0])
    
def PhotoImage(path , width , height):
    return ImageTk.PhotoImage(Image.open(path).resize((width , height), Image.Resampling.BOX))

class App():
    def __init__(self , master):
        self.root = master
        self.root.title("Translator")
        self.GUImain()
        self.GUARDactive(.9)
        self.from_ = "en"
        self.to_ = "ur"
        # frames
        self.divScr = ctk.CTkScrollableFrame(self.root , fg_color="white",width=980,height=500)

        self.divScr2 = ctk.CTkScrollableFrame(self.root , fg_color="white",width=980,height=500)


    def GUImain(self,from_name = "English", to_name="Urdu"):
        divInp  = tk.Frame(self.root,background="white")
        # self.input_txt_val = tk.StringVar()
        inpdiv = tk.Frame(divInp)
        self.i_btn = ctk.CTkButton(inpdiv,height=37+7,hover_color="White",fg_color="White",bg_color="white",text_color="#1a0dab",border_width=1,border_color="lightgrey",font=("Consolas",16),text=from_name,width=499,anchor="w",command=lambda:self.GUIchangefrom(divInp))
        self.i_btn.pack(anchor="nw",ipadx=0,ipady=3)

        self.input_txt = ctk.CTkTextbox(inpdiv,fg_color="white",width=500,height=470,font=("Consolas",27),border_width=0)
        self.input_txt.pack(side="left") 
        inpdiv.pack(side="left",padx=10)
        ctk.CTkLabel(divInp,text="",image=PhotoImage("_imgs\\change.png",25,36) ,width=60, fg_color="white").pack(anchor="n",side="left",pady=5)
        oupdiv = tk.Frame(divInp ,background="White")
        self.o_btn = ctk.CTkButton(oupdiv,height=37+7,hover_color="White",fg_color="White",text_color="#1a0dab",border_width=1,border_color="lightgrey",font=("Consolas",16),anchor="w",text=to_name , width=499,command=lambda:self.GUIchangeto(divInp))
        self.o_btn.pack(ipadx=10,ipady=3)

        self.output_txt = ctk.CTkTextbox(oupdiv,border_width=0,width=500,state="disabled",font=("Consolas",27),height=470)

        self.output_txt.configure(state="normal")
        self.output_txt.insert("1.0","Tranlation")
        self.output_txt.configure(state="disabled")
        self.output_txt.pack(pady=10) 
        oupdiv.pack(padx=10)

        divInp.pack(anchor="nw" ,padx=10)

        self.starttrans(self.input_txt , self.output_txt)

    # @count
    @lru_cache
    def GUIchangefrom(self, dis):
        def selected(btn, opframe):
            lang = btn.cget("text")
            # p(findCode(lang))
            self.form_ = findCode(lang)
            opframe.place_forget()
            self.GUImain(self.GUImain(findLang(self.from_),findLang(self.to)))

        dis.pack_forget()
        # img = tk.Label(divScr, image=givehwi("search icon.png",100,100)).pack()
        divhead = tk.Frame(self.divScr, background="white")
        # iconSearh =  tk.Label(divhead , text="⌕",font=("Consolas",15)).pack()
        iconSearh =  ctk.CTkLabel(divhead , text="⌕",font=("Consolas",105)).place(x=100,y=100)
        # lg_EN = ctk.CTkEntry(divhead,width=900,height=39,placeholder_text="Translate from")
        # lg_EN.pack(side="left")
        lableSe = tk.Button(divhead, borderwidth=0,background="white",command=lambda:self.GUImain(findLang(self.from_),findLang(self.to_)), text="✖",font=("Consolas",18)).pack(padx=10)
        divhead.pack(anchor="ne")
        ind = 0

        for _ in range(int(len(language_codes)/3)):
            w = 290
            lg_l = tk.Frame(self.divScr , background="white")
            b1 = ctk.CTkButton(lg_l , text=language_codes[ind][0],width=w ,  anchor="nw",fg_color="white",text_color="black",hover_color="lightgrey")
            b1.configure(command=lambda x=b1:selected(x,self.divScr))
            b1.pack(side="left")
 
            b2 = ctk.CTkButton(lg_l ,text=language_codes[ind + 1][0],width=w ,  anchor="nw", fg_color="white",text_color="black",hover_color="lightgrey")
            b2.configure(command=lambda y=b2:selected(y,self.divScr))
            b2.pack(side="left",padx=10,pady=3)
            
            b3 = ctk.CTkButton(lg_l ,text=language_codes[ind + 2][0],width=w ,  anchor="nw"  ,fg_color="white",text_color="black",hover_color="lightgrey")
            b3.configure(command=lambda z=b3:selected(z,self.divScr))
            b3.pack()
            lg_l.pack()
            ind += 3
        # divScr.place_forget()
        self.divScr.place(x=0 , y=0)

    @lru_cache
    def GUIchangeto(self, dis):
        def selected(btn, opframe):
            lang = btn.cget("text")
            # pp(findCode(lang))
            self.to_ = findCode(lang)
            opframe.place_forget()
            self.GUImain(to_name=lang)

        dis.pack_forget()

        # img = tk.Label(divScr, image=givehwi("search icon.png",100,100)).pack()
        divhead = tk.Frame(self.divScr2, background="white")
        # iconSearh =  tk.Label(divhead , text="⌕",font=("Consolas",15)).pack()
        # iconSearh =  ctk.CTkLabel(divhead , text="⌕",font=("Consolas",105)).place(x=100,y=100)
        # lg_EN = ctk.CTkEntry(divhead,width=900,height=39,placeholder_text="Translate to")
        # lg_EN.pack(side="left")
        lableSe = tk.Button(divhead, borderwidth=0,background="white", text="✖",command=lambda:self.GUImain(findLang(self.from_),findLang(self.to_)),font=("Consolas",18)).pack(padx=10)
        divhead.pack(anchor="ne")
        ind = 0
        for l in range(int(len(language_codes)/3)):
            w = 290
            lg_l = tk.Frame(self.divScr2 , background="white")
            b1 = ctk.CTkButton(lg_l , text=language_codes[ind][0],width=w ,  anchor="nw",fg_color="white",text_color="black",hover_color="lightgrey")
            b1.configure(command=lambda x=b1:selected(x,self.divScr2))
            b1.pack(side="left")
 
            b2 = ctk.CTkButton(lg_l ,text=language_codes[ind + 1][0],width=w ,  anchor="nw", fg_color="white",text_color="black",hover_color="lightgrey")
            b2.configure(command=lambda y=b2:selected(y,self.divScr2))
            b2.pack(side="left",padx=10,pady=3)
            
            b3 = ctk.CTkButton(lg_l ,text=language_codes[ind + 2][0],width=w ,  anchor="nw"  ,fg_color="white",text_color="black",hover_color="lightgrey")
            b3.configure(command=lambda z=b3:selected(z,self.divScr2))
            b3.pack()
            lg_l.pack()
            ind += 3
        # divScr.place_forget()
        self.divScr2.place(x=0 , y=0)

    def fealtrans(self,inp_w,out_w):      
        while True:
            time.sleep(.9)
            txt_to_trans = inp_w.get("1.0",ctk.END)
            try:
                translated_txt = self.translator(txt_to_trans)
                # print("Your text:",translated_txt)
                # print("Translated text:",txt_to_trans)
                out_w.configure(state="normal")
                out_w.delete("1.0",tk.END)

                out_w.insert("1.0",translated_txt)
                out_w.configure(state="disabled")
                
            except Exception as e:
                pass

    def translator(self , text):
        try:
            if text == "\n":
                return "Translatation"
            if self.to_ == "ur":
                return " ".join(Translator().translate(text,dest=self.to_,src=self.from_).text.split(" ")[::-1])
            else:
                return Translator().translate(text,dest=self.to_,src=self.from_).text
        except :
            try:
                re = requests.get(url="https://www.google.com/")
                # print("jkjk")
                # print()
            except:
                return "Please, Check Your Internet Connection."
                
            # if res:
            # if res:
        # return " ".join(translation.split(" ")[::-1])

    def starttrans(self, inp_w , out_w):
        th = Thread(target=self.fealtrans , args=(inp_w , out_w,))
        th.start()

    def GUARDgui(self, dutytime=.5 ):
        while True:
            time.sleep(dutytime)

            screenheight = self.root.winfo_height()
            screenwidth = self.root.winfo_width()

            self.divScr.configure(width=screenwidth   - 20, height=screenheight)
            self.divScr.update_idletasks()
            self.divScr2.configure(height=screenheight, width=screenwidth   - 20)
            self.divScr2.update_idletasks()
            self.i_btn.configure(width=int(screenwidth/2)-10)
            self.input_txt.configure(width=int(screenwidth/2)-10, height=screenheight - 30)
            self.o_btn.configure(width=int(screenwidth/2)-10)
            self.output_txt.configure(width=int(screenwidth/2)-10 , height=screenheight - 30)
            # self.
            self.root.update_idletasks()
            self.root.update()

            # "
            # divs 1 , 2 : width = totalw - 20 , height = totalh
            # optionbtn : x , y, z:  total - 100 ** x / 3 **  y - 10 ;
            # input : width=totalw ,height = totalh - 30 ;
            # "
 
    def GUARDactive(self, return_in=.5):
        th = Thread(target=self.GUARDgui,args=(return_in,))
        th.start()

win = tk.Tk()
win.configure(background="white")
win.geometry("1000x500")
win.iconbitmap("_imgs\\trans.ico")
App(win)
win.mainloop()
