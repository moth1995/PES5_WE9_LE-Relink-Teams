from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from tkinter import ttk

def read_data(file_to_read,pos,grab):
    with open(file_to_read,"rb") as opened_file:
        opened_file.seek(pos,0)
        grabed_data=opened_file.read(grab)
    return grabed_data

def to_dec(var):
    var1=int.from_bytes(var,"little")
    return var1

def tobytes(import_var):
    import_var1=(import_var).to_bytes(4,byteorder="little")
    return import_var1

def tobytes2(import_var):
    import_var1=(import_var).to_bytes(2,byteorder="little")
    return import_var1

def make_backup():
    with open(root.filename,"rb") as rf_exe:
        chunk_size=4096
        with open(Path(root.filename).stem+".bak","wb") as wf_exe:
            rf_exe_chunk = rf_exe.read(chunk_size)
            while len(rf_exe_chunk) >0:
                wf_exe.write(rf_exe_chunk)
                rf_exe_chunk = rf_exe.read(chunk_size)

def find_index(elem,vec):
    if elem in vec:
        return vec.index(elem)

def get_key_by_value(decval,diclo):
    z=""
    for i, j in diclo.items():
        if j == decval:
            #print(i)
            z=i
    return z

def save_changes():
    if root.filename=="":
        messagebox.showerror(title=app_name, message="Seleccione un PES5/WE9/LE.exe")
    else:
        if backup_check.get():
            make_backup()
        try:
            with open(root.filename,"r+b") as opened_file:
                start_teamid=[
                    mycmb_0.get(),mycmb_1.get(),mycmb_2.get(),mycmb_3.get(),mycmb_4.get(),mycmb_5.get(),mycmb_6.get(),mycmb_7.get(),mycmb_8.get(),mycmb_9.get(),
                    mycmb_10.get(),mycmb_11.get(),mycmb_12.get(),mycmb_13.get(),mycmb_14.get(),mycmb_15.get(),mycmb_16.get(),mycmb_17.get(),mycmb_18.get(),
                    mycmb_19.get(),mycmb_20.get(),mycmb_21.get(),mycmb_22.get(),mycmb_23.get()
                    ]
                end_teamid=[
                    mycmb_24.get(),mycmb_25.get(),mycmb_26.get(),mycmb_27.get(),mycmb_28.get(),mycmb_29.get(),mycmb_30.get(),mycmb_31.get(),mycmb_32.get(),
                    mycmb_33.get(),mycmb_34.get(),mycmb_35.get(),mycmb_36.get(),mycmb_37.get(),mycmb_38.get(),mycmb_39.get(),mycmb_40.get(),mycmb_41.get(),
                    mycmb_42.get(),mycmb_43.get(),mycmb_44.get(),mycmb_45.get(),mycmb_46.get(),mycmb_47.get()
                    ]
                #exhibition
                offset=0x80F680
                #play again with differents teams
                offset2=0x98E5A0
                if Path(root.filename).stat().st_size ==22793412:
                    offset=0x74CE40
                    offset2=0x8CB8A0
                for i in range(0, len(start_teamid)): 
                    start_teamid[i] = tobytes(int(start_teamid[i])) 
                    opened_file.seek(offset+(i*0x8),0)
                    opened_file.write(start_teamid[i])
                    opened_file.seek(offset2+(i*0x8),0)
                    opened_file.write(start_teamid[i])
                for i in range(0, len(end_teamid)): 
                    end_teamid[i] = tobytes(int(end_teamid[i])) 
                    opened_file.seek(offset+(i*0x8)+4,0)
                    opened_file.write(end_teamid[i])
                    opened_file.seek(offset2+(i*0x8)+4,0)
                    opened_file.write(end_teamid[i])
                #now we write the strings names ids
                str_nameid=[
                    mycmb_48.get(),mycmb_49.get(),mycmb_50.get(),mycmb_51.get(),mycmb_52.get(),mycmb_53.get(),mycmb_54.get(),mycmb_55.get(),mycmb_56.get(),
                    mycmb_57.get(),mycmb_58.get(),mycmb_59.get(),mycmb_60.get(),mycmb_61.get(),mycmb_62.get(),mycmb_63.get(),mycmb_64.get(),mycmb_65.get(),
                    mycmb_66.get(),mycmb_67.get(),mycmb_68.get(),mycmb_69.get(),mycmb_70.get()
                    ]
                offset=0x80F5B0
                offset2=0x98E4D0
                if Path(root.filename).stat().st_size ==22793412:
                    offset=0x74CD70
                    offset2=0x8CB7D0
                for i in range(0, len(str_nameid)): 
                    str_nameid[i] = tobytes2(int(str_nameid[i])) 
                    opened_file.seek(offset+(i*0x4),0)
                    opened_file.write(str_nameid[i])
                    extra=b'\x66\x00'
                    if str_nameid[i]==b'\xFF\xFF' or str_nameid[i]==b'\xFE\xFF' :
                        extra=b'\xFF\xFF'
                    opened_file.seek(offset+(i*0x4)+2,0)
                    opened_file.write(extra)
                #print ((str_nameid))

                logos_ids=[
                    mycmb_71.get(),mycmb_72.get(),mycmb_73.get(),mycmb_74.get(),mycmb_75.get(),mycmb_76.get(),mycmb_77.get(),mycmb_78.get(),mycmb_79.get(),
                    mycmb_80.get(),mycmb_81.get(),mycmb_82.get(),mycmb_83.get(),mycmb_84.get(),mycmb_85.get(),mycmb_86.get(),mycmb_87.get(),mycmb_88.get(),
                    mycmb_89.get(),mycmb_90.get(),mycmb_91.get(),mycmb_92.get(),mycmb_93.get(),mycmb_94.get()
                    ]
                offset=0x80F618
                offset2=0x98E538
                dict_logos=dict_logos_pes5
                if Path(root.filename).stat().st_size ==22793412:
                    offset=0x74CDD8
                    offset2=0x8CB838
                    dict_logos=dict_logos_we9le
                for i in range(0, len(logos_ids)): 
                    logos_ids[i] = tobytes(dict_logos.get(logos_ids[i]))
                    #print(logos_ids[i])
                    opened_file.seek(offset+(i*0x4),0)
                    opened_file.write(logos_ids[i])
                    opened_file.seek(offset2+(i*0x4),0)
                    opened_file.write(logos_ids[i])
                #print(dict_logos.get(logos_ids[6]))
                #print(tobytes(dict_logos.get(logos_ids[6])))
                #print(logos_ids)
                
                start_cl_teamid=[
                    mycmb_95.get(),mycmb_96.get()
                    ]
                end_cl_teamid=[
                    mycmb_97.get(),mycmb_98.get()
                    ]
                offset=0x80F750
                offset2=0x5C7000
                offset3=0x6BA1ED
                if Path(root.filename).stat().st_size ==22793412:
                    offset=0x74CF10
                    offset2=0x5C9570
                    offset3=0x6BC89D
                for i in range(0, len(start_cl_teamid)): 
                    start_cl_teamid[i] = tobytes(int(start_cl_teamid[i])) 
                    opened_file.seek(offset+(i*0x10),0)
                    opened_file.write(start_cl_teamid[i])
                    opened_file.seek(offset2+(i*0x10),0)
                    opened_file.write(start_cl_teamid[i])
                    opened_file.seek(offset3+(i*0x18),0)
                    opened_file.write(start_cl_teamid[i])
                #print ((start_cl_teamid))
                for i in range(0, len(end_cl_teamid)): 
                    end_cl_teamid[i] = tobytes(int(end_cl_teamid[i])) 
                    opened_file.seek(offset+(i*0x10)+4,0)
                    opened_file.write(end_cl_teamid[i])                
                    opened_file.seek(offset2+(i*0x10)+8,0)
                    opened_file.write(end_cl_teamid[i])
                    opened_file.seek(offset3+(i*0x18)+8,0)
                    opened_file.write(end_cl_teamid[i])
                edit_mode_startids=[mycmb_1.get(),mycmb_2.get(),mycmb_3.get(),mycmb_4.get(),mycmb_10.get(),mycmb_11.get(),mycmb_12.get(),mycmb_13.get(),mycmb_14.get(),mycmb_15.get(),
                mycmb_16.get(),mycmb_17.get()]
                edit_start_offset=[0x6BA038,0x6BA04E,0x6BA064,0x6BA088,0x6BA0D6,0x6BA0EC,0x6BA102,0x6BA118,0x6BA13C,0x6BA152,0x6BA168,0x6BA17E]
                0x26A5
                edit_mode_endids=[mycmb_24.get(),mycmb_25.get(),mycmb_26.get(),mycmb_27.get(),mycmb_28.get(),mycmb_34.get(),mycmb_35.get(),mycmb_36.get(),mycmb_37.get(),mycmb_38.get(),
                mycmb_39.get(),mycmb_40.get(),mycmb_41.get()]
                edit_end_offset=[0x6BA02D,0x6BA043,0X6BA059,0x6BA06F,0x6BA093,0x6BA0E1,0x6BA0F7,0x6BA10D,0x6BA123,0x6BA147,0x6BA15D,0x6BA173,0x6BA189]
                for i in range (0,12):
                    edit_mode_startids[i] = tobytes(int(edit_mode_startids[i]))
                    opened_file.seek(edit_start_offset[i],0)
                    if Path(root.filename).stat().st_size ==22793412:
                        opened_file.seek(edit_start_offset[i]+0x26B0,0)
                    opened_file.write(edit_mode_startids[i])
                for i in range (0,13):
                    edit_mode_endids[i] = tobytes(int(edit_mode_endids[i]))
                    opened_file.seek(edit_end_offset[i],0)
                    if Path(root.filename).stat().st_size ==22793412:
                        opened_file.seek(edit_end_offset[i]+0x26B0,0)
                    opened_file.write(edit_mode_endids[i])
            messagebox.showinfo(title=app_name, message="Ok!")
            get_teams_locations()
            get_string_locations()
            get_logos_locations()
            get_classic_teams_locations()
        except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=app_name, message="Error al escribir en PES5/WE9/LE.exe\nejecute como administrador o revise los permisos")

