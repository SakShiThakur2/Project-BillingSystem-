from tkinter import*
from datetime import datetime
from tkinter import messagebox
import random,os,tempfile

def send_email():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('ERROR','Bill is empty')
    else:
        root1=Toplevel()
        root1.title('send gmail')
        root1.config(bg='steelblue2')
        root1.resizable(0,0)

        senderFrame=LabelFrame(root1,text='SENDER',font=("arial",16,'bold'),bg='steelblue2',fg='midnight blue')
        senderFrame.grid(row=0,column=0,padx=45,pady=25)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='steelblue2',fg='midnight blue')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bd=6,bg='steelblue2',fg='midnight blue')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=("arial",16,'bold'),bd=6,bg='steelblue2',fg='midnight blue')
        recipientFrame.grid(row=1,column=0,padx=45,pady=20)

        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bd=6,bg='steelblue2',fg='midnight blue')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bd=6,bg='steelblue2',fg='midnight blue')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_Textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_Textarea.grid(row=2,column=0,columnspan=2)
        email_Textarea.delete(1.0,END)
        email_Textarea.insert(END,textArea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t        '))

        sendButton=Button(root1,text="SEND",font=('arial',16,'bold'),width=15)
        sendButton.grid(row=2,column=0,pady=25)


        root1.mainloop()

def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file,'w').write(textArea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==Bill_noEntry.get():
            f = open(f'bills/{i}','r')
            textArea.delete(1.0,END)
            for data in f:
                textArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')



if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        try:
            bill_content = textArea.get(1.0, END)
            # Use 'utf-8' encoding to handle special characters like ₹
            with open(f'bills/{billnumber}.txt', 'w', encoding='utf-8') as file:
                file.write(bill_content)
            
            messagebox.showinfo('Success', f'Bill {billnumber} is saved successfully')
            billnumber = random.randint(0, 1000000)
        except Exception as e:
            messagebox.showerror('Error', f'Failed to save the bill: {e}')


billnumber=random.randint(0,1000000)

def bill_area():
    if PhoneEntry.get()=="":
        messagebox.showerror("Error","Customer Mobile No. Are Required !")
    
    elif cosPrice_Entry.get()=='' or grossPrice_Entry.get()=='' or coldDrink_Entry.get()=='':
        messagebox.showerror("Error","No Products Are Selected !")

    elif cosPrice_Entry.get()=='0 Rs' and grossPrice_Entry.get()=='0 Rs' and coldDrink_Entry.get()=='0 Rs':
        messagebox.showerror("Error","No Products Are Selected !")
    
    else:
        textArea.insert(END,"\t\t\tWELCOME CUSTOMER\n")
        textArea.insert(END,f'\n------------------------------------------------------------')
        textArea.insert(END,f'\nBill Number : {billnumber}')
        textArea.insert(END,f'\nCustomer Phone No. : {PhoneEntry.get()}')
        textArea.insert(END,f'\n============================================================')
        textArea.insert(END,'\nProduct \t\t\tQuantity \t\t\tPrice')
        textArea.insert(END,f'\n============================================================')

        if bathSoap_Entry.get()!='0':
            textArea.insert(END,f"\nBath Soap \t\t\t {bathSoap_Entry.get()} \t\t\t{bathSoap} Rs")
        if faceCream_Entry.get()!='0':
            textArea.insert(END,f"\nFace Cream \t\t\t {faceCream_Entry.get()} \t\t\t{faceCream} Rs")
        if faceWash_Entry.get()!='0':
            textArea.insert(END,f"\nFace Wash \t\t\t {faceWash_Entry.get()} \t\t\t{faceWash} Rs")
        if hairSpray_Entry.get()!='0':
            textArea.insert(END,f"\nHair Spray \t\t\t {hairSpray_Entry.get()} \t\t\t{hairSpray} Rs")
        if hairWash_Entry.get()!='0':
            textArea.insert(END,f"\nHair Wash \t\t\t {hairWash_Entry.get()} \t\t\t{hairWash} Rs")
        if bodyLotion_Entry.get()!='0':
            textArea.insert(END,f"\nBody Lotion \t\t\t {bodyLotion_Entry.get()} \t\t\t{bodyLotion} Rs")



        if Rice_Entry.get()!='0':
            textArea.insert(END,f"\nRice \t\t\t {Rice_Entry.get()} kg \t\t\t{Rice} Rs")
        if oil_Entry.get()!='0':
            textArea.insert(END,f"\nOil\t\t\t {oil_Entry.get()} \t\t\t{oil} Rs")
        if dall_Entry.get()!='0':
            textArea.insert(END,f"\nDall\t\t\t {dall_Entry.get()}kg \t\t\t{dall} Rs")
        if wheat_Entry.get()!='0':
            textArea.insert(END,f"\nWheat\t\t\t {wheat_Entry.get()}kg \t\t\t{wheat} Rs")
        if sugar_Entry.get()!='0':
            textArea.insert(END,f"\nSugar\t\t\t {sugar_Entry.get()}kg \t\t\t{sugar} Rs")
        if Tea_Entry.get()!='0':
            textArea.insert(END,f"\nTea\t\t\t {Tea_Entry.get()} \t\t\t{Tea} Rs")



        if Cola_Entry.get()!='0':
            textArea.insert(END,f"\nCoke \t\t\t {Cola_Entry.get()} \t\t\t{cola} Rs")
        if maza_Entry.get()!='0':
            textArea.insert(END,f"\nMaza \t\t\t {maza_Entry.get()} \t\t\t{maza} Rs")
        if Pepsi_Entry.get()!='0':
            textArea.insert(END,f"\nPepsi \t\t\t {Pepsi_Entry.get()} \t\t\t{Pepsi} Rs")
        if Sprite_Entry.get()!='0':
            textArea.insert(END,f"\nSprite \t\t\t {Sprite_Entry.get()} \t\t\t{Sprite} Rs")
        if Dew_Entry.get()!='0':
            textArea.insert(END,f"\nDew \t\t\t {Dew_Entry.get()} \t\t\t{Dew} Rs")
        if Frooti_Entry.get()!='0':
            textArea.insert(END,f"\nFrooti \t\t\t {Frooti_Entry.get()} \t\t\t{Frooti} Rs")
        
        
        textArea.insert(END,f'\n------------------------------------------------------------')
        if cosTax_Entry.get()!='0.0 Rs':
            textArea.insert(END,f'\nCosmetic Tax \t\t\t{cosTax_Entry.get()}')
        if grossTax_Entry.get()!='0.0 Rs':
            textArea.insert(END,f'\nGrocery Tax \t\t\t{grossTax_Entry.get()}')
        if coldTax_Entry.get()!='0.0 Rs':
            textArea.insert(END,f'\nCold Drink Tax \t\t\t{coldTax_Entry.get()}')
        textArea.insert(END,f'\n\nTotal Bill \t\t\t{total_bill}')
        textArea.insert(END,f'\n------------------------------------------------------------')
        save_bill()

    


def set_date():
    current_date_time = datetime.now().strftime("%d-%m-%Y , %H:%M:%S ")  # Format the date and time
    dateEntry.delete(0, END)  # Clear any existing text in the entry
    dateEntry.insert(0, current_date_time)  # Insert the current date and time

def total():
    global bathSoap,faceCream,faceWash,hairSpray,hairWash,bodyLotion
    global Rice,oil,dall,wheat,sugar,Tea
    global cola,maza,Pepsi,Sprite,Dew,Frooti
    global cosTax_Entry,grossTax_Entry,coldTax_Entry
    global total_bill

    bathSoap=int(bathSoap_Entry.get())*20
    faceCream=int(faceCream_Entry.get())*150
    faceWash=int(faceWash_Entry.get())*100
    hairSpray=int(hairSpray_Entry.get())*180
    hairWash=int(hairWash_Entry.get())*200
    bodyLotion=int(bodyLotion_Entry.get())*250

    total_cos_price = bathSoap + faceCream + faceWash + hairSpray + hairWash+bodyLotion
    cosPrice_Entry.delete(0,END)
    cosPrice_Entry.insert(0,f'{total_cos_price:.2f} Rs')

    cosTax=total_cos_price*0.12    #0.12% tax on cosmatics
    cosTax_Entry.delete(0,END)
    cosTax_Entry.insert(0,f'{cosTax:.2f} Rs')

    Rice = float(Rice_Entry.get())*50
    oil = float(oil_Entry.get())*180
    dall = float(dall_Entry.get())*150
    wheat = float(wheat_Entry.get())*35
    sugar = float(sugar_Entry.get())*80
    Tea = int(Tea_Entry.get())*150

    total_gross_price = Rice + oil + dall + wheat + sugar + Tea
    grossPrice_Entry.delete(0,END)
    grossPrice_Entry.insert(0,f'{total_gross_price:.2f} Rs')

    grossTax=total_gross_price*0.05   #0.05% tax on grocery
    grossTax_Entry.delete(0,END)
    grossTax_Entry.insert(0,f'{grossTax:.2f} Rs')


    cola = int(Cola_Entry.get())*45
    maza = int(maza_Entry.get())*50
    Pepsi = int(Pepsi_Entry.get())*50
    Sprite = int(Sprite_Entry.get())*40
    Dew = int(Dew_Entry.get())*45
    Frooti = int(Frooti_Entry.get())*55


    total_drink_price = cola + maza + Pepsi + Sprite + Dew + Frooti
    coldDrink_Entry.delete(0,END)
    coldDrink_Entry.insert(0,f'{total_drink_price} Rs')

    coldDrinkTax = total_drink_price*0.08    #0.08% tax on cold drink
    coldTax_Entry.delete(0,END)
    coldTax_Entry.insert(0,f'{coldDrinkTax:.2f} Rs')

    total_bill = total_cos_price + cosTax + total_gross_price + grossTax + total_drink_price + coldDrinkTax
    


root =Tk()
root.title('BillEase (retail billing system)')   #title of the window
root.maxsize()
# root.geometry('1400x1470')       #change the size of widow so we use geometry method('widthxheight)
root.iconbitmap('BILLING_SYATEM/pay_cash_payment_money_dollar_bill_icon_143267.ico') #by default the icon is leaf so we change the icon using method iconbitmap
root.resizable(0,0)
#-------------          HEADING LABEL(BILL EASE)        ----------------------------------------------------
#add font ,background color,font color for text, than add border (bd)to label in x-direction
headingLabel=Label(root,text='BillEase (Retail Billing System)',
                   font=('times new roman',30,'bold'),bg='steel blue',fg='midnight blue',bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)       #position of label, so it simply add label in top fill=X is for completely fill label on x-axis


#----------------------------------                        CUSTOMER DETAILS LABEL FRAME         --------------------------------------------------------------------------:
customer_detail_frame=LabelFrame(root,text='Customer Details',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
customer_detail_frame.pack(fill=X,pady=5)

#<----------|     DATE TIME        |--------->
dateLabel=Label(customer_detail_frame,text='Date & Time',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
dateLabel.grid(row=0,column=0,padx=20)

#<----------|      DATE TIME       |---------->
dateEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=20)
dateEntry.grid(row=0,column=1,padx=8)

set_date()
#<----------|     PHONE       |---------->
PhoneLabel=Label(customer_detail_frame,text='Phone No.',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
PhoneLabel.grid(row=0,column=2,padx=20,pady=2)

#<----------|     PHONE ENTRY     |---------->
PhoneEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=20)
PhoneEntry.grid(row=0,column=3,padx=8)

#<----------|     BILL_NO     |---------->
Bill_noLabel=Label(customer_detail_frame,text='Bill No.',font=('times new roman',14,'bold'),bg='light goldenrod',fg='brown')
Bill_noLabel.grid(row=0,column=4,padx=20,pady=2)

#<----------|     BILL_NO ENTRY       |---------->
Bill_noEntry=Entry(customer_detail_frame,font=('arial',16),bd=8,width=20)
Bill_noEntry.grid(row=0,column=5,padx=8)

#<----------|     SEARCH BUTTON       |---------->
searchButton=Button(customer_detail_frame,text='SEARCH',font=('arial',11,'bold'),bd=10,width=11,command=search_bill)
searchButton.grid(row=0,column=6,padx=35,pady=20)


#----------------------------------             COSMATICS LABEL FRAME         --------------------------------------------------:
productFrame=Frame(root)
productFrame.pack(pady=5)

cosmaticFrame=LabelFrame(productFrame,text='Cosmatics',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
cosmaticFrame.grid(row=0,column=0)
#....................................................... BATH SOAP ............................................................ 
bathSoapLabel=Label(cosmaticFrame,text='Soap',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
bathSoapLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

bathSoap_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
bathSoap_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
bathSoap_Entry.insert(0,0)

#........................................................FACE CREAM..........................................................
faceCreamLabel=Label(cosmaticFrame,text='Moisturizer',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
faceCreamLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

faceCream_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
faceCream_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
faceCream_Entry.insert(0,0)
#........................................................FACE WASH..........................................................
faceWashLabel=Label(cosmaticFrame,text='Face Wash',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
faceWashLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

faceWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
faceWash_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
faceWash_Entry.insert(0,0)
#........................................................HAIR COLOR..........................................................
hairSprayLabel=Label(cosmaticFrame,text='Hair Color',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
hairSprayLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

hairSpray_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
hairSpray_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
hairSpray_Entry.insert(0,0)
#........................................................Shampoo ..........................................................
hairWashLabel=Label(cosmaticFrame,text='Shampoo',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
hairWashLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

hairWash_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
hairWash_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
hairWash_Entry.insert(0,0)
#........................................................BODY LOTION..........................................................
bodyLotionLabel=Label(cosmaticFrame,text='Body Lotion',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
bodyLotionLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

bodyLotion_Entry=Entry(cosmaticFrame,font=('times new roman',13,'bold'),width=11,bd=5)
bodyLotion_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')
bodyLotion_Entry.insert(0,0)



# ------------------------------------------------        Grocery     ---------------------------------------------------------------------     

grossFrame=LabelFrame(productFrame,text='Grocery',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
grossFrame.grid(row=0,column=1)
#.......................................................    RICE    ............................................................ 
RiceLabel=Label(grossFrame,text='Rice (kg)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
RiceLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

Rice_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Rice_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
Rice_Entry.insert(0,0)

# #........................................................ OIL ..........................................................
oilLabel=Label(grossFrame,text='Oil (Pack)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
oilLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

oil_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
oil_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
oil_Entry.insert(0,0)

# #........................................................ DALL ..........................................................
dallLabel=Label(grossFrame,text='Dall (kg)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
dallLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

dall_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
dall_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
dall_Entry.insert(0,0)

# #........................................................      WHEAT   ..........................................................
wheatLabel=Label(grossFrame,text='Wheat (kg)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
wheatLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

wheat_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
wheat_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
wheat_Entry.insert(0,0)
# #........................................................     SUGAR   ..........................................................
sugarLabel=Label(grossFrame,text='Sugar (kg)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
sugarLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

sugar_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
sugar_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
sugar_Entry.insert(0,0)
# #........................................................     TEA     ..........................................................
TeaLabel=Label(grossFrame,text='Tea (Pack)',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
TeaLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

Tea_Entry=Entry(grossFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Tea_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')
Tea_Entry.insert(0,0)




# -----------------------------------------------         DRINK   -------------------------------------------------------------

drinkFrame=LabelFrame(productFrame,text='Cold Drinks',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
drinkFrame.grid(row=0,column=2)
#.......................................................    COCA COLA    ............................................................ 
ColaLabel=Label(drinkFrame,text='Coke',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
ColaLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')

Cola_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Cola_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')
Cola_Entry.insert(0,0)
#.......................................................    MAZA    ............................................................ 
mazaLabel=Label(drinkFrame,text='Maza',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
mazaLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')

maza_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
maza_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')
maza_Entry.insert(0,0)
#.......................................................    PEPSI    ............................................................ 
PepsiLabel=Label(drinkFrame,text='Pepsi',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
PepsiLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')

Pepsi_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Pepsi_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')
Pepsi_Entry.insert(0,0)

#.......................................................    SPRITE    ............................................................ 
SpriteLabel=Label(drinkFrame,text='Sprite',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
SpriteLabel.grid(row=3,column=0,pady=10,padx=20,sticky='w')

Sprite_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Sprite_Entry.grid(row=3,column=1,pady=10,padx=20,sticky='w')
Sprite_Entry.insert(0,0)
#.......................................................    DEW    ............................................................ 
DewLabel=Label(drinkFrame,text='Dew',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
DewLabel.grid(row=4,column=0,pady=10,padx=20,sticky='w')

Dew_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Dew_Entry.grid(row=4,column=1,pady=10,padx=20,sticky='w')
Dew_Entry.insert(0,0)
#.......................................................    FROOTI    ............................................................ 
FrootiLabel=Label(drinkFrame,text='Frooti',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
FrootiLabel.grid(row=5,column=0,pady=10,padx=20,sticky='w')

Frooti_Entry=Entry(drinkFrame,font=('times new roman',13,'bold'),width=11,bd=5)
Frooti_Entry.grid(row=5,column=1,pady=10,padx=20,sticky='w')
Frooti_Entry.insert(0,0)

# ******************************************        BILL FRAME          *********************************************************

billFrame=Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=15)

billareaLabel=Label(billFrame,text="Bill Area",font=('times new roman',15,'bold'),bd=8,relief=GROOVE)
billareaLabel.pack(fill=X)


scrollbar=Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)


textArea=Text(billFrame,height=18,width=60,yscrollcommand=scrollbar.set)
textArea.pack()
scrollbar.config(command=textArea.yview)


BillMenueFrame=LabelFrame(root,text='Bill Menu',
                                 font=('times new roman',16,'bold'),fg='dark blue',bd=10,relief=GROOVE,bg='light goldenrod')
BillMenueFrame.pack()

cosPriceLabel=Label(BillMenueFrame,text='Cosmatic Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
cosPriceLabel.grid(row=0,column=0,pady=10,padx=20,sticky='w')
cosPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
cosPrice_Entry.grid(row=0,column=1,pady=10,padx=20,sticky='w')

grossPriceLabel=Label(BillMenueFrame,text='Grocery Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
grossPriceLabel.grid(row=1,column=0,pady=10,padx=20,sticky='w')
grossPrice_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
grossPrice_Entry.grid(row=1,column=1,pady=10,padx=20,sticky='w')

coldDrinkLabel=Label(BillMenueFrame,text='Cold Drink Price',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
coldDrinkLabel.grid(row=2,column=0,pady=10,padx=20,sticky='w')
coldDrink_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
coldDrink_Entry.grid(row=2,column=1,pady=10,padx=20,sticky='w')

cosTaxLabel=Label(BillMenueFrame,text='Cosmatic Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
cosTaxLabel.grid(row=0,column=2,pady=10,padx=20,sticky='w')
cosTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
cosTax_Entry.grid(row=0,column=3,pady=10,padx=20,sticky='w')

grossTaxLabel=Label(BillMenueFrame,text='Grocery Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
grossTaxLabel.grid(row=1,column=2,pady=10,padx=20,sticky='w')
grossTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
grossTax_Entry.grid(row=1,column=3,pady=10,padx=20,sticky='w')

coldTaxLabel=Label(BillMenueFrame,text='Cold Drink Tax',
                                 font=('times new roman',13,'bold'),fg='brown',bd=0,relief=GROOVE,bg='light goldenrod')
coldTaxLabel.grid(row=2,column=2,pady=10,padx=20,sticky='w')
coldTax_Entry=Entry(BillMenueFrame,font=('times new roman',13,'bold'),width=14,bd=5)
coldTax_Entry.grid(row=2,column=3,pady=10,padx=20,sticky='w')

buttonFrame=Frame(BillMenueFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton = Button(buttonFrame,text="Total",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=8,pady=5,command=total)
totalButton.grid(row=0,column=0,pady=10,padx=5)

billButton = Button(buttonFrame,text="Bill",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5,command=bill_area)
billButton.grid(row=0,column=1,pady=10,padx=5)

emailButton = Button(buttonFrame,text="Email",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=8,pady=5,command=send_email)
emailButton.grid(row=0,column=2,pady=10,padx=5)

printButton = Button(buttonFrame,text="Print",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=7,pady=5,command=print_bill)
printButton.grid(row=0,column=3,pady=10,padx=5)

clearButton = Button(buttonFrame,text="Clear",font=('arial',18,'bold'),bg='light goldenrod',fg='brown',bd=2,width=8,pady=5)
clearButton.grid(row=0,column=4,pady=10,padx=5)

root.mainloop()   # it move vry fast so it help to viewing our window

