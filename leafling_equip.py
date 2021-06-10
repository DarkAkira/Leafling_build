from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Weapondb as db
import math
import os

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

frm_top = tk.Frame(window, bg='black', width=910, height=200)
frm_bot = tk.Frame(window, bg='black', width=910, height=530)

frm_top.grid(row=0, sticky="ew")
frm_bot.grid(row=1, sticky="nsew", pady=2.5)

frm_class = tk.Frame(frm_top,  bg='blue', width=200, height=200)
frm_skills = tk.Frame(frm_top, bg='#3f5946', width=535, height=200)
frm_buffs = tk.Frame(frm_top, bg='#308a48', width=175, height=200)

frm_class.grid(row=0, column=0, sticky="ns")
frm_class.grid_propagate(False)
frm_skills.grid(row=0, column=2, sticky="nsew")
frm_skills.grid_propagate(False)
frm_buffs.grid(row=0, column=3, sticky="nsew",padx =2.5)
frm_buffs.grid_propagate(False)

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
        Buff_Stats[s] = newval

    calc_perc()

    print(Stats)


    deal_buffs()

    print(Buff_Stats)
    deal_skills()

    ## Rebuild header ##
    rebuild_stats()



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
    
    create_buff()

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
            Buff_Stats[s] = math.ceil(float("{:.1f}".format(final_stat)))
        elif final_stat <= 0 and s == 'HP':
            Stats[s] = 1
            Buff_Stats[s] = 1

        else:
            Stats[s] = 0
            Buff_Stats[s] = 0
        if final_stat >= 500 and s in ['Atk', 'Mag', 'Defense', 'Resist', 'Speed']:
            Stats[s] = 500
            Buff_Stats[s] = 500
        if final_stat >= 250 and s in ['Fire', 'Water', 'Wind', 'Earth', 'Dark', 'Light']:
            Stats[s] = 250
            Buff_Stats[s] = 250

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


def create_buff(*args):
    for lab in frm_buffs.winfo_children():
        lab.destroy()   

    MenuBttn = tk.Menubutton(frm_buffs, text = "Buffs", relief ="raised")
    Menu1 = tk.Menu(MenuBttn, tearoff = 0)
    print(clicked_c.get(), list(db.Skills_b[clicked_c.get()].keys()))
    buff_present = []
    for i in list(db.Skills_b[clicked_c.get()].keys()):
        if db.Skills_b[clicked_c.get()][i]['type'] == 'buff':
            buff_present.append(i)

    for n in buff_present:
        s_var[n] = tk.IntVar()
        Menu1.add_checkbutton(label = n, variable = s_var[n], command=lambda: calculate())

    MenuBttn["menu"] = Menu1

    MenuBttn.grid(row=0, columnspan=6, pady=5, padx=5, sticky='nsew')
    MenuBttn.config(width=26)


def deal_buffs(*args):
    for widget in frm_buffs.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    buff_present = []
    for i in list(db.Skills_b[clicked_c.get()].keys()):
        if db.Skills_b[clicked_c.get()][i]['type'] == 'buff':
            buff_present.append(i)
    c=0
    for n in buff_present:
        print(n,s_var[n].get())
        if s_var[n].get() == 1:
            ### Put skill image below ###
            imgpath = db.Skills_b[clicked_c.get()][n]['img']
            img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((15, 15), Image.ANTIALIAS))
            lbl_skill = tk.Label(frm_buffs, image=img_skill, bg='#3f5946')
            lbl_skill.img = img_skill 

            CreateToolTip(lbl_skill, db.Skills_b[clicked_c.get()][n]['Skilltext'])

            print(c)

            if c > 5:
                col = c-6
                lbl_skill.grid(row=2, column=col, padx=5, pady=2)
            else:
                
                lbl_skill.grid(row=1, column=c, padx=5, pady=2)

            c = c + 1


            for s in Buff_Stats.keys():
                s_buff = 0
                if s in db.Skills_b[clicked_c.get()][n]:
                    s_buff = s_buff + db.Skills_b[clicked_c.get()][n][s]
                    
                buff_s = Buff_Stats[s] * (1 + s_buff)

                Buff_Stats[s] = math.ceil(float("{:.1f}".format(buff_s)))



