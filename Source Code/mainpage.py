# project by -----------
# Pranesh Kulkarni
# Rucha Patil
# Aniket kesarkar
# Ankit lad 
# Tanmay Paratkar
# Avishkar kandhare

#-------------------------------------------------------
# Topic : Restaurant Management System using MySQL databases and Tkinter GUI
#---------------------------------------------------------

from tkinter import *
from tkinter import messagebox
import time
import smtplib
import mysql.connector
from dbConnect import DBConnect
import os
from openpyxl import Workbook


def software():

	def workspace1():

		root = Tk()
		localtime=str(time.asctime(time.localtime()))
		def exits():
			msg=messagebox.askyesno('Restaurant Management System','Do You Want To Exit ?')
			if msg:
				os._exit(1)

		def resets():
			txt_servicetax.delete('1.0',END)
			txt_subtotal.delete('1.0',END)
			txt_date.delete('1.0',END)
			txt_totalcost.delete('1.0',END)
			txt_totalprint.delete('1.0',END)
		def backs():
			root.destroy()
			software()

		def bills():
			a=(dal.get());
			if(a==""):
				a=0
				aemail=""
			else:
				a=200*int(a)
				astr=str(a)
				aemail='Dal Makhani -'+'    200    '+astr+'\n'
				txt_totalprint.insert('5.0',aemail)
			b=(roti.get());
			if(b==""):
				b=0
				bemail=""
			else:
				b=30*int(b)
				bstr=str(b)
				bemail='Butter Roti -'+'    30    '+bstr+'\n'
				txt_totalprint.insert('6.0',bemail)
			c =(rice.get());
			if(c==""):
				c=0
				cemail=""
			else:
				c=180*int(c)
				cstr=str(c)
				cemail='Rice -'+'    180    '+cstr+'\n'
				txt_totalprint.insert('7.0',cemail)
			d =(icecream.get());
			if(d==""):
				d=0
				demail=""
			else:
				d =50*int(d)
				dstr=str(d)
				demail='Vanila Ice-Cream -'+'    50    '+dstr+'\n'
				txt_totalprint.insert('8.0',demail)
			e =(milkshake.get());
			if(e==""):
				e=0
				eemail=""
			else:
				e =60*int(e)
				estr=str(e)
				eemail='Milkshake -'+'    60    '+estr+'\n'
				txt_totalprint.insert('9.0',eemail)
			f =(cola.get());
			if(f==""):
				f=0
				femail=""
			else:
				f =40*int(f)
				fstr=str(f)
				femail='Cola -'+'    40    '+fstr+'\n'
				txt_totalprint.insert('10.0',femail)
			g =(gulab.get());
			if(g==""):
				g=0
				gemail=""
			else:
				g =70*int(g)
				gstr=str(g)
				gemail='Gulab-Jamun -'+'    70    '+gstr+'\n'
				txt_totalprint.insert('11.0',gemail)
			h =(shrikhand.get());
			if(h==""):
				h=0
				hemail=""
			else:
				h =55*int(h)
				hstr=str(h)
				hemail='Shrikhand -'+'    55    '+hstr+'\n'
				txt_totalprint.insert('12.0',hemail)
			i =(pizza.get());
			if(i==""):
				i=0
				iemail=""
			else:
				i =199*int(i)
				istr=str(i)
				iemail='Pizza -'+'    199    '+istr+'\n'
				txt_totalprint.insert('13.0',iemail)
			j =(burger.get());
			if(j==""):
				j=0
				jemail=""
			else:
				j =72*int(j)
				jstr=str(j)
				jemail='Veg Burger -'+'    72    '+jstr+'\n'
				txt_totalprint.insert('14.0',jemail)
			k =(lavacake.get());
			if(k==""):
				k=0
				kemail=""
			else:
				k =86*int(k)
				kstr=str(k)
				kemail='Lava Cake -'+'    86    '+kstr+'\n'
				txt_totalprint.insert('15.0',kemail)
			l =(coffee.get());
			if(l==""):
				l=0
				lemail=""
			else:
				l =45*int(l)
				lstr=str(l)
				lemail='Black Coffee -'+'    45    '+lstr+'\n'
				txt_totalprint.insert('16.0',lemail)
			m =(tea.get());
			if(m==""):
				m=0
				memail=""
			else:
				m =25*int(m)
				mstr=str(m)
				memail='Tea -'+'    25    '+mstr+'\n'
				txt_totalprint.insert('17.0',memail)
			n =(frenchfries.get());
			if(n==""):
				n=0
				nemail=""
			else:
				n =106*int(n)
				nstr=str(n)
				nemail='Frenchfries -'+'    106    '+nstr+'\n'
				txt_totalprint.insert('18.0',nemail)
			o =(pasta.get());
			if(o==""):
				o=0
				oemail=""
			else:
				o =520*int(o)
				ostr=str(o)
				oemail='Pasta -'+'    520    '+ostr+'\n'
				txt_totalprint.insert('19.0',oemail)
			p =(soup.get());
			if(p==""):
				p=0
				pemail=""
			else:
				p =70*int(p)
				pstr=str(p)
				pemail='Soup -'+'    70    '+pstr+'\n'
				txt_totalprint.insert('20.0',pemail)
			q =(gujaratithali.get());
			if(q==""):
				q=0
				qemail=""
			else:
				q =465*int(q)
				qstr=str(q)
				qemail='Gujarati Thali -'+'    465    '+qstr+'\n'
				txt_totalprint.insert('21.0',qemail)
			r =(punjabithali.get());
			if(r==""):
				r=0
				remail=""
			else:
				r =535*int(r)
				rstr=str(r)
				remail='Punjabi Thali -'+'    535    '+rstr+'\n'
				txt_totalprint.insert('22.0',remail)
			s =(Paneer.get());
			if(s==""):
				s=0
				semail=""
			else:
				s =210*int(s)
				sstr=str(s)
				semail='Paneer -'+'    210    '+sstr+'\n'
				txt_totalprint.insert('23.0',semail)
			dis=(txt_discount.get());
			if(dis==""):
				dis=0
				disemail=""
			else:
				dis=int(dis)
				disstr=str(dis)
				disemail='Discount(in %) -\t'+disstr+'\n'
				txt_totalprint.insert('24.0','----------------------------------------------------'+'\n')
				txt_totalprint.insert('27.0',disemail)


			email =(costname.get());
			email=str(email)
			receiptnumber=(receiptno.get());
			receiptnumber=str(receiptnumber)

			sum=a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s
			discount = (dis*sum)/100
			tax=(5*sum)/100
			totalcost=sum+tax-discount
			
			taxstr=str(tax)
			txt_servicetax.insert('1.0','Rs. \t'+taxstr)
			taxemail='Servicetax (in Rs.)-\t'+taxstr+'\n'

			totalcoststr=str(totalcost)
			txt_totalcost.insert('1.0','Rs. \t'+totalcoststr)
			totalcostemail='Total  (in Rs.)-\t'+totalcoststr+'\n'

			sumstr=str(sum)
			txt_subtotal.insert('1.0','Rs. \t'+sumstr)
			subtotalemail='Subtotal (in Rs.)-\t'+sumstr+'\n'

			txt_totalprint.insert('1.0','------Sample Hotel, Pune--------\n')
			txt_totalprint.insert('2.0',localtime+'\n')
			txt_totalprint.insert('3.0',email+'\n')
			txt_totalprint.insert('25.0',subtotalemail)
			txt_totalprint.insert('26.0',taxemail)
			txt_totalprint.insert('28.0','----------------------------------------------------'+'\n')
			txt_totalprint.insert('29.0',totalcostemail)
			txt_totalprint.insert('30.0','----------------------------------------------------'+'\n')

			#---------------------email module----------------
			if(email==""):
				messagebox.showerror('Restaurant Management System ','Kindly fill email address of Consumer')
			else :
				msg=messagebox.askyesno("Restaurant Management System","Do You Want To Proceed to payment?")
				if msg:
					header = 'To: '+email + '\n' + 'From: '+'restaurantmanager67@gmail.com \n'+ 'Subject: Restaurant Bill \n'
					contentpart1='-----------Sample Hotel------------\n'+'Receipt Number- \t'+receiptnumber+'\n'+localtime+'\n'+email+'\n'+'----------------\n'
					contentpart2=aemail+bemail+cemail+demail+eemail+femail+gemail+hemail+iemail+jemail+kemail+lemail+memail+nemail+oemail+pemail+qemail+remail+semail
					contentpart3='-----------------------------\n'+disemail+subtotalemail+taxemail+'----------------------\n'+totalcostemail+'\n\n Thank You Visit Again !!!'
					totcontaint=header+contentpart1+contentpart2+contentpart3
					mail= smtplib.SMTP('smtp.gmail.com',587)
					# host name is smtp.gmail.com and port number is 587
					mail.ehlo()
					# USed to identify client by server, prompting server for supported features
					mail.starttls()
					#Put the SMTP connection in TLS (Transport Layer Security) mode. to encode or enscript message 
					# because gmail doesn't allow any unsecure message transfer
					mail.login('restaurantmanager67@gmail.com','Pass@123')
					mail.sendmail('restaurantmanager67@gmail.com',email,totcontaint)
					mail.close()
					messagebox.showinfo("Restaurant Management System","Payment Successful !!!!")

					try:
						database = DBConnect(host='localhost',user='root',password='Pass@123', database='rest2019')
						new_user = {'Recieptnumber': receiptnumber,'email': email,'subtotal': sumstr,'discount': disstr,'totalcost': totalcoststr,'datei': localtime}
						database.insert(new_user,'newhotelpune')
						messagebox.showinfo('etax-2019','Data was entered successfully')
						root.destroy()
						workspace1()
					except:
						messagebox.showerror('Restaurant Management System','Error Occured while connecting to the server. Please contact your administrator')
						 

		font10 = "-family {Rockwell Extra Bold} -size 36 -weight bold "  \
		"-slant roman -underline 0 -overstrike 0"
		font16 = "-family Rockwell -size 12 -weight normal -slant " \
			"roman -underline 0 -overstrike 0"

		root.geometry("1566x835+-20+10")
		root.title("Restaurant Management System")
		root.configure(background="#777777")

		Frame1 = Frame(root)
		Frame1.place(relx=0.013, rely=0.024, relheight=0.102
		         , relwidth=0.699)
		Frame1.configure(background="#474747",width=1095,borderwidth="10",relief='ridge')


		Label1 =Label(Frame1)
		Label1.place(relx=0.055, rely=0.118, height=62, width=945)
		Label1.configure(background="#474747",font=font10,foreground="#fff23d",text='''Restaurant Management System''')

		Frame4 = Frame(root)
		Frame4.place(relx=0.715, rely=0.024, relheight=0.102
		                 , relwidth=0.259)
		Frame4.configure(background="#474747",borderwidth="10",relief='ridge')

		lab_workspace =Label(Frame4)
		lab_workspace.place(relx=0.099, rely=0.118, height=61, width=334)
		lab_workspace.configure(background="#474747",foreground="#fff23d",text='''WORKSPACE''',font=font10)

		Frame2_3 = Frame(root)
		Frame2_3.place(relx=0.332, rely=0.18, relheight=0.413
		         , relwidth=0.303)
		Frame2_3.configure(relief='ridge',borderwidth="10",background="#474747",width=475)
		 
		lab_dal = Label(Frame2_3)
		lab_dal.place(relx=0.063, rely=0.087, height=21, width=194)
		lab_dal.configure(background="#474747",foreground="aqua",font=font16,text='''Dal Makhani''')
		 
		dal = Entry(Frame2_3)
		dal.place(relx=0.632, rely=0.087,height=20, relwidth=0.303)
		dal.configure(background="white",foreground="red",font=font16)

		 
		lab_roti = Label(Frame2_3)
		lab_roti.place(relx=0.063, rely=0.203, height=21, width=194)
		lab_roti.configure(font=font16)
		lab_roti.configure(background="#474747",foreground="aqua",text='''Butter Roti''')
		 
		lab_rice = Label(Frame2_3)
		lab_rice.place(relx=0.063, rely=0.319, height=21, width=194)
		lab_rice.configure(background="#474747")
		lab_rice.configure(foreground="aqua")
		lab_rice.configure(text='''Rice''')
		lab_rice.configure(font=font16)

		lab_icecream = Label(Frame2_3)
		lab_icecream.place(relx=0.063, rely=0.435, height=21, width=194)
		lab_icecream.configure(background="#474747")
		lab_icecream.configure(foreground="aqua")
		lab_icecream.configure(text='''Vanila Ice-Cream''')
		lab_icecream.configure(font=font16)
		 
		lab_milkshake = Label(Frame2_3)
		lab_milkshake.place(relx=0.063, rely=0.551, height=21, width=194)
		lab_milkshake.configure(background="#474747")
		lab_milkshake.configure(foreground="aqua")
		lab_milkshake.configure(text='''Milkshake''')
		lab_milkshake.configure(font=font16)
		 
		lab_cola = Label(Frame2_3)
		lab_cola.place(relx=0.063, rely=0.667, height=21, width=194)
		lab_cola.configure(background="#474747")
		lab_cola.configure(foreground="aqua")
		lab_cola.configure(text='''Cola''')
		lab_cola.configure(font=font16)
		 
		lab_gulab = Label(Frame2_3)
		lab_gulab.place(relx=0.063, rely=0.783, height=21, width=194)
		lab_gulab.configure(background="#474747")
		lab_gulab.configure(foreground="aqua")
		lab_gulab.configure(text='''Gulab-Jamun''')
		lab_gulab.configure(font=font16)
		 
		lab_shrikhand = Label(Frame2_3)
		lab_shrikhand.place(relx=0.063, rely=0.899, height=21, width=194)
		lab_shrikhand.configure(background="#474747")
		lab_shrikhand.configure(foreground="aqua")
		lab_shrikhand.configure(text='''Shrikhand''')
		lab_shrikhand.configure(font=font16)
		 
		roti = Entry(Frame2_3)
		roti.place(relx=0.632, rely=0.203,height=20, relwidth=0.303)
		roti.configure(background="white")
		roti.configure(foreground="red")
		roti.configure(font = font16)

		rice = Entry(Frame2_3)
		rice.place(relx=0.632, rely=0.319,height=20, relwidth=0.303)
		rice.configure(background="white")
		rice.configure(foreground="red")
		rice.configure(font = font16)

		icecream = Entry(Frame2_3)
		icecream.place(relx=0.632, rely=0.435,height=20, relwidth=0.303)
		icecream.configure(background="white")
		icecream.configure(foreground="red")
		icecream.configure(font = font16)

		milkshake = Entry(Frame2_3)
		milkshake.place(relx=0.632, rely=0.551,height=20, relwidth=0.303)
		milkshake.configure(background="white")
		milkshake.configure(foreground="red")
		milkshake.configure(font = font16)

		cola = Entry(Frame2_3)
		cola.place(relx=0.632, rely=0.667,height=20, relwidth=0.303)
		cola.configure(background="white")
		cola.configure(foreground="red")
		cola.configure(font = font16)

		gulab = Entry(Frame2_3)
		gulab.place(relx=0.632, rely=0.783,height=20, relwidth=0.303)
		gulab.configure(background="white")
		gulab.configure(foreground="red")
		gulab.configure(font = font16)

		shrikhand = Entry(Frame2_3)
		shrikhand.place(relx=0.632, rely=0.899,height=20, relwidth=0.303)
		shrikhand.configure(background="white")
		shrikhand.configure(foreground="red")
		shrikhand.configure(font = font16)

		Frame2_4 = Frame(root)
		Frame2_4.place(relx=0.013, rely=0.79, relheight=0.174
		                 , relwidth=0.623)
		Frame2_4.configure(relief='ridge')
		Frame2_4.configure(borderwidth="10")
		Frame2_4.configure(background="#474747")
		Frame2_4.configure(width=975)
		 
		lab_servicetax = Label(Frame2_4)
		lab_servicetax.place(relx=0.021, rely=0.138, height=21, width=194)
		lab_servicetax.configure(background="#474747")
		lab_servicetax.configure(foreground="aqua")
		lab_servicetax.configure(font=font16)
		lab_servicetax.configure(text='''Service Tax''')
		 
		lab_discount = Label(Frame2_4)
		lab_discount.place(relx=0.021, rely=0.414, height=21, width=194)
		lab_discount.configure(background="#474747")
		lab_discount.configure(foreground="aqua")
		lab_discount.configure(font=font16)
		lab_discount.configure(text='''Discount (in %)''')
		 
		lab_totalcost = Label(Frame2_4)
		lab_totalcost.place(relx=0.544, rely=0.414, height=21, width=194)
		lab_totalcost.configure(background="#474747")
		lab_totalcost.configure(foreground="aqua")
		lab_totalcost.configure(font=font16)
		lab_totalcost.configure(text='''Total Cost''')
		
		txt_subtotal = Text(Frame2_4)
		txt_subtotal.place(relx=0.8, rely=0.138, relheight=0.166
		                 , relwidth=0.148)
		txt_subtotal.configure(background="white")
		txt_subtotal.configure(font=font16)
		txt_subtotal.configure(foreground="blue")

		txt_totalcost = Text(Frame2_4)
		txt_totalcost.place(relx=0.8, rely=0.414, relheight=0.166
		                 , relwidth=0.148)
		txt_totalcost.configure(background="white")
		txt_totalcost.configure(font=font16)
		txt_totalcost.configure(foreground="blue")
		 
		lab_subtotal = Label(Frame2_4)
		lab_subtotal.place(relx=0.544, rely=0.138, height=21, width=194)
		lab_subtotal.configure(background="#474747")
		lab_subtotal.configure(foreground="aqua")
		lab_subtotal.configure(font=font16)
		lab_subtotal.configure(text='''Subtotal''')
		 
		txt_servicetax = Text(Frame2_4)
		txt_servicetax.place(relx=0.308, rely=0.138, relheight=0.166
		                 , relwidth=0.148)
		txt_servicetax.configure(background="white")
		txt_servicetax.configure(font=font16)
		txt_servicetax.configure(foreground="blue")

		txt_discount = Entry(Frame2_4)
		txt_discount.place(relx=0.308, rely=0.414, relheight=0.166
		                 , relwidth=0.148)
		txt_discount.configure(background="white")
		txt_discount.configure(font=font16)
		txt_discount.configure(foreground="blue")

		Frame2_5 = Frame(root)
		Frame2_5.place(relx=0.702, rely=0.18, relheight=0.174
		                 , relwidth=0.22)
		Frame2_5.configure(relief='ridge')
		Frame2_5.configure(borderwidth="10")
		Frame2_5.configure(background="#474747")
		Frame2_5.configure(width=345)
		 
		Frame2_6 = Frame(Frame2_5)
		Frame2_6.place(relx=0.0, rely=0.0, relheight=0.007, relwidth=0.003)
		Frame2_6.configure(relief='ridge')
		Frame2_6.configure(borderwidth="10")
		Frame2_6.configure(background="#474747")
		Frame2_6.configure(width=475)

		lab_owner = Label(Frame2_5)
		lab_owner.place(relx=0.058, rely=0.138, height=21, width=304)
		lab_owner.configure(background="#474747")
		lab_owner.configure(foreground="aqua")
		lab_owner.configure(text='''Hotel Manager : Sample Sample''')
		lab_owner.configure(font=font16)
		 
		lab_hotelname = Label(Frame2_5)
		lab_hotelname.place(relx=0.058, rely=0.345, height=21, width=304)
		lab_hotelname.configure(background="#474747")
		lab_hotelname.configure(foreground="aqua")
		lab_hotelname.configure(text='''Sample Hotel''')
		 
		lab_address = Label(Frame2_5)
		lab_address.place(relx=0.058, rely=0.552, height=21, width=304)
		lab_address.configure(background="#474747")
		lab_address.configure(foreground="aqua")
		lab_address.configure(text='''Pune''')
		 
		lab_contact = Label(Frame2_5)
		lab_contact.place(relx=0.058, rely=0.759, height=21, width=304)
		lab_contact.configure(font=font16)
		lab_contact.configure(background="#474747")
		lab_contact.configure(foreground="aqua")
		lab_contact.configure(text='''Contact : 9999999999''')
		 
		Frame2_21 = Frame(root)
		Frame2_21.place(relx=0.651, rely=0.359, relheight=0.657
		                 , relwidth=0.316)
		Frame2_21.configure(relief='ridge')
		Frame2_21.configure(borderwidth="10")
		Frame2_21.configure(relief='ridge')
		Frame2_21.configure(background="#474747")
		 
		txt_totalprint = Text(Frame2_21)
		txt_totalprint.place(relx=0.04, rely=0.018, relheight=0.857
		                , relwidth=0.917)
		txt_totalprint.configure(background="white")
		txt_totalprint.configure(foreground="green")
		 
		btn_total = Button(Frame2_21)
		btn_total.place(relx=0.04, rely=0.92, height=34, width=107)
		btn_total.configure(background="green")
		btn_total.configure(foreground="white")
		btn_total.configure(text='''TOTAL''')
		btn_total.configure(command=bills)
		 
		btn_reset = Button(Frame2_21)
		btn_reset.place(relx=0.283, rely=0.92, height=34, width=97)
		btn_reset.configure(background="red")
		btn_reset.configure(foreground="white")
		btn_reset.configure(text='''RESET''')
		btn_reset.configure(command=resets)
		 
		btn_pay = Button(Frame2_21)
		btn_pay.place(relx=0.505, rely=0.92, height=34, width=107)
		btn_pay.configure(background="yellow")
		btn_pay.configure(foreground="black")
		btn_pay.configure(text='''BACK''',command=backs)

		btn_exit = Button(Frame2_21)
		btn_exit.place(relx=0.747, rely=0.92, height=34, width=107)
		btn_exit.configure(background="blue")
		btn_exit.configure(foreground="white")
		btn_exit.configure(text='''EXIT''')
		btn_exit.configure(width=107)
		btn_exit.configure(command=exits)
		 
		Frame2_4 = Frame(root)
		Frame2_4.place(relx=0.013, rely=0.18, relheight=0.581
		                 , relwidth=0.303)
		Frame2_4.configure(relief='ridge')
		Frame2_4.configure(borderwidth="10")
		Frame2_4.configure(relief='ridge')
		Frame2_4.configure(background="#474747")

		lab_pizza = Label(Frame2_4)
		lab_pizza.place(relx=0.063, rely=0.062, height=21, width=194)
		lab_pizza.configure(background="#474747")
		lab_pizza.configure(foreground="aqua")
		lab_pizza.configure(font=font16)
		lab_pizza.configure(text='''Pizza''')
		 
		pizza = Entry(Frame2_4)
		pizza.place(relx=0.632, rely=0.062,height=20, relwidth=0.303)
		pizza.configure(background="white")
		pizza.configure(font=font16)
		pizza.configure(foreground="red")
		pizza.configure(takefocus="0")
		 
		lab_burger = Label(Frame2_4)
		lab_burger.place(relx=0.063, rely=0.144, height=21, width=194)
		lab_burger.configure(background="#474747")
		lab_burger.configure(foreground="aqua")
		lab_burger.configure(font=font16)
		lab_burger.configure(text='''Veg Burger''')
		 
		lab_lavacake = Label(Frame2_4)
		lab_lavacake.place(relx=0.063, rely=0.227, height=21, width=194)
		lab_lavacake.configure(background="#474747")
		lab_lavacake.configure(foreground="aqua")
		lab_lavacake.configure(font=font16)
		lab_lavacake.configure(text='''Lava Cake''')
		 
		lab_coffee = Label(Frame2_4)
		lab_coffee.place(relx=0.063, rely=0.309, height=21, width=194)
		lab_coffee.configure(background="#474747")
		lab_coffee.configure(foreground="aqua")
		lab_coffee.configure(font=font16)
		lab_coffee.configure(text='''Black Coffee''')

		lab_tea = Label(Frame2_4)
		lab_tea.place(relx=0.063, rely=0.392, height=21, width=194)
		lab_tea.configure(background="#474747")
		lab_tea.configure(foreground="aqua")
		lab_tea.configure(font=font16)
		lab_tea.configure(text='''Tea''')
		 
		lab_frenchfries = Label(Frame2_4)
		lab_frenchfries.place(relx=0.063, rely=0.474, height=21, width=194)
		lab_frenchfries.configure(background="#474747")
		lab_frenchfries.configure(foreground="aqua")
		lab_frenchfries.configure(font=font16)
		lab_frenchfries.configure(text='''Frenchfries''')
		 
		lab_pasta = Label(Frame2_4)
		lab_pasta.place(relx=0.063, rely=0.557, height=21, width=194)
		lab_pasta.configure(font=font16)
		lab_pasta.configure(background="#474747")
		lab_pasta.configure(foreground="aqua")
		lab_pasta.configure(text='''Pasta''')
		 
		lab_soup = Label(Frame2_4)
		lab_soup.place(relx=0.063, rely=0.639, height=21, width=194)
		lab_soup.configure(background="#474747")
		lab_soup.configure(foreground="aqua")
		lab_soup.configure(font=font16)
		lab_soup.configure(text='''Tomato Soup''')
		 
		burger = Entry(Frame2_4)
		burger.place(relx=0.632, rely=0.144,height=20, relwidth=0.303)
		burger.configure(background="white")
		burger.configure(font=font16)
		burger.configure(foreground="red")
		 
		lavacake = Entry(Frame2_4)
		lavacake.place(relx=0.632, rely=0.227,height=20, relwidth=0.303)
		lavacake.configure(background="white")
		lavacake.configure(font=font16)
		lavacake.configure(foreground="red")
		 
		coffee = Entry(Frame2_4)
		coffee.place(relx=0.632, rely=0.309,height=20, relwidth=0.303)
		coffee.configure(background="white")
		coffee.configure(font=font16)
		coffee.configure(foreground="red")
		
		tea = Entry(Frame2_4)
		tea.place(relx=0.632, rely=0.392,height=20, relwidth=0.303)
		tea.configure(background="white")
		tea.configure(font=font16)
		tea.configure(foreground="red")
		 
		frenchfries = Entry(Frame2_4)
		frenchfries.place(relx=0.632, rely=0.474, height=20, relwidth=0.303)
		frenchfries.configure(background="white")
		frenchfries.configure(font=font16)
		frenchfries.configure(foreground="red")
		 
		pasta = Entry(Frame2_4)
		pasta.place(relx=0.632, rely=0.557,height=20, relwidth=0.303)
		pasta.configure(background="white")
		pasta.configure(font=font16)
		pasta.configure(foreground="red")
		 
		soup = Entry(Frame2_4)
		soup.place(relx=0.632, rely=0.639,height=20, relwidth=0.303)
		soup.configure(background="white")
		soup.configure(font=font16)
		soup.configure(foreground="red")
		 
		lab_gujaratithali = Label(Frame2_4)
		lab_gujaratithali.place(relx=0.063, rely=0.722, height=21
		                 , width=194)
		lab_gujaratithali.configure(background="#474747")
		lab_gujaratithali.configure(foreground="aqua")
		lab_gujaratithali.configure(font=font16)
		lab_gujaratithali.configure(text='''Gujarati Thali''')
		 
		lab_punjabithali = Label(Frame2_4)
		lab_punjabithali.place(relx=0.063, rely=0.804, height=21, width=194)
		lab_punjabithali.configure(background="#474747")
		lab_punjabithali.configure(foreground="aqua")
		lab_punjabithali.configure(font=font16)
		lab_punjabithali.configure(text='''Punjabi Thali''')
		 
		lab_Paneer = Label(Frame2_4)
		lab_Paneer.place(relx=0.063, rely=0.887, height=21, width=194)
		lab_Paneer.configure(background="#474747")
		lab_Paneer.configure(foreground="aqua")
		lab_Paneer.configure(font=font16)
		lab_Paneer.configure(text='''Paneer Makhani''')
		 
		gujaratithali = Entry(Frame2_4)
		gujaratithali.place(relx=0.632, rely=0.722, height=20
		                 , relwidth=0.303)
		gujaratithali.configure(background="white")
		gujaratithali.configure(font=font16)
		gujaratithali.configure(foreground="red")

		punjabithali = Entry(Frame2_4)
		punjabithali.place(relx=0.632, rely=0.804, height=20
		                 , relwidth=0.303)
		punjabithali.configure(background="white")
		punjabithali.configure(font=font16)
		punjabithali.configure(foreground="red")
		 
		Paneer = Entry(Frame2_4)
		Paneer.place(relx=0.632, rely=0.887,height=20, relwidth=0.303)
		Paneer.configure(background="white")
		Paneer.configure(font=font16)
		Paneer.configure(foreground="red")
		 
		Frame4_22 = Frame(root)
		Frame4_22.place(relx=0.332, rely=0.611, relheight=0.162
		                 , relwidth=0.303)
		Frame4_22.configure(relief='groove')
		Frame4_22.configure(borderwidth="10")
		Frame4_22.configure(relief='groove')
		Frame4_22.configure(background="#474747")
		 
		lab_costname = Label(Frame4_22)
		lab_costname.place(relx=0.063, rely=0.148, height=21, width=194)
		lab_costname.configure(background="#474747")
		lab_costname.configure(foreground="aqua")
		lab_costname.configure(font=font16)
		lab_costname.configure(text='''Consumer's Email :''')
		 
		lab_receiptno = Label(Frame4_22)
		lab_receiptno.place(relx=0.063, rely=0.444, height=21, width=194)
		lab_receiptno.configure(background="#474747")
		lab_receiptno.configure(foreground="aqua")
		lab_receiptno.configure(font=font16)
		lab_receiptno.configure(text='''Receipt Number :''')
		 
		lab_date = Label(Frame4_22)
		lab_date.place(relx=0.063, rely=0.741, height=21, width=194)
		lab_date.configure(background="#474747")
		lab_date.configure(foreground="aqua")
		lab_date.configure(font=font16)
		lab_date.configure(text='''Date :''')
		 
		costname = Entry(Frame4_22)
		costname.place(relx=0.547, rely=0.148,height=20, relwidth=0.408)
		costname.configure(background="white")
		costname.configure(font=font16)
		costname.configure(foreground="green")
		 
		receiptno = Entry(Frame4_22)
		receiptno.place(relx=0.547, rely=0.444,height=20, relwidth=0.408)
		receiptno.configure(background="white")
		receiptno.configure(font=font16)
		receiptno.configure(foreground="green")

		txt_date = Text(Frame4_22)
		txt_date.place(relx=0.547, rely=0.741,height=20, relwidth=0.408)
		txt_date.configure(background="white")
		txt_date.configure(insertbackground="green")
		txt_date.configure(foreground="green")
		txt_date.configure(width=194)
		txt_date.insert('1.0',localtime)
		txt_date.configure(state="disabled")


		root.mainloop()