def update_cmb_c_teams(lstct):
    mycmb_95.current(find_index(lstct[0],lst))
    mycmb_96.current(find_index(lstct[2],lst))
    mycmb_97.current(find_index(lstct[1],lst))
    mycmb_98.current(find_index(lstct[3],lst))

def update_cmb_logos(lstl,dicl):
    mycmb_71.current(find_index(get_key_by_value(lstl[0],dicl),cmb_logos_values))
    mycmb_72.current(find_index(get_key_by_value(lstl[1],dicl),cmb_logos_values))
    mycmb_73.current(find_index(get_key_by_value(lstl[2],dicl),cmb_logos_values))
    mycmb_74.current(find_index(get_key_by_value(lstl[3],dicl),cmb_logos_values))
    mycmb_75.current(find_index(get_key_by_value(lstl[4],dicl),cmb_logos_values))
    mycmb_76.current(find_index(get_key_by_value(lstl[5],dicl),cmb_logos_values))
    mycmb_77.current(find_index(get_key_by_value(lstl[6],dicl),cmb_logos_values))
    mycmb_78.current(find_index(get_key_by_value(lstl[7],dicl),cmb_logos_values))
    mycmb_79.current(find_index(get_key_by_value(lstl[8],dicl),cmb_logos_values))
    mycmb_80.current(find_index(get_key_by_value(lstl[9],dicl),cmb_logos_values))
    mycmb_81.current(find_index(get_key_by_value(lstl[10],dicl),cmb_logos_values))
    mycmb_82.current(find_index(get_key_by_value(lstl[11],dicl),cmb_logos_values))
    mycmb_83.current(find_index(get_key_by_value(lstl[12],dicl),cmb_logos_values))
    mycmb_84.current(find_index(get_key_by_value(lstl[13],dicl),cmb_logos_values))
    mycmb_85.current(find_index(get_key_by_value(lstl[14],dicl),cmb_logos_values))
    mycmb_86.current(find_index(get_key_by_value(lstl[15],dicl),cmb_logos_values))
    mycmb_87.current(find_index(get_key_by_value(lstl[16],dicl),cmb_logos_values))
    mycmb_88.current(find_index(get_key_by_value(lstl[17],dicl),cmb_logos_values))
    mycmb_89.current(find_index(get_key_by_value(lstl[18],dicl),cmb_logos_values))
    mycmb_90.current(find_index(get_key_by_value(lstl[19],dicl),cmb_logos_values))
    mycmb_91.current(find_index(get_key_by_value(lstl[20],dicl),cmb_logos_values))
    mycmb_92.current(find_index(get_key_by_value(lstl[21],dicl),cmb_logos_values))
    mycmb_93.current(find_index(get_key_by_value(lstl[22],dicl),cmb_logos_values))
    mycmb_94.current(find_index(get_key_by_value(lstl[23],dicl),cmb_logos_values))