def deal_skills(*args):
    #### Dmging Skills
    Skills={
        'Class':{
        #    'Base1':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 0, 'Cooldown': 0},
        #    'Base2':{'type': 'debuff' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Effect': '', 'Duration': 0, 'Cooldown': 0},
        #    'Base3':{'type': 'heal' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Stat': 0, 'Cooldown': 0},
        },

        'Hunter':{
            'Ensnare':{'type': 'debuff', 'img':'.\image\skill\Hens.png', 'Skilltext': 'Strike at your target\'s heels, inflicting snare. Needs a dagger equiped','Effect': 'Snare', 'Duration': 4.2, 'Cooldown': 14.8},
            'Sand Swipe':{'type': 'debuff', 'img':'.\image\skill\Hsand.png', 'Skilltext': 'Toss sand in front of you inflicting Blind on all enemies hit.','Effect': 'Blind', 'Duration': 2.5, 'Cooldown': 15},
            'Scouting Flare':{'type': 'dmg', 'img':'.\image\skill\Hscout.png', 'Skilltext': 'Fire a light above you, dealing 1 true damage to all enemies within 12 tiles and revealing stealthed enemies. Must have a bow equiped.','Dmg': 1, 'Cooldown': 10},
            'Quick Nock':{'type': 'dmg' , 'img':'.\image\skill\Hquick.png', 'Skilltext': 'nstantly fire an arrow at your target with no delay. Must have bow equiped.','Dmg': 100 + (0.8*Buff_Stats['Speed']), 'Cooldown': 0.1},
            'Flurry':{'type': 'dmg' , 'img':'.\image\skill\Hflurry.png', 'Skilltext': 'Fire an entire quiver of arrows in quick succession','Dmg': 200 + (1.2*Buff_Stats['Speed']), 'Cooldown': 20},
            'Pusruit':{'type': 'dmg' , 'img':'.\image\skill\Hpur.png', 'Skilltext': 'Leap to your target through the shadows and inflict stun. Must have dagger equiped.','Dmg': 40 + (0.85*Buff_Stats['Atk']), 'Cooldown': 28},
            'Cripple':{'type': 'debuff',  'img':'.\image\skill\Hcripp.png', 'Skilltext': 'Drastically lower your targets speed, reducing their ability to dodge or run away. ','Effect': 'Lower speed.', 'Duration': 6, 'Cooldown': 11.9},
        },

        'Assassin':{
            'Cross Strike':{'type': 'dmg' , 'img':'.\image\skill\AScross.png', 'Skilltext': 'Deal two rapid strikes with a 50% \chance to Critical Hit for 1.6x damage','Dmg': 250 + Buff_Stats['Atk'] + Buff_Stats['Dark'], 'Cooldown': 9.8},
            'Shadowbind':{'type': 'debuff', 'img':'.\image\skill\ASshadow.png', 'Skilltext': 'Bind your target with their own shadow, setting them up for assasination.','Effect': 'Snare', 'Duration': 4, 'Cooldown': 18},
            'Waylay':{'type': 'dmg' , 'img':'.\image\skill\ASway.png', 'Skilltext': 'Surprise attack your target inflicting Stun for 2.4 s.','Dmg': 100 + (2*Buff_Stats['Atk']), 'Cooldown': 22},
            'Cloak of Shadows':{'type': 'debuff' , 'img':'.\image\skill\AScloak.png', 'Skilltext': 'Cloak yourself in a blanket of shadows.','Effect': 'Stealth', 'Duration': 12, 'Cooldown': 24.5},
            'Shadowstep':{'type': 'debuff' , 'img':'.\image\skill\ASstep.png', 'Skilltext': 'Step through the shadows, instantly dashing in the direction you\'re moving','Effect': 'Dash', 'Duration': 0, 'Cooldown': 3},
            'Volley of Knives':{'type': 'dmg' , 'img':'.\image\skill\ASvolley.png', 'Skilltext': 'Let loose a volley of throwing knives at your target.','Dmg': 225 + (Buff_Stats['Atk']), 'Cooldown': 6.2},
            'Viper Strike':{'type': 'dmg' , 'img':'.\image\skill\Asviper.png', 'Skilltext': 'Strike your target with a poisoned blade and inflicting silence for 3 s.','Dmg': 25 + (0.35*Buff_Stats['Mag']) + (2*Buff_Stats['Water']), 'Cooldown': 26.5},
            'Death Mark':{'type': 'debuff' , 'img':'.\image\skill\ASdeath.png', 'Skilltext': 'Mark your target for death, temporarily reducing their defences by 50% for the duration.','Effect': '-50% target Def', 'Duration': 6.5, 'Cooldown': 35},
        },

        'Saboteur':{
            'Beguile':{'type': 'dmg' , 'img':'.\image\skill\SAbeg.png', 'Skilltext': 'Surprise your foe with a gust of wind, knocking them backwards and inflicting stun for 16.5 s','Dmg': 125 + (Buff_Stats['Mag']) + (4*Buff_Stats['Wind']), 'Cooldown': 16.5},
            'Bear Trap':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Lay down a bear trap that can Snare a target.','Dmg': 200 + (2* Buff_Stats['Mag']) + (10*Buff_Stats['Earth']), 'Cooldown': 5},
            'Noxious Poison':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Afflict your target with a noxious poison and inflicting Silence for 3 s','Dmg': 70 + (0.65*Buff_Stats['Mag'] + (1.5 * Buff_Stats['Dark'])), 'Cooldown': 15},
            'Debilitating Toxin':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Afflict your target with a debilitating poison, reducing Armor and Resist by 20% for 6 s','Dmg': 100 + (0.8 * Buff_Stats['Mag']) + (1.25 * Buff_Stats['Earth']), 'Cooldown': 5},
            
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

        'Elementalist':{
            'Wildfire':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Wildfire\n\nIgnite your target and all nearby. Deals Magic damage each tick for the duration of 5s.','Dmg': (100 + (0.8*Buff_Stats['Mag']) + (1.6 * Buff_Stats['Fire'])), 'Cooldown': 3.6},
            
            'Chain Lightning':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Chain Lightning\n\nBlast your targets with lightning that bounces to nearby targets.\n\nHP:-400','Dmg': (400 + (2*Buff_Stats['Mag']) + (4*Buff_Stats['Wind'])), 'Cooldown': 3.6},
            
            'Quake':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Quake\n\nStrike at all enemies near your target with earth magic.\n\nInflicts stun','Dmg': (400 + (3*Buff_Stats['Mag']) + (5*Buff_Stats['Earth'])), 'Cooldown': 3.6},
            
            'Blizzard':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Blizzard\n\nSummons a Blizzard at your target\'s location.\n60% target speed reduced.','Dmg': (400+(3*Buff_Stats['Mag']) + (4*Buff_Stats['Water'])), 'Cooldown': 3.6},
        },

        'Soldier':{
            'Pommel Strike':{'type': 'dmg' , 'img':'.\image\skill\Spom.png', 'Skilltext': 'Strike your target with the pommel of your sword and inflicting stun','Dmg': 20 + (0.6*Buff_Stats['Atk']), 'Cooldown': 12.5},
            'Whirlwind':{'type': 'dmg' , 'img':'.\image\skill\Sw.png', 'Skilltext': 'Swing your sword around you inflicting stun.','Dmg': 100+(3.5*Buff_Stats['Atk']), 'Cooldown': 14},
            'Leg Trample':{'type': 'dmg' , 'img':'.\image\skill\Sleg.png', 'Skilltext': 'Attack your target\'s legs reducing target Speed by 80% \for the 3s..','Dmg': Buff_Stats['Atk'], 'Cooldown': 22},
            'Lacerate':{'type': 'dmg' , 'img':'.\image\skill\Slac.png', 'Skilltext': 'Deal a blow to your target\'s vitals, causing them to bleed','Dmg': 50 + (1.25* Buff_Stats['Atk']), 'Cooldown': 16},
        },

        'Vanguard':{
            'Commanding Swing':{'type': 'dmg' , 'img':'.\image\skill\Vswing.png', 'Skilltext': 'trike at your target with a steeled will and inflicting stun','Dmg': 150 + (0.55*Buff_Stats['Atk']), 'Cooldown': 4},
            'Righteous Strike':{'type': 'dmg' , 'img':'.\image\skill\Vstrike.png', 'Skilltext': 'Smash your target with righteous glory','Dmg': 250+(1.5*Buff_Stats['Atk']), 'Cooldown': 14.25},
            'Guardian Will':{'type': 'debuff' , 'img':'.\image\skill\Vguard.png', 'Skilltext': 'You steel yourself with the will of a guardian, becoming immune to damage','Effect': 'Immune to Damage', 'Duration': 8.5, 'Cooldown': 65},
            'Block':{'type': 'debuff' , 'img':'.\image\skill\Vblock.png', 'Skilltext': 'Block an incoming attack, becoming invulnerable for a brief moment.','Effect': 'Invulnerable', 'Duration': 0.6, 'Cooldown': 6},
            'Shield Formation':{'type': 'debuff' , 'img':'.\image\skill\Vshield.png', 'Skilltext': 'Enter a defensive stance, increasing your defenses for the duration and Cleansing yourself of negative effects.','Effect': 'Cleanse', 'Duration': 4, 'Cooldown': 22},
            'War Cry':{'type': 'debuff' , 'img':'.\image\skill\Vcry.png', 'Skilltext': 'You scream in pride, challenging all nearby enemies. Inflicts Taunt for the duration','Effect': 'Taunt', 'Duration': 4, 'Cooldown': 14},
            'War Chant':{'type': 'debuff' , 'img':'.\image\skill\Vchant.png', 'Skilltext': 'Let out a bolsterous roar, granting all nearby allies a Shield for (10% MaxHP)','Effect': 'Shield allies', 'Duration': 4.5, 'Cooldown': 15},
        },

        'Warlord':{
            'Decimate':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Charge a Powerfull Swing. Deals physical Damage and inflicts stun.','Dmg': (3 * Buff_Stats['Atk']) + ( 3.5 * Buff_Stats['Fire']), 'Cooldown': 14},
            'Throwing Axe':{'type': 'dmg' , 'img':'.\image\skill\Waxe.png', 'Skilltext': 'Throw a heavy axe dealing physical damage, inflicting Snare and reducing target Speed by 80% \for the duration.','Dmg': 50 + (1.5 * Buff_Stats['Atk']), 'Cooldown': 21},
            'Shockwave':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Dmg': 20 + (0.5*Buff_Stats['Atk']) + (5 * Buff_Stats['Earth']), 'Cooldown': 0},
            'Frenzy Swirl':{'type': 'dmg' , 'img':'.\image\skill\Wfren.png', 'Skilltext': 'Unleash a devastating whirlwind of blade and blood','Dmg': 750 + (10*Buff_Stats['Atk']), 'Cooldown': 48}, 
            'Warlord tears':{'type': 'heal' , 'img':'.\image\skill\watears.png', 'Skilltext': 'The sweat the drips down your body replenishes you.','HP': (0.01*Buff_Stats['HP']) + (2.5 * Buff_Stats['Water']), 'Cooldown': 35},
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
            'Heavy Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 1000 + (5 * Buff_Stats['Speed']), 'Cooldown': 3 * (1 - (Buff_Stats['Spell_Haste']/100))},
            'Air Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn2.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 240 + (1.25 * Buff_Stats['Speed'] + (1.65 * Buff_Stats['Wind'])), 'Cooldown': 2.5 * (1 - (Buff_Stats['Spell_Haste']/100))},
            'Vortex Shot':{'type': 'dmg' , 'img':'.\image\skill\Sn3.png' ,'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 250 +(2 * Buff_Stats['Speed'] + 3.5 * Buff_Stats['Wind']), 'Cooldown': 2.5 * (1 - (Buff_Stats['Spell_Haste']/100))},
            'Volley':{'type': 'dmg' , 'img':'.\image\skill\Sn5.png', 'Skilltext': 'Fires a shot imbued with wind magic.','Dmg': 100 +(0.5 * Buff_Stats['Speed']), 'Cooldown': 16.5 * (1 - (Buff_Stats['Spell_Haste']/100))},
        },

        'Monk':{
            'Tiger Strike':{'type': 'dmg' , 'img':'.\image\skill\Mtig.png', 'Skilltext': 'This skill does ....','Dmg': 150 + Buff_Stats['Atk'] + (2* Buff_Stats['Fire']), 'Cooldown': 3},
            'Falcon Strike':{'type': 'dmg' , 'img':'.\image\skill\Mfal.png', 'Skilltext': 'This skill does ....','Dmg': 150 + Buff_Stats['Atk'] + (2* Buff_Stats['Wind']), 'Cooldown': 3},
            'Cobra Strike':{'type': 'dmg' , 'img':'.\image\skill\Mcobra.png', 'Skilltext': 'This skill does ....','Dmg': 150 + Buff_Stats['Atk'] + (2* Buff_Stats['Water']), 'Cooldown': 3},
            'Golem Strike':{'type': 'dmg' , 'img':'.\image\skill\Mgol.png', 'Skilltext': 'This skill does ....','Dmg': 150 + Buff_Stats['Atk'] + (2* Buff_Stats['Earth']), 'Cooldown': 3},
            'Ki Devastation':{'type': 'dmg' , 'img':'.\image\skill\Mki.png', 'Skilltext': 'This skill does ....','Dmg': 225 + (1.75* Buff_Stats['Atk']), 'Cooldown': 45},
            'Chakra':{'type': 'heal' , 'img':'.\image\skill\Mchakra.png', 'Skilltext': 'Channel your inner Chakra, restoring Health and Mana and Cleansing yourself of debuffs.','HP': 0.3 * Buff_Stats['HP'], 'Mana': 0.3 * Buff_Stats['Mana'], 'Cooldown': 65},
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
        'Corrupted Jewel':{'Arcane Missiles':{'type': 'dmg' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'Fire a wave of empowered Mana Bolts ','Dmg': 4*Stats['Mag'], 'Cooldown': 20},
        },

        'Treants Spine': {'Entaglement':{'type': 'debuff' , 'img':'.\image\skill\Sn1.png', 'Skilltext': 'This skill does ....','Effect': 'Snare', 'Duration': 0, 'Cooldown': 0}}
    }
    ### Rebuild Skills ###

    for labs in frm_skills.winfo_children():
        labs.destroy()

    skill_dic ={}

    Eqs= {
        'W': clicked_wep.get(),
        'Ar': clicked_arm.get(),
        'O': clicked_off.get(),
        'Ac': clicked_acc.get(),
        'S': clicked_soul.get()
    }

    skill_dic.update(Skills[clicked_c.get()])

    for eq in Eqs.keys():
        print(Eqs[eq])
        if Eqs[eq] in Skills.keys():
            skill_dic.update(Skills[Eqs[eq]])
    
    print(skill_dic)
    for r in range(0,2,1):
        for c in range(0,5,1):
            row = (r * 3)  
            if r > 0:
                k = (r*4) + c + 1
            else:
                k = c

            if k < len(skill_dic.keys()):
                skill = list(skill_dic.keys())[k]
                imgpath = skill_dic[skill]['img']

                if skill_dic[skill]['type'] == 'dmg' :
                    img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((25, 25), Image.ANTIALIAS))
                    lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                    lbl_skill.img = img_skill 
                    lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                    CreateToolTip(lbl_skill, skill_dic[skill]['Skilltext'])

                    dmg= math.ceil(float("{:.1f}".format(skill_dic[skill]['Dmg'])))
                    lbl_dmg = tk.Label(frm_skills, 
                    text = f"Dmg: {dmg}",
                    bg='#3f5946', fg="white", font="Helvetica 8 bold"
                    )
                    lbl_dmg.grid(row=row + 1 , column=c, padx=5, pady=0)

                    ### Cdr ###
                    cool= float("{:.2f}".format(skill_dic[skill]['Cooldown']))
                    lbl_dmg = tk.Label(frm_skills, 
                    text = f"Cooldown: {cool}",
                    bg='#3f5946', fg="white", font="Helvetica 8 bold"
                    )
                    lbl_dmg.grid(row=row + 2, column=c, padx=5, pady=0)

                if skill_dic[skill]['type'] == 'heal' :
                    img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((25, 25), Image.ANTIALIAS))
                    lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                    lbl_skill.img = img_skill 
                    lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                    CreateToolTip(lbl_skill, skill_dic[skill]['Skilltext'])

                    HP= math.ceil(float("{:.1f}".format(skill_dic[skill]['HP'])))
                    lbl_heal = tk.Label(frm_skills, 
                    text = f"Hp recovered: {HP}",
                    bg='#3f5946', fg="white", font="Helvetica 10 bold"
                    )
                    lbl_heal.grid(row=row + 1 , column=c, padx=5, pady=0)

                    ### Cdr ###
                    cool= float("{:.2f}".format(skill_dic[skill]['Cooldown']))
                    lbl_cdr = tk.Label(frm_skills, 
                    text = f"Cooldown: {cool}",
                    bg='#3f5946', fg="white", font="Helvetica 8 bold"
                    )
                    lbl_cdr.grid(row=row + 2, column=c, padx=5, pady=0)

                if skill_dic[skill]['type'] == 'debuff' :
                    img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((25, 25), Image.ANTIALIAS))
                    lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                    lbl_skill.img = img_skill 
                    lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                    CreateToolTip(lbl_skill, skill_dic[skill]['Skilltext'])
                    
                    deb = "Effect: " + str(skill_dic[skill]['Effect'])
                    lbl_debuff = tk.Label(frm_skills, 
                    text =  deb,
                    bg='#3f5946', fg="white", font="Helvetica 8 bold", justify='center', wraplength=100
                    )
                    lbl_debuff.grid(row=row + 1 , column=c, padx=5, pady=0)

                    ### Cdr ###
                    cool= float("{:.2f}".format(skill_dic[skill]['Cooldown']))
                    lbl_cdr = tk.Label(frm_skills, 
                    text = f"Cooldown: {cool}",
                    bg='#3f5946', fg="white", font="Helvetica 8 bold"
                    )
                    lbl_cdr.grid(row=row + 2, column=c, padx=5, pady=0)