#-------------------///////////////////////\\\\\\\\\\\\\\\\\\\\\\\---------------------------------------------------------

	def database1():
		root = Tk()
		font11 = "-family Calibri -size 18 -weight bold -slant roman "  \
		"-underline 0 -overstrike 0"
		font13 = "-family {Segoe UI} -size 19 -weight bold -slant "  \
		"roman -underline 0 -overstrike 0"
		font14 = "-family Rockwell -size 12 -weight normal -slant "  \
		"roman -underline 0 -overstrike 0"
		font15 = "-family {Rockwell Extra Bold} -size 12 -weight bold "  \
		"-slant roman -underline 0 -overstrike 0"
		font16 = "-family {Franklin Gothic Demi} -size 11 -weight "  \
		"normal -slant roman -underline 0 -overstrike 0"
		font9 = "-family {Rockwell Extra Bold} -size 40 -weight bold "  \
		"-slant roman -underline 0 -overstrike 0"
		font10= "-family {Segoe UI Semibold} -size 17 -weight bold"

		localtime=str(time.asctime(time.localtime()))
		def exits():
			msg=messagebox.askyesno('Restaurant Management System','Do you want to exit ?')
			if msg:
				os._exit(1)


		def clearalls():
			listbox.delete(0,END)

		def backs():
			root.destroy()
			software()


		def displays():
			findentry1=str(findentry.get('1.0',END));
			mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='rest2019')
			mycursor=mydb.cursor()
			query = ("SELECT Recieptnumber, email, subtotal, discount, totalcost, datei FROM newhotelpune WHERE Recieptnumber = "+findentry1)
			mycursor.execute(query)
			for(Recieptnumber, email, subtotal, discount, totalcost, datei) in mycursor:
				s="{}               {}               {}               {}               {}               {}".format(Recieptnumber, subtotal, discount, totalcost, datei, email)
				listbox.insert(0,s)

		def clears():
			listbox.delete(0,END)
			findentry.delete('1.0',END)

		def viewalls():
			mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='rest2019')
			mycursor=mydb.cursor()
			# This provides pointer in database that is mycurser
			query = ("SELECT Recieptnumber, email, subtotal, discount, totalcost, datei FROM newhotelpune")
			mycursor.execute(query)
			# Now all the data has been stored into mycurser in the form of tuple
			for(Recieptnumber, email, subtotal, discount, totalcost, datei) in mycursor:
				s="{}               {}               {}               {}               {}               {}".format(Recieptnumber, subtotal, discount, totalcost, datei, email)
				listbox.insert(0,s)

		def export_exel():
			try :
			    mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='rest2019')
			except :
			    messagebox.showerror('etax-2019','Failed to connect server, Please contact your administrator')

			mycursor=mydb.cursor()
			wb = Workbook()

			query = 'SELECT * from newhotelpune;'
			mycursor.execute(query)
			results = mycursor.fetchall()
			ws = wb.create_sheet(0)
			ws.title = 'NewHotelPune_data'
			ws.append(mycursor.column_names)
			for row in results:
			    ws.append(row)
			wb.save("newhotelpune.xlsx")
			messagebox.showinfo('Restaurant Management System ','Successfully Created Exel File. You Can Access the file from directory ')


				
		root.geometry("1566x835+-20+10")
		root.title("Restaurant Management System")
		root.configure(background="#777777")

		Frame1 = Frame(root)
		Frame1.place(relx=0.013, rely=0.034, relheight=0.097
		                , relwidth=0.686)
		Frame1.configure(relief='ridge')
		Frame1.configure(borderwidth="10")
		Frame1.configure(relief='ridge')
		Frame1.configure(background="#4c4c4c")
		Frame1.configure(width=1055)

		Label1 =Label(Frame1)
		Label1.place(relx=0.019, rely=0.118, height=58, width=1021)
		Label1.configure(background="#4c4c4c")
		Label1.configure(font=font9)
		Label1.configure(foreground="#f7ff14")
		Label1.configure(text='''Restaurant Management System''')

		Frame1_1 = Frame(root)
		Frame1_1.place(relx=0.728, rely=0.034, relheight=0.097
		                , relwidth=0.25)
		Frame1_1.configure(relief='ridge')
		Frame1_1.configure(borderwidth="10")
		Frame1_1.configure(background="#4c4c4c")

		Label1_1 = Label(Frame1_1)
		Label1_1.place(relx=0.078, rely=0.118, height=58, width=331)
		Label1_1.configure(background="#4c4c4c")
		Label1_1.configure(font=font9)
		Label1_1.configure(foreground="#f7ff14")
		Label1_1.configure(text='''Database''')

		Frame2 = Frame(root)
		Frame2.place(relx=0.02, rely=0.171, relheight=0.644, relwidth=0.679)
		Frame2.configure(relief='ridge')
		Frame2.configure(borderwidth="10")
		Frame2.configure(relief='ridge')
		Frame2.configure(background="#4c4c4c")

		listbox = Listbox(Frame2)
		listbox.place(relx=0.019, rely=0.080, relheight=0.888
		                , relwidth=0.961)
		listbox.configure(background="white")
		listbox.configure(borderwidth="10")
		listbox.configure(font=font16)
		listbox.configure(foreground="#1509bc")
		listbox.configure(relief='ridge')

		Frame3 = Frame(root)
		Frame3.place(relx=0.741, rely=0.182, relheight=0.165
		                , relwidth=0.205)
		Frame3.configure(relief='ridge')
		Frame3.configure(borderwidth="10")
		Frame3.configure(relief='ridge')
		Frame3.configure(background="#4c4c4c")

		Label3_7 = Label(Frame3)
		Label3_7.place(relx=0.159, rely=0.138, height=21, width=224)
		Label3_7.configure(background="#4c4c4c")
		Label3_7.configure(font=font14)
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''Manager : Sample Sample''')

		Label3_7 = Label(Frame3)
		Label3_7.place(relx=0.317, rely=0.345, height=21, width=124)
		Label3_7.configure(background="#4c4c4c")
		Label3_7.configure(font=font14)
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''Sample Hotel''')

		Label3_7 = Label(Frame3)
		Label3_7.place(relx=0.444, rely=0.552, height=21, width=54)
		Label3_7.configure(background="#4c4c4c")
		Label3_7.configure(font=font14)
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''Pune''')

		Label3_7 = Label(Frame3)
		Label3_7.place(relx=0.222, rely=0.759, height=21, width=194)
		Label3_7.configure(background="#4c4c4c")
		Label3_7.configure(font=font14)
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''Contact : 9999999999''')

		Frame4 = Frame(root)
		Frame4.place(relx=0.748, rely=0.467, relheight=0.473
		                , relwidth=0.205)
		Frame4.configure(relief='ridge')
		Frame4.configure(borderwidth="10")
		Frame4.configure(relief='ridge')
		Frame4.configure(background="#4c4c4c")

		Label2 = Label(Frame4)
		Label2.place(relx=0.317, rely=0.072, height=31, width=104)
		Label2.configure(background="#4c4c4c")
		Label2.configure(font=font13)
		Label2.configure(foreground="#fcfc12")
		Label2.configure(text='''Find Bill''')

		findentry = Text(Frame4)
		findentry.place(relx=0.032, rely=0.554,height=20, relwidth=0.902)
		findentry.configure(background="white")
		findentry.configure(font="TkFixedFont")
		findentry.configure(foreground="#000000")

		Label3 = Label(Frame4)
		Label3.place(relx=0.032, rely=0.458, height=21, width=154)
		Label3.configure(background="#4c4c4c")
		Label3.configure(font=font14)
		Label3.configure(foreground="aqua")
		Label3.configure(text='''receipt Number -''')

		Label3_6 = Label(Frame4)
		Label3_6.place(relx=0.032, rely=0.217, height=21, width=74)
		Label3_6.configure(background="#4c4c4c")
		Label3_6.configure(font=font14)
		Label3_6.configure(foreground="aqua")
		Label3_6.configure(text='''Date -''')

		txt_date = Text(Frame4)
		txt_date.place(relx=0.032, rely=0.313, relheight=0.058
		                , relwidth=0.902)
		txt_date.configure(background="white")
		txt_date.configure(font="TkTextFont")
		txt_date.configure(foreground="black")
		txt_date.insert('1.0',localtime)

		btn_display = Button(Frame4)
		btn_display.place(relx=0.095, rely=0.723, height=34, width=257)
		btn_display.configure(background="#12cccc")
		btn_display.configure(font=font15)
		btn_display.configure(foreground="#000000")
		btn_display.configure(text='''DISPLAY''',command= displays)

		Frame4_7 = Frame(Frame4)
		Frame4_7.place(relx=0.0, rely=0.0, relheight=0.002, relwidth=0.003)
		Frame4_7.configure(relief='ridge')
		Frame4_7.configure(borderwidth="10")
		Frame4_7.configure(background="#4c4c4c")

		Label2_8 = Label(Frame4_7)
		Label2_8.place(relx=0.0, rely=0.0, height=1, width=1)
		Label2_8.configure(background="#4c4c4c")
		Label2_8.configure(font=font13)
		Label2_8.configure(foreground="#fcfc12")
		Label2_8.configure(text='''Find Bill''')

		Label3_10 = Label(Frame4_7)
		Label3_10.place(relx=0.0, rely=0.0, height=1, width=1)
		Label3_10.configure(background="#4c4c4c")
		Label3_10.configure(font=font14)
		Label3_10.configure(foreground="aqua")
		Label3_10.configure(text='''receipt Number -''')

		Label3_7 = Label(Frame4_7)
		Label3_7.place(relx=0.0, rely=0.0, height=1, width=1)
		Label3_7.configure(background="#4c4c4c")
		Label3_7.configure(font=font14)
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''Date -''')

		btn_clear = Button(Frame4)
		btn_clear.place(relx=0.095, rely=0.867, height=34, width=257)
		btn_clear.configure(background="#12cccc")
		btn_clear.configure(font=font15)
		btn_clear.configure(foreground="#000000")
		btn_clear.configure(text='''CLEAR''',command= clears)

		Frame_btn = Frame(root)
		Frame_btn.place(relx=0.117, rely=0.843, relheight=0.074
		                , relwidth=0.471)
		Frame_btn.configure(relief='ridge')
		Frame_btn.configure(borderwidth="10")
		Frame_btn.configure(background="#4c4c4c")

		btn_viewall = Button(Frame_btn)
		btn_viewall.place(relx=0.055, rely=0.108, height=34, width=127)
		btn_viewall.configure(background="#19680c")
		btn_viewall.configure(font=font11)
		btn_viewall.configure(foreground="#ffffff")
		btn_viewall.configure(text='''VIEW ALL''',command=viewalls)

		btn_clearall = Button(Frame_btn)
		btn_clearall.place(relx=0.29, rely=0.108, height=34, width=137)
		btn_clearall.configure(background="#351fff")
		btn_clearall.configure(font=font11)
		btn_clearall.configure(foreground="#ffffff")
		btn_clearall.configure(text='''CLEAR''',command= clearalls)

		btn_back = Button(Frame_btn)
		btn_back.place(relx=0.552, rely=0.108, height=34, width=127)
		btn_back.configure(background="#ffff14")
		btn_back.configure(font=font11)
		btn_back.configure(foreground="#000000")
		btn_back.configure(text='''BACK''',command=backs)

		btn_exit = Button(Frame_btn)
		btn_exit.place(relx=0.786, rely=0.108, height=34, width=117)
		btn_exit.configure(background="#ff150d")
		btn_exit.configure(font=font11)
		btn_exit.configure(foreground="#ffffff")
		btn_exit.configure(text='''EXIT''',command= exits)

		Label1 = Label(root)
		Label1.place(relx=0.019, rely=0.137, height=21, width=84)
		Label1.configure(background="#727272")
		Label1.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1.configure(foreground="#f7ff14")
		Label1.configure(text='''Reciept No.''')

		Label1_1 = Label(root)
		Label1_1.place(relx=0.082, rely=0.137, height=21, width=64)
		Label1_1.configure(background="#727272")
		Label1_1.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1_1.configure(foreground="#f7ff14")
		Label1_1.configure(text='''Subtotal''')

		Label1_2 = Label(root)
		Label1_2.place(relx=0.417, rely=0.137, height=21, width=124)
		Label1_2.configure(background="#727272")
		Label1_2.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1_2.configure(foreground="#f7ff14")
		Label1_2.configure(text='''E-mail address''')

		Label1_3 = Label(root)
		Label1_3.place(relx=0.202, rely=0.137, height=21, width=84)
		Label1_3.configure(background="#727272")
		Label1_3.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1_3.configure(foreground="#f7ff14")
		Label1_3.configure(text='''Total Cost''')

		Label1_4 = Label(root)
		Label1_4.place(relx=0.133, rely=0.137, height=21, width=94)
		Label1_4.configure(background="#727272")
		Label1_4.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1_4.configure(foreground="#f7ff14")
		Label1_4.configure(text='''Discount (%)''')

		Label1_5 = Label(root)
		Label1_5.place(relx=0.285, rely=0.137, height=21, width=84)
		Label1_5.configure(background="#727272")
		Label1_5.configure(font="-family {Serifa BT} -size 11 -weight bold")
		Label1_5.configure(foreground="#f7ff14")
		Label1_5.configure(text='''Date''')

		btn_export = Button(root)
		btn_export.place(relx=0.599, rely=0.856, height=44, width=177)
		btn_export.configure(background="#227715")
		btn_export.configure(borderwidth="10")
		btn_export.configure(font=font10)
		btn_export.configure(foreground="#ffffff")
		btn_export.configure(text='''Export To Exel''',command=export_exel)
		root.mainloop()

#---------------------------------////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\--------------------------------------

	def support1():
		root = Tk()

		def submits():
			a=str(hotelname.get());
			b=str(code.get());
			c=str(emailadd.get());
			d=str(containt.get());
			totcontaint= a+"\n"+b+"\n"+c+"\n"+d 

			msg=messagebox.askyesno("Restaurant Management System","Do You Want To Submit ?")
			if msg:
				mail= smtplib.SMTP('smtp.gmail.com',587)
				mail.ehlo()
				mail.starttls()
				mail.login('restaurantmanager67@gmail.com','Pass@123')
				mail.sendmail('restaurantmanager67@gmail.com','restaurantmanager67@gmail.com',totcontaint)
				mail.close()
				messagebox.showinfo("Restaurant Management System","Your Responce is successfully recorded, Our support team will contact you soon !!!")
		def backs():
			root.destroy()
			software()


		def exits():
			msg=messagebox.askyesno("Restaurant Management System","Do You Want To EXIT ?")
			if msg:
				os._exit(1)

		root.geometry("1013x675+273+114")
		root.title("Restaurent Management System")
		root.configure(background="#ffa914")

		Frame1 = Frame(root)
		Frame1.place(relx=0.543, rely=0.178, relheight=0.333, relwidth=0.38)

		Frame1.configure(relief='ridge')
		Frame1.configure(borderwidth="10")
		Frame1.configure(relief='ridge')
		Frame1.configure(background="#ffa914")

		Label2 = Label(Frame1)
		Label2.place(relx=0.026, rely=0.0, height=36, width=142)
		Label2.configure(background="#d83d25")
		Label2.configure(font="-family {Segoe UI} -size 18 -weight bold")
		Label2.configure(foreground="#000000")
		Label2.configure(text='''Features:''')

		Label3 = Label(Frame1)
		Label3.place(relx=0.078, rely=0.178, height=26, width=332)
		Label3.configure(background="#ffa914")
		Label3.configure(foreground="#000000")
		Label3.configure(text='''1.Acccess Data Anywhere''')

		Label4 = Label(Frame1)
		Label4.place(relx=0.104, rely=0.311, height=26, width=322)
		Label4.configure(background="#ffa914")
		Label4.configure(foreground="#000000")
		Label4.configure(text='''2.Online Support''')

		Label5 = Label(Frame1)
		Label5.place(relx=0.13, rely=0.444, height=26, width=302)
		Label5.configure(background="#ffa914")
		Label5.configure(foreground="#000000")
		Label5.configure(text='''3.Email Receipt''')

		Label5_1 = Label(Frame1)
		Label5_1.place(relx=0.13, rely=0.578, height=26, width=322)
		Label5_1.configure(background="#ffa914")
		Label5_1.configure(foreground="#000000")
		Label5_1.configure(text='''4.Online Data Recovery''')

		Label5_2 = Label(Frame1)
		Label5_2.place(relx=0.182, rely=0.711, height=26, width=282)
		Label5_2.configure(background="#ffa914")
		Label5_2.configure(foreground="#000000")
		Label5_2.configure(text='''5.Easy to use''')

		Label1 = Label(root)
		Label1.place(relx=0.01, rely=0.015, height=56, width=992)
		Label1.configure(background="#369dd8")
		Label1.configure(font="-family {Segoe UI} -size 28 -weight bold -slant italic")
		Label1.configure(foreground="#000000")
		Label1.configure(text='''RESTAURANT MANAGEMENT SYSTEM''')

		Frame2 = Frame(root)
		Frame2.place(relx=0.464, rely=0.593, relheight=0.363
		        , relwidth=0.518)
		Frame2.configure(relief='ridge')
		Frame2.configure(borderwidth="10")
		Frame2.configure(relief='ridge')
		Frame2.configure(background="#ffa914")

		Label6 = Label(Frame2)
		Label6.place(relx=0.019, rely=0.041, height=36, width=202)
		Label6.configure(background="#d83d25")
		Label6.configure(font="-family {Segoe UI} -size 14 -weight bold")
		Label6.configure(foreground="#000000")
		Label6.configure(text='''::  Developers ::''')

		Label7 = Label(Frame2)
		Label7.place(relx=0.324, rely=0.204, height=26, width=202)
		Label7.configure(background="#ffa914")
		Label7.configure(foreground="#000000")
		Label7.configure(text='''::   Aniket Kesarkar  ::''')

		Label5_3 = Label(Frame2)
		Label5_3.place(relx=0.305, rely=0.327, height=26, width=212)
		Label5_3.configure(background="#ffa914")
		Label5_3.configure(foreground="#000000")
		Label5_3.configure(text='''::  Pranesh Kulkarni ::''')

		Label5_4 = Label(Frame2)
		Label5_4.place(relx=0.305, rely=0.449, height=26, width=212)
		Label5_4.configure(background="#ffa914")
		Label5_4.configure(foreground="#000000")
		Label5_4.configure(text='''::  Rucha Patil ::''')

		Label5_2 = Label(Frame2)
		Label5_2.place(relx=0.343, rely=0.571, height=26, width=172)
		Label5_2.configure(background="#ffa914")
		Label5_2.configure(foreground="#000000")
		Label5_2.configure(text='''::  Tanmay Paratkar  ::''')

		Label5_5 = Label(Frame2)
		Label5_5.place(relx=0.305, rely=0.694, height=26, width=212)
		Label5_5.configure(background="#ffa914")
		Label5_5.configure(foreground="#000000")
		Label5_5.configure(text='''::  Avishkar Kandhare  ::''')

		Label5_6 = Label(Frame2)
		Label5_6.place(relx=0.305, rely=0.816, height=26, width=212)
		Label5_6.configure(background="#ffa914")
		Label5_6.configure(foreground="#000000")
		Label5_6.configure(text=''':: Ankit Lad ::''')

		Frame1_2 = Frame(root)
		Frame1_2.place(relx=0.049, rely=0.193, relheight=0.778
		        , relwidth=0.38)
		Frame1_2.configure(relief='ridge')
		Frame1_2.configure(borderwidth="10")
		Frame1_2.configure(relief='ridge')
		Frame1_2.configure(background="#ffa914")

		Label2_3 = Label(Frame1_2)
		Label2_3.place(relx=0.026, rely=0.019, height=36, width=212)
		Label2_3.configure(background="#d83d25")
		Label2_3.configure(font="-family {Segoe UI} -size 18 -weight bold")
		Label2_3.configure(foreground="#000000")
		Label2_3.configure(text='''Online Support :''')

		emailadd = Entry(Frame1_2)
		emailadd.place(relx=0.078, rely=0.171,height=20, relwidth=0.868)
		emailadd.configure(background="white")
		emailadd.configure(font="TkFixedFont")
		emailadd.configure(foreground="#000000")

		containt = Entry(Frame1_2)
		containt.place(relx=0.052, rely=0.533,height=220, relwidth=0.894)
		containt.configure(background="white")
		containt.configure(font="TkFixedFont")
		containt.configure(foreground="#000000")

		Label8 = Label(Frame1_2)
		Label8.place(relx=0.078, rely=0.114, height=21, width=114)
		Label8.configure(background="#ffa914")
		Label8.configure(foreground="#000000")
		Label8.configure(text='''Your Email Address :''')

		Label9 = Label(Frame1_2)
		Label9.place(relx=0.078, rely=0.476, height=21, width=37)
		Label9.configure(background="#ffa914")
		Label9.configure(foreground="#000000")
		Label9.configure(text='''Help :''')

		Label10 = Label(Frame1_2)
		Label10.place(relx=0.078, rely=0.229, height=21, width=85)
		Label10.configure(background="#ffa914")
		Label10.configure(foreground="#000000")
		Label10.configure(text='''Product Code :''')

		code = Entry(Frame1_2)
		code.place(relx=0.078, rely=0.286,height=20, relwidth=0.868)
		code.configure(background="white")
		code.configure(font="TkFixedFont")
		code.configure(foreground="#000000")

		Label11 = Label(Frame1_2)
		Label11.place(relx=0.078, rely=0.362, height=21, width=76)
		Label11.configure(background="#ffa914")
		Label11.configure(foreground="#000000")
		Label11.configure(text='''Hotel Name :''')

		hotelname = Entry(Frame1_2)
		hotelname.place(relx=0.078, rely=0.419,height=20, relwidth=0.868)
		hotelname.configure(background="white")
		hotelname.configure(font="TkFixedFont")
		hotelname.configure(foreground="#000000")

		back_btn = Button(root)
		back_btn.place(relx=0.079, rely=0.119, height=34, width=67)
		back_btn.configure(background="#1c6d13")
		back_btn.configure(foreground="#ffffff")
		back_btn.configure(text='''BACK''',command= backs)

		exit_btn = Button(root)
		exit_btn.place(relx=0.188, rely=0.119, height=34, width=77)
		exit_btn.configure(background="#0b0696")
		exit_btn.configure(foreground="#ffffff")
		exit_btn.configure(text='''EXIT''', command= exits)

		btn_submit = Button(Frame1_2)
		btn_submit.place(relx=0.182, rely=0.914, height=24, width=227)
		btn_submit.configure(background="#4edd2a")
		btn_submit.configure(foreground="#000000")
		btn_submit.configure(text='''SUBMIT''',command = submits)


		root.mainloop()
#------------------------------------------------///////////////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\-----------------
	def about1():
		def menucard1():
			root.destroy()
			software()

		root = Tk()
		font11 = "-family {Script MT Bold} -size 17 -weight bold"
		font13 = "-family {Script MT Bold} -size 22 -weight bold"
		font15 = "-family {Rockwell Extra Bold} -size 15 -weight bold"
		font16 = "-family {Rockwell Extra Bold} -size 17 -weight bold"
		font9 = "-family {Rockwell Extra Bold} -size 30 -weight bold"

		root.geometry("1053x704+259+88")
		root.title("New rootlevel")
		root.configure(borderwidth="10")
		root.configure(relief="ridge")
		root.configure(background="#7a7a7a")

		Frame1 = Frame(root)
		Frame1.place(relx=0.038, rely=0.028, relheight=0.107
		        , relwidth=0.916)
		Frame1.configure(relief='ridge')
		Frame1.configure(borderwidth="10")
		Frame1.configure(relief='ridge')
		Frame1.configure(background="#444444")

		Label1 = Label(Frame1)
		Label1.place(relx=0.031, rely=0.133, height=43, width=880)
		Label1.configure(background="#444444")
		Label1.configure(font=font9)
		Label1.configure(foreground="#fff01c")
		Label1.configure(text='''Restaurant Management System''')

		Frame1_1 = Frame(root)
		Frame1_1.place(relx=0.313, rely=0.156, relheight=0.107
		        , relwidth=0.366)
		Frame1_1.configure(relief='ridge')
		Frame1_1.configure(borderwidth="10")
		Frame1_1.configure(relief='ridge')
		Frame1_1.configure(background="#444444")
		Frame1_1.configure(width=385)

		Label2 = Label(Frame1_1)
		Label2.place(relx=0.156, rely=0.133, height=53, width=288)
		Label2.configure(background="#444444")
		Label2.configure(font=font9)
		Label2.configure(foreground="#f7eb3e")
		Label2.configure(text='''Menu Card''')

		Frame1_2 = Frame(root)
		Frame1_2.place(relx=0.109, rely=0.284, relheight=0.689
		        , relwidth=0.755)
		Frame1_2.configure(relief='ridge')
		Frame1_2.configure(borderwidth="10")
		Frame1_2.configure(background="#444444")

		Label3 = Label(Frame1_2)
		Label3.place(relx=0.038, rely=0.103, height=26, width=104)
		Label3.configure(background="#444444")
		Label3.configure(font=font11)
		Label3.configure(foreground="aqua")
		Label3.configure(text='''1. Pizza''')

		Label3_4 = Label(Frame1_2)
		Label3_4.place(relx=0.038, rely=0.165, height=26, width=134)
		Label3_4.configure(background="#444444")
		Label3_4.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_4.configure(foreground="aqua")
		Label3_4.configure(text='''2.Veg Burger''')

		Label3_5 = Label(Frame1_2)
		Label3_5.place(relx=0.038, rely=0.247, height=26, width=124)
		Label3_5.configure(background="#444444")
		Label3_5.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_5.configure(foreground="aqua")
		Label3_5.configure(text='''3.Lava Cake''')

		Label3_6 = Label(Frame1_2)
		Label3_6.place(relx=0.038, rely=0.309, height=36, width=144)
		Label3_6.configure(background="#444444")
		Label3_6.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_6.configure(foreground="aqua")
		Label3_6.configure(text='''4.Black Coffee''')

		Label3_7 = Label(Frame1_2)
		Label3_7.place(relx=0.013, rely=0.392, height=16, width=104)
		Label3_7.configure(background="#444444")
		Label3_7.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_7.configure(foreground="aqua")
		Label3_7.configure(text='''5.Tea''')

		Label3_8 = Label(Frame1_2)
		Label3_8.place(relx=0.038, rely=0.598, height=26, width=144)
		Label3_8.configure(background="#444444")
		Label3_8.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_8.configure(foreground="aqua")
		Label3_8.configure(text='''8.Tomato Soup''')

		Label3_9 = Label(Frame1_2)
		Label3_9.place(relx=0.553, rely=0.371, height=26, width=104)
		Label3_9.configure(background="#444444")
		Label3_9.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_9.configure(foreground="aqua")
		Label3_9.configure(text='''14.Rice''')

		Label3_10 = Label(Frame1_2)
		Label3_10.place(relx=0.566, rely=0.206, height=26, width=174)
		Label3_10.configure(background="#444444")
		Label3_10.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_10.configure(foreground="aqua")
		Label3_10.configure(text='''12. Dal Makhani''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.541, rely=0.289, height=26, width=184)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="aqua")
		Label3_11.configure(text='''13.Butter Roti''')

		Label3_12 = Label(Frame1_2)
		Label3_12.place(relx=0.038, rely=0.66, height=26, width=154)
		Label3_12.configure(background="#444444")
		Label3_12.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_12.configure(foreground="aqua")
		Label3_12.configure(text='''9.Gujarati Thali''')

		Label3_13 = Label(Frame1_2)
		Label3_13.place(relx=-0.239, rely=0.309, height=26, width=104)
		Label3_13.configure(background="#444444")
		Label3_13.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_13.configure(foreground="aqua")
		Label3_13.configure(text='''1. Pizza''')

		Label3_14 = Label(Frame1_2)
		Label3_14.place(relx=-0.239, rely=0.309, height=26, width=104)
		Label3_14.configure(background="#444444")
		Label3_14.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_14.configure(foreground="aqua")
		Label3_14.configure(text='''1. Pizza''')

		Label3_15 = Label(Frame1_2)
		Label3_15.place(relx=0.579, rely=0.124, height=26, width=174)
		Label3_15.configure(background="#444444")
		Label3_15.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_15.configure(foreground="aqua")
		Label3_15.configure(text='''11.Paneer Makhani''')

		Label3_16 = Label(Frame1_2)
		Label3_16.place(relx=0.038, rely=0.742, height=26, width=164)
		Label3_16.configure(background="#444444")
		Label3_16.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_16.configure(foreground="aqua")
		Label3_16.configure(text='''10.Punjabi Thali''')

		Label3_17 = Label(Frame1_2)
		Label3_17.place(relx=0.579, rely=0.454, height=26, width=194)
		Label3_17.configure(background="#444444")
		Label3_17.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_17.configure(foreground="aqua")
		Label3_17.configure(text='''15.Vanilla Ice-cream''')

		Label3_18 = Label(Frame1_2)
		Label3_18.place(relx=0.553, rely=0.515, height=26, width=104)
		Label3_18.configure(background="#444444")
		Label3_18.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_18.configure(foreground="aqua")
		Label3_18.configure(text='''16.Cola''')

		Label3_19 = Label(Frame1_2)
		Label3_19.place(relx=0.025, rely=0.515, height=26, width=104)
		Label3_19.configure(background="#444444")
		Label3_19.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_19.configure(foreground="aqua")
		Label3_19.configure(text='''7.Pasta''')

		Label3_20 = Label(Frame1_2)
		Label3_20.place(relx=0.038, rely=0.433, height=36, width=144)
		Label3_20.configure(background="#444444")
		Label3_20.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_20.configure(foreground="aqua")
		Label3_20.configure(text='''6.French Fries''')

		Label3_18 = Label(Frame1_2)
		Label3_18.place(relx=0.553, rely=0.66, height=26, width=194)
		Label3_18.configure(background="#444444")
		Label3_18.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_18.configure(foreground="aqua")
		Label3_18.configure(text='''18. Gulab Jamun''')

		Label3_18 = Label(Frame1_2)
		Label3_18.place(relx=0.528, rely=0.598, height=26, width=194)
		Label3_18.configure(background="#444444")
		Label3_18.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_18.configure(foreground="aqua")
		Label3_18.configure(text='''17.milkshake''')

		Label3_8 = Label(Frame1_2)
		Label3_8.place(relx=0.566, rely=0.742, height=26, width=144)
		Label3_8.configure(background="#444444")
		Label3_8.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_8.configure(foreground="aqua")
		Label3_8.configure(text='''19.Shrikhand''')

		Label3_10 = Label(Frame1_2)
		Label3_10.place(relx=0.39, rely=0.103, height=26, width=64)
		Label3_10.configure(background="#444444")
		Label3_10.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_10.configure(foreground="#fafffd")
		Label3_10.configure(text='''- 199''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.247, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 86''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.371, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 25''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.309, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 45''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.165, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 72''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.881, rely=0.206, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 200''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.881, rely=0.124, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 210''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.742, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 535''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.66, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 465''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.598, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 70''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.515, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 520''')

		Label3_11 = Label(Frame1_2)
		Label3_11.place(relx=0.39, rely=0.433, height=26, width=64)
		Label3_11.configure(background="#444444")
		Label3_11.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_11.configure(foreground="#fafffd")
		Label3_11.configure(text='''- 106''')

		Label3_12 = Label(Frame1_2)
		Label3_12.place(relx=0.881, rely=0.454, height=26, width=64)
		Label3_12.configure(background="#444444")
		Label3_12.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_12.configure(foreground="#fafffd")
		Label3_12.configure(text='''- 50''')

		Label3_12 = Label(Frame1_2)
		Label3_12.place(relx=0.881, rely=0.371, height=26, width=64)
		Label3_12.configure(background="#444444")
		Label3_12.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_12.configure(foreground="#fafffd")
		Label3_12.configure(text='''- 180''')

		Label3_12 = Label(Frame1_2)
		Label3_12.place(relx=0.881, rely=0.289, height=26, width=64)
		Label3_12.configure(background="#444444")
		Label3_12.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_12.configure(foreground="#fafffd")
		Label3_12.configure(text='''- 30''')

		Label3_13 = Label(Frame1_2)
		Label3_13.place(relx=0.881, rely=0.577, height=26, width=64)
		Label3_13.configure(background="#444444")
		Label3_13.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_13.configure(foreground="#fafffd")
		Label3_13.configure(text='''- 60''')

		Label3_13 = Label(Frame1_2)
		Label3_13.place(relx=0.881, rely=0.66, height=26, width=64)
		Label3_13.configure(background="#444444")
		Label3_13.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_13.configure(foreground="#fafffd")
		Label3_13.configure(text='''- 70''')

		Label3_13 = Label(Frame1_2)
		Label3_13.place(relx=0.881, rely=0.742, height=26, width=64)
		Label3_13.configure(background="#444444")
		Label3_13.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_13.configure(foreground="#fafffd")
		Label3_13.configure(text='''- 55''')

		Label3_13 = Label(Frame1_2)
		Label3_13.place(relx=0.881, rely=0.515, height=26, width=64)
		Label3_13.configure(background="#444444")
		Label3_13.configure(font="-family {Script MT Bold} -size 17 -weight bold")
		Label3_13.configure(foreground="#fafffd")
		Label3_13.configure(text='''- 40''')

		Label3_14 = Label(Frame1_2)
		Label3_14.place(relx=0.038, rely=0.021, height=26, width=134)
		Label3_14.configure(background="#444444")
		Label3_14.configure(font=font13)
		Label3_14.configure(foreground="#46ff21")
		Label3_14.configure(text='''Item''')

		Label3_15 = Label(Frame1_2)
		Label3_15.place(relx=0.352, rely=0.021, height=26, width=134)
		Label3_15.configure(background="#444444")
		Label3_15.configure(font="-family {Script MT Bold} -size 22 -weight bold")
		Label3_15.configure(foreground="#46ff21")
		Label3_15.configure(text='''Rate''')

		Label3_15 = Label(Frame1_2)
		Label3_15.place(relx=0.881, rely=0.021, height=26, width=74)
		Label3_15.configure(background="#444444")
		Label3_15.configure(font="-family {Script MT Bold} -size 22 -weight bold")
		Label3_15.configure(foreground="#46ff21")
		Label3_15.configure(text='''Rate''')

		Label3_15 = Label(Frame1_2)
		Label3_15.place(relx=0.591, rely=0.021, height=26, width=134)
		Label3_15.configure(background="#444444")
		Label3_15.configure(font="-family {Script MT Bold} -size 22 -weight bold")
		Label3_15.configure(foreground="#46ff21")
		Label3_15.configure(text='''Item''')

		btn_back = Button(root)
		btn_back.place(relx=0.038, rely=0.185, height=34, width=107)
		btn_back.configure(background="#d8d809")
		btn_back.configure(font=font15)
		btn_back.configure(foreground="#2e1bdd")
		btn_back.configure(pady="0")
		btn_back.configure(text='''Back''',command=menucard1)

		Frame1_2 = Frame(root)
		Frame1_2.place(relx=0.703, rely=0.156, relheight=0.107
		        , relwidth=0.261)
		Frame1_2.configure(relief='ridge')
		Frame1_2.configure(borderwidth="10")
		Frame1_2.configure(background="#444444")
		Frame1_2.configure(width=275)

		Label3_4 = Label(Frame1_2)
		Label3_4.place(relx=0.109, rely=0.267, height=36, width=214)
		Label3_4.configure(background="#444444")
		Label3_4.configure(font=font16)
		Label3_4.configure(foreground="#47ff19")
		Label3_4.configure(text='''--SAMPLE HOTEL--''')
		Label3_4.configure(width=214)


		root.mainloop()