def update_cmb_str(lsts):
    mycmb_48.current(find_index(lsts[0],lst_str))
    mycmb_49.current(find_index(lsts[1],lst_str))
    mycmb_50.current(find_index(lsts[2],lst_str))
    mycmb_51.current(find_index(lsts[3],lst_str))
    mycmb_52.current(find_index(lsts[4],lst_str))
    mycmb_53.current(find_index(lsts[5],lst_str))
    mycmb_54.current(find_index(lsts[6],lst_str))
    mycmb_55.current(find_index(lsts[7],lst_str))
    mycmb_56.current(find_index(lsts[8],lst_str))
    mycmb_57.current(find_index(lsts[9],lst_str))
    mycmb_58.current(find_index(lsts[10],lst_str))
    mycmb_59.current(find_index(lsts[11],lst_str))
    mycmb_60.current(find_index(lsts[12],lst_str))
    mycmb_61.current(find_index(lsts[13],lst_str))
    mycmb_62.current(find_index(lsts[14],lst_str))
    mycmb_63.current(find_index(lsts[15],lst_str))
    mycmb_64.current(find_index(lsts[16],lst_str))
    mycmb_65.current(find_index(lsts[17],lst_str))
    mycmb_66.current(find_index(lsts[18],lst_str))
    mycmb_67.current(find_index(lsts[19],lst_str))
    mycmb_68.current(find_index(lsts[20],lst_str))
    mycmb_69.current(find_index(lsts[21],lst_str))
    mycmb_70.current(find_index(lsts[22],lst_str))

