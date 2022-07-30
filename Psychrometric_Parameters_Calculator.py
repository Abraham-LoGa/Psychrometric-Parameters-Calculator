"""
Programa elaborado por: López García Abraham
En caso de dudas contactar a: abraham.lg.chap@gmail.com
"""
  # Importación de librerias
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def ventana_calculadora():
	  # Ventana
	objeto_ventana2=Tk()
	objeto_ventana2.title('Calculador')
	objeto_ventana2.geometry("550x760")

	def label_box(Name_object,Text,cord_x,cord_y,tipo_d_Letra,tamano):
		LabelG=Label(Name_object,text=Text)
		LabelG.place(x=cord_x,y=cord_y)
		LabelG.configure(font=(tipo_d_Letra,tamano))
	  # Función para Botones
	def boton(Name_object,Text,llamar,cord_x,cord_y,w,h):
		botonG=Button(Name_object,text=Text,command=llamar,width=w,height=h)
		botonG.place(x=cord_x,y=cord_y)
	  # Decalracion de Variables
	pvs=DoubleVar()
	Pv=DoubleVar()
	w_r=DoubleVar()
	w_s=DoubleVar()
	g_s=DoubleVar()
	v_e_a=DoubleVar()
	Tem_PR=DoubleVar()
	h=DoubleVar()
	h_r=DoubleVar()
	Tbh=DoubleVar()
	Label1=label_box(objeto_ventana2,"CALCULADORA DE",120,20,"Courier",24)
	Label2=label_box(objeto_ventana2,"DATOS PSCROMÉTRICOS",70,60,"Courier",24)
	  # Textos para obtener datos
	L_0=label_box(objeto_ventana2,"Ingrese los datos solicitados",50,120,"Corbel",11)
	L_g=label_box(objeto_ventana2,"Primero:",340,130,"Corbel",10)
	L_guia=label_box(objeto_ventana2,"Después:",340,190,"Corbel",10)
	L_1=label_box(objeto_ventana2,"Tbs",45,150,"Corbel",12)
	L_1=label_box(objeto_ventana2,"°C",230,150,"Corbel",12)
	L_2=label_box(objeto_ventana2,"H_r",40,190,"Corbel",12)
	L_2=label_box(objeto_ventana2,"%",230,190,"Corbel",12)
	L_3=label_box(objeto_ventana2,"Altura",30,230,"Corbel",12)
	L_3=label_box(objeto_ventana2,"m",230,230,"Corbel",12)
	T_C=Entry(objeto_ventana2)
	T_C.place(x=100,y=155)
	Humedad_r=Entry(objeto_ventana2)
	Humedad_r.place(x=100,y=195)
	Altura=Entry(objeto_ventana2)
	Altura.place(x=100,y=235)

	def calculos_psicrometricos():
		  # Obtención de variables
		Tc=float(T_C.get())
		Tk=Tc+273.15
		P_h_r=float(Humedad_r.get())
		Alt=float(Altura.get())
		p_atm=101.325*pow(1-2.25577*(pow(10,-5)*(Alt)),5.2559)
		  # Funciones para obtención de datos de cada parámetro
		def presion_v_s(t):
			a1=-5.8002206*(pow(10,3))
			a2=1.3914993
			a3=-4.8640239*(pow(10,-2))
			a4=4.1764768*(pow(10,-5))
			a5=-1.4452093*(pow(10,-8))
			a6=6.5459673
			p_v_s=np.exp(a1/t+a2+a3*t+a4*(pow(t,2))+a5*(pow(t,3))+a6*np.log(t))
			return p_v_s
		def presion_parcial(P_V_S,P_H):
			p_p_v=(P_V_S)*(P_H)/100
			return p_p_v
		def razon_humedad(p,patm):
			r_w=0.622*(p/(patm-p))
			return r_w
		def razon_humedad_saturacion(p,patm):
			a=p/1000
			r_w=0.622*(a/(patm-a))
			return r_w
		def grado_saturacion(rw,sw):
			g_u=rw/sw
			return g_u
		def volumen_especifico(patm,rw,t):
			vh=(287.055*(t)/(patm*1000))*((1+1.6078*rw)/(1+rw))
			return vh
		def temperatura_puntoR(pV):
			T_pr=-35.957-1.8726*np.log(pV)+1.1689*(pow(np.log(pV),2))
			return T_pr
		def Entalpia_h(t,rw):
			h_e=1.006*(t)+rw*(2501+1.805*(t))
			return h_e
		def temperatura_bulbo_h(patm,t,t_r,p_par):
			Tb=((0.00621945*patm*t)+(41860*p_par)/(pow((t_r+232.6),2)*t_r))/(0.00621945*patm + (41860*p_par)/(pow((t_r+232.6),2)))+6
			return Tb

		  # Obtención de datos  
		p_vs=presion_v_s(Tk)
		p_pv=presion_parcial(p_vs,P_h_r)/1000
		p_pv2=presion_parcial(p_vs,P_h_r)
		wr=razon_humedad(p_pv,p_atm)
		ws=razon_humedad_saturacion(p_vs,p_atm)
		g_s_u=grado_saturacion(wr,ws)
		v_e_h=volumen_especifico(p_atm,wr,Tk)
		T_Roc=temperatura_puntoR(p_pv2)
		hp=Entalpia_h(Tc,wr)
		T_bulbo=temperatura_bulbo_h(p_atm,Tc,T_Roc,p_pv)

		  # Retorno de datos obtenidos 
		return pvs.set(p_vs),Pv.set(p_pv),w_r.set(wr),w_s.set(ws),g_s.set(g_s_u),v_e_a.set(v_e_h),Tem_PR.set(T_Roc),h.set(hp),Tbh.set(T_bulbo)  
	  # Función para salir de ventana
	def quit2():
		objeto_ventana2.destroy()
	
	  # Botonoes para calcular y salir 
	B1=boton(objeto_ventana2,"Calcular",calculos_psicrometricos,320,150,10,1)
	B3=boton(objeto_ventana2,"Salir",quit2,180,700,13,1)
	  # Entradas y textos para obtención de datos
	L_4=label_box(objeto_ventana2,"Propiedades asociados con vapor de agua",110,300,"Corbel",11)
	L_Pv=label_box(objeto_ventana2,"Pv(pa)",20,330,"Corbel",11)
	P_v=Entry(objeto_ventana2,textvariable=pvs)
	P_v.place(x=90,y=335)
	L_W=label_box(objeto_ventana2,"W(kg/kg)",250,330,"Corbel",11)
	W=Entry(objeto_ventana2,textvariable=w_r)
	W.place(x=330,y=335)
	L_u=label_box(objeto_ventana2,"u",50,370,"Corbel",11)
	u_s=Entry(objeto_ventana2,textvariable=g_s)
	u_s.place(x=90,y=375)
	L_Ppv=label_box(objeto_ventana2,"Pvs (kPa)",250,370,"Corbel",11)
	Ppv=Entry(objeto_ventana2,textvariable=Pv)
	Ppv.place(x=330,y=375)
	L_5=label_box(objeto_ventana2,"Propiedades asociados con la Temperatura",110,400,"Corbel",11)
	L_Tpr=label_box(objeto_ventana2,"Tpr(°C)",20,430,"Corbel",11)
	Tp_r=Entry(objeto_ventana2,textvariable=Tem_PR)
	Tp_r.place(x=90,y=435)
	L_Tbh=label_box(objeto_ventana2,"Tbh(°C)",250,430,"Corbel",11)
	Tb_h=Entry(objeto_ventana2,textvariable=Tbh)
	Tb_h.place(x=330,y=435)
	L_5=label_box(objeto_ventana2,"Propiedades asociados con el volúmen y energía",90,470,"Corbel",11)
	L_Veh=label_box(objeto_ventana2,"Veh(m^3/kg)",20,510,"Corbel",11)
	Ve_h=Entry(objeto_ventana2,textvariable=v_e_a)
	Ve_h.place(x=110,y=515)
	L_h=label_box(objeto_ventana2,"h (kJ/kg)",250,510,"Corbel",11)
	h_a=Entry(objeto_ventana2,textvariable=h)
	h_a.place(x=330,y=515)
	L_Ws=label_box(objeto_ventana2,"Ws(kg/kg)",20,550,"Corbel",11)
	Ws=Entry(objeto_ventana2,textvariable=w_s)
	Ws.place(x=110,y=555)

	  # Grafica de carta Psicrométrica
	def carta_Psicrometrica():
		  # Declaranción de matrices a obtener
		Tc=np.zeros(19)
		Tc2=np.zeros(36)
		Hre=np.zeros((36,10))
		W_1=np.zeros((36,10))
		h_enta=np.zeros((36,16))
		v_es=np.zeros((36,10))
		W_h=np.zeros(19)
		h_v=np.zeros(36)
		v_e=np.zeros(19)
		P=np.zeros(19)
		  # Obtención de variables y parámetros
		valores_T=float(T_C.get())
		valores_W=float(W.get())
		valor_Ws=float(Ws.get())
		valor_Tbh=float(Tb_h.get())
		valor_Tpr=float(Tp_r.get())
		z=float(Altura.get())
		p= 101.325*pow(1-2.25577*(pow(10,-5)*(z)),5.2559)*1000
		pA= 101.325*pow(1-2.25577*(pow(10,-5)*(z)),5.2559)*7.501
		c=0
		prc=100
		  # Constantes para temperatura de 0 a 200°C 
		def presion_v_s(t):
			a1=-5.8002206*(pow(10,3))
			a2=1.3914993
			a3=-4.8640239*(pow(10,-2))
			a4=4.1764768*(pow(10,-5))
			a5=-1.4452093*(pow(10,-8))
			a6=6.5459673
			p_v_s=np.exp(a1/t+a2+a3*t+a4*(pow(t,2))+a5*(pow(t,3))+a6*np.log(t))
			return p_v_s

		for i in range(1,19):
			c=c+5.0
			Tc[i]=c
			k=c+273.15
			P[i]=presion_v_s(k)
			P[i]=P[i]*0.007501
		Tc[0]=0.01
		k=Tc[0]+273.15
		P[0]=presion_v_s(k)
		P[0]=P[0]*0.007501

		for i in range(10):
			for j in range(19):
				Hre[j][i]=P[j]*prc/100
			prc=prc-10

		for i in range(10):
			for j in range(19):
				W_1[j][i]=(Hre[j][i]*0.622)/(pA-Hre[j][i])

		c2=0
		# Creación de matriz de temeperatuera para 36 datos
		for i in range(1,36):
			c2=c2+5.0
			Tc2[i]=c2
		Tc2[0]=0.01
		R_Hf=10
			# Entalpía
		for i in range(16):
			for j in range(36):
				h_enta[j][i]=((R_Hf)/4.18-(0.24*Tc2[j]))/(0.46*Tc2[j]+597.2)
			R_Hf=R_Hf+10
			# Volumen específico
		Range=0.8
		for i in range(10):
			for j in range(19):
				v_es[j][i]=18*(Range*((p)/101325)/(0.082*(Tc[j]+273.15))-1/29)
			Range=Range+0.05

		  # Función para Entalpía
		def graf(t,w,x1):
			y1=-0.00039*(x1-t)+w
			return y1
		x=np.linspace(-10,200)
		y=graf(valores_T,valores_W,x)

		  # Inicialización de gráfica
		plt.figure()
		  # Configuración general de gráfica
		plt.title('Volúmen Específico m^3/kg (0.80-1.25) Diagonal verde', fontsize=10)
		plt.suptitle('Carta Psicrométrica')

		ax = plt.gca()
		ax2 = plt.gca()
		  # Configuración de gráfica 
		ax.grid(True)
		ax.set_xticks(np.linspace(0,90,19))
		ax.set_xlim(0,50)
		ax.set_xlabel("Temperatura de Bulbo Seco (°C)")
		ax.set_yticks(np.linspace(0,120,11))
		ax.set_ylim(0,130)
		ax.set_ylabel("Entalpía (kJ/kg)")
		ax2 = ax.twinx()
		ax2.set_ylabel(r"Relación Humedad Kg de agua/Kg de aire seco" )
		ax2.set_ylim(0,0.05,11)

		 # Graficación de datos
		for i in range (10):
			for j in range (19):
				v_e[j]=v_es[j][i]
			ax2.plot(Tc,v_e,"g--",linewidth=1)
		for i in range (16):
			for j in range (36):
				h_v[j]=h_enta[j][i]
			ax2.plot(Tc2,h_v,"r--",linewidth=1)
		for i in range (10):
			for j in range (19):
				W_h[j]=W_1[j][i]
			ax2.plot(Tc,W_h)
		
		ax2.plot(valores_T,valores_W,"ko")
		ax2.axvline(valores_T,color="red")
		ax2.axhline(valores_W,color="blue")
		ax2.axvline(valor_Tpr,color="green")
		ax2.axhline(valor_Ws,color="brown")
		ax2.axvline(valor_Tbh,color="black")
		ax2.plot(x,y,"k--")

		  # Mostrar gráfica
		plt.show()

	  # Boton para gráfica
	B2=boton(objeto_ventana2,"Graficar punto",carta_Psicrometrica,320,210,10,1)
	
	  # Impresion de Instrucciones.
	L_I=label_box(objeto_ventana2,"Instrucciones de Grafica",170,590,"Corbel",11)
	L_I1=label_box(objeto_ventana2,"Tbs= Línea vertical Roja",50,620,"Corbel",11)
	L_I2=label_box(objeto_ventana2,"Tbh= Línea vertical Negra",50,640,"Corbel",11)
	L_I3=label_box(objeto_ventana2,"Tpr= Línea vertical Verde",50,660,"Corbel",11)
	L_I4=label_box(objeto_ventana2,"W= Línea horizontal Azul",250,620,"Corbel",11)
	L_I5=label_box(objeto_ventana2,"Ws= Línea horizontal Café",250,640,"Corbel",11)
	L_I5=label_box(objeto_ventana2,"H(Entalpía)= Diagonal punteada Negra",250,660,"Corbel",11)
	
	  # Mostramos ventana
	objeto_ventana2.mainloop()


# Llamamos ventana Principal
cal=ventana_calculadora()