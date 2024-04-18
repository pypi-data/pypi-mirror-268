# pyinstaller.exe --onefile --icon=MAZAlib.ico --add-data MAZAlib.ico. MAZAlib_gui.py --noconsole
import tkinter as tk
from tkinter import filedialog as tkfiledialog
import numpy as np
from PIL import Image, ImageTk
import mazalib
import threading
import queue
import time
import os,glob
import re
import imageio
import gc
import sys

import locale
old_locale = locale.getlocale(locale.LC_NUMERIC)

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

locale.setlocale(locale.LC_NUMERIC, locale=old_locale)

# def windowsChangeSize(event):
# 	print(event.width,event.height)

class simSetting:
	def __init__(self):
		self.upperThreshold						=tk.IntVar()
		self.lowerThreshold						=tk.IntVar()
		self.previsualisation					=tk.IntVar()
		self.previsualisation.set(0)

		self.krigingVariogramComputationMethod	=tk.IntVar()
		self.krigingVariogramComputationMethod.set(0)
		self.krigingVariogramDirection			=tk.IntVar()
		self.krigingVariogramDirection.set(1)
		self.krigingVariationPrintingType		=tk.IntVar()
		self.krigingVariationPrintingType.set(0)
		self.krigingVariogramRadius				=tk.IntVar()
		self.krigingVariogramRadius.set(3)

		self.MRFbeta							=tk.DoubleVar()
		self.MRFbeta.set(0.5)
		self.MRFcooling							=tk.DoubleVar()
		self.MRFcooling.set(0.98)
		self.MRFmethod							=tk.IntVar()
		self.MRFmethod.set(0)
		self.MRFT_start							=tk.DoubleVar()
		self.MRFT_start.set(1.0)
		self.MRFalpha							=tk.DoubleVar()
		self.MRFalpha.set(0.5)
		self.MRFenergy							=tk.DoubleVar()
		self.MRFenergy.set(0.001)
		self.MRFmax								=tk.IntVar()
		self.MRFmax.set(3)

		self.CACalpha_G							=tk.DoubleVar()
		self.CACalpha_G.set(1.01)
		self.CACalpha_I							=tk.DoubleVar()
		self.CACalpha_I.set(1.02)
		self.CACG0								=tk.DoubleVar()
		self.CACG0.set(1.0)
		
		self.unsharp_mask_strengths				=tk.DoubleVar()
		self.unsharp_mask_strengths.set(1.0)
		
		self.nlm_iters_count					=tk.IntVar()
		self.nlm_iters_count.set(1)
		self.nlm_radius							=tk.IntVar()
		self.nlm_radius.set(1)