def update_cmb(lstf):
    #start id
    mycmb_0.current(find_index(lstf[0],lst))
    mycmb_1.current(find_index(lstf[2],lst))
    mycmb_2.current(find_index(lstf[4],lst))
    mycmb_3.current(find_index(lstf[6],lst))
    mycmb_4.current(find_index(lstf[8],lst))
    mycmb_5.current(find_index(lstf[10],lst))
    mycmb_6.current(find_index(lstf[12],lst))
    mycmb_7.current(find_index(lstf[14],lst))
    mycmb_8.current(find_index(lstf[16],lst))
    mycmb_9.current(find_index(lstf[18],lst))
    mycmb_10.current(find_index(lstf[20],lst))
    mycmb_11.current(find_index(lstf[22],lst))
    mycmb_12.current(find_index(lstf[24],lst))
    mycmb_13.current(find_index(lstf[26],lst))
    mycmb_14.current(find_index(lstf[28],lst))
    mycmb_15.current(find_index(lstf[30],lst))
    mycmb_16.current(find_index(lstf[32],lst))
    mycmb_17.current(find_index(lstf[34],lst))
    mycmb_18.current(find_index(lstf[36],lst))
    mycmb_19.current(find_index(lstf[38],lst))
    mycmb_20.current(find_index(lstf[40],lst))
    mycmb_21.current(find_index(lstf[42],lst))
    mycmb_22.current(find_index(lstf[44],lst))
    mycmb_23.current(find_index(lstf[46],lst))
    #end id
    mycmb_24.current(find_index(lstf[1],lst))
    mycmb_25.current(find_index(lstf[3],lst))
    mycmb_26.current(find_index(lstf[5],lst))
    mycmb_27.current(find_index(lstf[7],lst))
    mycmb_28.current(find_index(lstf[9],lst))
    mycmb_29.current(find_index(lstf[11],lst))
    mycmb_30.current(find_index(lstf[13],lst))
    mycmb_31.current(find_index(lstf[15],lst))
    mycmb_32.current(find_index(lstf[17],lst))
    mycmb_33.current(find_index(lstf[19],lst))
    mycmb_34.current(find_index(lstf[21],lst))
    mycmb_35.current(find_index(lstf[23],lst))
    mycmb_36.current(find_index(lstf[25],lst))
    mycmb_37.current(find_index(lstf[27],lst))
    mycmb_38.current(find_index(lstf[29],lst))
    mycmb_39.current(find_index(lstf[31],lst))
    mycmb_40.current(find_index(lstf[33],lst))
    mycmb_41.current(find_index(lstf[35],lst))
    mycmb_42.current(find_index(lstf[37],lst))
    mycmb_43.current(find_index(lstf[39],lst))
    mycmb_44.current(find_index(lstf[41],lst))
    mycmb_45.current(find_index(lstf[43],lst))
    mycmb_46.current(find_index(lstf[45],lst))
    mycmb_47.current(find_index(lstf[47],lst))