##### Rebuild Stats Information #####

def rebuild_stats(*args):
    for labs in frm_stats.winfo_children():
        labs.destroy()
    
    lbl_dmg = tk.Label(master=frm_stats,  bg='#3f5946', fg="white" , text="Damage", font="Helvetica 10 bold")
    lbl_dmg.grid(row=0, column=0, padx=15, pady=5)
    dmg_numb = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
    dmg_numb["text"] = f"{Buff_Stats['Dmg']}"
    dmg_numb.config(width=5)
    dmg_numb.grid(row=0, column=1, padx=15, pady=5)

    for c in range(0,2,1):
        for r in range(1,13,1):
            col = c * 2
            row = r
            keyn = (((c + 1) * 12) - 12) + r
            if keyn < len(Buff_Stats.keys()):
                key = list(Buff_Stats.keys())[keyn]
                lbl_key = tk.Label(master=frm_stats, bg='#3f5946', fg="white", text=key, font="Helvetica 10 bold")
                lbl_key.grid(row=row, column=col, padx=5, pady=10)
                lbl_keyres = tk.Label(master=frm_stats, bg='#3f5946', fg="white", font="Helvetica 10 bold", text="")
                lbl_keyres["text"] = f"{Buff_Stats[key]}"
                lbl_keyres.config(width=5)
                lbl_keyres.grid(row=row, column=f"{col + 1}", padx=5, pady=10)

    