class App:
	def __init__(self,root):
		self.initDirectory='~'

		self.sourceImage=None
		self.filteredImage=None
		self.sourceImageMin=0
		self.sourceImageMax=0
		self.simImage=None
		self.zPosition=tk.IntVar()
		self.zPosition.set(0)
		self.zScale=None
		self.resultAsInputButton=None
		
		self.selectedFilter=-1
		self.computedFilter=-1
		self.computedFilterParam=None

		self.imshowSource=None
		self.imshowSim=None
		self.figureSource=None
		self.figureSim=None
		self.figureHistogram=None
		self.histColor=None
		self.histCanvas=[]

		self.listConfigAlgo=None
		self.listConfigFilter=None

		self.startPosition4SubSample=None
		self.endPosition4SubSample=None

		self.param=simSetting()
		self.root=root
		self.thresholdUpWidgets=[]
		self.thresholdDownWidgets=[]

		self.filemenu=None
		self.menu()
		self.visualiser()
		self.config()
		root.wm_title("MAZAlib")
		root.geometry("1200x800")
		self.queue=queue.SimpleQueue()
		self.resultQueue=queue.SimpleQueue()
		self.processingProcess=threading.Thread(target=self.runProcessing, args=(self.queue,self.resultQueue))

		self.processingProcess.start()
		self.look4results()

	def look4results(self):
		# self.root.config(cursor="wait")
		if not self.resultQueue.empty():
			param,val=self.resultQueue.get(False)
			(thMin, thmax,previ)=param
			if(previ==1):
				self.simImage=(self.sourceImage.astype('float')-thMin)/(thmax-thMin)
				self.simImage[self.startPosition4SubSample[0]:self.endPosition4SubSample[0],
					self.startPosition4SubSample[1]:self.endPosition4SubSample[1],
					self.startPosition4SubSample[2]:self.endPosition4SubSample[2]]=val
				self.changeSaveStatus(False)
			else:
				self.simImage=val
				self.changeSaveStatus(True)
			self.setNotBusy()
			self.requestUpdateViusalisation()
		# self.root.config(cursor="")

	def release(self):
		self.queue.put(None)
		self.processingProcess.join()

	def runProcessing(self,queue, resultQueue):
		while True:
			info=queue.get()
			if info is None:
				break
			im,filtering,param,job,args=info
			self.filter(filtering,im)
			if job is None:
				minval=self.filteredImage.min()
				rangeVal=self.filteredImage.max()-minval
				val=(self.filteredImage-minval)/rangeVal
			else:
				val=job(self.filteredImage,*args)
			resultQueue.put((param,val))
		pass

	def filter(self,filtering,image):
		filterIndex,param=filtering
		if(self.computedFilter==filterIndex and self.computedFilterParam==param):
			return
		if filterIndex==0: #NLM
			self.filteredImage=mazalib.nlm(image,param)
		elif filterIndex==1: #unsharp
			self.filteredImage=mazalib.unsharp(image,param)
		else:
			self.filteredImage=image

		self.computedFilterParam=param
		self.computedFilter=filterIndex

	def LoadFileImageAction(self):
		filename = tkfiledialog.askopenfilename(initialdir = self.initDirectory, title = "Select file")
		self.loadfile(filename)
		pass

	def LoadDirectoryImageAction(self):
		directory = tkfiledialog.askdirectory(initialdir = self.initDirectory, title = "Select driectory",mustexist=True)
		self.loadDirectory(directory)

	def loadfile(self,filename):
		if filename:
			self.initDirectory=os.path.dirname(filename)
			im=np.fromfile(filename, dtype='uint8')
			sideSize=int(round(im.size**(1/3)))
			if(sideSize**3!=im.size):
				tk.messagebox.showerror("Binary image size issue", "The binary data need to represent a perfect cube of data")
			self.sourceImage=np.moveaxis(np.reshape(im,(sideSize,sideSize,sideSize)), [0, 1, 2], [2, 0, 1])
			gc.collect()
			self.setupImageParameter()

	def initRandomImage(self):
		self.initDirectory = os.getcwd()
		self.sourceImage = (np.random.rand(100,100,100)*255).astype('uint8')
		gc.collect()
		self.setupImageParameter()

	def loadDirectory(self,directoryName):
		if directoryName:
			self.initDirectory=os.path.dirname(directoryName)
			os.chdir(directoryName)
			files_grabbed = []
			[ files_grabbed.extend(glob.glob('./*.'+typeFile)) for typeFile in ['tiff', 'tif','jpg','jpeg','bmp']]		
			files_grabbed=sorted(files_grabbed, key=lambda text: [ int(c) if c.isdigit() else c for c in re.split(r'(\d+)', text) ])
			firstImage=imageio.imread(files_grabbed[0])
			imSize = firstImage.shape[:2]
			print(imSize)
			volume=np.empty(imSize+(len(files_grabbed),),dtype=firstImage.dtype)
			print(volume.shape)
			for i in range(len(files_grabbed)):
				im=imageio.imread(files_grabbed[i])
				if(im.shape[:2] == imSize):
					if(len(im.shape)>2):
						volume[:,:,i]=im[:,:,0]
					else:
						volume[:,:,i]=im
				else:
					tk.messagebox.showerror("Image size issue", "All the images should have the same shape currently "+files_grabbed[i]+" has not the same size as the reference image("+files_grabbed[0]+")")
					break
				pass
			gc.collect()
			self.sourceImage=volume
			self.setupImageParameter()


	def setupImageParameter(self):
		if self.sourceImage is not None:
			self.sourceImageMin=self.sourceImage.min()
			self.sourceImageMax=self.sourceImage.max()
			self.zScale.configure(to=self.sourceImage.shape[2]-1)
			[scale.configure(to=self.sourceImageMax) for scale in self.thresholdUpWidgets+self.thresholdDownWidgets]
			[scale.configure(from_=self.sourceImageMin) for scale in self.thresholdUpWidgets+self.thresholdDownWidgets]

			rangeVal=self.sourceImageMax-self.sourceImageMin
			dt=self.sourceImage.size//524287+1
			v1,v2=np.quantile(self.sourceImage.flat[::dt], [0.25,0.75])
			self.param.upperThreshold.set(v2)
			self.param.lowerThreshold.set(v1)
			shape=np.array(self.sourceImage.shape)
			sizetoUse=np.minimum(shape,300)
			self.startPosition4SubSample=np.maximum(np.floor((shape-sizetoUse)/2),0).astype('int')
			self.endPosition4SubSample=(self.startPosition4SubSample+sizetoUse).astype('int')
			self.zPosition.set(shape[0]//2)
			#plt.figure(figsize=(3,5), dpi=300)
			self.axHistogram.cla()
			h, bins, patches=self.axHistogram.hist(self.sourceImage.flat[::dt], range=(self.sourceImageMin,self.sourceImageMax), bins=50)
			self.histColor=list(zip(patches, bins))
			self.axHistogram.set_xlim(xmin=self.sourceImageMin, xmax=self.sourceImageMax)
			# plt.yscale('log')
			# Use the bins to make a single histogram

			self.axHistogram.axis('off')
			self.requestUpdateViusalisation()

	def SaveImageAsFileAction(self):
		filename = tkfiledialog.asksaveasfilename(initialdir = "./",title = "Where to save", filetypes=(("raw file", "*.raw"),("Binary file", "*.bin")))
		if filename:
			self.sourceImage=np.moveaxis((255*self.simImage), [2, 0, 1], [0, 1, 2]).astype('uint8').tofile(filename)
			File_object = open(filename+'.info',"w")
			sizeIm=self.simImage.shape
			File_object.write("Size: {} {} {}\n".format(sizeIm[0],sizeIm[1],sizeIm[2]))
			File_object.write("Format: uint8\n".format(sizeIm[0],sizeIm[1],sizeIm[2]))
			File_object.close()

	def SaveImageAsDirectoryAction(self):
		filename = tkfiledialog.asksaveasfilename(initialdir = "./",title = "Where to save as a directory")
		if filename:
			os.mkdir(filename)
			os.chdir(filename)
			for i in range(self.simImage.shape[2]):
			 	imageio.imwrite(filename+'/im_{0:04}.bmp'.format(i), (255*self.simImage[:, :, i]).astype('uint8'))

	def donothing(self):
		pass

	def changeSaveStatus(self,status):
		if status:
			self.filemenu.entryconfig("Save as a file", state="active")
			self.filemenu.entryconfig("Save as directory", state="active")
		else:
			self.filemenu.entryconfig("Save as a file", state="disabled")
			self.filemenu.entryconfig("Save as directory", state="disabled")
			

	def menu(self):
		# menu
		menubar = tk.Menu(self.root)
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Load a file", command=self.LoadFileImageAction)
		filemenu.add_command(label="Load directory", command=self.LoadDirectoryImageAction)
		filemenu.add_command(label="Save as a file", command=self.SaveImageAsFileAction)
		filemenu.add_command(label="Save as directory", command=self.SaveImageAsDirectoryAction)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.root.quit)
		self.filemenu=filemenu
		self.changeSaveStatus(False)
		menubar.add_cascade(label="File", menu=filemenu)
		helpmenu = tk.Menu(menubar, tearoff=0)
		helpmenu.add_command(label="Help Index", command=self.donothing) # to be added
		helpmenu.add_command(label="About...", command=self.donothing) # to be added
		menubar.add_cascade(label="Help", menu=helpmenu)

		self.root.config(menu=menubar)
		pass

	def updateViusalisation(self):
		if(self.sourceImage is not None):
			self.imshowSource.set_data((self.sourceImage[:,:,self.zPosition.get()]-self.sourceImageMin)/(self.sourceImageMax-self.sourceImageMin))		
		if(self.simImage is not None):
			self.imshowSim.set_data((self.simImage[:,:,self.zPosition.get()]))
		elif(self.sourceImage is not None):
			localMax=self.param.upperThreshold.get()
			localMin=self.param.lowerThreshold.get()
			self.imshowSim.set_data((self.sourceImage[:,:,self.zPosition.get()].astype('float')-localMin)/(localMax-localMin))
		self.figureSource.canvas.draw()
		self.figureSim.canvas.draw()
		# print(self.histColor)
		if(self.histColor is not None):
			# print("update")
			plt.figure(self.figureHistogram.number)
			plt.setp([p for p,b in self.histColor], color='gray')
			plt.setp([p for p,b in self.histColor if b >= self.param.upperThreshold.get()], color='w')
			plt.setp([p for p,b in self.histColor if b <= self.param.lowerThreshold.get()], color='k')
			# self.figureHistogram.canvas.draw()
			if self.selectedIndexProcessing <4:
				self.histCanvas[self.selectedIndexProcessing].draw()
			# for x in self.histCanvas:
			# 	x.draw()
		# self.figureSource.canvas.flush_events()
		# self.figureSim.canvas.flush_events()
		pass

	def requestUpdateViusalisation(self):
		# if self.sourceImage is not None:
		# 	print(self.sourceImage.dtype)
		# if self.filteredImage is not None:
		# 	print(self.filteredImage.dtype)
		# if self.simImage is not None:
		# 	print(self.simImage.dtype)
		self.updateViusalisation()

	def updateZposition(self, val):
		self.requestUpdateViusalisation()
		pass

	def resultAsInput(self):
		self.resultAsInputButton["state"] = "disabled"
		if(self.simImage is not None):
			self.sourceImage=self.filteredImage
			self.computedFilter=None
			self.filteredImage=None
			self.sourceImageMin=0
			self.sourceImageMax=0
			self.simImage=None
			self.setupImageParameter()
		pass

	def visualiser(self):
		# border=0.0125
		border=0
		# viuslaisation
		visuframe = tk.Frame(self.root)
		visuframe.pack(expand=True,fill='both')

		self.figureSource = plt.figure(figsize=(10,10), dpi=300)
		plt.subplots_adjust(left=border, bottom=border, right=1-border, top=1-border)
		self.figureSource.patch.set_facecolor([(x>>8)/255 for x in visuframe.winfo_rgb(visuframe["background"])])
		self.imshowSource=plt.imshow(np.random.rand(10,10))
		self.imshowSource.set_cmap('gray')
		plt.axis('off')
		chart_type = FigureCanvasTkAgg(self.figureSource, visuframe)
		chart_type.get_tk_widget().place(relx=0.25, rely=0.05, relheight=0.9, relwidth=0.45, anchor='n')

		self.zScale = tk.Scale(visuframe ,command=self.updateZposition, from_=0, variable=self.zPosition)
		self.zScale.place(relx=0.5, rely=0.05, relheight=0.9, relwidth=0.05, anchor='n')

		self.resultAsInputButton = tk.Button(visuframe, text ="<--", command = self.resultAsInput)
		self.resultAsInputButton["state"] = "disabled"
		self.resultAsInputButton.place(relx=0.5, rely=0.00, relheight=0.05, relwidth=0.05, anchor='n')

		self.figureSim = plt.figure(figsize=(10,10), dpi=300)
		plt.subplots_adjust(left=border, bottom=border, right=1-border, top=1-border)
		self.figureSim.patch.set_facecolor([(x>>8)/255 for x in visuframe.winfo_rgb(visuframe["background"])])
		self.imshowSim=plt.imshow(np.random.rand(10,10))
		self.imshowSim.set_cmap('gray')
		plt.axis('off')
		chart_type = FigureCanvasTkAgg(self.figureSim, visuframe)
		chart_type.get_tk_widget().place(relx=0.75, rely=0.05, relheight=0.9, relwidth=0.45, anchor='n')

		tk.Label( visuframe, text="Source", font=("Courier", 20) ).place(anchor = tk.N, relx=0.25, rely=0.02, relheight=0.03, relwidth=0.45)
		tk.Label( visuframe, text="Output", font=("Courier", 20) ).place(anchor = tk.N, relx=0.75, rely=0.02, relheight=0.03, relwidth=0.45)

		self.figureHistogram=plt.figure(figsize=(10,20), dpi=300)
		self.figureHistogram.patch.set_facecolor([(x>>8)/255 for x in visuframe.winfo_rgb(visuframe["background"])])
		self.axHistogram=plt.subplot(111)
		plt.subplots_adjust(left=0.0, bottom=0, right=1, top=1)
		pass

	def changeMethod(self,evt):
		w = evt.widget
		index = int(w.curselection()[0])
		self.switchTo(index)

	def changeFilterMethod(self,evt):
		w = evt.widget
		index = int(w.curselection()[0])
		self.switchFilterTo(index)

	def updateUpperThreshold(self,event):
		self.param.lowerThreshold.set(min(self.param.upperThreshold.get()-1,self.param.lowerThreshold.get()))
		self.previsualisation()
		#threading.Thread(target=self.previsualisation,args=self).start()
		pass

	def updateLowerThreshold(self,event):
		self.param.upperThreshold.set(max(self.param.upperThreshold.get(),self.param.lowerThreshold.get()+1))
		self.previsualisation()
		#threading.Thread(target=self.previsualisation,args=self).start()
		pass

	def previsualisation(self):
		if self.sourceImage is not None:
			self.simImage=None
			self.changeSaveStatus(False)
			self.requestUpdateViusalisation()

	def config(self):
		# config
		configFrame = tk.LabelFrame(self.root, text="config",height=250, bd=3)
		configFrame.pack(expand=False,fill='x',side='bottom')

		# filters

		mylistFilter = tk.Listbox(configFrame,selectmode=tk.SINGLE)
		mylistFilter.configure(exportselection=False)
		mylistFilter.insert(tk.END,"NLM")
		mylistFilter.insert(tk.END,"Unsharp")
		mylistFilter.insert(tk.END,"None")
		mylistFilter.pack(fill="y",side='left')

		labelframeFilterNLM = tk.LabelFrame(configFrame, text="Configuration for NLM", width=200 )
		self.configFilterNLM(labelframeFilterNLM)
		labelframeFilterUnsharp = tk.LabelFrame(configFrame, text="Configuration for Unsharp", width=200 )
		self.configFilterUnsharp(labelframeFilterUnsharp)
		labelframeFilterNone = tk.LabelFrame(configFrame, text="No processing", width=200 )
		self.configFilterNone(labelframeFilterNone)

		listConfigFilter=[]
		listConfigFilter.append(labelframeFilterNLM)
		listConfigFilter.append(labelframeFilterUnsharp)
		listConfigFilter.append(labelframeFilterNone)
		self.listConfigFilter=listConfigFilter

		mylistFilter.bind('<<ListboxSelect>>', self.changeFilterMethod)
		indexFilter=0
		self.root.after(500, lambda : mylistFilter.select_set(indexFilter))
		self.switchFilterTo(indexFilter)

		# algo
		mylist = tk.Listbox(configFrame,selectmode=tk.SINGLE)
		mylist.configure(exportselection=False)
		mylist.insert(tk.END,"Kriging")
		mylist.insert(tk.END,"CAC")
		mylist.insert(tk.END,"MRF")
		mylist.insert(tk.END,"RGS")
		mylist.insert(tk.END,"None")
		# mylist.insert(tk.END,"Windowed Hessian")
		mylist.pack(fill="y",side='right')


		labelframeKriging = tk.LabelFrame(configFrame, text="Configuration for Kriging")
		self.configKriging(labelframeKriging)
		labelframeCAC = tk.LabelFrame(configFrame, text="Configuration for CAC")
		self.configCAC(labelframeCAC)
		labelframeMRF = tk.LabelFrame(configFrame, text="Configuration for MRF")
		self.configMRF(labelframeMRF)
		labelframeRGS = tk.LabelFrame(configFrame, text="Configuration for RGS")
		self.configRGS(labelframeRGS)
		labelframeNone = tk.LabelFrame(configFrame, text="No processing")
		self.configNone(labelframeNone)
		# labelframeHessian = tk.LabelFrame(configFrame, text="Configuration for Hessian")
		# self.configHessian(labelframeHessian)
		# labelframeWindowedHessian = tk.LabelFrame(configFrame, text="Configuration for Windowed Hessian")
		# self.configWindowedHessian(labelframeWindowedHessian)

		listConfigAlgo=[]
		listConfigAlgo.append(labelframeKriging)
		listConfigAlgo.append(labelframeCAC)
		listConfigAlgo.append(labelframeMRF)
		listConfigAlgo.append(labelframeRGS)
		listConfigAlgo.append(labelframeNone)
		self.listConfigAlgo=listConfigAlgo

		mylist.bind('<<ListboxSelect>>', self.changeMethod)
		index=2
		self.root.after(1000, lambda : mylist.select_set(index))
		self.switchTo(index)
		pass

	def switchTo(self,index):
		for i in self.listConfigAlgo:
			i.pack_forget()
		#if(index<len(self.listConfigAlgo)-1):
		self.selectedIndexProcessing=index
		self.listConfigAlgo[index].pack(expand=True,fill='both',side='right')
		self.requestUpdateViusalisation()

	def switchFilterTo(self,index):
		self.selectedFilter=index
		for i in self.listConfigFilter:
			i.pack_forget()
		if(index<len(self.listConfigFilter)-1):
			self.listConfigFilter[index].pack(fill='y',side='left')

	def configFilterNLM(self,frame):
		w = tk.Spinbox(frame, from_=1, to=99999999, increment=1, textvariable=self.param.nlm_iters_count)
		w.place(anchor = tk.NW, relx=0.025, rely=0.3,relheight=0.2, relwidth=0.95)
		tk.Label( frame, text="Iters count", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.025, rely=0.2,relheight=0.1, relwidth=0.95)
		w = tk.Spinbox(frame, from_=1, to=99999999, increment=1, textvariable=self.param.nlm_radius)
		w.place(anchor = tk.NW, relx=0.025, rely=0.7,relheight=0.2, relwidth=0.95)
		tk.Label( frame, text="Radius", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.025, rely=0.6,relheight=0.1, relwidth=0.95)
		pass

	def configFilterUnsharp(self,frame):
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.unsharp_mask_strengths)
		w.place(anchor = tk.NW, relx=0.025, rely=0.7,relheight=0.2, relwidth=0.95)
		tk.Label( frame, text="Mask strengths", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.025, rely=0.6,relheight=0.1, relwidth=0.95)
		pass

	def configFilterNone(self,frame):
		pass

	def configKriging(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runKriging)
		runButton.pack()

		w = tk.Spinbox(frame, from_=1, to=99999999, increment=1, textvariable=self.param.krigingVariogramRadius)
		w.place(anchor = tk.NW, relx=0.03, rely=0.12,relheight=0.2, relwidth=0.2)
		tk.Label( frame, text="Radius", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.03, rely=0.03,relheight=0.1, relwidth=0.2)

		R1 = tk.Radiobutton(frame, text="moving window semivariogram", variable=self.param.krigingVariogramComputationMethod, value=0)
		R1.place( anchor = tk.NW, relx=0.02, rely=0.35)

		R2 = tk.Radiobutton(frame, text="classic semivariogram", variable=self.param.krigingVariogramComputationMethod, value=1)
		R2.place( anchor = tk.NW, relx=0.02, rely=0.55)

		R3 = tk.Radiobutton(frame, text="classic covariance", variable=self.param.krigingVariogramComputationMethod, value=2)
		R3.place( anchor = tk.NW, relx=0.02, rely=0.75)

		R1 = tk.Radiobutton(frame, text="horizontal", variable=self.param.krigingVariogramDirection, value=0)
		R1.place( anchor = tk.NW, relx=0.24, rely=0.35)

		R2 = tk.Radiobutton(frame, text="isotropic", variable=self.param.krigingVariogramDirection, value=1)
		R2.place( anchor = tk.NW, relx=0.24, rely=0.55)

		R3 = tk.Radiobutton(frame, text="vertical", variable=self.param.krigingVariogramDirection, value=2)
		R3.place( anchor = tk.NW, relx=0.24, rely=0.75)

		R1 = tk.Radiobutton(frame, text="semivariogram", variable=self.param.krigingVariationPrintingType, value=0)
		R1.place( anchor = tk.NW, relx=0.33, rely=0.45)

		R2 = tk.Radiobutton(frame, text="covariance", variable=self.param.krigingVariationPrintingType, value=1)
		R2.place( anchor = tk.NW, relx=0.33, rely=0.65)

		C1 = tk.Checkbutton(frame, text = "Previsu-\nalisation\n(300^3)", variable = self.param.previsualisation, onvalue = 1, offvalue = 0)
		C1.place(anchor = tk.NW, relx=0.44, rely=0.5,relheight=0.4, relwidth=0.1)

		chart_type = FigureCanvasTkAgg(self.figureHistogram, frame)
		self.histCanvas.append(chart_type)
		chart_type.get_tk_widget().place(anchor = tk.NW, relx=0.55, rely=0.05,relheight=0.3, relwidth=0.4)

		tk.Label( frame, text="thresholds", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.55, rely=0.35,relheight=0.1, relwidth=0.4)
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		self.thresholdUpWidgets.append(s)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)
		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		self.thresholdDownWidgets.append(s2)
		pass

	def configCAC(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runCAC)
		runButton.pack()

		# {alpha_G} {alpha_I} {G0} = real numbers, constants from speed function, defaults are 1.01, 1.02, 1.0 respectively
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.CACalpha_G)
		w.place(anchor = tk.NW, relx=0.005, rely=0.1,relheight=0.2, relwidth=0.4)
		tk.Label( frame, text="alpha_G", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.0,relheight=0.1, relwidth=0.2)
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.CACalpha_I)
		w.place(anchor = tk.NW, relx=0.005, rely=0.4,relheight=0.2, relwidth=0.4)
		tk.Label( frame, text="alpha_I", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.3,relheight=0.1, relwidth=0.2)
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.CACG0)
		w.place(anchor = tk.NW, relx=0.005, rely=0.7,relheight=0.2, relwidth=0.4)
		tk.Label( frame, text="G0", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.6,relheight=0.1, relwidth=0.2)

		C1 = tk.Checkbutton(frame, text = "Previsu-\nalisation\n(300^3)", variable = self.param.previsualisation, onvalue = 1, offvalue = 0)
		C1.place(anchor = tk.NW, relx=0.44, rely=0.5,relheight=0.4, relwidth=0.1)

		chart_type = FigureCanvasTkAgg(self.figureHistogram, frame)
		self.histCanvas.append(chart_type)
		chart_type.get_tk_widget().place(anchor = tk.NW, relx=0.55, rely=0.05,relheight=0.3, relwidth=0.4)

		tk.Label( frame, text="thresholds", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.55, rely=0.35,relheight=0.1, relwidth=0.4)
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		self.thresholdUpWidgets.append(s)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)
		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		self.thresholdDownWidgets.append(s2)
		pass

	def configMRF(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runMRF)
		runButton.pack()

		# {beta constant} = real number >= 0, see the equation (1), default is 0.5
		tk.Label( frame, text="beta", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.0,relheight=0.1, relwidth=0.2)
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.MRFbeta)
		w.place(anchor = tk.NW, relx=0.005, rely=0.10,relheight=0.2, relwidth=0.2)
		# {cooling speed} = real number 0 < c < 1, used in MMD algorithm, default is 0.98
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.MRFcooling, tickinterval=0.1,  orient="horizontal",resolution=0.01)
		s.place(anchor = tk.NW, relx=0.005, rely=0.38,relheight=0.27, relwidth=0.2)
		tk.Label( frame, text="cooling", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.30,relheight=0.12, relwidth=0.2)
		# {alpha constant} = real number 0 < α < 1, used in MMD algorithm, default is 0.5
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.MRFalpha, tickinterval=0.1,  orient="horizontal",resolution=0.01)
		s.place(anchor = tk.NW, relx=0.005, rely=0.73,relheight=0.27, relwidth=0.2)
		tk.Label( frame, text="alpha", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.005, rely=0.65,relheight=0.12, relwidth=0.2)

		# {method} = 0 for MMD, 1 for ICM algorithm to be chosen for optimization
		R1 = tk.Radiobutton(frame, text="MMD", variable=self.param.MRFmethod, value=0)
		R1.place( anchor = tk.NW, relx=0.21, rely=0.0)
		R2 = tk.Radiobutton(frame, text="ICM", variable=self.param.MRFmethod, value=1)
		R2.place( anchor = tk.NW, relx=0.31, rely=0.0)
		# {T_start} = real number > 0, used in MMD algorithm, default is 1
		tk.Label( frame, text="T_start", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.21, rely=0.15,relheight=0.1, relwidth=0.2)
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.01, textvariable=self.param.MRFT_start)
		w.place(anchor = tk.NW, relx=0.21, rely=0.25,relheight=0.2, relwidth=0.2)

		# {energy threshold} = relative energy change, once reached, optimization stops, default is 0.001
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=0.001, format='%.3f',textvariable=self.param.MRFenergy)
		w.place(anchor = tk.NW, relx=0.21, rely=0.55,relheight=0.2, relwidth=0.2)
		tk.Label( frame, text="energy threshold", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.21, rely=0.45,relheight=0.1, relwidth=0.2)
		# {max iterations} = integer > 0, maximum amount of iterations to be passed
		w = tk.Spinbox(frame, from_=0, to=99999999, increment=1, textvariable=self.param.MRFmax)
		w.place(anchor = tk.NW, relx=0.21, rely=0.80,relheight=0.2, relwidth=0.2)
		tk.Label( frame, text="max iterations", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.21, rely=0.7,relheight=0.1, relwidth=0.2)

		C1 = tk.Checkbutton(frame, text = "Previsu-\nalisation\n(300^3)", variable = self.param.previsualisation, onvalue = 1, offvalue = 0)
		C1.place(anchor = tk.NW, relx=0.44, rely=0.5,relheight=0.4, relwidth=0.1)


		chart_type = FigureCanvasTkAgg(self.figureHistogram, frame)
		self.histCanvas.append(chart_type)
		chart_type.get_tk_widget().place(anchor = tk.NW, relx=0.55, rely=0.05,relheight=0.3, relwidth=0.4)


		tk.Label( frame, text="thresholds", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.55, rely=0.35,relheight=0.1, relwidth=0.4)
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		self.thresholdUpWidgets.append(s)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)
		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		self.thresholdDownWidgets.append(s2)
		pass

	def configRGS(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runRGS)
		runButton.pack()

		C1 = tk.Checkbutton(frame, text = "Previsu-\nalisation\n(300^3)", variable = self.param.previsualisation, onvalue = 1, offvalue = 0)
		C1.place(anchor = tk.NW, relx=0.44, rely=0.5,relheight=0.4, relwidth=0.1)

		chart_type = FigureCanvasTkAgg(self.figureHistogram, frame)
		self.histCanvas.append(chart_type)
		chart_type.get_tk_widget().place(anchor = tk.NW, relx=0.55, rely=0.05,relheight=0.3, relwidth=0.4)

		tk.Label( frame, text="thresholds", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.55, rely=0.35,relheight=0.1, relwidth=0.4)
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		self.thresholdUpWidgets.append(s)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)
		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		self.thresholdDownWidgets.append(s2)
		pass

	def configHessian(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runHessian)
		runButton.pack()

		tk.Label( frame, text="thresholds", relief=tk.RAISED ).place(anchor = tk.NW, relx=0.55, rely=0.35,relheight=0.1, relwidth=0.4)
		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		self.thresholdUpWidgets.append(s)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)
		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=1)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		self.thresholdDownWidgets.append(s2)
		pass

	def configWindowedHessian(self,frame):
		runButton=tk.Button(frame, text ="Run", command = self.runWindowedHessian)
		runButton.pack()

		s= tk.Scale(frame, from_=0, to=1, variable=self.param.upperThreshold, command=self.updateUpperThreshold, tickinterval=0.1,  orient="horizontal",resolution=0.01)
		s.place(anchor = tk.NW, relx=0.55, rely=0.45,relheight=0.3, relwidth=0.4)

		s2= tk.Scale(frame, from_=0, to=1, variable=self.param.lowerThreshold, command=self.updateLowerThreshold, tickinterval=0.1,  orient="horizontal",resolution=0.01)
		s2.place(anchor = tk.NW, relx=0.55, rely=0.7,relheight=0.3, relwidth=0.4)
		pass

	def configNone(self,frame):
		runButton=tk.Button(frame, text ="Filter only", command = self.runFilterOnly)
		runButton.pack()

		C1 = tk.Checkbutton(frame, text = "Previsu-\nalisation\n(300^3)", variable = self.param.previsualisation, onvalue = 1, offvalue = 0)
		C1.place(anchor = tk.NW, relx=0.44, rely=0.5,relheight=0.4, relwidth=0.1)

		pass

	def runKriging(self):
		self.setBusy()
		thMin=int(self.param.lowerThreshold.get())
		thmax=int(self.param.upperThreshold.get())
		localIm=None
		if(self.param.previsualisation.get()==1):
			localIm=self.subSampleImage(self.sourceImage)
		else:
			localIm=self.sourceImage
		self.queue.put((localIm,self.getFilterParam(),(thMin, thmax,self.param.previsualisation.get()),
						 mazalib.kriging,(
										(self.param.krigingVariogramRadius.get()),
										(thMin, thmax))))
		pass

	def runCAC(self):
		self.setBusy()
		thMin=int(self.param.lowerThreshold.get())
		thmax=int(self.param.upperThreshold.get())
		# print((self.sourceImage,(self.param.CACalpha_G.get(), self.param.CACalpha_I.get(), self.param.CACG0.get(), self.param.CACunsharp_mask_strengths.get(),1, 10),(thMin, thmax)))
		localIm=None
		if(self.param.previsualisation.get()==1):
			localIm=self.subSampleImage(self.sourceImage)
		else:
			localIm=self.sourceImage
		self.queue.put((localIm,self.getFilterParam(),(thMin, thmax,self.param.previsualisation.get()),
						mazalib.cac,((self.param.CACalpha_G.get(), self.param.CACalpha_I.get(), self.param.CACG0.get()),(thMin, thmax))))
		pass

	def runMRF(self):
		self.setBusy()
		thMin=int(self.param.lowerThreshold.get())
		thmax=int(self.param.upperThreshold.get())
		# print((self.sourceImage,(self.param.MRFbeta.get(), self.param.MRFcooling.get(), self.param.MRFmethod.get(), self.param.MRFT_start.get(), self.param.MRFalpha.get(), self.param.MRFenergy.get(), self.param.MRFmax.get()),(thMin, thmax)))
		localIm=None
		if(self.param.previsualisation.get()==1):
			localIm=self.subSampleImage(self.sourceImage)
		else:
			localIm=self.sourceImage
		self.queue.put((localIm,self.getFilterParam(),(thMin, thmax,self.param.previsualisation.get()),
						mazalib.mrf,((self.param.MRFbeta.get(), self.param.MRFcooling.get(), self.param.MRFmethod.get(), self.param.MRFT_start.get(), self.param.MRFalpha.get(), self.param.MRFenergy.get(), self.param.MRFmax.get()),(thMin, thmax))))
		pass

	def runRGS(self):
		self.setBusy()
		thMin=int(self.param.lowerThreshold.get())
		thmax=int(self.param.upperThreshold.get())
		localIm=None
		if(self.param.previsualisation.get()==1):
			localIm=self.subSampleImage(self.sourceImage)
		else:
			localIm=self.sourceImage

		self.queue.put((localIm,self.getFilterParam(),(thMin, thmax,self.param.previsualisation.get()),
						mazalib.rgs,((thMin, thmax),)))
		pass

	def runHessian(self):
		self.setBusy()
		pass

	def runWindowedHessian(self):
		self.setBusy()
		pass

	def runFilterOnly(self):
		self.setBusy()
		self.resultAsInputButton["state"] = "normal"
		thMin=int(self.param.lowerThreshold.get())
		thmax=int(self.param.upperThreshold.get())
		localIm=None
		if(self.param.previsualisation.get()==1):
			localIm=self.subSampleImage(self.sourceImage)
		else:
			localIm=self.sourceImage

		self.queue.put((localIm,self.getFilterParam(),(thMin, thmax, self.param.previsualisation.get()),
						None,()))

	def getFilterParam(self):
		param=()
		if self.selectedFilter==0: #NLM
			param = (self.param.nlm_iters_count.get(),self.param.nlm_radius.get())
		elif self.selectedFilter==1: #unsharp
			param = (self.param.unsharp_mask_strengths.get(),)
		return (self.selectedFilter,param)

	def subSampleImage(self,image):
		print(self.startPosition4SubSample)
		print(self.endPosition4SubSample)
		return image[self.startPosition4SubSample[0]:self.endPosition4SubSample[0],
					self.startPosition4SubSample[1]:self.endPosition4SubSample[1],
					self.startPosition4SubSample[2]:self.endPosition4SubSample[2]]

	def setBusy(self):
		self.resultAsInputButton["state"] = "disabled"
		self.root.config(cursor="exchange")
		try:
			self.root.config(cursor="wait")
		except Exception as e:
			pass

	def setNotBusy(self):
		self.root.config(cursor="")

def run():

	root=tk.Tk()
	root.title("MAZAlib")
	# root.resizable(0, 0)
	
	app=App(root)

	import os.path as path
	cur_dir = path.dirname(path.realpath(__file__))
	path_to_icon = path.join(cur_dir, 'MAZAlib.ico')
	try:
		root.iconbitmap(path_to_icon)
	except Exception as e:
		print('No-icon: ', path_to_icon, e)
	

	# app.loadfile(path.join(cur_dir, 'image3d.raw'))
	app.initRandomImage()
	# app.loadDirectory('/Users/mathieugravey/Downloads/stack_soilXCT_Ah1')


	need_stop = False
	while not need_stop:
		app.look4results()
		try:
			root.update_idletasks()
			root.update()
		except Exception as e:
			need_stop = True
		time.sleep(0.01)

	app.release()

# if __name__ == "__main__":
# 	main()