def get_classic_teams_locations():
    count=0
    offset=0x80F750
    if Path(root.filename).stat().st_size ==22793412:
        offset=0x74CF10
    pos_c_teams=[]
    for count in range (2):
        x=to_dec(read_data(root.filename,offset+(count*0x10),0X4))
        pos_c_teams.append(x)
        y=to_dec(read_data(root.filename,offset+(count*0x10)+4,0X4))
        pos_c_teams.append(y)
    if pos_c_teams!=[]:
        #print(pos_c_teams)
        update_cmb_c_teams(pos_c_teams)

def get_logos_locations():
    count=0
    offset=0x80F618
    dict_logos=dict_logos_pes5
    if Path(root.filename).stat().st_size ==22793412:
        offset=0x74CDD8
        dict_logos=dict_logos_we9le
    pos_logos=[]
    for count in range (24):
        x=to_dec(read_data(root.filename,offset+(count*0x4),0X4))
        pos_logos.append(x)
    if pos_logos!=[]:        
        #print(pos_logos)
        #print(dict_logos)
        update_cmb_logos(pos_logos,dict_logos)

def get_string_locations():
    count=0
    offset=0x80F5B0
    if Path(root.filename).stat().st_size ==22793412:
        offset=0x74CD70
    pos_string=[]
    for count in range (23):
        x=to_dec(read_data(root.filename,offset+(count*0x4),0X2))
        pos_string.append(x)
    #print(pos_string)
    if pos_string!=[]:
        update_cmb_str(pos_string)

def get_teams_locations():
    count=0
    offset=0x80F680
    if Path(root.filename).stat().st_size ==22793412:
        offset=0x74CE40
    pos_teams=[]
    for count in range (48):
        x=to_dec(read_data(root.filename,offset+(count*0x4),0X4))
        pos_teams.append(x)
    #print(pos_teams)
    if pos_teams!=[]:
        update_cmb(pos_teams)

def search_exe():
    global my_label
    my_label.destroy()
    root.filename=filedialog.askopenfilename(initialdir=".",title="Select a file", filetypes=[("PES5/WE9/LE Executable", "*.exe"),("All files", "*.*")])
    if root.filename!='':
        #print(Path(root.filename).stat().st_size)
        my_label= Label(root, text=root.filename)
        my_label.place(x=5,y=480)
        get_teams_locations()
        get_string_locations()
        get_logos_locations()
        get_classic_teams_locations()
    else: # parent of IOError, OSError *and* WindowsError where available
        messagebox.showerror(title=app_name, message="Seleccione un PES5/WE9/LE.exe")

def close():
    root.destroy()

app_name="PES5/WE9/LE Relink Teams"
root = Tk()
root.title(app_name)
w = 700 # width for the Tk root
h = 500 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.filename=""
my_btn= Button(root, text="Selecciona el ejecutable \nPES5/WE9/LE.exe",command=search_exe)
my_btn1= Button(root, text="Guardar cambios",command=save_changes)
my_btn2= Button(root, text="Salir",command=close,width=11)
my_label= Label(root)
backup_check=IntVar()
checkbox_backup=Checkbutton(root, text="Hacer backup",variable=backup_check)

lst=list(range(222))
lst.append(234)
lst.append(4294967295)
#print(lst)
lst_str=list(range(153))
lst_str.append(65534)
lst_str.append(65535)
dict_logos_pes5={
"Europa A" :20087, 
"Europa B" :20086, 
"Africa" :20083, 
"America" :20084, 
"Asia" :20085, 
"No Logo" :4294967295, 
"Premier League" :20088, 
"Ligue 1" :20089, 
"Bundesliga" :20090, 
"Serie A" :20091, 
"Eredivisie" :20092, 
"Liga Española" :20093, 
"Otras A" :20094, 
"Otras B" :20095, 
"Liga Master" :20238    
}

dict_logos_we9le={
"Europa A" :20090, 
"Europa B" :20089, 
"Africa" :20086, 
"America" :20087, 
"Asia" :20088, 
"No Logo" :4294967295, 
"Premier League" :20091, 
"Ligue 1" :20092, 
"Bundesliga" :20093, 
"Serie A" :20094, 
"Eredivisie" :20095, 
"Liga Española" :20096, 
"Otras A" :20097, 
"Otras B" :20098, 
"Liga Master" :20235    
}