#---------------------------------------///////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\------------------------------
	root = Tk()
	class main:
		font11 = "-family Rockwell -size 13 -weight bold -slant roman " \
		"-underline 0 -overstrike 0"
		font14 = "-family {Bodoni MT Black} -size 40 -weight bold " \
		"-slant roman -underline 0 -overstrike 0"
		font15 = "-family {Rockwell Extra Bold} -size 20 -weight bold " \
		"-slant roman -underline 0 -overstrike 0"
		font16 = "-family Rockwell -size 12 -weight normal -slant " \
		"roman -underline 0 -overstrike 0"
		font9 = "-family {Rockwell Extra Bold} -size 23 -weight bold " \
		"-slant roman -underline 0 -overstrike 0"


		def exits():
			msg=messagebox.askyesno('etax-2019','Do You Want To Exit ?');
			if msg:
				os._exit(1)

		def workspaces():
			root.destroy()
			workspace1()

		def databases():
			root.destroy()
			database1()

		def supports():
			root.destroy()
			support1()


		def abouts():
			root.destroy()
			about1()

		root.geometry("1121x755+49+81")
		root.title("New findlevel")
		root.configure(background="#0c5fef")
		root.configure(highlightcolor="#132863")


		Label1=Label(root, text="Restaurant Management System")
		Label1.place(relx=-0.047, rely=0.235, height=41, width=514)
		Label1.configure(background="#0c5fef")
		Label1.configure(font=font14)
		Label1.configure(foreground="#fff71c")
		Label1.pack()

		btnexit = Button(root, text="EXIT")
		btnexit.place(relx=0.928, rely=0.927, height=44, width=77)
		btnexit.configure(background="#fff71c")
		btnexit.configure(font=font11)
		btnexit.configure(foreground="red")
		btnexit.configure(command=exits)

		Frame2 = Frame(root)
		Frame2.place(relx=0.054, rely=0.172, relheight=0.364
				  , relwidth=0.397)
		Frame2.configure(background="#f7ff08")
		Frame2.configure(width=445)

		Label2 = Label(Frame2,text="WORKSPACE")
		Label2.place(relx=0.045, rely=0.109, height=91, width=404)
		Label2.configure(background="#f7ff08")
		Label2.configure(font=font14)
		Label2.configure(foreground="#5f16dd")

		btnworkspace = Button(Frame2,text="OPEN")
		btnworkspace.place(relx=0.315, rely=0.582, height=54, width=177)
		btnworkspace.configure(background="#160fd8")
		btnworkspace.configure(font=font15)
		btnworkspace.configure(foreground="#fcfeff")
		btnworkspace.configure(command=workspaces)

		Frame2_2 = Frame(root)
		Frame2_2.place(relx=0.517, rely=0.172, relheight=0.364
					, relwidth=0.397)
		Frame2_2.configure(background="#f7ff08")

		Label2_5 = Label(Frame2_2)
		Label2_5.place(relx=0.045, rely=0.073, height=91, width=404)
		Label2_5.configure(background="#f7ff08")
		Label2_5.configure(font=font14)
		Label2_5.configure(foreground="#5f16dd")
		Label2_5.configure(text='''DATABASE''')

		btndatabase = Button(Frame2_2)
		btndatabase.place(relx=0.292, rely=0.582, height=54, width=177)
		btndatabase.configure(background="#160fd8",font=font15,foreground="#fcfeff",command=databases, text='''OPEN''')

		Frame2_3 = Frame(root)
		Frame2_3.place(relx=0.054, rely=0.57, relheight=0.364
					, relwidth=0.397)
		Frame2_3.configure(background="#f7ff08")

		Label2_6 = Label(Frame2_3)
		Label2_6.place(relx=0.045, rely=0.073, height=91, width=404)
		Label2_6.configure(background="#f7ff08")
		Label2_6.configure(font=font14)
		Label2_6.configure(foreground="#5f16dd")
		Label2_6.configure(text='''ABOUT''')

		btnsupport = Button(Frame2_3)
		btnsupport.place(relx=0.292, rely=0.545, height=54, width=177)
		btnsupport.configure(background="#160fd8")
		btnsupport.configure(font=font15)
		btnsupport.configure(foreground="#fcfeff")
		btnsupport.configure(command=supports, text='''OPEN''')

		Frame2_4 =Frame(root)
		Frame2_4.place(relx=0.517, rely=0.57, relheight=0.364
					, relwidth=0.397)
		Frame2_4.configure(background="#f7ff08")

		Label2_7 = Label(Frame2_4)
		Label2_7.place(relx=0.022, rely=0.036, height=91, width=404)
		Label2_7.configure(background="#f7ff08")
		Label2_7.configure(font=font14)
		Label2_7.configure(foreground="#5f16dd")
		Label2_7.configure(text='''MENU CARD''')

		btnabout = Button(Frame2_4)
		btnabout.place(relx=0.315, rely=0.545, height=54, width=177)
		btnabout.configure(background="#160fd8")
		btnabout.configure(font=font15)
		btnabout.configure(foreground="#fcfeff")
		btnabout.configure(command=abouts, text='''OPEN''')

		Label4 = Label(root)
		Label4.place(relx=0.919, rely=0.106, height=25, width=81)
		Label4.configure(background="#0c5fef")
		Label4.configure(font=font16)
		Label4.configure(foreground="white")
		Label4.configure(text='''Username''')

		Label5 = Label(root)
		Label5.place(relx=0.009, rely=0.94, height=21, width=54)
		Label5.configure(background="#0c5fef")
		Label5.configure(foreground="white")
		Label5.configure(text='''v 1.0.2''')

		Label5_10 = Label(root)
		Label5_10.place(relx=0.009, rely=0.967, height=21, width=174)
		Label5_10.configure(background="#0c5fef")
		Label5_10.configure(foreground="white")
		Label5_10.configure(text='''Connected to MySQL server 81''')

		root.mainloop()
print("WELCOME..................................")
print("Please Wait while connecting to the MySQL server,................\n\n\n")
try:
	database = DBConnect(host='localhost',user='root',password='Pass@123', database='rest2019')
	mydb=mysql.connector.connect(host='localhost',user='root',passwd='Pass@123',database='rest2019')
	software()
except:
	print("Error Occured while connecting to the server. Please contact your administrator \n\n\n ")
	print("Press key 1 to Work Offline or Press any other key to exit. \n\n\n")
	try:
		choice=eval(input())
	except:
		os._exit(1)
	if choice==1 or choice==1:
		software()
	else :
		os._exit(1)