##################################################  

#### Save and retreive build definitions

def ask_save():
    global pop
    pop = tk.Toplevel(window)
    pop.title("Save Build")
    pop.geometry("400x150")
    pop.config(bg='#308a48')
    pop.attributes('-topmost', 'true')

    pop_lbl = tk.Label(pop, text="Choose your build name!",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946")
    pop_lbl.pack(pady=5)

    frame_save = tk.Frame(pop, bg="#3f5946")
    frame_save.pack()

    save_entry = tk.Entry(frame_save, width=15)
    save_entry.grid(row=0,column=0, sticky="w",padx=10)

    saveb = tk.Button(frame_save, 
    text="Save", 
    bg='#3f5946',
    fg='White',
    font="Helvetica 12 bold",
    command=lambda: save_build(save_entry.get())
    )
    saveb.grid(row=0, column=1, padx=10, pady=10)

def save_build(save_name):

    save_content = [clicked_c.get(), clicked_wep_p.get(), clicked_wep.get(), clicked_wep_s.get(), clicked_arm_p.get(), clicked_arm.get(), clicked_arm_s.get(), 
    clicked_acc_p.get(), clicked_acc.get(), clicked_acc_s.get(), clicked_off_p.get(), clicked_off.get(), clicked_off_s.get(), clicked_soul.get()]

    if os.path.exists('.\saves') == False :
        os.mkdir('.\saves')

    with open('.\saves\\'+ save_name +'.dat', 'w') as save:
        for i in save_content:
            save.write(i + '\n')

    pop.destroy()


def ask_load():
    global pops
    pops = tk.Toplevel(window)
    pops.title("Load Build")
    pops.geometry("400x150")
    pops.config(bg='#308a48')
    pops.attributes('-topmost', 'true')

    pops_lbl = tk.Label(pops, text="Choose the build name you want to load!",
    font="Helvetica 15 bold",
    fg="White",
    bg="#3f5946")
    pops_lbl.pack(pady=5)

    frame_load = tk.Frame(pops, bg="#3f5946")
    frame_load.pack()

    save_entry = tk.Entry(frame_load, width=15)
    save_entry.grid(row=0,column=0, sticky="w",padx=10)

    loadb = tk.Button(frame_load, 
    text="Load", 
    bg='#3f5946',
    fg='White',
    font="Helvetica 12 bold",
    command=lambda: load_build(save_entry.get())
    )
    loadb.grid(row=0, column=1, padx=10, pady=10)

def load_build(load_name):

    load_content = []

    if os.path.exists('.\saves\\'+ load_name +'.dat') == False :
        messagebox.showwarning(title="Load Error", message="Build save not found!")
    else:
        with open('.\saves\\'+ load_name +'.dat', 'r') as save:
            for i in save.readlines():
                line = i.rstrip()
                load_content.append(line)
        
        clicked_c.set(load_content[0])
        class_change()

        clicked_wep_p.set(load_content[1])
        clicked_wep.set(load_content[2])
        clicked_wep_s.set(load_content[3]) 
        clicked_arm_p.set(load_content[4]) 
        clicked_arm.set(load_content[5])
        clicked_arm_s.set(load_content[6])
        clicked_acc_p.set(load_content[7])
        clicked_acc.set(load_content[8])
        clicked_acc_s.set(load_content[9])
        clicked_off_p.set(load_content[10])
        clicked_off.set(load_content[11])
        clicked_off_s.set(load_content[12])
        clicked_soul.set(load_content[13])

        calculate()

        pops.destroy()
   

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

Buff_Stats={'Dmg': 0,'HP': 0,'Mana': 0,'Atk': 0,'Mag': 0,'Defense': 0,'Resist': 0,'Speed': 0,'Spell_Haste': 0,'Lifesteal': 0,'Tenacity': 0,'Crit': 0,'Luck': 0,
'Dodge': 0,'Fire': 0,'Water': 0,'Wind': 0,'Earth': 0,'Light': 0,'Dark': 0,'Threat': 0
}

s_var = {}

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

### Make a save button ###

mainmenu = tk.Menu(window)
mainmenu.add_command(label = "Save Build", command=lambda: ask_save())
mainmenu.add_command(label = "Load Build", command=lambda: ask_load())

window.config(menu = mainmenu)

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
    for c in range(0,5,1):
        row = (r * 3) - 3  
        k = (((r * 4) - 4) + c)

        if k < len(Skills[clicked_c.get()]):
            skill = list(Skills[clicked_c.get()].keys())[k]
            imgpath = Skills[clicked_c.get()][skill]['img']

            if Skills[clicked_c.get()][skill]['type'] == 'dmg' :
                img_skill = ImageTk.PhotoImage(Image.open(imgpath).resize((35, 35), Image.ANTIALIAS))
                lbl_skill = tk.Label(frm_skills, image=img_skill, bg='#3f5946')
                lbl_skill.img = img_skill 
                lbl_skill.grid(row=row, column=c, padx=10, pady=5)

                CreateToolTip(lbl_skill, Skills[clicked_c.get()][skill]['Skilltext'])

                 ### Dmg ###
                dmg= math.ceil(float("{:.1f}".format(Skills[clicked_c.get()][skill]['Dmg'])))
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

create_buff()

window.mainloop()