cmb_logos_values=list(dict_logos_pes5.keys())

#labels headers

mylbl_h1 = Label(root,text="Slot name")
mylbl_h2 = Label(root,text="Start team ID")
mylbl_h3 = Label(root,text="End team ID")
mylbl_h4 = Label(root,text="Name string ID")
mylbl_h5 = Label(root,text="Logo ID")
mylbl_h6 = Label(root,text="Classic teams start ID")
mylbl_h7 = Label(root,text="Classic teams end ID")

#labels for slots

mylbl_0 = Label(root,text="Europa A")
mylbl_1 = Label(root,text="Europa B")
mylbl_2 = Label(root,text="Africa")
mylbl_3 = Label(root,text="America")
mylbl_4 = Label(root,text="Asia")
mylbl_5 = Label(root,text="Secret A")
mylbl_6 = Label(root,text="Secret B")
mylbl_7 = Label(root,text="Secret C")
mylbl_8 = Label(root,text="Secret D")
mylbl_9 = Label(root,text="Secret E")
mylbl_10 = Label(root,text="Premier League")
mylbl_11 = Label(root,text="Ligue 1")
mylbl_12 = Label(root,text="Bundesliga")
mylbl_13 = Label(root,text="Serie A")
mylbl_14 = Label(root,text="Eredivisie")
mylbl_15 = Label(root,text="Liga Española")
mylbl_16 = Label(root,text="Otras A")
mylbl_17 = Label(root,text="Otras B")
mylbl_18 = Label(root,text="Secret F")
mylbl_19 = Label(root,text="Secret G")
mylbl_20 = Label(root,text="Secret H")
mylbl_21 = Label(root,text="Secret I")
mylbl_22 = Label(root,text="Secret J")
mylbl_23 = Label(root,text="Liga Master")

#combos

#start id

mycmb_0 = ttk.Combobox(root, value=lst,width=11)
mycmb_1 = ttk.Combobox(root, value=lst,width=11)
mycmb_2 = ttk.Combobox(root, value=lst,width=11)
mycmb_3 = ttk.Combobox(root, value=lst,width=11)
mycmb_4 = ttk.Combobox(root, value=lst,width=11)
mycmb_5 = ttk.Combobox(root, value=lst,width=11)
mycmb_6 = ttk.Combobox(root, value=lst,width=11)
mycmb_7 = ttk.Combobox(root, value=lst,width=11)
mycmb_8 = ttk.Combobox(root, value=lst,width=11)
mycmb_9 = ttk.Combobox(root, value=lst,width=11)
mycmb_10 = ttk.Combobox(root, value=lst,width=11)
mycmb_11 = ttk.Combobox(root, value=lst,width=11)
mycmb_12 = ttk.Combobox(root, value=lst,width=11)
mycmb_13 = ttk.Combobox(root, value=lst,width=11)
mycmb_14 = ttk.Combobox(root, value=lst,width=11)
mycmb_15 = ttk.Combobox(root, value=lst,width=11)
mycmb_16 = ttk.Combobox(root, value=lst,width=11)
mycmb_17 = ttk.Combobox(root, value=lst,width=11)
mycmb_18 = ttk.Combobox(root, value=lst,width=11)
mycmb_19 = ttk.Combobox(root, value=lst,width=11)
mycmb_20 = ttk.Combobox(root, value=lst,width=11)
mycmb_21 = ttk.Combobox(root, value=lst,width=11)
mycmb_22 = ttk.Combobox(root, value=lst,width=11)
mycmb_23 = ttk.Combobox(root, value=lst,width=11)


#end id

