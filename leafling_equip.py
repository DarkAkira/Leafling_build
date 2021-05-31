from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import Weapondb as db
import math

window = tk.Tk()
window.geometry("910x750")
window.resizable(width=0, height=0)

window.title("Leafling: Equip Builder")

window.configure(background="black")
#window.grid_rowconfigure(1, weight=1)
#window.grid_columnconfigure(0, weight=1)


window.option_add("*TCombobox*Listbox.Background", '#3f5946')
window.option_add("*TCombobox*Listbox.Foreground", 'White')

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#3f5946',
                                       'fieldbackground': '#3f5946',
                                       'background': '#3f5946',
                                       'foreground': 'White',
                                       }}})

combostyle.theme_use('combostyle') 

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + -50
        y = y + cy + self.widget.winfo_rooty() + 40
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify='left',
                      background="#3f5946", relief='solid', borderwidth=1,
                      foreground="White",
                      font=("Helvetica", "12", "bold"),
                      wraplength=200)
        label.pack(ipadx=1)


    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()


##### make layout #####

frm_top = tk.Frame(window, bg='#308a48', width=910, height=200)
frm_bot = tk.Frame(window, bg='black', width=910, height=550)

frm_top.grid(row=0, sticky="ew")
frm_bot.grid(row=1, sticky="nsew", pady=2.5)

frm_class = tk.Frame(frm_top,  bg='blue', width=200, height=200)
frm_skills = tk.Frame(frm_top, bg='#308a48', width=710, height=200)

frm_class.grid(row=0, column=0, sticky="ns")
frm_class.grid_propagate(False)
frm_skills.grid(row=0, column=2, sticky="nsew")
frm_skills.grid_propagate(False)

frm_items = tk.Frame(frm_bot, bg='#308a48', width=600, height=550)
frm_stats = tk.Frame(frm_bot, bg='#308a48', width=310, height=550)

frm_items.grid(row=0, column=0, sticky="ns")
frm_items.grid_propagate(False)
frm_stats.grid(row=0, column=1, sticky="ns", padx=2.5)
frm_stats.grid_propagate(False)

################# SET Backgrounds #######################


img = ImageTk.PhotoImage(Image.open('.\image\logo.png').resize((200, 200), Image.ANTIALIAS))
lbl = tk.Label(frm_class, image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.



############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
                                                ##### Functions #####
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

def calculate(*args):
    pclass = clicked_c.get()
    Base_stats = db.Base_Stats[pclass]

    Wep = clicked_wep.get()
    Wepp = clicked_wep_p.get()
    Weps = clicked_wep_s.get()
    
    Arm = clicked_arm.get()
    Armp = clicked_arm_p.get()
    Arms = clicked_arm_s.get()

    Off = clicked_off.get()
    Offp = clicked_off_p.get()
    Offs = clicked_off_s.get()

    Acc = clicked_acc.get()
    Accp = clicked_acc_p.get()
    Accs = clicked_acc_s.get()

    So = clicked_soul.get()
    #Sop = clicked_soul_p.get()
    #Sos = clicked_soul_s.get()

    for s in Stats.keys():
        newval = Base_stats[s] + db.Weapon[Wep][s] + db.prefix[Wepp][s] + db.sufix[Weps][s] + db.Armor[Arm][s] + db.prefix[Armp][s] + db.sufix[Arms][s] + db.Offhand[Off][s] + db.prefix[Offp][s] + db.sufix[Offs][s] + db.Accessory[Acc][s] + db.prefix[Accp][s] + db.sufix[Accs][s] + db.Soul[So][s] #+ db.prefix[Sop][s] + db.sufix[Sos][s]
        Stats[s] = newval

    calc_perc()


    ## Rebuild header ##
    rebuild_stats()


    deal_skills()



def class_change(*args):

    #### Get New item types for the class #################

    pclass = clicked_c.get()
    Base_stats = db.Base_Stats[pclass]

    ### Construct the weapons of a class ###

    wepname = []
    for w in db.Weapon.keys():
        if pclass in db.Weapon[w]['Class'] or 'All' in db.Weapon[w]['Class']:
                wepname.append(w)

    wepname = sorted(wepname)

    armname = []
    for arm in db.Armor.keys():
        if pclass in db.Armor[arm]['Class'] or 'All' in db.Armor[arm]['Class']:
                armname.append(arm)
    
    armname = sorted(armname)

    offname = []
    for off in db.Offhand.keys():
        if pclass in db.Offhand[off]['Class'] or 'All' in db.Offhand[off]['Class']:
                offname.append(off)
    
    offname = sorted(offname)

    accname = []
    for acc in db.Accessory.keys():
        if pclass in db.Accessory[acc]['Class'] or 'All' in db.Accessory[acc]['Class']:
                accname.append(acc)
    
    accname = sorted(accname)

    soulname = []
    for soul in db.Soul.keys():
        if pclass in db.Soul[soul]['Class'] or 'All' in db.Soul[soul]['Class']:
                soulname.append(soul)
    
    soulname = sorted(soulname)

    drop_Weapon = ttk.Combobox(frm_items , textvariable= clicked_wep, values=wepname, state='readonly')
    drop_Weapon.bind('<<ComboboxSelected>>', calculate)
    drop_Weapon.grid(row=1, column=1, padx=10, pady=10)

    drop_Armor = ttk.Combobox(frm_items , textvariable= clicked_arm, values=armname, state='readonly')
    drop_Armor.bind('<<ComboboxSelected>>', calculate)
    drop_Armor.grid(row=3, column=1, padx=10, pady=10)

    drop_Offhand = ttk.Combobox(frm_items , textvariable= clicked_off, values=offname, state='readonly')
    drop_Offhand.bind('<<ComboboxSelected>>', calculate)
    drop_Offhand.grid(row=5, column=1, padx=10, pady=10)

    drop_Accessory = ttk.Combobox(frm_items , textvariable= clicked_acc, values=accname, state='readonly')
    drop_Accessory.bind('<<ComboboxSelected>>', calculate)
    drop_Accessory.grid(row=7, column=1, padx=10, pady=10)

    drop_soul = ttk.Combobox(frm_items , textvariable= clicked_soul, values=soulname, state='readonly')
    drop_soul.bind('<<ComboboxSelected>>', calculate)
    drop_soul.grid(row=9, column=1, padx=10, pady=10)
    
    calculate()

def get_base(*args):
    
    pclass = clicked_c.get()
    Base_stats = db.Base_Stats[pclass]

    lbl_dmg = tk.Label(master=frm_stats,  bg='#3f5946', fg="white" , text="Damage", font="Helvetica 10 bold")
    lbl_dmg.grid(row=0, column=0, padx=15, pady=5)
    dmg_numb = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
    dmg_numb["text"] = f"{Stats['Dmg']}"
    dmg_numb.config(width=5)
    dmg_numb.grid(row=0, column=1, padx=15, pady=5)
    for c in range(0,2,1):
        for r in range(1,13,1):
            col = c * 2
            row = r
            keyn = (((c + 1) * 12) - 12) + r
            if keyn < len(Base_stats.keys()):
                key = list(Base_stats.keys())[keyn]
                lbl_key = tk.Label(master=frm_stats, bg='#3f5946', fg="white", text=key, font="Helvetica 10 bold")
                lbl_key.grid(row=row, column=col, padx=5, pady=10)
                lbl_keyres = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
                lbl_keyres["text"] = f"{Base_stats[key]}"
                lbl_keyres.config(width=5)
                lbl_keyres.grid(row=row, column=f"{col + 1}", padx=5, pady=10)

    return(Base_stats)
###################################################

def calc_perc():
    It = {
        'W': db.Weapon[clicked_wep.get()], 'Wp': db.prefix[clicked_wep_p.get()], 'Ws': db.sufix[clicked_wep_s.get()],
        'Ar': db.Armor[clicked_arm.get()], 'Arp': db.prefix[clicked_arm_p.get()], 'Ars': db.sufix[clicked_arm_s.get()], 
        'O': db.Offhand[clicked_off.get()], 'Op': db.prefix[clicked_off_p.get()], 'Os': db.sufix[clicked_off_s.get()], 
        'Ac': db.Accessory[clicked_acc.get()], 'Acp': db.prefix[clicked_acc_p.get()], 'Acs': db.sufix[clicked_acc_s.get()], 
        'S': db.Soul[clicked_soul.get()]
    }
    for s in Stats.keys():
        s_perc = 0
        for items in It.keys():
            if 'Perc' in It[items] and s in It[items]['Perc']:
                s_perc = s_perc + It[items]['Perc'][s]

        final_stat = Stats[s] * (1 + s_perc )
        if final_stat > 0 : 
            
            Stats[s] = math.ceil(float("{:.1f}".format(final_stat))) #"{:.1f}".format
        elif final_stat <= 0 and s == 'HP':
                Stats[s] = 1
        else:
            Stats[s] = 0
        if final_stat >= 500 and s in ['Atk', 'Mag', 'Defense', 'Resist', 'Speed']:
            Stats[s] = 500
        if final_stat >= 250 and s in ['Fire', 'Water', 'Wind', 'Earth', 'Dark', 'Light']:
            Stats[s] = 250

def clear(*args):
    clicked_wep_p.set("Prefix")
    clicked_wep.set("Weapon")
    clicked_wep_s.set("Suffix")

    clicked_arm_p.set("Prefix")
    clicked_arm.set("Armor")
    clicked_arm_s.set("Suffix")

    clicked_off_p.set("Prefix")
    clicked_off.set("Off-hand")
    clicked_off_s.set("Suffix")

    clicked_acc_p.set("Prefix")
    clicked_acc.set("Accessory")
    clicked_acc_s.set("Suffix")

    clicked_soul.set("Soul")

    calculate()


def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def deal_skills(*args):
    Skills={
        'Class':{'Base1':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},},

        'Hunter':{'Base1':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Assassin':{'Base1':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Saboteur':{'Base1':{'type': 'dmg' , 'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Acolyte':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Elementalist':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Soldier':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Vanguard':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Warlord':{'Decimate':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Charge a Powerfull Swing. Deals physical Damage and inflicts stun.','Dmg': (3 * Stats['Atk']) + ( 3.5 * Stats['Fire']), 'Cooldown': 14},
            'Throwing Axe':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Throw a heavy axe dealing physical damage and inflicting Snare','Dmg': 50 + (1.5 * Stats['Atk']), 'Cooldown': 21},
            'Shockwave':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 20 + (0.5*Stats['Atk']) + (5 * Stats['Earth']), 'Cooldown': 0},
            'Frenzy Swirl':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 750 + (10*Stats['Atk']), 'Cooldown': 48},
            'Enrage':{'type': 'buff' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Become fueled by rage! Increase Attack by 50%  while reducing defense by 50%','Duration': 20 , 'Cooldown': 0.25, 'Defense': -0.5, 'Atk': 0.5},
        },

        'Cleric':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Aquamancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Alchemist':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Dreadknight':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Sniper':{ 
            'Heavy Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 1000 + (5 * Stats['Speed']), 'Cooldown': 3 * (1 - (Stats['Spell_Haste']/100))},
            'Air Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn2.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 240 + (1.25 * Stats['Speed'] + (1.65 * Stats['Wind'])), 'Cooldown': 2.5 * (1 - (Stats['Spell_Haste']/100))},
            'Vortex Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn3.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 250 +(2 * Stats['Speed'] + 3.5 * Stats['Wind']), 'Cooldown': 2.5 * (1 - (Stats['Spell_Haste']/100))},
            'Volley':{'type': 'dmg' , 'img':'.\image\skill\Sn5.png', 'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 100 +(0.5 * Stats['Speed']), 'Cooldown': 16.5 * (1 - (Stats['Spell_Haste']/100))},
        },

        'Monk':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Dragonslayer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Necromancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Timeweaver':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Shinobi':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Ronin':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Wrath':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Mercy':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Paladin Protector':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },

        'Pyromancer':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
            'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        },
    }
    ### Rebuild Skills ###

    for labs in frm_skills.winfo_children():
        labs.destroy()

    for r in range(1,3,1):
        for c in range(0,6,1):
            row = (r * 3) - 3  
            k = (((r * 5) - 5) + c)
            #print(k)
            if k < len(Skills[clicked_c.get()]):
                skill = list(Skills[clicked_c.get()].keys())[k]
                #print(skill)
                imgpath = Skills[clicked_c.get()][skill]['img']

                
                img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((35, 35), Image.ANTIALIAS))
                lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                lbl_skill.img = img_skill 
                lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                CreateToolTip(lbl_skill, Skills[clicked_c.get()][skill]['Skilltext'])

                if Skills[clicked_c.get()][skill]['type'] == 'dmg' :
                    ### Dmg ###
                    dmg= math.ceil(float("{:.1f}".format(Skills[clicked_c.get()][skill]['Dmg'])))
                    lbl_dmg = tk.Label(frm_skills, 
                    text = f"Dmg: {dmg}",
                    bg='#3f5946', fg="white", font="Helvetica 10 bold"
                    )
                    lbl_dmg.grid(row=row + 1 , column=c, padx=5, pady=0)

                if Skills[clicked_c.get()][skill]['type'] == 'buff' :
                    ### Duration ###
                    Duration= math.ceil(float("{:.1f}".format(Skills[clicked_c.get()][skill]['Duration'])))
                    lbl_dmg = tk.Label(frm_skills, 
                    text = f"Duration: {Duration}",
                    bg='#3f5946', fg="white", font="Helvetica 10 bold"
                    )
                    lbl_dmg.grid(row=row + 1 , column=c, padx=5, pady=0)

                ### Cdr ###
                cool= float("{:.2f}".format(Skills[clicked_c.get()][skill]['Cooldown']))
                lbl_dmg = tk.Label(frm_skills, 
                text = f"Cooldown: {cool}",
                bg='#3f5946', fg="white", font="Helvetica 10 bold"
                )
                lbl_dmg.grid(row=row + 2, column=c, padx=5, pady=0)