mycmb_24 = ttk.Combobox(root, value=lst,width=11)
mycmb_25 = ttk.Combobox(root, value=lst,width=11)
mycmb_26 = ttk.Combobox(root, value=lst,width=11)
mycmb_27 = ttk.Combobox(root, value=lst,width=11)
mycmb_28 = ttk.Combobox(root, value=lst,width=11)
mycmb_29 = ttk.Combobox(root, value=lst,width=11)
mycmb_30 = ttk.Combobox(root, value=lst,width=11)
mycmb_31 = ttk.Combobox(root, value=lst,width=11)
mycmb_32 = ttk.Combobox(root, value=lst,width=11)
mycmb_33 = ttk.Combobox(root, value=lst,width=11)
mycmb_34 = ttk.Combobox(root, value=lst,width=11)
mycmb_35 = ttk.Combobox(root, value=lst,width=11)
mycmb_36 = ttk.Combobox(root, value=lst,width=11)
mycmb_37 = ttk.Combobox(root, value=lst,width=11)
mycmb_38 = ttk.Combobox(root, value=lst,width=11)
mycmb_39 = ttk.Combobox(root, value=lst,width=11)
mycmb_40 = ttk.Combobox(root, value=lst,width=11)
mycmb_41 = ttk.Combobox(root, value=lst,width=11)
mycmb_42 = ttk.Combobox(root, value=lst,width=11)
mycmb_43 = ttk.Combobox(root, value=lst,width=11)
mycmb_44 = ttk.Combobox(root, value=lst,width=11)
mycmb_45 = ttk.Combobox(root, value=lst,width=11)
mycmb_46 = ttk.Combobox(root, value=lst,width=11)
mycmb_47 = ttk.Combobox(root, value=lst,width=11)

#combo string id

mycmb_48 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_49 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_50 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_51 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_52 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_53 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_54 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_55 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_56 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_57 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_58 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_59 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_60 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_61 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_62 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_63 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_64 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_65 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_66 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_67 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_68 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_69 = ttk.Combobox(root, value=lst_str,width=6)
mycmb_70 = ttk.Combobox(root, value=lst_str,width=6)

#combo logos id

mycmb_71 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_72 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_73 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_74 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_75 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_76 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_77 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_78 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_79 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_80 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_81 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_82 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_83 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_84 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_85 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_86 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_87 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_88 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_89 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_90 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_91 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_92 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_93 = ttk.Combobox(root, value=cmb_logos_values,width=15)
mycmb_94 = ttk.Combobox(root, value=cmb_logos_values,width=15)


#combo classics teams start id

mycmb_95 = ttk.Combobox(root, value=lst,width=11)
mycmb_96 = ttk.Combobox(root, value=lst,width=11)

#combo classics teams end id

mycmb_97 = ttk.Combobox(root, value=lst,width=11)
mycmb_98 = ttk.Combobox(root, value=lst,width=11)


#buttons position

my_btn.place(x=250,y=400)
checkbox_backup.place(x=400,y=410)
my_btn1.place(x=190,y=450)
my_btn2.place(x=350,y=450)


#header positioning

mylbl_h1.grid(row=0,column=0)
mylbl_h2.grid(row=0,column=1)
mylbl_h3.grid(row=0,column=2)
mylbl_h4.grid(row=0,column=3)
mylbl_h5.grid(row=0,column=4)
mylbl_h6.grid(row=0,column=5)
mylbl_h7.grid(row=0,column=6)

#labels positioning

mylbl_0.grid(row=1,column=0)
mylbl_1.grid(row=2,column=0)
mylbl_2.grid(row=3,column=0)
mylbl_3.grid(row=4,column=0)
mylbl_4.grid(row=5,column=0)
#mylbl_5.grid(row=6,column=0)
#mylbl_6.grid(row=7,column=0)
#mylbl_7.grid(row=8,column=0)
#mylbl_8.grid(row=9,column=0)
#mylbl_9.grid(row=10,column=0)
mylbl_10.grid(row=11,column=0)
mylbl_11.grid(row=12,column=0)
mylbl_12.grid(row=13,column=0)
mylbl_13.grid(row=14,column=0)
mylbl_14.grid(row=15,column=0)
mylbl_15.grid(row=16,column=0)
mylbl_16.grid(row=17,column=0)
mylbl_17.grid(row=18,column=0)
#mylbl_18.grid(row=19,column=0)
#mylbl_19.grid(row=20,column=0)
#mylbl_20.grid(row=21,column=0)
#mylbl_21.grid(row=22,column=0)
#mylbl_22.grid(row=23,column=0)
mylbl_23.grid(row=24,column=0)


#combo positioning

#start id