##### Rebuild Stats Information #####

def rebuild_stats(*args):
    for labs in frm_stats.winfo_children():
        labs.destroy()
    
    lbl_dmg = tk.Label(master=frm_stats,  bg='#3f5946', fg="white" , text="Damage", font="Helvetica 10 bold")
    lbl_dmg.grid(row=0, column=0, padx=15, pady=5)
    dmg_numb = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
    dmg_numb["text"] = f"{Stats['Dmg']}"
    dmg_numb.config(width=5)
    dmg_numb.grid(row=0, column=1, padx=15, pady=5)

    for c in range(0,2,1):
        for r in range(1,13,1):
            col = c * 2
            row = r
            keyn = (((c + 1) * 12) - 12) + r
            if keyn < len(Stats.keys()):
                key = list(Stats.keys())[keyn]
                lbl_key = tk.Label(master=frm_stats, bg='#3f5946', fg="white", text=key, font="Helvetica 10 bold")
                lbl_key.grid(row=row, column=col, padx=5, pady=10)
                lbl_keyres = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
                lbl_keyres["text"] = f"{Stats[key]}"
                lbl_keyres.config(width=5)
                lbl_keyres.grid(row=row, column=f"{col + 1}", padx=5, pady=10)

       

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

Stats={'Dmg': 0,'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0
}