mycmb_0.grid(row=1,column=1)
mycmb_1.grid(row=2,column=1)
mycmb_2.grid(row=3,column=1)
mycmb_3.grid(row=4,column=1)
mycmb_4.grid(row=5,column=1)
#mycmb_5.grid(row=6,column=1)
#mycmb_6.grid(row=7,column=1)
#mycmb_7.grid(row=8,column=1)
#mycmb_8.grid(row=9,column=1)
#mycmb_9.grid(row=10,column=1)
mycmb_10.grid(row=11,column=1)
mycmb_11.grid(row=12,column=1)
mycmb_12.grid(row=13,column=1)
mycmb_13.grid(row=14,column=1)
mycmb_14.grid(row=15,column=1)
mycmb_15.grid(row=16,column=1)
mycmb_16.grid(row=17,column=1)
mycmb_17.grid(row=18,column=1)
#mycmb_18.grid(row=19,column=1)
#mycmb_19.grid(row=20,column=1)
#mycmb_20.grid(row=21,column=1)
#mycmb_21.grid(row=22,column=1)
#mycmb_22.grid(row=23,column=1)
mycmb_23.grid(row=24,column=1)


#end id

mycmb_24.grid(row=1,column=2)
mycmb_25.grid(row=2,column=2)
mycmb_26.grid(row=3,column=2)
mycmb_27.grid(row=4,column=2)
mycmb_28.grid(row=5,column=2)
#mycmb_29.grid(row=6,column=2)
#mycmb_30.grid(row=7,column=2)
#mycmb_31.grid(row=8,column=2)
#mycmb_32.grid(row=9,column=2)
#mycmb_33.grid(row=10,column=2)
mycmb_34.grid(row=11,column=2)
mycmb_35.grid(row=12,column=2)
mycmb_36.grid(row=13,column=2)
mycmb_37.grid(row=14,column=2)
mycmb_38.grid(row=15,column=2)
mycmb_39.grid(row=16,column=2)
mycmb_40.grid(row=17,column=2)
mycmb_41.grid(row=18,column=2)
#mycmb_42.grid(row=19,column=2)
#mycmb_43.grid(row=20,column=2)
#mycmb_44.grid(row=21,column=2)
#mycmb_45.grid(row=22,column=2)
#mycmb_46.grid(row=23,column=2)
mycmb_47.grid(row=24,column=2)

#combo string id

mycmb_48.grid(row=1,column=3)
mycmb_49.grid(row=2,column=3)
mycmb_50.grid(row=3,column=3)
mycmb_51.grid(row=4,column=3)
mycmb_52.grid(row=5,column=3)
#mycmb_53.grid(row=6,column=3)
#mycmb_54.grid(row=7,column=3)
#mycmb_55.grid(row=8,column=3)
#mycmb_56.grid(row=9,column=3)
#mycmb_57.grid(row=10,column=3)
mycmb_58.grid(row=11,column=3)
mycmb_59.grid(row=12,column=3)
mycmb_60.grid(row=13,column=3)
mycmb_61.grid(row=14,column=3)
mycmb_62.grid(row=15,column=3)
mycmb_63.grid(row=16,column=3)
mycmb_64.grid(row=17,column=3)
mycmb_65.grid(row=18,column=3)
#mycmb_66.grid(row=19,column=3)
#mycmb_67.grid(row=20,column=3)
#mycmb_68.grid(row=21,column=3)
#mycmb_69.grid(row=22,column=3)
#mycmb_70.grid(row=23,column=3)


#combo string id

mycmb_71.grid(row=1,column=4)
mycmb_72.grid(row=2,column=4)
mycmb_73.grid(row=3,column=4)
mycmb_74.grid(row=4,column=4)
mycmb_75.grid(row=5,column=4)
#mycmb_76.grid(row=6,column=4)
#mycmb_77.grid(row=7,column=4)
#mycmb_78.grid(row=8,column=4)
#mycmb_79.grid(row=9,column=4)
#mycmb_80.grid(row=10,column=4)
mycmb_81.grid(row=11,column=4)
mycmb_82.grid(row=12,column=4)
mycmb_83.grid(row=13,column=4)
mycmb_84.grid(row=14,column=4)
mycmb_85.grid(row=15,column=4)
mycmb_86.grid(row=16,column=4)
mycmb_87.grid(row=17,column=4)
mycmb_88.grid(row=18,column=4)
#mycmb_89.grid(row=19,column=4)
#mycmb_90.grid(row=20,column=4)
#mycmb_91.grid(row=21,column=4)
#mycmb_92.grid(row=22,column=4)
#mycmb_93.grid(row=23,column=4)
mycmb_94.grid(row=24,column=4)

#combo classics teams start id

mycmb_95.grid(row=2,column=5)
mycmb_96.grid(row=4,column=5)

#combo classics teams end id

mycmb_97.grid(row=2,column=6)
mycmb_98.grid(row=4,column=6)


root.resizable(False, False)
root.mainloop()