Skill_toggle = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
                                                ##### Build the labels #####
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

###### Class Box ##########
lbl_class = tk.Label(master=frm_class,
    text="Class",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_class.configure(width=10)
lbl_class.grid(row=0, column=0, padx=10, pady=15)
clicked_c = tk.StringVar()
clicked_c.set("Class")
classname = sorted(list(db.Base_Stats.keys()))

####################################################################
####################################################################
####################################################################
####################################################################
####################################################################

prefix = sorted(list(db.prefix.keys()))
sufix = sorted(list(db.sufix.keys()))

###### Weapon Box ##########
lbl_Weapon = tk.Label(master=frm_items,
    text="Weapon",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_Weapon.grid(row=0, column=1, padx=10, pady=10)
clicked_wep = tk.StringVar()
clicked_wep.set("Weapon")
wepname = sorted(list(db.Weapon.keys()))
clicked_wep_p = tk.StringVar()
clicked_wep_p.set("Prefix")
clicked_wep_s = tk.StringVar()
clicked_wep_s.set("Suffix")

###### Armor Box ##########

lbl_Armor = tk.Label(master=frm_items,
    text="Armor",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_Armor.grid(row=2, column=1, padx=10, pady=10)
clicked_arm = tk.StringVar()
clicked_arm.set("Armor")
armname = sorted(list(db.Armor.keys()))
clicked_arm_p = tk.StringVar()
clicked_arm_p.set("Prefix")
clicked_arm_s = tk.StringVar()
clicked_arm_s.set("Suffix")

###### Off-hand Box ##########
lbl_Offhand = tk.Label(master=frm_items,
    text="Off-hand",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_Offhand.grid(row=4, column=1, padx=10, pady=10)
clicked_off = tk.StringVar()
clicked_off.set("Off-hand")
offname = sorted(list(db.Offhand.keys()))
clicked_off_p = tk.StringVar()
clicked_off_p.set("Prefix")
clicked_off_s = tk.StringVar()
clicked_off_s.set("Suffix")

###### Accessory Box ##########
lbl_accessory = tk.Label(master=frm_items,
    text="Accessory",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_accessory.grid(row=6, column=1, padx=10, pady=10)
clicked_acc = tk.StringVar()
clicked_acc.set("Accessory")
accname = sorted(list(db.Accessory.keys()))
clicked_acc_p = tk.StringVar()
clicked_acc_p.set("Prefix")
clicked_acc_s = tk.StringVar()
clicked_acc_s.set("Suffix")

###### Soul Box ##########
lbl_Soul = tk.Label(master=frm_items,
    text="Soul",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946", #rgb works 
    relief="raised")
lbl_Soul.grid(row=8, column=1, padx=10, pady=10)
clicked_soul = tk.StringVar()
clicked_soul.set("Soul")
soulname = sorted(list(db.Soul.keys()))

############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
                                                ##### Make buttons with command #####
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################

drop_class = ttk.Combobox(frm_class , textvariable= clicked_c, values=classname, state='readonly')
drop_class.bind('<<ComboboxSelected>>', class_change)
drop_class.grid(row=1, column=0, padx=25, pady=25)

Base_stats = get_base()

drop_Weapon_pref = ttk.Combobox(frm_items , textvariable=clicked_wep_p, values=prefix, state='readonly')
drop_Weapon_pref.bind('<<ComboboxSelected>>', calculate)
drop_Weapon_pref.grid(row=1, column=0, padx=10, pady=10)

drop_Weapon = ttk.Combobox(frm_items , textvariable= clicked_wep, values=wepname, state='readonly')
drop_Weapon.bind('<<ComboboxSelected>>', calculate)
drop_Weapon.grid(row=1, column=1, padx=10, pady=10)

drop_Weapon_suf = ttk.Combobox(frm_items , textvariable=clicked_wep_s, values=sufix, state='readonly')
drop_Weapon_suf.bind('<<ComboboxSelected>>', calculate)
drop_Weapon_suf.grid(row=1, column=3, padx=10, pady=10)

####################

drop_Armor_pref = ttk.Combobox(frm_items , textvariable=clicked_arm_p, values=prefix, state='readonly')
drop_Armor_pref.bind('<<ComboboxSelected>>', calculate)
drop_Armor_pref.grid(row=3, column=0, padx=10, pady=10)

drop_Armor = ttk.Combobox(frm_items , textvariable= clicked_arm, values=armname, state='readonly')
drop_Armor.bind('<<ComboboxSelected>>', calculate)
drop_Armor.grid(row=3, column=1, padx=10, pady=10)

drop_Armor_suf = ttk.Combobox(frm_items , textvariable=clicked_arm_s, values=sufix, state='readonly')
drop_Armor_suf.bind('<<ComboboxSelected>>', calculate)
drop_Armor_suf.grid(row=3, column=3, padx=10, pady=10)

#############################

drop_Offhand_pref = ttk.Combobox(frm_items , textvariable=clicked_off_p, values=prefix, state='readonly')
drop_Offhand_pref.bind('<<ComboboxSelected>>', calculate)
drop_Offhand_pref.grid(row=5, column=0, padx=10, pady=10)

drop_Offhand = ttk.Combobox(frm_items , textvariable= clicked_off, values=offname, state='readonly')
drop_Offhand.bind('<<ComboboxSelected>>', calculate)
drop_Offhand.grid(row=5, column=1, padx=10, pady=10)

drop_Offhand_suf = ttk.Combobox(frm_items , textvariable=clicked_off_s, values=sufix, state='readonly')
drop_Offhand_suf.bind('<<ComboboxSelected>>', calculate)
drop_Offhand_suf.grid(row=5, column=3, padx=10, pady=10)

##############################

drop_Accessory_pref = ttk.Combobox(frm_items , textvariable=clicked_acc_p, values=prefix, state='readonly')
drop_Accessory_pref.bind('<<ComboboxSelected>>', calculate)
drop_Accessory_pref.grid(row=7, column=0, padx=10, pady=10)

drop_Accessory = ttk.Combobox(frm_items , textvariable= clicked_acc, values=accname, state='readonly')
drop_Accessory.bind('<<ComboboxSelected>>', calculate)
drop_Accessory.grid(row=7, column=1, padx=10, pady=10)

drop_Accessory_suf = ttk.Combobox(frm_items, textvariable=clicked_acc_s, values=sufix, state='readonly')
drop_Accessory_suf.bind('<<ComboboxSelected>>', calculate)
drop_Accessory_suf.grid(row=7, column=3, padx=10, pady=10)

###########################

drop_soul = ttk.Combobox(frm_items , background = '#3f5946', textvariable= clicked_soul, values=soulname, state='readonly')
drop_soul.bind('<<ComboboxSelected>>', calculate)
drop_soul.grid(row=9, column=1, padx=10, pady=10)

######################################

### Make a Clear button ###

clear = tk.Button(frm_items,
text="Clear Build",
bg='#3f5946',
fg='White',
font="Helvetica 12 bold",
command=clear)
clear.grid(row=0, column=3, padx=10, pady=10)


###########################################################################
###########################################################################
###########################################################################

#### Fim, fazer class Skills ####

###########################################################################
###########################################################################
###########################################################################

### Dont change this dictionary, you should change the one inside the calculate function ###
Skills={
    'Class':{'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base2':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base3':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base4':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base5':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base6':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base7':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
    'Base8':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},},
}


for r in range(1,3,1):
    for c in range(0,6,1):
        row = (r * 3) - 3  
        k = (((r * 5) - 5) + c)

        if k < len(Skills[clicked_c.get()]):
            skill = list(Skills[clicked_c.get()].keys())[k]
            print(skill)
            imgpath = Skills[clicked_c.get()][skill]['img']

            if Skills[clicked_c.get()][skill]['type'] == 'dmg' :
                img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((35, 35), Image.ANTIALIAS))
                lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                lbl_skill.img = img_skill 
                lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                CreateToolTip(lbl_skill, Skills[clicked_c.get()][skill]['Skilltext'])

                 ### Dmg ###
                dmg= math.ceil(float("{:.1f}".format(Skills[clicked_c.get()][skill]['Dmg'])))
                print(Skills[clicked_c.get()][skill]['Dmg'])
                lbl_dmg = tk.Label(frm_skills, 
                text = f"Dmg: {dmg}",
                 bg='#3f5946', fg="white", font="Helvetica 10 bold"
                )
                lbl_dmg.grid(row=row + 1 , column=c, padx=5, pady=0)

                ### Cdr ###
                cool= float("{:.2f}".format(Skills[clicked_c.get()][skill]['Cooldown']))
                lbl_dmg = tk.Label(frm_skills, 
                text = f"Cooldown: {cool}",
                bg='#3f5946', fg="white", font="Helvetica 10 bold"
                )
                lbl_dmg.grid(row=row + 2, column=c, padx=5, pady=0)



window.mainloop()